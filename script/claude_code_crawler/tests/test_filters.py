import sys
import unittest
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from claude_code_crawler import ClaudeCodeCrawler
from anthropic_blog_crawler import AnthropicBlogCrawler


class TestClaudeCodeCrawlerFilters(unittest.TestCase):
    def setUp(self):
        self.crawler = ClaudeCodeCrawler()

    def test_docs_en_allowed(self):
        self.assertTrue(
            self.crawler.is_valid_doc_url("https://code.claude.com/docs/en/overview")
        )

    def test_docs_ko_blocked(self):
        self.assertFalse(
            self.crawler.is_valid_doc_url("https://code.claude.com/docs/ko/overview")
        )

    def test_assets_blocked(self):
        self.assertFalse(
            self.crawler.is_valid_doc_url("https://code.claude.com/docs/en/overview.png")
        )

    def test_normalize_url(self):
        normalized = self.crawler.normalize_url(
            "https://code.claude.com/docs/en/overview?x=1#y"
        )
        self.assertEqual(normalized, "https://code.claude.com/docs/en/overview")

    def test_exclude_pattern(self):
        crawler = ClaudeCodeCrawler(exclude_path_patterns=[r"/docs/en/iam"])
        self.assertFalse(crawler.is_valid_doc_url("https://code.claude.com/docs/en/iam"))

    def test_strip_noise(self):
        html = """
        <html><body>
        <main>
          <nav>Nav</nav>
          <aside>Aside</aside>
          <header><div>Logo</div></header>
          <header><h1>Title</h1></header>
          <section>Keep me</section>
          <footer>Footer</footer>
        </main>
        </body></html>
        """
        soup = BeautifulSoup(html, "html.parser")
        content = soup.find("main")
        self.crawler.strip_noise(content)
        self.assertIsNone(content.find("nav"))
        self.assertIsNone(content.find("aside"))
        self.assertIsNone(content.find("footer"))
        headers = content.find_all("header")
        self.assertTrue(any(header.find("h1") for header in headers))
        self.assertEqual(len(headers), 1)


class TestAnthropicBlogCrawlerFilters(unittest.TestCase):
    def setUp(self):
        self.crawler = AnthropicBlogCrawler()

    def test_news_post_allowed(self):
        self.assertTrue(
            self.crawler.is_valid_post_url(
                "https://www.anthropic.com/news/claude-opus-4-5"
            )
        )

    def test_news_index_blocked(self):
        self.assertFalse(self.crawler.is_valid_post_url("https://www.anthropic.com/news"))

    def test_blog_post_allowed(self):
        self.assertTrue(
            self.crawler.is_valid_post_url("https://www.anthropic.com/blog/some-post")
        )

    def test_assets_blocked(self):
        self.assertFalse(
            self.crawler.is_valid_post_url("https://www.anthropic.com/news/foo.png")
        )

    def test_domain_allowed(self):
        self.assertTrue(
            self.crawler.is_valid_post_url(
                "https://anthropic.com/news/claude-opus-4-5"
            )
        )

    def test_normalize_url(self):
        normalized = self.crawler.normalize_url(
            "https://www.anthropic.com/news/x?y=1#z"
        )
        self.assertEqual(normalized, "https://www.anthropic.com/news/x")

    def test_exclude_pattern(self):
        crawler = AnthropicBlogCrawler(
            exclude_path_patterns=[r"/news/claude-opus-4-5"]
        )
        self.assertFalse(
            crawler.is_valid_post_url("https://www.anthropic.com/news/claude-opus-4-5")
        )


if __name__ == "__main__":
    unittest.main()
