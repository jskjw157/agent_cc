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
# Security Hardening Checklist

SecurityHeadersCSPProductionDownloadCopy Workflow---
description: Essential security headers, CSP, and rate limiting
---

1. \*\*Security Headers (`next.config.js`)\*\*:
 - Add these headers to prevent common attacks.
```
module.exports = {
     async headers() {
       return [
         {
           source: '/:path*',
           headers: [
             { key: 'X-DNS-Prefetch-Control', value: 'on' },
             { key: 'Strict-Transport-Security', value: 'max-age=63072000; includeSubDomains; preload' },
             { key: 'X-Content-Type-Options', value: 'nosniff' },
             { key: 'X-Frame-Options', value: 'SAMEORIGIN' },
             { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' }
           ]
         }
       ]
     }
   }
```

2. \*\*Content Security Policy (CSP)\*\*:
 - Create `src/middleware.ts`.
```
import { NextResponse } from 'next/server';
   import type { NextRequest } from 'next/server';

   export function middleware(request: NextRequest) {
     const nonce = Buffer.from(crypto.randomUUID()).toString('base64');
     const cspHeader =
       default-src 'self';
       script-src 'self' 'nonce-${nonce}' 'strict-dynamic';
       style-src 'self' 'nonce-${nonce}';
       img-src 'self' blob: data:;
       font-src 'self';
       object-src 'none';
       base-uri 'self';
       form-action 'self';
       frame-ancestors 'none';
       upgrade-insecure-requests;
     .replace(/\s{2,}/g, ' ').trim();

     const requestHeaders = new Headers(request.headers);
     requestHeaders.set('x-nonce', nonce);
     requestHeaders.set('Content-Security-Policy', cspHeader);

     const response = NextResponse.next({
       request: {
         headers: requestHeaders,
       },
     });
     response.headers.set('Content-Security-Policy', cspHeader);
     return response;
   }
```

3. \*\*Rate Limiting (API Routes)\*\*:
 - Prevent abuse with simple in-memory rate limiting.
```
// lib/rate-limit.ts
   const rateLimit = new Map();

   export function checkRateLimit(ip: string, limit = 10) {
     const now = Date.now();
     const windowMs = 60 * 1000; // 1 minute
     const record = rateLimit.get(ip) || { count: 0, resetTime: now + windowMs };

     if (now > record.resetTime) {
       record.count = 1;
       record.resetTime = now + windowMs;
     } else {
       record.count++;
     }

     rateLimit.set(ip, record);
     return record.count <= limit;
   }
```

4. \*\*Pro Tips\*\*:
 - Never commit `.env` files.
 - Regularly audit your dependencies: `npm audit fix`.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `security-hardening-headers-csp-rate-limiting.md`
4. In Antigravity, type `/security_hardening_headers_csp_rate_limiting` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Ultimate Next.js SEO Setup

Next.jsSEOProduction+1--- description: Complete checklist for sitemap, robots, manifest, and JSON-LD --- 1. \*\*Metadata Base (Crucial)\*\*: - In `src/app/layout.tsx`, define `metadataBase` to resolve relative URLs. ```tsx export const metadata: Metadata = { metadataBase: new URL('https://acme.com'), titl...](/workflows/production/setup-nextjs-seo-sitemap-robots-jsonld)[### Implement Rate Limiting

SecurityRate LimitingAPI--- description: Protect APIs with rate limits --- 1. \*\*Install Upstash\*\*: // turbo - Run `npm install @upstash/ratelimit @upstash/redis` 2. \*\*Setup\*\*: ```ts import { Ratelimit } from '@upstash/ratelimit'; const ratelimit = new Ratelimit({ redis, limiter: Ratelimit.sli...](/workflows/production/implement-api-rate-limiting-upstash-redis)[### Setup RBAC

SecurityAuthorizationRBAC--- description: Role-based permissions --- 1. \*\*Define Roles\*\*: ```prisma enum Role { USER ADMIN MODERATOR } ``` 2. \*\*Protect Routes\*\*: ```ts if (session?.user?.role !== 'ADMIN') { return Response.json({ error: 'Forbidden' }, { status: 403 }); } ``` 3....](/workflows/production/setup-role-based-access-control-rbac)
## Recommended Rules

[View more rules →](/rules)[### 🔒 Security Audit Agent - Vulnerability Detection

Agentic AISecurityVulnerabilityYou are an expert security audit agent specialized in identifying vulnerabilities and security risks. Apply systematic reasoning following OWASP guide...](/rules/agentic-ai/security-audit-agent)[### Python Security Best Practices

PythonSecurityCryptographyYou are an expert in Python security and secure coding practices. Key Principles: - Never trust user input - Use principle of least privilege - Keep ...](/rules/python/python-security-best-practices)[### Web Security Best Practices Expert

SecurityWeb DevelopmentOWASPYou are an expert in web security and secure coding practices. Key Principles: - Follow OWASP Top 10 guidelines - Implement defense in depth - Valida...](/rules/web-development/web-security-best-practices)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![BoostSecurity](https://boostsecurity.io/hs-fs/hubfs/blue-logo.png)
### BoostSecurity

Official

Powered by [BoostSecurity](https://boostsecurity.io/), the MCP guardrails coding agents against introducing dependencies with vulnerabilities, malware or typosquatting.](/mcp/boostsecurity)[![Contrast Security](https://contrastsecurity.com/favicon.ico)
### Contrast Security

Official

Brings Contrast's vulnerability and SCA data into your coding agent to quickly remediate vulnerabilities.](/mcp/contrast-security)[![CrowdStrike Falcon](https://www.crowdstrike.com/etc.clientlibs/crowdstrike/clientlibs/crowdstrike-common/resources/favicon.ico)
### CrowdStrike Falcon

Official

Connects AI agents with the CrowdStrike Falcon platform for intelligent security analysis, providing programmatic access to detections, incidents, behaviors, threat intelligence, hosts, vulnerabilities, and identity protection capabilities.](/mcp/crowdstrike-falcon)
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


