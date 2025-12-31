---
paths: "**/*.tsx"
---

# React Project Rules

이 규칙은 react 프로젝트에 적용됩니다.

## Best Practices

- Memoize expensive computations with useMemo/useCallback
- Use functional components with hooks
- Keep components small and focused (Single Responsibility)
- Implement proper error boundaries
- Use TypeScript for type safety

## Common Patterns

- Controlled vs Uncontrolled components
- Custom Hooks for reusable logic
- Context API for global state
- Component composition over inheritance

## Anti-patterns to Avoid

- ❌ Prop drilling (use Context or state management)
- ❌ Too many useState hooks (consider useReducer)
- ❌ Missing dependency arrays in useEffect
- ❌ Mutating state directly

## Naming Conventions

- Test files: ComponentName.test.tsx
- Hooks: camelCase starting with 'use' (useAuth.ts)
- Files: match component name
- Components: PascalCase (UserProfile.tsx)

## Recommended File Structure

```
src/hooks/ - Custom hooks
src/utils/ - Utility functions
src/context/ - Context providers
src/components/ - Reusable UI components
src/pages/ - Page components
```

## Testing Guidelines

- Jest for unit tests
- React Testing Library for component tests
- Test user interactions, not implementation
- Aim for >70% coverage on business logic

