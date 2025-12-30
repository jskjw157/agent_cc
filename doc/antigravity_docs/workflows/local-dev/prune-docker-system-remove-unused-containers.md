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
# Prune Docker System

DockerCleanupDisk SpaceDownloadCopy Workflow---
description: Reclaim disk space by removing unused containers and images
---

1. \*\*Check Current Usage\*\*:
 - See how much space Docker is using.
 // turbo
 - Run `docker system df`

2. \*\*Run Prune\*\*:
 - ⚠️ \*\*WARNING\*\*: This will remove all stopped containers and unused images!
 - Remove all stopped containers, unused networks, and dangling images.
 // turbo
 - Run `docker system prune -a`

3. \*\*Verify Space Reclaimed\*\*:
 - Check the new disk usage.
 // turbo
 - Run `docker system df`

4. \*\*Pro Tips\*\*:
 - Add `--volumes` to also delete unused volumes (DATA LOSS WARNING!).
 - To remove only dangling images: `docker image prune`.
 - Set up automatic cleanup: add `"log-opts": {"max-size": "10m"}` to Docker daemon config.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `prune-docker-system-remove-unused-containers.md`
4. In Antigravity, type `/prune_docker_system_remove_unused_containers` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Kill Port 3000

DevOpsTerminalProcess--- description: Instantly find and kill the process hogging your dev port --- 1. \*\*The Best Way (Cross-Platform)\*\*: - Kill it in one command using npx. Works on Mac, Windows, and Linux. // turbo - Run `npx kill-port 3000` 2. \*\*Mac/Linux Manual Method\*\*: - Find PID: `lsof -ti:3000` ...](/workflows/local-dev/kill-process-on-port-3000-terminal-command)[### Generate .env from Example

ConfigEnvironmentSetup--- description: Safely create a local .env file from .env.example --- 1. \*\*Check for .env.example\*\*: - Ensure the example file exists. // turbo - Run `test -f .env.example && echo "✅ Found .env.example" || echo "❌ .env.example not found"` 2. \*\*Copy to .env.local\*\*: - Create your local...](/workflows/local-dev/generate-local-env-file-from-example)[### Update All Dependencies

npmMaintenanceUpdates--- description: Interactively check and update outdated packages --- 1. \*\*Check for Updates\*\*: - Use `npm-check-updates` to see what's new. // turbo - Run `npx npm-check-updates` 2. \*\*Review Changes\*\*: - ⚠️ \*\*WARNING\*\*: Always review major version changes before updating! - Check c...](/workflows/local-dev/update-npm-dependencies-check-updates)
## Recommended Rules

[View more rules →](/rules)[### Docker & Containerization Expert

DockerContainersDevOpsYou are an expert in Docker and containerization technologies. Key Principles: - Build once, run anywhere - Keep images small and secure - Use multi-...](/rules/devops-infrastructure/docker-containerization-expert)[### 🚀 DevOps & CI/CD Agent - Pipeline Expert

Agentic AIDevOpsCI/CDYou are an expert DevOps and CI/CD agent specialized in designing and implementing robust deployment pipelines and infrastructure. Apply systematic re...](/rules/agentic-ai/devops-cicd-agent)[### Strong Reasoner & Planner Agent (Official Google Template)

Agentic AIReasoningPlanningYou are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses. 📋 Source: Google Gemin...](/rules/agentic-ai/strong-reasoner-planner-agent)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![Cleanup Crew](https://cleanupcrew.ai/favicon-light.png)
### Cleanup Crew

Official

Real-time human support service for non-technical founders using AI coding tools. When AI hits a wall, request instant human help directly from your IDE.](/mcp/cleanup-crew)[![Program Integrity Alliance (PIA)](https://programintegrity.org/wp-content/uploads/2024/07/PIA-Favicon.svg)
### Program Integrity Alliance (PIA)

Official

Local and Hosted MCP servers providing AI-friendly access to U.S. Government Open Datasets. Also available on [Docker MCP Catalog](https://hub.docker.com/mcp/explore?search=PIA). See [our website](https://programintegrity.org) for more details.](/mcp/program-integrity-alliance-pia)[A
### AgentMode

Community

Connect to dozens of databases, data warehouses, Github & more, from a single MCP server. Run the Docker image locally, in the cloud, or on-premise.](/mcp/agentmode)
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


