#!/usr/bin/env python3
"""
OpenAI Codex Developers Docs Crawler
Developers 문서를 크롤링하여 마크다운으로 변환합니다.
"""

import json
import os
import re
import time
from pathlib import Path
from urllib.parse import urlparse, urlunparse

import html2text
import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString

CODEX_OUTPUT_DIR = os.path.join("doc", "openai_codex_crawler")

DEFAULT_URLS = [
    "https://developers.openai.com/codex/quickstart",
    "https://developers.openai.com/codex/cli/",
    "https://developers.openai.com/codex/cli/features/",
    "https://developers.openai.com/codex/cli/reference/",
    "https://developers.openai.com/codex/local-config",
    "https://developers.openai.com/codex/config-basic/",
    "https://developers.openai.com/codex/config-advanced/",
    "https://developers.openai.com/codex/config-reference",
    "https://developers.openai.com/codex/config-sample",
    "https://developers.openai.com/codex/security/",
    "https://developers.openai.com/codex/sandbox/",
    "https://developers.openai.com/codex/exec-policy",
    "https://developers.openai.com/codex/auth",
    "https://developers.openai.com/codex/guides/agents-md/",
    "https://developers.openai.com/codex/mcp/",
    "https://developers.openai.com/codex/noninteractive",
    "https://developers.openai.com/codex/models/",
    "https://developers.openai.com/codex/changelog/",
    "https://developers.openai.com/codex/open-source",
    "https://developers.openai.com/codex/feature-maturity",
    "https://developers.openai.com/codex/cloud/",
    "https://developers.openai.com/codex/cloud/environments/",
    "https://developers.openai.com/codex/cloud/internet-access/",
    "https://developers.openai.com/codex/integrations/github/",
    "https://developers.openai.com/codex/github-action/",
    "https://developers.openai.com/codex/guides/autofix-ci/",
    "https://developers.openai.com/codex/workflows",
    "https://developers.openai.com/codex/prompting",
    "https://developers.openai.com/codex/sdk/",
]


class CodexDocsCrawler:
    def __init__(
        self,
        output_dir=CODEX_OUTPUT_DIR,
        urls=None,
        compact_mode=True,
        keep_links=True,
    ):
        self.base_url = "https://developers.openai.com"
        self.output_dir = output_dir
        self.urls = urls or list(DEFAULT_URLS)
        self.visited_urls = []
        self.failed_urls = []
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        self.html_converter = html2text.HTML2Text()
        self.compact_mode = compact_mode
        self.keep_links = keep_links
        self.html_converter.ignore_links = compact_mode and not keep_links
        self.html_converter.ignore_images = compact_mode
        self.html_converter.body_width = 0

        Path(output_dir).mkdir(parents=True, exist_ok=True)

    def normalize_url(self, url):
        """쿼리/프래그먼트 제거"""
        parsed = urlparse(url)
        return urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", "", ""))

    def strip_noise(self, content):
        """네비게이션/푸터 등 불필요한 요소 제거"""
        if content is None:
            return
        selectors = [
            "nav",
            "aside",
            "footer",
            "form",
            "button",
            '[role="navigation"]',
            '[role="search"]',
            '[aria-label="Search"]',
            ".sidebar",
            ".toc",
            ".table-of-contents",
            ".breadcrumbs",
            ".search",
            ".navigation",
            ".skip-to-content",
        ]
        for selector in selectors:
            for tag in content.select(selector):
                tag.decompose()
        for header in content.find_all("header"):
            if header.find("h1") is None:
                header.decompose()

    def trim_to_first_heading(self, content, heading_tag="h1"):
        """첫 번째 제목 이전의 콘텐츠 제거"""
        if content is None:
            return
        first_heading = content.find(heading_tag)
        if not first_heading:
            return
        node = first_heading
        while node and node is not content:
            prev = node.previous_sibling
            while prev:
                to_remove = prev
                prev = prev.previous_sibling
                if isinstance(to_remove, NavigableString):
                    to_remove.extract()
                else:
                    to_remove.decompose()
            node = node.parent

    def compress_markdown(self, markdown):
        """마크다운 크기 축소"""
        if not markdown:
            return markdown
        markdown = markdown.replace("\u200b", "")
        skip_exact = {
            "Copy",
            "Copied",
            "Skip to main content",
            "Search",
            "Navigation",
        }
        lines = []
        in_code_block = False
        prev_blank = False
        skip_next_blank = False
        for raw_line in markdown.splitlines():
            line = raw_line.rstrip()
            stripped = line.strip()
            if stripped.startswith("```"):
                if not in_code_block:
                    while lines and lines[-1] == "":
                        lines.pop()
                else:
                    skip_next_blank = True
                in_code_block = not in_code_block
                lines.append(line)
                prev_blank = False
                continue
            if not in_code_block:
                if stripped in skip_exact:
                    continue
                if re.match(r"^#+\s*$", stripped):
                    continue
            if not stripped:
                if skip_next_blank:
                    continue
                if prev_blank:
                    continue
                prev_blank = True
                lines.append("")
                continue
            if skip_next_blank:
                skip_next_blank = False
            prev_blank = False
            lines.append(line)
        return "\n".join(lines).strip()

    def get_page_content(self, url):
        """페이지 내용 가져오기"""
        try:
            response = requests.get(url, headers=self.headers, timeout=20)
            response.raise_for_status()
            return response.text
        except Exception as exc:
            print(f"❌ Error fetching {url}: {exc}")
            return None

    def extract_main_content(self, soup):
        """메인 콘텐츠 추출"""
        selectors = [
            "main",
            "article",
            "[data-testid='content']",
            ".docs-content",
            ".documentation",
            ".prose",
            "[role='main']",
        ]
        for selector in selectors:
            content = soup.select_one(selector)
            if content:
                return content
        return soup.find("body")

    def clean_filename(self, url):
        """URL에서 안전한 파일명 생성"""
        parsed = urlparse(url)
        path = parsed.path.strip("/")

        path = re.sub(r"^codex/", "", path)

        if not path:
            path = "index"

        filename = path.replace("/", "_") + ".md"
        return filename

    def html_to_markdown(self, html_content):
        """HTML을 마크다운으로 변환"""
        try:
            markdown = self.html_converter.handle(str(html_content))
            markdown = re.sub(r"\n{3,}", "\n\n", markdown)
            markdown = markdown.strip()
            if self.compact_mode:
                markdown = self.compress_markdown(markdown)
            return markdown
        except Exception as exc:
            print(f"⚠️  Markdown conversion error: {exc}")
            return str(html_content)

    def save_markdown(self, url, content, title=""):
        """마크다운 파일로 저장"""
        filename = self.clean_filename(url)
        filepath = os.path.join(self.output_dir, filename)

        metadata = ["---", f"source: {url}"]
        if title:
            metadata.append(f"title: {title}")
        metadata.append("---\n")
        metadata_block = "\n".join(metadata)

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(metadata_block + "\n" + content)

        print(f"✅ Saved: {filename}")
        return filepath

    def crawl_page(self, url):
        """단일 페이지 크롤링"""
        url = self.normalize_url(url)
        if url in self.visited_urls:
            return

        print(f"\n🔍 Crawling: {url}")
        html_content = self.get_page_content(url)
        if not html_content:
            self.failed_urls.append(url)
            return

        soup = BeautifulSoup(html_content, "html.parser")
        title = ""
        title_tag = soup.find("h1") or soup.title
        if title_tag:
            title = title_tag.get_text(strip=True)

        main_content = self.extract_main_content(soup)
        self.strip_noise(main_content)
        self.trim_to_first_heading(main_content)

        markdown_content = self.html_to_markdown(main_content)
        self.save_markdown(url, markdown_content, title)

        self.visited_urls.append(url)

    def crawl(self):
        """전체 문서 크롤링"""
        print("🚀 Starting Codex docs crawl")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"📄 Total URLs: {len(self.urls)}\n")

        for index, url in enumerate(self.urls, 1):
            self.crawl_page(url)
            if index % 5 == 0:
                print(f"\n📈 Progress: {index}/{len(self.urls)} pages crawled")
            time.sleep(1.0)

        stats = {
            "total_pages": len(self.visited_urls),
            "visited_urls": self.visited_urls,
            "failed_urls": self.failed_urls,
            "output_dir": self.output_dir,
        }

        with open(os.path.join(self.output_dir, "_crawl_stats.json"), "w", encoding="utf-8") as file:
            json.dump(stats, file, indent=2, ensure_ascii=False)

        print(f"\n✨ Crawling complete!")
        print(f"📊 Pages crawled: {len(self.visited_urls)}")
        if self.failed_urls:
            print(f"⚠️  Failed: {len(self.failed_urls)}")
        print(f"📁 Files saved in: {self.output_dir}")


def main():
    crawler = CodexDocsCrawler(output_dir=CODEX_OUTPUT_DIR)
    crawler.crawl()


if __name__ == "__main__":
    main()
