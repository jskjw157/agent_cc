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
[Back to 💻 Local Dev Environment](/workflows/local-dev)
# Update All Dependencies

npmMaintenanceUpdatesDownloadCopy Workflow---
description: Interactively check and update outdated packages
---

1. \*\*Check for Updates\*\*:
 - Use `npm-check-updates` to see what's new.
 // turbo
 - Run `npx npm-check-updates`

2. \*\*Review Changes\*\*:
 - ⚠️ \*\*WARNING\*\*: Always review major version changes before updating!
 - Check changelogs for breaking changes.
 - Look for major version bumps (e.g., 1.x.x → 2.x.x).

3. \*\*Update package.json\*\*:
 - Update versions in your package file.
 // turbo
 - Run `npx npm-check-updates -u`

4. \*\*Install New Versions\*\*:
 - Install the updated packages.
 // turbo
 - Run `npm install`

5. \*\*Test Thoroughly\*\*:
 - Run your tests immediately after updating.
 // turbo
 - Run `npm test`

6. \*\*Pro Tips\*\*:
 - Use `-i` for interactive mode to selectively update: `npx ncu -i`.
 - Update only minor/patch versions: `npx ncu -u --target minor`.
 - Check for peer dependency conflicts with `npm ls`.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `update-npm-dependencies-check-updates.md`
4. In Antigravity, type `/update_npm_dependencies_check_updates` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Kill Port 3000

DevOpsTerminalProcess--- description: Instantly find and kill the process hogging your dev port --- 1. \*\*The Best Way (Cross-Platform)\*\*: - Kill it in one command using npx. Works on Mac, Windows, and Linux. // turbo - Run `npx kill-port 3000` 2. \*\*Mac/Linux Manual Method\*\*: - Find PID: `lsof -ti:3000` ...](/workflows/local-dev/kill-process-on-port-3000-terminal-command)[### Generate .env from Example

ConfigEnvironmentSetup--- description: Safely create a local .env file from .env.example --- 1. \*\*Check for .env.example\*\*: - Ensure the example file exists. // turbo - Run `test -f .env.example && echo "✅ Found .env.example" || echo "❌ .env.example not found"` 2. \*\*Copy to .env.local\*\*: - Create your local...](/workflows/local-dev/generate-local-env-file-from-example)[### Prune Docker System

DockerCleanupDisk Space--- description: Reclaim disk space by removing unused containers and images --- 1. \*\*Check Current Usage\*\*: - See how much space Docker is using. // turbo - Run `docker system df` 2. \*\*Run Prune\*\*: - ⚠️ \*\*WARNING\*\*: This will remove all stopped containers and unused images! - Remov...](/workflows/local-dev/prune-docker-system-remove-unused-containers)
## Recommended Rules

[View more rules →](/rules)[### iOS Swift Development

iOSSwiftSwiftUIYou are an expert in iOS development using Swift and SwiftUI/UIKit. Key Principles: - Follow Apple's Human Interface Guidelines (HIG) - Write safe, f...](/rules/mobile-development/ios-swift-development)[### Android Kotlin Development

AndroidKotlinJetpack ComposeYou are an expert in Android development using Kotlin and Jetpack Compose. Key Principles: - Follow Material Design guidelines - Build responsive and...](/rules/mobile-development/android-kotlin-development)[### Mobile UI/UX Best Practices

UI/UXMobileDesignYou are an expert in Mobile UI/UX design and implementation. Key Principles: - Design for touch (fingers are not cursors) - Content first, chrome sec...](/rules/mobile-development/mobile-ui-ux-best-practices)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[C
### ClickUp

Community

MCP server for ClickUp task management, supporting task creation, updates, bulk operations, and markdown descriptions.](/mcp/clickup)[C
### Cursor MCP Installer

Community

A tool to easily install and configure other MCP servers within Cursor IDE, with support for npm packages, local directories, and Git repositories.](/mcp/cursor-mcp-installer)[l
### lucid-mcp-server

Community

An MCP server for Lucidchart and Lucidspark: connect, search, and obtain text representations of your Lucid documents and diagrams via LLM - driven AI Vision analysis. [npm](https://www.npmjs.com/package/lucid-mcp-server)](/mcp/lucid-mcp-server)
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


