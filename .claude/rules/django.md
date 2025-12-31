---
paths: "**/*.py"
---

# Django Project Rules

이 규칙은 django 프로젝트에 적용됩니다.

## Best Practices

- Use Django ORM efficiently (select_related, prefetch_related)
- Follow Django's MVT pattern strictly
- Implement proper permission checks
- Use Django forms for validation

## Common Patterns

- Signals for decoupled actions
- Mixins for reusable view logic
- Class-based views for complex logic
- Function-based views for simple endpoints

## Naming Conventions

- Models: Singular, PascalCase (User, BlogPost)
- Views: snake_case (user_list_view)
- URLs: kebab-case (/blog-posts/)
- Apps: plural, snake_case (blog_posts)

