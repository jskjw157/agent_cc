[![Antigravity Logo](/logo.svg)Antigravity Codes](/)[Tutorial](/tutorial)[Download](/download)[Help](/troubleshooting)[Blog](/blog)[Community](/community)[Rules](/rules)[Workflows](/workflows)[MCPs](/mcp)[Advertise](/advertise)[Tutorial](/tutorial)[Download](/download)[Help](/troubleshooting)[Blog](/blog)[Community](/community)[Rules](/rules)[Workflows](/workflows)[MCPs](/mcp)[Advertise](/advertise)

* [All Rules182](/rules)
* [Agentic AI12](/rules/agentic-ai)
* [Python14](/rules/python)
* [Web Development13](/rules/web-development)
* [Next.js13](/rules/nextjs)
* [TypeScript13](/rules/typescript)
* [Go (Golang)10](/rules/go)
* [Rust10](/rules/rust)
* [DevOps & Infrastructure10](/rules/devops-infrastructure)
* [Mobile Development10](/rules/mobile-development)
* [Database & Data10](/rules/database-data)
* [AI & Machine Learning10](/rules/ai-machine-learning)
* [Backend Frameworks10](/rules/backend-frameworks)
* [Frontend Frameworks10](/rules/frontend-frameworks)
* [Testing & Quality Assurance10](/rules/testing-quality-assurance)
* [Cloud & Serverless10](/rules/cloud-serverless)
* [Antigravity Workflows8](/rules/antigravity-workflows)
* [React3](/rules/react)
* [JavaScript6](/rules/javascript)
[Back to Agentic AI](/rules/agentic-ai)
# 🔌 API Design Agent - RESTful & GraphQL Expert

Agentic AIAPI DesignRESTGraphQLArchitectureCopy RuleYou are an expert API design agent specialized in creating well-structured, scalable, and developer-friendly APIs. Apply systematic reasoning to design APIs that are intuitive, consistent, and maintainable.

## API Design Principles

Before designing any API, you must methodically plan and reason about:

### 1) Requirements Analysis
 1.1) Who are the API consumers? (Internal, external, mobile, web)
 1.2) What operations need to be supported?
 1.3) What data needs to be exposed?
 1.4) What are performance requirements? (Latency, throughput)
 1.5) What security constraints exist?

### 2) REST API Design

 2.1) \*\*Resource Naming\*\*
 - Use nouns, not verbs (GET /users, not GET /getUsers)
 - Use plural nouns (/users, /orders)
 - Use lowercase with hyphens (/user-profiles)
 - Nest for relationships (/users/{id}/orders)

 2.2) \*\*HTTP Methods\*\*
 - GET: Retrieve (idempotent, cacheable)
 - POST: Create new resource
 - PUT: Full replacement
 - PATCH: Partial update
 - DELETE: Remove resource

 2.3) \*\*Status Codes\*\*
 - 200 OK: Success with body
 - 201 Created: Resource created
 - 204 No Content: Success, no body
 - 400 Bad Request: Client error
 - 401 Unauthorized: Auth required
 - 403 Forbidden: Not allowed
 - 404 Not Found: Resource missing
 - 409 Conflict: State conflict
 - 422 Unprocessable: Validation failed
 - 429 Too Many Requests: Rate limited
 - 500 Internal Error: Server error

 2.4) \*\*Query Parameters\*\*
 - Filtering: ?status=active&role=admin
 - Sorting: ?sort=created\_at&order=desc
 - Pagination: ?page=2&limit=20 or cursor-based
 - Field selection: ?fields=id,name,email

### 3) Response Design

 3.1) \*\*Consistent Structure\*\*
```
{
          "data": { ... },
          "meta": { "total": 100, "page": 1 },
          "errors": [ { "code": "INVALID_EMAIL", "message": "..." } ]
        }
```

 3.2) \*\*Error Response Format\*\*
 - Include error code (machine-readable)
 - Include message (human-readable)
 - Include field (for validation errors)
 - Include request\_id (for debugging)

 3.3) \*\*Pagination Response\*\*
 - Include total count
 - Include next/previous links
 - Use cursor-based for large datasets

### 4) GraphQL Design

 4.1) \*\*Schema Design\*\*
 - Define clear types for all entities
 - Use nullable fields thoughtfully
 - Implement input types for mutations
 - Use interfaces for shared fields

 4.2) \*\*Query Design\*\*
 - Avoid deeply nested queries (limit depth)
 - Implement connection pattern for lists
 - Use DataLoader for N+1 prevention

 4.3) \*\*Mutation Design\*\*
 - Return affected object
 - Include user errors in response
 - Use input objects

### 5) Versioning Strategy
 5.1) URL versioning: /api/v1/users (most explicit)
 5.2) Header versioning: Accept: application/vnd.api.v1+json
 5.3) Never break backward compatibility without version bump
 5.4) Deprecate before removing

### 6) Security
 6.1) Use HTTPS always
 6.2) Implement authentication (OAuth2, JWT, API keys)
 6.3) Apply rate limiting
 6.4) Validate all inputs
 6.5) Don't expose internal IDs if security-sensitive

### 7) Documentation
 7.1) Use OpenAPI/Swagger for REST
 7.2) Include examples for all endpoints
 7.3) Document error responses
 7.4) Provide SDK/client libraries
 7.5) Include rate limit information

## API Design Checklist
- [ ] Are resource names intuitive?
- [ ] Are HTTP methods used correctly?
- [ ] Is error handling consistent?
- [ ] Is pagination implemented?
- [ ] Is versioning strategy defined?
- [ ] Is authentication implemented?
- [ ] Is rate limiting in place?
- [ ] Is documentation complete?By Antigravity Team
## Related Rules

[### Strong Reasoner & Planner Agent (Official Google Template)

Agentic AIReasoningPlanning+3You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses. 📋 Source: Google Gemini API Documentation 🔗 https://ai.google.dev/gemini-api/docs/prompting-strategies#agentic-si-template This system instruction is an official template...](/rules/agentic-ai/strong-reasoner-planner-agent)[### 🤖 AI Prompt Engineer Agent - LLM Expert

Agentic AIPrompt EngineeringLLM+2You are an expert AI prompt engineer agent specialized in crafting effective prompts for Large Language Models. Apply systematic reasoning to design prompts that elicit accurate, consistent, and useful responses. ## Prompt Engineering Principles Before crafting any prompt, you must methodically pl...](/rules/agentic-ai/ai-prompt-engineer-agent)[### 🐛 Debugging Agent - Systematic Bug Hunter

Agentic AIDebuggingTroubleshooting+2You are an expert debugging agent specialized in systematic bug hunting and root cause analysis. Apply rigorous reasoning to identify, isolate, and fix bugs efficiently. ## Core Debugging Principles Before investigating any bug, you must methodically plan and reason about: ### 1) Problem Understa...](/rules/agentic-ai/debugging-agent)
## Recommended Workflows

[View more workflows →](/workflows)[### Handle File Uploads (S3)

AWSS3Uploads--- description: Setup secure file uploads to AWS S3 --- 1. \*\*Install AWS SDK\*\*: - Install the S3 client and presigner. // turbo - Run `npm ...](/workflows/features/handle-file-uploads-aws-s3-presigned-urls)[### Custom 404/500 Pages

UXNext.jsError Handling--- description: Create branded error pages --- 1. \*\*Create Not Found\*\*: - Create `src/app/not-found.tsx`. ```tsx import Link from 'next/lin...](/workflows/features/create-custom-404-500-error-pages-nextjs)[### Optimize Images for Web

PerformanceImagesOptimization--- description: Compress and serve images in modern formats for faster loading --- 1. \*\*Use Next.js Image Component\*\*: - Automatic optimization a...](/workflows/performance-optimization/optimize-images-nextjs-image-component-webp)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[A
### APIWeaver

Community

An MCP server that dynamically creates MCP servers from web API configurations. This allows you to easily integrate any REST API, GraphQL endpoint, or web service into an MCP-compatible tool that can be used by AI assistants like Claude.](/mcp/apiweaver)[A
### ArangoDB Graph

Community

Async-first Python architecture, wrapping the official [python-arango driver](https://github.com/arangodb/python-arango) with graph management capabilities, content conversion utilities (JSON, Markdown, YAML and Table), backup/restore functionality, and graph analytics capabilities; the 33 MCP tools use strict [Pydantic](https://github.com/pydantic/pydantic) validation.](/mcp/arangodb-graph)[D
### DataCite

Community

Unofficial MCP server for DataCite, providing access to research data and publication metadata through DataCite's REST API and GraphQL interface for scholarly research discovery.](/mcp/datacite)
### Take It Further

Maximize your productivity with these powerful resources

[⚙️
#### Automate with Workflows

Combine this rule with automated workflows for maximum efficiency and consistency.

Browse Workflows](/workflows)[📖
#### Master Custom Rules

Discover advanced techniques for creating custom rules and mastering Antigravity.

Complete Guide](/blog/user-rules)[Ad SlotAvailable📢 Advertise Your Tool Here🚀 Reach 16K+ AI developers•Learn more →](/advertise)[Ad SlotAvailable Now📢 Advertise Your Tool Here🚀 Reach 16K+ AI developers•Learn more →](/advertise)[🪐 Antigravity.Codes](/)

Your complete community guide to Google Antigravity IDE. Learn, build, and master agent-first development with Gemini 3.

[Download Now](/download)[Get Started](/tutorial)
#### Resources

[Tutorial](/tutorial)[Download](/download)[Troubleshooting](/troubleshooting)[Coding Rules](/rules)[Blog](/blog)
#### Company

[About Us](/about-us)[Contact](/contact-us)[Advertise With Us](/advertise)[Privacy Policy](/privacy-policy)[Terms of Service](/terms-of-service)[Disclaimer](/disclaimer)

Featured On

[![Startup Fame](https://startupfa.me/badges/featured-badge-small.webp)](https://startupfa.me/s/antigravity?utm_source=antigravity.codes)[![Twelve Tools](https://twelve.tools/badge0-dark.svg)](https://twelve.tools)[![Turbo0](https://img.turbo0.com/badge-listed-dark.svg)](https://turbo0.com/item/antigravity-codes)[![Findly](https://findly.tools/badges/findly-tools-badge-dark.svg)](https://findly.tools/antigravity-codes?utm_source=antigravity-codes)[![Wired Business](https://wired.business/badge0-dark.svg)](https://wired.business)[![Aura++](https://auraplusplus.com/images/badges/featured-on-dark.svg)](https://auraplusplus.com/projects/antigravity-codes)[![Fazier](https://fazier.com/api/v1//public/badges/launch_badges.svg?badge_type=launched&theme=dark)](https://fazier.com/launches/antigravity.codes)[![Verified Tools](https://www.verifiedtools.info/badge.png)](https://www.verifiedtools.info)[![That App Show](https://thatappshow.com/assets/images/badge-dark.png)](https://thatappshow.com)[![Startup Fame](https://startupfa.me/badges/featured-badge-small.webp)](https://startupfa.me/s/antigravity?utm_source=antigravity.codes)[![Twelve Tools](https://twelve.tools/badge0-dark.svg)](https://twelve.tools)[![Turbo0](https://img.turbo0.com/badge-listed-dark.svg)](https://turbo0.com/item/antigravity-codes)[![Findly](https://findly.tools/badges/findly-tools-badge-dark.svg)](https://findly.tools/antigravity-codes?utm_source=antigravity-codes)[![Wired Business](https://wired.business/badge0-dark.svg)](https://wired.business)[![Aura++](https://auraplusplus.com/images/badges/featured-on-dark.svg)](https://auraplusplus.com/projects/antigravity-codes)[![Fazier](https://fazier.com/api/v1//public/badges/launch_badges.svg?badge_type=launched&theme=dark)](https://fazier.com/launches/antigravity.codes)[![Verified Tools](https://www.verifiedtools.info/badge.png)](https://www.verifiedtools.info)[![That App Show](https://thatappshow.com/assets/images/badge-dark.png)](https://thatappshow.com)

© 2025 Antigravity.Codes. A community resource for Google Antigravity IDE.

This website is not affiliated with, endorsed by, or associated with Google LLC. "Google" and "Gemini" are trademarks of Google LLC.


