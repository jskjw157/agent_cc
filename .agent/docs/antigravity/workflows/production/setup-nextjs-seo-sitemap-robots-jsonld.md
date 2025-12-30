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
# Ultimate Next.js SEO Setup

Next.jsSEOProductionMetadataDownloadCopy Workflow---
description: Complete checklist for sitemap, robots, manifest, and JSON-LD
---

1. \*\*Metadata Base (Crucial)\*\*:
 - In `src/app/layout.tsx`, define `metadataBase` to resolve relative URLs.
```
export const metadata: Metadata = {
     metadataBase: new URL('https://acme.com'),
     title: 'Acme Corp',
     // ...
   };
```

2. \*\*Dynamic Sitemap (`sitemap.ts`)\*\*:
 - Create `src/app/sitemap.ts`.
```
import { MetadataRoute } from 'next';

   export default function sitemap(): MetadataRoute.Sitemap {
     return [
       {
         url: 'https://acme.com',
         lastModified: new Date(),
         changeFrequency: 'yearly',
         priority: 1,
       },
       // Add dynamic routes here
     ];
   }
```

3. \*\*Robots.txt (`robots.ts`)\*\*:
 - Create `src/app/robots.ts`.
```
import { MetadataRoute } from 'next';

   export default function robots(): MetadataRoute.Robots {
     return {
       rules: {
         userAgent: '*',
         allow: '/',
         disallow: '/private/',
       },
       sitemap: 'https://acme.com/sitemap.xml',
     };
   }
```

4. \*\*JSON-LD Structured Data\*\*:
 - Add structured data to your `layout.tsx`.
```
<script
     type="application/ld+json"
     dangerouslySetInnerHTML={{
       __html: JSON.stringify({
         '@context': 'https://schema.org',
         '@type': 'Organization',
         name: 'Acme Corp',
         url: 'https://acme.com',
         logo: 'https://acme.com/logo.png',
       }),
     }}
   />
```

5. \*\*Pro Tips\*\*:
 - Use \*\*Open Graph\*\* image generation (`opengraph-image.tsx`).
 - Verify with \*\*Google Search Console\*\*.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `setup-nextjs-seo-sitemap-robots-jsonld.md`
4. In Antigravity, type `/setup_nextjs_seo_sitemap_robots_jsonld` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Core Web Vitals Optimizer

PerformanceLCPCLS+1--- description: Audit and fix LCP, CLS, and INP issues for better ranking --- 1. \*\*Fix LCP (Large Contentful Paint)\*\*: - The largest element (usually the hero image) must load fast. - \*\*Fix:\*\* Add `priority` to your Hero image. ```tsx <Image src="/hero.png" alt="Hero" width={800} heigh...](/workflows/production/optimize-core-web-vitals-lcp-cls-inp)[### Security Hardening Checklist

SecurityHeadersCSP+1--- description: Essential security headers, CSP, and rate limiting --- 1. \*\*Security Headers (`next.config.js`)\*\*: - Add these headers to prevent common attacks. ```js module.exports = { async headers() { return [ { source: '/:path\*', headers: [ ...](/workflows/production/security-hardening-headers-csp-rate-limiting)[### Implement Rate Limiting

SecurityRate LimitingAPI--- description: Protect APIs with rate limits --- 1. \*\*Install Upstash\*\*: // turbo - Run `npm install @upstash/ratelimit @upstash/redis` 2. \*\*Setup\*\*: ```ts import { Ratelimit } from '@upstash/ratelimit'; const ratelimit = new Ratelimit({ redis, limiter: Ratelimit.sli...](/workflows/production/implement-api-rate-limiting-upstash-redis)
## Recommended Rules

[View more rules →](/rules)[### Next.js SEO & Metadata Expert

Next.jsSEOMetadataYou are an expert in Next.js SEO and metadata optimization. Key Principles: - Use Metadata API for SEO - Implement dynamic metadata - Use proper Open...](/rules/nextjs/nextjs-seo-metadata)[### Next.js App Router Best Practices

Next.jsApp RouterRoutingYou are an expert in Next.js App Router. Key Principles: - Use Server Components by default - Use Client Components only when necessary (interactivit...](/rules/nextjs/nextjs-app-router-best-practices)[### Next.js Performance Optimization

Next.jsPerformanceOptimizationYou are an expert in Next.js performance optimization. Key Principles: - Optimize images and fonts - Minimize client-side JavaScript - Use proper cac...](/rules/nextjs/nextjs-performance-optimization)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![Alibaba Cloud AnalyticDB for MySQL](https://img.alicdn.com/imgextra/i4/O1CN01epkXwH1WLAXkZfV6N_!!6000000002771-2-tps-200-200.png)
### Alibaba Cloud AnalyticDB for MySQL

Official

Connect to an [AnalyticDB for MySQL](https://www.alibabacloud.com/en/product/analyticdb-for-mysql) cluster for getting database or table metadata, querying and analyzing data. It will be supported to add the OpenAPI for cluster operation in the future.](/mcp/alibaba-cloud-analyticdb-for-mysql)[![DataHub](https://datahub.com/wp-content/uploads/2025/04/cropped-Artboard-1-32x32.png)
### DataHub

Official

Search your data assets, traverse data lineage, write SQL queries, and more using [DataHub](https://datahub.com/) metadata.](/mcp/datahub)[![fetchSERP](https://fetchserp.com/icon.png)
### fetchSERP

Official

All-in-One SEO & Web Intelligence Toolkit API [fetchSERP](https://www.fetchserp.com/)](/mcp/fetchserp)
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


