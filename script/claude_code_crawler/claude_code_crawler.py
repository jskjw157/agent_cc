#!/usr/bin/env python3
"""
Claude Code Documentation Crawler
크롤링한 문서를 마크다운 파일로 변환합니다.
"""

import requests
from bs4 import BeautifulSoup
import html2text
import os
import time
import re
from urllib.parse import urljoin, urlparse, urlunparse
from pathlib import Path
import json

DOCS_OUTPUT_DIR = os.path.join("doc", "claude_code_docs")


class ClaudeCodeCrawler:
    def __init__(
        self,
        base_url="https://code.claude.com",
        output_dir=DOCS_OUTPUT_DIR,
        include_path_prefixes=None,
        exclude_path_patterns=None,
    ):
        self.base_url = base_url
        self.output_dir = output_dir
        if include_path_prefixes is None:
            include_path_prefixes = ["/docs/en/"]
        self.include_path_prefixes = include_path_prefixes
        self.exclude_path_patterns = [
            re.compile(pattern) for pattern in (exclude_path_patterns or [])
        ]
        self.visited_urls = set()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        self.html_converter = html2text.HTML2Text()
        self.html_converter.ignore_links = False
        self.html_converter.ignore_images = False
        self.html_converter.body_width = 0  # 줄바꿈 방지
        
        # 출력 디렉토리 생성
        Path(output_dir).mkdir(parents=True, exist_ok=True)

    def strip_noise(self, content):
        """네비게이션/푸터 등 불필요한 요소 제거"""
        if content is None:
            return
        selectors = [
            'nav',
            'aside',
            'footer',
            'form',
            'button',
            '[role="navigation"]',
            '[role="search"]',
            '[aria-label="Search"]',
            '.sidebar',
            '.toc',
            '.table-of-contents',
            '.breadcrumbs',
            '.search',
            '.navigation',
            '.skip-to-content',
        ]
        for selector in selectors:
            for tag in content.select(selector):
                tag.decompose()
        for header in content.find_all('header'):
            if header.find('h1') is None:
                header.decompose()
        
    def is_valid_doc_url(self, url):
        """문서 URL인지 확인"""
        parsed = urlparse(url)
        path = parsed.path or ""
        return (
            parsed.netloc == "code.claude.com" and
            "/docs/" in path and
            (
                not self.include_path_prefixes
                or any(path.startswith(prefix) for prefix in self.include_path_prefixes)
            ) and
            not path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.css', '.js')) and
            not any(pattern.search(path) for pattern in self.exclude_path_patterns)
        )

    def normalize_url(self, url):
        """쿼리/프래그먼트 제거"""
        parsed = urlparse(url)
        return urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", "", ""))
    
    def get_page_content(self, url):
        """페이지 내용 가져오기"""
        try:
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"❌ Error fetching {url}: {str(e)}")
            return None
    
    def extract_main_content(self, soup):
        """메인 콘텐츠 추출"""
        # 다양한 선택자 시도
        selectors = [
            'main',
            'article',
            '.docs-content',
            '.documentation',
            '[role="main"]',
            '#main-content'
        ]
        
        for selector in selectors:
            content = soup.select_one(selector)
            if content:
                return content
        
        # 찾지 못하면 body 반환
        return soup.find('body')
    
    def clean_filename(self, url):
        """URL에서 파일명 생성"""
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        
        # /docs/en/ 제거
        path = re.sub(r'^docs/(en|ko)/', '', path)
        
        # 빈 경로는 index로
        if not path or path == 'docs':
            path = 'index'
        
        # 안전한 파일명으로 변환
        filename = path.replace('/', '_') + '.md'
        return filename
    
    def html_to_markdown(self, html_content):
        """HTML을 마크다운으로 변환"""
        try:
            markdown = self.html_converter.handle(str(html_content))
            # 불필요한 공백 정리
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)
            return markdown.strip()
        except Exception as e:
            print(f"⚠️  Markdown conversion error: {str(e)}")
            return str(html_content)
    
    def extract_links(self, soup, current_url):
        """페이지에서 문서 링크 추출"""
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(current_url, href)

            full_url = self.normalize_url(full_url)

            if self.is_valid_doc_url(full_url):
                links.add(full_url)
        
        return links
    
    def save_markdown(self, url, content, title=""):
        """마크다운 파일로 저장"""
        filename = self.clean_filename(url)
        filepath = os.path.join(self.output_dir, filename)
        
        # 메타데이터 추가
        metadata = f"""---
source: {url}
title: {title}
---

"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(metadata + content)
        
        print(f"✅ Saved: {filename}")
        return filepath
    
    def crawl_page(self, url):
        """단일 페이지 크롤링"""
        if url in self.visited_urls:
            return set()
        
        print(f"\n🔍 Crawling: {url}")
        self.visited_urls.add(url)
        
        # 페이지 가져오기
        html_content = self.get_page_content(url)
        if not html_content:
            return set()
        
        # HTML 파싱
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 제목 추출
        title = soup.title.string if soup.title else ""
        
        # 메인 콘텐츠 추출
        main_content = self.extract_main_content(soup)
        self.strip_noise(main_content)
        
        # 마크다운 변환
        markdown_content = self.html_to_markdown(main_content)
        
        # 저장
        self.save_markdown(url, markdown_content, title)
        
        # 링크 추출
        new_links = self.extract_links(soup, url)
        
        return new_links
    
    def crawl(self, start_url, max_pages=50):
        """전체 문서 크롤링"""
        print(f"🚀 Starting crawl from: {start_url}")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"📄 Max pages: {max_pages}\n")
        
        to_visit = {start_url}
        pages_crawled = 0
        
        while to_visit and pages_crawled < max_pages:
            url = to_visit.pop()
            
            try:
                new_links = self.crawl_page(url)
                
                # 아직 방문하지 않은 링크만 추가
                for link in new_links:
                    if link not in self.visited_urls:
                        to_visit.add(link)
                
                pages_crawled += 1
                
                # 서버 부하 방지
                time.sleep(1)
                
            except Exception as e:
                print(f"❌ Error crawling {url}: {str(e)}")
                continue
        
        print(f"\n✨ Crawling complete!")
        print(f"📊 Pages crawled: {pages_crawled}")
        print(f"📁 Files saved in: {self.output_dir}")
        
        # 크롤링 통계 저장
        stats = {
            "total_pages": pages_crawled,
            "visited_urls": list(self.visited_urls),
            "output_dir": self.output_dir
        }
        
        with open(os.path.join(self.output_dir, '_crawl_stats.json'), 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)


def main():
    """메인 실행 함수"""
    # 크롤러 생성
    crawler = ClaudeCodeCrawler(
        base_url="https://code.claude.com",
        output_dir=DOCS_OUTPUT_DIR
    )
    
    # 시작 URL
    start_url = "https://code.claude.com/docs/en/overview"
    
    # 크롤링 시작 (최대 50페이지)
    crawler.crawl(start_url, max_pages=50)


if __name__ == "__main__":
    main()
