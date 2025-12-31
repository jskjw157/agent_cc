#!/usr/bin/env python3
"""
Web Scraping Cache Manager
웹 크롤링 결과를 캐시하여 반복 크롤링을 방지합니다.
TTL 기반 캐시 만료 지원.
"""

import json
import hashlib
import os
import time
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime, timedelta


class CacheManager:
    """웹 스크래핑 캐시 관리자"""

    def __init__(
        self,
        cache_dir: str = ".claude/cache",
        default_ttl_days: int = 7
    ):
        """
        Args:
            cache_dir: 캐시 저장 디렉토리
            default_ttl_days: 기본 TTL (일 단위)
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.default_ttl_days = default_ttl_days
        self.stats_file = self.cache_dir / "_cache_stats.json"

    def _url_to_cache_key(self, url: str) -> str:
        """URL을 캐시 키로 변환"""
        return hashlib.sha256(url.encode()).hexdigest()

    def _get_cache_path(self, cache_key: str) -> Path:
        """캐시 파일 경로 반환"""
        return self.cache_dir / f"{cache_key}.json"

    def get(self, url: str) -> Optional[Dict[str, Any]]:
        """
        캐시에서 데이터 조회

        Args:
            url: 조회할 URL

        Returns:
            캐시된 데이터 또는 None (캐시 미스 또는 만료)
        """
        cache_key = self._url_to_cache_key(url)
        cache_path = self._get_cache_path(cache_key)

        if not cache_path.exists():
            self._update_stats("miss")
            return None

        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)

            # TTL 확인
            expires_at = cache_data.get("expires_at")
            if expires_at and time.time() > expires_at:
                # 만료된 캐시 삭제
                cache_path.unlink()
                self._update_stats("expired")
                return None

            self._update_stats("hit")
            return cache_data.get("data")

        except (json.JSONDecodeError, KeyError) as e:
            print(f"⚠️  Cache read error for {url}: {e}")
            self._update_stats("error")
            return None

    def set(
        self,
        url: str,
        data: Dict[str, Any],
        ttl_days: Optional[int] = None
    ) -> None:
        """
        데이터를 캐시에 저장

        Args:
            url: 캐시할 URL
            data: 저장할 데이터
            ttl_days: TTL (일 단위), None이면 default_ttl_days 사용
        """
        cache_key = self._url_to_cache_key(url)
        cache_path = self._get_cache_path(cache_key)

        ttl = ttl_days if ttl_days is not None else self.default_ttl_days
        expires_at = time.time() + (ttl * 86400)  # 초 단위로 변환

        cache_data = {
            "url": url,
            "data": data,
            "cached_at": time.time(),
            "expires_at": expires_at,
            "ttl_days": ttl
        }

        try:
            with open(cache_path, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=2, ensure_ascii=False)
            self._update_stats("write")
        except Exception as e:
            print(f"⚠️  Cache write error for {url}: {e}")

    def invalidate(self, url: str) -> bool:
        """
        특정 URL의 캐시 무효화

        Args:
            url: 무효화할 URL

        Returns:
            삭제 성공 여부
        """
        cache_key = self._url_to_cache_key(url)
        cache_path = self._get_cache_path(cache_key)

        if cache_path.exists():
            cache_path.unlink()
            self._update_stats("invalidate")
            return True
        return False

    def clear_expired(self) -> int:
        """
        만료된 캐시 파일 모두 삭제

        Returns:
            삭제된 파일 수
        """
        deleted_count = 0
        current_time = time.time()

        for cache_file in self.cache_dir.glob("*.json"):
            if cache_file.name.startswith("_"):
                continue

            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    cache_data = json.load(f)

                expires_at = cache_data.get("expires_at")
                if expires_at and current_time > expires_at:
                    cache_file.unlink()
                    deleted_count += 1
            except Exception:
                continue

        if deleted_count > 0:
            print(f"🗑️  Cleared {deleted_count} expired cache entries")
        return deleted_count

    def clear_all(self) -> int:
        """
        모든 캐시 삭제

        Returns:
            삭제된 파일 수
        """
        deleted_count = 0

        for cache_file in self.cache_dir.glob("*.json"):
            if cache_file.name.startswith("_"):
                continue
            cache_file.unlink()
            deleted_count += 1

        print(f"🗑️  Cleared all {deleted_count} cache entries")
        self._reset_stats()
        return deleted_count

    def get_stats(self) -> Dict[str, Any]:
        """캐시 통계 반환"""
        if not self.stats_file.exists():
            return {
                "hit": 0,
                "miss": 0,
                "expired": 0,
                "write": 0,
                "invalidate": 0,
                "error": 0,
                "hit_rate": 0.0
            }

        try:
            with open(self.stats_file, 'r', encoding='utf-8') as f:
                stats = json.load(f)

            # 히트율 계산
            total_requests = stats.get("hit", 0) + stats.get("miss", 0)
            hit_rate = (stats.get("hit", 0) / total_requests * 100) if total_requests > 0 else 0.0
            stats["hit_rate"] = round(hit_rate, 2)

            return stats
        except Exception:
            return {
                "hit": 0,
                "miss": 0,
                "expired": 0,
                "write": 0,
                "invalidate": 0,
                "error": 0,
                "hit_rate": 0.0
            }

    def _update_stats(self, event_type: str) -> None:
        """통계 업데이트"""
        stats = self.get_stats()
        stats[event_type] = stats.get(event_type, 0) + 1

        # 히트율 재계산
        total_requests = stats.get("hit", 0) + stats.get("miss", 0)
        stats["hit_rate"] = (stats.get("hit", 0) / total_requests * 100) if total_requests > 0 else 0.0
        stats["hit_rate"] = round(stats["hit_rate"], 2)

        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2)
        except Exception:
            pass

    def _reset_stats(self) -> None:
        """통계 초기화"""
        if self.stats_file.exists():
            self.stats_file.unlink()


def main():
    """CLI 테스트"""
    import argparse

    parser = argparse.ArgumentParser(description="Cache Manager CLI")
    parser.add_argument("--action", choices=["get", "set", "invalidate", "clear-expired", "clear-all", "stats"], required=True)
    parser.add_argument("--url", help="Target URL")
    parser.add_argument("--data", help="Data to cache (JSON string)")
    parser.add_argument("--ttl", type=int, help="TTL in days")
    parser.add_argument("--cache-dir", default=".claude/cache", help="Cache directory")

    args = parser.parse_args()

    cache = CacheManager(cache_dir=args.cache_dir)

    if args.action == "get":
        if not args.url:
            print("❌ --url required for get action")
            return
        result = cache.get(args.url)
        if result:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print("Cache miss")

    elif args.action == "set":
        if not args.url or not args.data:
            print("❌ --url and --data required for set action")
            return
        data = json.loads(args.data)
        cache.set(args.url, data, ttl_days=args.ttl)
        print(f"✅ Cached: {args.url}")

    elif args.action == "invalidate":
        if not args.url:
            print("❌ --url required for invalidate action")
            return
        if cache.invalidate(args.url):
            print(f"✅ Invalidated: {args.url}")
        else:
            print(f"⚠️  Not found: {args.url}")

    elif args.action == "clear-expired":
        count = cache.clear_expired()
        print(f"✅ Cleared {count} expired entries")

    elif args.action == "clear-all":
        count = cache.clear_all()
        print(f"✅ Cleared {count} entries")

    elif args.action == "stats":
        stats = cache.get_stats()
        print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
