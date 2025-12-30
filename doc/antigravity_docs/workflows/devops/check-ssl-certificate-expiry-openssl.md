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
[Back to 🚢 DevOps & Deployment](/workflows/devops)
# Check SSL Certificates

SecurityDevOpsSSLDownloadCopy Workflow---
description: Verify SSL certificate validity and expiration
---

1. \*\*Check Expiry\*\*:
 - Use openssl to check a domain. Replace `google.com` with your domain.
 // turbo
 - Run `echo | openssl s_client -servername google.com -connect google.com:443 2>/dev/null | openssl x509 -noout -dates`

2. \*\*Pro Tips\*\*:
 - Set up a monitoring alert (like UptimeRobot) to notify you 7 days before expiry.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `check-ssl-certificate-expiry-openssl.md`
4. In Antigravity, type `/check_ssl_certificate_expiry_openssl` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Implement Feature Flags

Feature FlagsDeploymentA/B Testing+1--- description: Safely release features with toggles for gradual rollouts --- 1. \*\*Simple Approach: Environment Variables\*\*: - Use env vars for basic flags. ```ts // lib/features.ts export const features = { newDashboard: process.env.NEXT\_PUBLIC\_FEATURE\_NEW\_DASHBOARD === 'true', ...](/workflows/devops/implement-feature-flags-gradual-rollout)[### Implement Blue-Green Deployment

DeploymentDevOpsZero-Downtime--- description: Zero-downtime deploys --- 1. \*\*Setup Two Environments\*\*: - Blue: Current (v1.0) - Green: New (v1.1) 2. \*\*Route Traffic Gradually\*\*: ```ts const rolloutPercent = await get('green\_rollout') || 0; if (Math.random() \* 100 < rolloutPercent) { return NextResponse.rew...](/workflows/devops/implement-blue-green-deployment-strategy)[### Analyze Bundle Size

PerformanceNext.jsOptimization--- description: Visualize and reduce your production build size --- 1. \*\*Install Analyzer\*\*: - Install the Next.js bundle analyzer. // turbo - Run `npm install @next/bundle-analyzer` 2. \*\*Configure next.config.js\*\*: - Wrap your config. ```js const withBundleAnalyzer = require('@...](/workflows/devops/analyze-nextjs-bundle-size-optimization)
## Recommended Rules

[View more rules →](/rules)[### Security & Compliance in DevOps

DevSecOpsSecurityComplianceYou are an expert in DevSecOps, security automation, and compliance. Key Principles: - Shift security left (start early) - Security as Code - Automat...](/rules/devops-infrastructure/devsecops-security-compliance)[### 🔒 Security Audit Agent - Vulnerability Detection

Agentic AISecurityVulnerabilityYou are an expert security audit agent specialized in identifying vulnerabilities and security risks. Apply systematic reasoning following OWASP guide...](/rules/agentic-ai/security-audit-agent)[### 🚀 DevOps & CI/CD Agent - Pipeline Expert

Agentic AIDevOpsCI/CDYou are an expert DevOps and CI/CD agent specialized in designing and implementing robust deployment pipelines and infrastructure. Apply systematic re...](/rules/agentic-ai/devops-cicd-agent)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![BoostSecurity](https://boostsecurity.io/hs-fs/hubfs/blue-logo.png)
### BoostSecurity

Official

Powered by [BoostSecurity](https://boostsecurity.io/), the MCP guardrails coding agents against introducing dependencies with vulnerabilities, malware or typosquatting.](/mcp/boostsecurity)[![Contrast Security](https://contrastsecurity.com/favicon.ico)
### Contrast Security

Official

Brings Contrast's vulnerability and SCA data into your coding agent to quickly remediate vulnerabilities.](/mcp/contrast-security)[![Cycode](https://app.cycode.com/img/favicon.ico)
### Cycode

Official

Boost security in your dev lifecycle via SAST, SCA, Secrets & IaC scanning with [Cycode](https://cycode.com/).](/mcp/cycode)
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


