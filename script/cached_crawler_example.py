#!/usr/bin/env python3
"""
Cached Crawler Example
cache_manager를 활용한 크롤러 캐시 통합 예제
"""

import sys
import os
from pathlib import Path

# script 디렉토리를 path에 추가
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from cache_manager import CacheManager
import requests
from bs4 import BeautifulSoup
import json


class CachedWebCrawler:
    """캐시를 활용한 웹 크롤러 예제"""

    def __init__(self, cache_ttl_days: int = 7):
        self.cache = CacheManager(
            cache_dir=".claude/cache",
            default_ttl_days=cache_ttl_days
        )
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def fetch_with_cache(self, url: str, force_refresh: bool = False) -> dict:
        """
        캐시를 활용한 웹 페이지 가져오기

        Args:
            url: 가져올 URL
            force_refresh: 캐시 무시하고 새로 가져오기

        Returns:
            페이지 데이터 (title, content, url)
        """
        # 1. 캐시 확인 (force_refresh가 아닐 때)
        if not force_refresh:
            cached = self.cache.get(url)
            if cached:
                print(f"✅ Cache hit: {url}")
                return cached

        print(f"🌐 Fetching from web: {url}")

        # 2. 웹에서 가져오기
        try:
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # 메인 콘텐츠 추출
            title = soup.title.string if soup.title else ""

            # main 태그 찾기
            main_content = soup.find('main') or soup.find('article') or soup.find('body')

            # 노이즈 제거
            for tag in main_content.select('nav, aside, footer, script, style'):
                tag.decompose()

            content = main_content.get_text(separator='\n', strip=True) if main_content else ""

            data = {
                "url": url,
                "title": title,
                "content": content[:5000],  # 처음 5000자만 (토큰 절약)
                "fetched_from": "web"
            }

            # 3. 캐시 저장
            self.cache.set(url, data)
            print(f"💾 Cached: {url}")

            return data

        except Exception as e:
            print(f"❌ Error fetching {url}: {e}")
            return {
                "url": url,
                "title": "Error",
                "content": f"Failed to fetch: {str(e)}",
                "fetched_from": "error"
            }

    def batch_fetch(self, urls: list, force_refresh: bool = False) -> list:
        """
        여러 URL을 배치로 가져오기

        Args:
            urls: URL 리스트
            force_refresh: 캐시 무시

        Returns:
            데이터 리스트
        """
        results = []

        print(f"📚 Batch fetching {len(urls)} URLs...\n")

        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}] {url}")
            data = self.fetch_with_cache(url, force_refresh)
            results.append(data)
            print()

        return results

    def get_cache_stats(self) -> dict:
        """캐시 통계 반환"""
        return self.cache.get_stats()

    def clear_cache(self) -> int:
        """캐시 전체 삭제"""
        return self.cache.clear_all()

    def clear_expired_cache(self) -> int:
        """만료된 캐시만 삭제"""
        return self.cache.clear_expired()


def integrate_with_existing_crawler():
    """기존 크롤러에 캐시 통합하는 방법 예시"""

    print("=" * 80)
    print("기존 크롤러에 캐시 통합 가이드")
    print("=" * 80)

    guide = """
# 기존 크롤러에 캐시 통합하기

## 1. CacheManager import
```python
from cache_manager import CacheManager
```

## 2. 크롤러 __init__에 캐시 매니저 추가
```python
class ClaudeCodeCrawler:
    def __init__(self, ...):
        # 기존 코드
        ...

        # 캐시 매니저 추가
        self.cache = CacheManager(
            cache_dir=".claude/cache",
            default_ttl_days=7  # 기술 문서는 7일
        )
```

## 3. get_page_content 메서드 수정
```python
def get_page_content(self, url):
    # 캐시 확인
    cached = self.cache.get(url)
    if cached:
        print(f"✅ Cache hit: {url}")
        return cached.get("html_content")

    # 캐시 미스 - 웹에서 가져오기
    try:
        response = requests.get(url, headers=self.headers, timeout=15)
        response.raise_for_status()
        html_content = response.text

        # 캐시 저장
        self.cache.set(url, {"html_content": html_content})

        return html_content
    except Exception as e:
        print(f"❌ Error fetching {url}: {str(e)}")
        return None
```

## 4. 캐시 통계 출력 (선택)
```python
def crawl(self, start_url, max_pages=50):
    # 기존 크롤링 코드
    ...

    # 크롤링 완료 후 캐시 통계 출력
    stats = self.cache.get_stats()
    print(f"\\n📊 Cache Statistics:")
    print(f"  Hit rate: {stats['hit_rate']}%")
    print(f"  Cache hits: {stats['hit']}")
    print(f"  Cache misses: {stats['miss']}")
```

## 토큰 절감 효과

- **캐시 히트 시**: HTML 크롤링(5,000토큰) → 캐시 조회(50토큰) = 99% 절감
- **중복 방문**: 동일 URL 재방문 시 네트워크 요청 0, 토큰 0
- **속도 향상**: 캐시 조회는 밀리초 단위 (웹 요청은 초 단위)

## 캐시 관리 명령어

```bash
# 캐시 통계 확인
python script/cache_manager.py --action stats

# 만료된 캐시 정리
python script/cache_manager.py --action clear-expired

# 전체 캐시 삭제
python script/cache_manager.py --action clear-all
```
"""

    print(guide)


def demo():
    """캐시 크롤러 데모"""
    print("=" * 80)
    print("Cached Crawler Demo")
    print("=" * 80 + "\n")

    # 크롤러 생성
    crawler = CachedWebCrawler(cache_ttl_days=7)

    # 테스트 URL들
    test_urls = [
        "https://code.claude.com/docs/en/overview",
        "https://docs.anthropic.com/en/home",
    ]

    # 첫 번째 실행 (캐시 미스)
    print("🔵 First run (cache miss expected):\n")
    results1 = crawler.batch_fetch(test_urls[:1])  # 1개만 테스트

    # 두 번째 실행 (캐시 히트)
    print("\n" + "=" * 80)
    print("🟢 Second run (cache hit expected):\n")
    results2 = crawler.batch_fetch(test_urls[:1])

    # 통계 출력
    print("\n" + "=" * 80)
    print("📊 Cache Statistics:")
    print("=" * 80)
    stats = crawler.get_cache_stats()
    print(json.dumps(stats, indent=2))


def main():
    """CLI 실행"""
    import argparse

    parser = argparse.ArgumentParser(description="Cached Crawler Example")
    parser.add_argument("--demo", action="store_true", help="Run demo")
    parser.add_argument("--guide", action="store_true", help="Show integration guide")
    parser.add_argument("--url", help="Fetch single URL")
    parser.add_argument("--urls", nargs="+", help="Fetch multiple URLs")
    parser.add_argument("--force", action="store_true", help="Force refresh (skip cache)")

    args = parser.parse_args()

    if args.guide:
        integrate_with_existing_crawler()
    elif args.demo:
        demo()
    elif args.url:
        crawler = CachedWebCrawler()
        data = crawler.fetch_with_cache(args.url, force_refresh=args.force)
        print(json.dumps(data, indent=2, ensure_ascii=False))
    elif args.urls:
        crawler = CachedWebCrawler()
        results = crawler.batch_fetch(args.urls, force_refresh=args.force)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
