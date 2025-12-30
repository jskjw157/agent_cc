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
# Core Web Vitals Optimizer

PerformanceLCPCLSNext.jsDownloadCopy Workflow---
description: Audit and fix LCP, CLS, and INP issues for better ranking
---

1. \*\*Fix LCP (Large Contentful Paint)\*\*:
 - The largest element (usually the hero image) must load fast.
 - \*\*Fix:\*\* Add `priority` to your Hero image.
```
<Image src="/hero.png" alt="Hero" width={800} height={600} priority />
```

2. \*\*Fix CLS (Cumulative Layout Shift)\*\*:
 - Elements jumping around as they load cause CLS.
 - \*\*Fix:\*\* Always define `width` and `height` for images (or use `fill` with a parent container).
 - \*\*Fix:\*\* Reserve space for ads or dynamic content using CSS `min-height`.

3. \*\*Optimize Fonts\*\*:
 - Fonts loading late cause layout shifts (FOUT/FOIT).
 - \*\*Fix:\*\* Use `next/font` which automatically optimizes and hosts fonts.
```
import { Inter } from 'next/font/google';
   const inter = Inter({ subsets: ['latin'] });
   // Use inter.className in your body or layout
```

4. \*\*Pro Tips\*\*:
 - Run a \*\*Lighthouse\*\* audit in Chrome DevTools (Incognito mode) to get a baseline score.
 - Use `@next/third-parties` to load scripts like Google Analytics efficiently.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `optimize-core-web-vitals-lcp-cls-inp.md`
4. In Antigravity, type `/optimize_core_web_vitals_lcp_cls_inp` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Ultimate Next.js SEO Setup

Next.jsSEOProduction+1--- description: Complete checklist for sitemap, robots, manifest, and JSON-LD --- 1. \*\*Metadata Base (Crucial)\*\*: - In `src/app/layout.tsx`, define `metadataBase` to resolve relative URLs. ```tsx export const metadata: Metadata = { metadataBase: new URL('https://acme.com'), titl...](/workflows/production/setup-nextjs-seo-sitemap-robots-jsonld)[### Security Hardening Checklist

SecurityHeadersCSP+1--- description: Essential security headers, CSP, and rate limiting --- 1. \*\*Security Headers (`next.config.js`)\*\*: - Add these headers to prevent common attacks. ```js module.exports = { async headers() { return [ { source: '/:path\*', headers: [ ...](/workflows/production/security-hardening-headers-csp-rate-limiting)[### Implement Rate Limiting

SecurityRate LimitingAPI--- description: Protect APIs with rate limits --- 1. \*\*Install Upstash\*\*: // turbo - Run `npm install @upstash/ratelimit @upstash/redis` 2. \*\*Setup\*\*: ```ts import { Ratelimit } from '@upstash/ratelimit'; const ratelimit = new Ratelimit({ redis, limiter: Ratelimit.sli...](/workflows/production/implement-api-rate-limiting-upstash-redis)
## Recommended Rules

[View more rules →](/rules)[### Next.js Performance Optimization

Next.jsPerformanceOptimizationYou are an expert in Next.js performance optimization. Key Principles: - Optimize images and fonts - Minimize client-side JavaScript - Use proper cac...](/rules/nextjs/nextjs-performance-optimization)[### ⚡ Performance Optimization Agent - Speed Expert

Agentic AIPerformanceOptimizationYou are an expert performance optimization agent specialized in identifying and fixing performance bottlenecks. Apply systematic reasoning to measure,...](/rules/agentic-ai/performance-optimization-agent)[### Web Performance Optimization Expert

PerformanceWeb VitalsOptimizationYou are an expert in web performance optimization and Core Web Vitals. Key Principles: - Optimize for Core Web Vitals - Minimize Time to First Byte (...](/rules/web-development/web-performance-optimization)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![Momento](https://console.gomomento.com/favicon.ico)
### Momento

Official

Momento Cache lets you quickly improve your performance, reduce costs, and handle load at any scale.](/mcp/momento)[A
### Actor Critic Thinking

Community

Actor-critic thinking for performance evaluation](/mcp/actor-critic-thinking)[A
### AI Endurance

Community

AI-powered training platform for runners, cyclists, and triathletes with over 20 tools for workout management, activity analysis, performance predictions, and recovery tracking.](/mcp/ai-endurance)
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


