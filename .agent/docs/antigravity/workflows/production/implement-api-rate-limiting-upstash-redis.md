[![Antigravity Logo](/logo.svg)Antigravity Codes](/)[Tutorial](/tutorial)[Download](/download)[Help](/troubleshooting)[Blog](/blog)[Community](/community)[Rules](/rules)[Workflows](/workflows)[MCPs](/mcp)[Advertise](/advertise)[Tutorial](/tutorial)[Download](/download)[Help](/troubleshooting)[Blog](/blog)[Community](/community)[Rules](/rules)[Workflows](/workflows)[MCPs](/mcp)[Advertise](/advertise)

* [All Workflows75](/workflows)
* [🚑 Emergency Room3](/workflows/emergency)
* [🚀 Production Readiness6](/workflows/production)
* [🛠️ Integrations & Setup6](/workflows/integrations)
* [💻 Local Dev Environment12](/workflows/local-dev)
* [🚢 DevOps & Deployment10](/workflows/devops)
* [🐛 Debugging & QA13](/workflows/qa-debugging)
* [✨ Feature Scaffolding5](/workflows/features)
* [⚡ Performance & Optimization9](/workflows/performance-optimization)
* [🧪 Testing & Monitoring3](/workflows/testing-monitoring)
* [🔧 Developer Experience8](/workflows/developer-experience)
[Back to 🚀 Production Readiness](/workflows/production)
# Implement Rate Limiting

SecurityRate LimitingAPIDownloadCopy Workflow---
description: Protect APIs with rate limits
---

1. \*\*Install Upstash\*\*:
 // turbo
 - Run `npm install @upstash/ratelimit @upstash/redis`

2. \*\*Setup\*\*:
```
import { Ratelimit } from '@upstash/ratelimit';

   const ratelimit = new Ratelimit({
     redis,
     limiter: Ratelimit.slidingWindow(10, '10 s')
   });
```

3. \*\*Apply to Routes\*\*:
```
const { success } = await ratelimit.limit(ip);
   if (!success) return Response.json({ error: 'Too many requests' }, { status: 429 });
```

4. \*\*Pro Tips\*\*:
 - Different limits per endpoint.
 - Log violations.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `implement-api-rate-limiting-upstash-redis.md`
4. In Antigravity, type `/implement_api_rate_limiting_upstash_redis` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Secure API from CSRF

SecurityCSRFAPI--- description: Prevent CSRF attacks --- 1. \*\*Use SameSite Cookies\*\*: ```ts response.headers.set('Set-Cookie', 'token=abc; SameSite=Strict; HttpOnly'); ``` 2. \*\*Implement CSRF Tokens\*\*: ```ts import { randomBytes } from 'crypto'; export function generateCSRFToken() { return...](/workflows/production/secure-api-csrf-protection-samesite-cookies)[### Security Hardening Checklist

SecurityHeadersCSP+1--- description: Essential security headers, CSP, and rate limiting --- 1. \*\*Security Headers (`next.config.js`)\*\*: - Add these headers to prevent common attacks. ```js module.exports = { async headers() { return [ { source: '/:path\*', headers: [ ...](/workflows/production/security-hardening-headers-csp-rate-limiting)[### Setup RBAC

SecurityAuthorizationRBAC--- description: Role-based permissions --- 1. \*\*Define Roles\*\*: ```prisma enum Role { USER ADMIN MODERATOR } ``` 2. \*\*Protect Routes\*\*: ```ts if (session?.user?.role !== 'ADMIN') { return Response.json({ error: 'Forbidden' }, { status: 403 }); } ``` 3....](/workflows/production/setup-role-based-access-control-rbac)
## Recommended Rules

[View more rules →](/rules)[### 🔒 Security Audit Agent - Vulnerability Detection

Agentic AISecurityVulnerabilityYou are an expert security audit agent specialized in identifying vulnerabilities and security risks. Apply systematic reasoning following OWASP guide...](/rules/agentic-ai/security-audit-agent)[### Python Security Best Practices

PythonSecurityCryptographyYou are an expert in Python security and secure coding practices. Key Principles: - Never trust user input - Use principle of least privilege - Keep ...](/rules/python/python-security-best-practices)[### Web Security Best Practices Expert

SecurityWeb DevelopmentOWASPYou are an expert in web security and secure coding practices. Key Principles: - Follow OWASP Top 10 guidelines - Implement defense in depth - Valida...](/rules/web-development/web-security-best-practices)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![GitGuardian](https://cdn.prod.website-files.com/5ee25cbe47310017adf964da/6323888a9b9f4e22a7bc766b_GG%20Favicon.svg)
### GitGuardian

Official

GitGuardian official MCP server - Scan projects using GitGuardian's industry-leading API, which features over 500 secret detectors to prevent credential leaks before they reach public repositories. Resolve security incidents directly with rich contextual data for rapid, automated remediation.](/mcp/gitguardian)[D
### Dataverse DevTools MCP Server

Community

An MCP server exposing ready-to-use Dataverse/Dynamics 365 tools for user and security administration, data operations, Web API executions, metadata exploration, and troubleshooting.](/mcp/dataverse-devtools-mcp-server)[![Codacy](https://app.codacy.com/static/images/favicon-16x16.png)
### Codacy

Official

Interact with [Codacy](https://www.codacy.com) API to query code quality issues, vulnerabilities, and coverage insights about your code.](/mcp/codacy)
### Take It Further

Maximize your productivity with these powerful resources

[📋
#### Define Your Standards

Set up coding standards to ensure this workflow produces consistent, high-quality results.

Browse Rules Library](/rules)[📖
#### Master Workflows

Learn how to create custom workflows, use Turbo Mode, and build your automation library.

Complete Guide](/blog/workflows)[Ad SlotAvailable📢 Advertise Your Tool Here🚀 Reach 16K+ AI developers•Learn more →](/advertise)[Ad SlotAvailable Now📢 Advertise Your Tool Here🚀 Reach 16K+ AI developers•Learn more →](/advertise)[🪐 Antigravity.Codes](/)

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


