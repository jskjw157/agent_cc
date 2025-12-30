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
[Back to 🚑 Emergency Room](/workflows/emergency)
# Nuke & Reinstall

npmTroubleshootingDependenciesTurboDownloadCopy Workflow---
description: The nuclear option for when dependencies are completely broken
---

1. \*\*Remove node\_modules\*\*:
 - Delete the existing `node_modules` folder to clear installed packages.
 // turbo
 - Run `rm -rf node_modules`

2. \*\*Remove Lock File\*\*:
 - Delete `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, or `bun.lockb`.
 // turbo
 - Run `rm package-lock.json yarn.lock pnpm-lock.yaml bun.lockb`

3. \*\*Clean Cache\*\*:
 - Clean the package manager cache.
 // turbo
 - Run `npm cache clean --force`

4. \*\*Reinstall Dependencies\*\*:
 - Install dependencies from scratch.
 // turbo
 - Run `npm install`

5. \*\*Pro Tips\*\*:
 - \*\*Yarn:\*\* `yarn install`
 - \*\*pnpm:\*\* `pnpm install`
 - \*\*Bun:\*\* `bun install`
 - Restart your VS Code window after this to ensure the TypeScript server picks up the new modules.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `nuke-node-modules-and-reinstall-dependencies.md`
4. In Antigravity, type `/nuke_node_modules_and_reinstall_dependencies` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Fix Next.js Hydration Errors

Next.jsDebuggingHydration+1--- description: Systematically debug and fix 'Text content does not match server-rendered HTML' errors --- 1. \*\*Check for Invalid HTML Nesting\*\*: - The most common cause is invalid HTML, like a `<div>` inside a `<p>` tag. - \*\*React 19 Update:\*\* React 19 provides much better hydration error d...](/workflows/emergency/fix-nextjs-hydration-error-text-content-mismatch)[### Debugging Infinite Re-renders

ReactDebuggingPerformance+1--- description: Track down and fix infinite loops in useEffect and component rendering --- 1. \*\*Check `useEffect` Dependencies\*\*: - The most common culprit is a `useEffect` that updates a state variable which is also in its dependency array. - \*\*Bad Pattern:\*\* ```tsx useEffect(() =...](/workflows/emergency/debug-react-infinite-rerenders-useeffect-loop)
## Recommended Rules

[View more rules →](/rules)[### 🐛 Debugging Agent - Systematic Bug Hunter

Agentic AIDebuggingTroubleshootingYou are an expert debugging agent specialized in systematic bug hunting and root cause analysis. Apply rigorous reasoning to identify, isolate, and fi...](/rules/agentic-ai/debugging-agent)[### 📦 Code Migration Agent - Safe Upgrade Expert

Agentic AIMigrationUpgradeYou are an expert code migration agent specialized in safely upgrading frameworks, languages, and dependencies. Apply systematic reasoning to plan and...](/rules/agentic-ai/code-migration-agent)[### Dependency Reset Workflow

WorkflowsNode.jsTroubleshootingFix "it works on my machine" issues by resetting dependencies. Workflow File: .agent/workflows/reset\_deps.md ```markdown --- description: Completely...](/rules/antigravity-workflows/dependency-reset-workflow)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![BoostSecurity](https://boostsecurity.io/hs-fs/hubfs/blue-logo.png)
### BoostSecurity

Official

Powered by [BoostSecurity](https://boostsecurity.io/), the MCP guardrails coding agents against introducing dependencies with vulnerabilities, malware or typosquatting.](/mcp/boostsecurity)[![CodeLogic](https://codelogic.com/wp-content/themes/codelogic/assets/img/favicon.png)
### CodeLogic

Official

Interact with [CodeLogic](https://codelogic.com), a Software Intelligence platform that graphs complex code and data architecture dependencies, to boost AI accuracy and insight.](/mcp/codelogic)[![YepCode](https://cdn.prod.website-files.com/632cd328ed2b485519c3f689/6334977a5d1a542102d4b9b5_favicon-32x32.png)
### YepCode

Official

Run code in a secure, scalable sandbox environment with full support for dependencies, secrets, logs, and access to APIs or databases. Powered by [YepCode](https://yepcode.io)](/mcp/yepcode)
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


