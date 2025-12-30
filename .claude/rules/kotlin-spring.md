---
paths: "**/*.kt"
---

# Kotlin/Spring Boot Project Rules

이 규칙은 Kotlin/Spring Boot 프로젝트에 적용됩니다.

## Code Review 추가 체크리스트

### Spring Boot 특화
- [ ] `@Transactional` 누락 여부 (데이터 수정 메서드)
- [ ] Repository 메서드 네이밍 컨벤션 (`findBy...`, `deleteBy...`)
- [ ] DTO/Entity 분리 확인 (Entity 직접 노출 금지)
- [ ] `@Valid` 어노테이션 누락 여부 (Controller 파라미터)

### Exception 처리
- [ ] `BusinessException(ErrorCode)` 패턴 사용
- [ ] 적절한 HTTP 상태 코드 반환

### Response 패턴
- [ ] `ApiResponse<T>` wrapper 사용 여부
- [ ] 일관된 응답 구조 유지

## Documentation (KDoc)

### KDoc 작성법
```kotlin
/**
 * 사용자 정보를 조회합니다.
 *
 * @param userId 조회할 사용자 ID
 * @return 사용자 정보
 * @throws UserNotFoundException 사용자가 존재하지 않는 경우
 */
fun getUser(userId: Long): User
```

### 필수 문서화 대상
- Controller의 모든 public endpoint
- Service interface의 public 메서드
- 복잡한 비즈니스 로직

## Naming Conventions

### Package
- `com.company.project.domain.entity`
- `com.company.project.domain.repository`
- `com.company.project.application.service`
- `com.company.project.interfaces.controller`

### Class/Interface
- Entity: `User`, `Order`
- Repository: `UserRepository`, `OrderRepository`
- Service: `UserService` (interface), `UserServiceImpl` (implementation)
- Controller: `UserController`
- DTO: `UserRequest`, `UserResponse`

## Common Patterns

### First-Writer-Wins (낙관적 락)
버전 기반 동시성 제어 패턴

### Namespace Enforcement
리소스 접근 시 소유권/권한 검증 필수
