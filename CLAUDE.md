# Agent CC Project

Claude Code 환경에서 Kotlin/Spring Boot 개발을 위한 전문화된 에이전트, 스킬, 훅, 워크플로우를 제공하는 프로젝트입니다.

## 기술 스택
- Kotlin, Spring Boot, Gradle

## 주요 명령어
- `./gradlew test` - 테스트 실행
- `./gradlew build` - 빌드

## 코딩 컨벤션
- ApiResponse<T> 래퍼 사용 필수
- BusinessException(ErrorCode) 패턴 준수
- @Transactional 데이터 수정 메서드에 필수

## 프로젝트 구조
- `.claude/agents/` - 전문화된 에이전트 (code-reviewer, doc-writer)
- `.claude/skills/` - 스킬 모음 (10개)
- `.claude/hooks/` - 자동화 훅 (Kotlin 테스트)

## 권장 워크플로우
1. DDD 설계 → 기능 계획 → 이슈 생성 → 개발 → 리뷰 → 문서화
