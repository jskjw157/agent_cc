---
name: code-reviewer
description: Comprehensive code review skill for TypeScript, JavaScript, Python, Swift, Kotlin, Go. Includes automated code analysis, best practice checking, security scanning, and review checklist generation. Use when reviewing pull requests, providing code feedback, identifying issues, or ensuring code quality standards.
---

# Code Reviewer

Complete toolkit for code reviewer with modern tools and best practices.

## Quick Start

```bash
# 코드 리뷰 분석 실행
python script/code_review_analyzer.py --output .claude/review-report.json
```

## Core Capabilities

### Code Review Analyzer

정적 분석 도구(ktlint, eslint, flake8)를 통합하여 JSON 리포트를 생성합니다.

**Features:**
- 언어별 린터 자동 실행 (Kotlin: ktlint, TS/JS: eslint, Python: flake8)
- 심각도 분류 (error/warning/info)
- 자동 수정 가능 여부 표시 (auto_fixable)
- 파일별 이슈 집계 및 상위 문제 파일 식별
- 개선 권장사항 자동 생성

**Usage:**
```bash
# 기본 실행
python script/code_review_analyzer.py

# 프로젝트 루트 지정
python script/code_review_analyzer.py --project-root /path/to/project

# 출력 파일 지정
python script/code_review_analyzer.py --output .claude/review-report.json
```

**Output (JSON):**
```json
{
  "summary": {
    "error": 5,
    "warning": 12,
    "info": 3,
    "total": 20,
    "auto_fixable": 8,
    "files_with_issues": 7
  },
  "issues": [...],
  "recommendations": [...]
}
```

## Reference Documentation

### Code Review Checklist

Comprehensive guide available in `references/code_review_checklist.md`:

- Detailed patterns and practices
- Code examples
- Best practices
- Anti-patterns to avoid
- Real-world scenarios

### Coding Standards

Complete workflow documentation in `references/coding_standards.md`:

- Step-by-step processes
- Optimization strategies
- Tool integrations
- Performance tuning
- Troubleshooting guide

### Common Antipatterns

Technical reference guide in `references/common_antipatterns.md`:

- Technology stack details
- Configuration examples
- Integration patterns
- Security considerations
- Scalability guidelines

## Tech Stack

**Languages:** TypeScript, JavaScript, Python, Go, Swift, Kotlin
**Frontend:** React, Next.js, React Native, Flutter
**Backend:** Node.js, Express, GraphQL, REST APIs
**Database:** PostgreSQL, Prisma, NeonDB, Supabase
**DevOps:** Docker, Kubernetes, Terraform, GitHub Actions, CircleCI
**Cloud:** AWS, GCP, Azure

## Development Workflow

### 1. Setup and Configuration

```bash
# Install dependencies
npm install
# or
pip install -r requirements.txt

# Configure environment
cp .env.example .env
```

### 2. Run Quality Checks

```bash
# 코드 리뷰 분석 실행
python script/code_review_analyzer.py --output .claude/review-report.json

# 리포트 확인 후 수정
```

### 3. Implement Best Practices

Follow the patterns and practices documented in:
- `references/code_review_checklist.md`
- `references/coding_standards.md`
- `references/common_antipatterns.md`

## Best Practices Summary

### Code Quality
- Follow established patterns
- Write comprehensive tests
- Document decisions
- Review regularly

### Performance
- Measure before optimizing
- Use appropriate caching
- Optimize critical paths
- Monitor in production

### Security
- Validate all inputs
- Use parameterized queries
- Implement proper authentication
- Keep dependencies updated

### Maintainability
- Write clear code
- Use consistent naming
- Add helpful comments
- Keep it simple

## Common Commands

```bash
# Development
npm run dev
npm run build
npm run test
npm run lint

# Analysis
python script/code_review_analyzer.py --output .claude/review-report.json

# Deployment
docker build -t app:latest .
docker-compose up -d
kubectl apply -f k8s/
```

## Troubleshooting

### Common Issues

Check the comprehensive troubleshooting section in `references/common_antipatterns.md`.

### Getting Help

- Review reference documentation
- Check script output messages
- Consult tech stack documentation
- Review error logs

## Resources

- Pattern Reference: `references/code_review_checklist.md`
- Workflow Guide: `references/coding_standards.md`
- Technical Guide: `references/common_antipatterns.md`
- Tool Scripts: `script/` directory
