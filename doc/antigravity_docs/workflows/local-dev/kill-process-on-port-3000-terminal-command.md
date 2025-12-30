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
# Kill Port 3000

DevOpsTerminalProcessDownloadCopy Workflow---
description: Instantly find and kill the process hogging your dev port
---

1. \*\*The Best Way (Cross-Platform)\*\*:
 - Kill it in one command using npx. Works on Mac, Windows, and Linux.
 // turbo
 - Run `npx kill-port 3000`

2. \*\*Mac/Linux Manual Method\*\*:
 - Find PID: `lsof -ti:3000`
 - Kill it: `kill -9 $(lsof -ti:3000)`

3. \*\*Windows Manual Method\*\*:
 - Find PID: `netstat -ano | findstr :3000`
 - Kill it: `taskkill /PID <PID> /F`

4. \*\*Pro Tips\*\*:
 - This works for any port, just change 3000 to whatever you need.
 - Add an alias to your shell profile: `alias kill3000="npx kill-port 3000"`.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `kill-process-on-port-3000-terminal-command.md`
4. In Antigravity, type `/kill_process_on_port_3000_terminal_command` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Setup Environment Variables Per Branch

DevOpsEnvironmentVercel+1--- description: Configure different env vars for dev, staging, and production --- 1. \*\*Local Development (.env.local)\*\*: - Create `.env.local` for local overrides (never commit this). ```bash # .env.local DATABASE\_URL=postgresql://localhost:5432/mydb API\_URL=http://localhost:3001 ...](/workflows/local-dev/setup-environment-variables-per-branch-vercel)[### Generate .env from Example

ConfigEnvironmentSetup--- description: Safely create a local .env file from .env.example --- 1. \*\*Check for .env.example\*\*: - Ensure the example file exists. // turbo - Run `test -f .env.example && echo "✅ Found .env.example" || echo "❌ .env.example not found"` 2. \*\*Copy to .env.local\*\*: - Create your local...](/workflows/local-dev/generate-local-env-file-from-example)[### Prune Docker System

DockerCleanupDisk Space--- description: Reclaim disk space by removing unused containers and images --- 1. \*\*Check Current Usage\*\*: - See how much space Docker is using. // turbo - Run `docker system df` 2. \*\*Run Prune\*\*: - ⚠️ \*\*WARNING\*\*: This will remove all stopped containers and unused images! - Remov...](/workflows/local-dev/prune-docker-system-remove-unused-containers)
## Recommended Rules

[View more rules →](/rules)[### 🚀 DevOps & CI/CD Agent - Pipeline Expert

Agentic AIDevOpsCI/CDYou are an expert DevOps and CI/CD agent specialized in designing and implementing robust deployment pipelines and infrastructure. Apply systematic re...](/rules/agentic-ai/devops-cicd-agent)[### Python DevOps & Infrastructure Automation

PythonDevOpsInfrastructureYou are an expert in Python for DevOps, infrastructure automation, and CI/CD. Key Principles: - Automate repetitive tasks - Use infrastructure as cod...](/rules/python/python-devops-and-infrastructure)[### Next.js Deployment & DevOps Expert

Next.jsDeploymentDevOpsYou are an expert in Next.js deployment and DevOps practices. Key Principles: - Use Vercel for optimal Next.js hosting - Implement proper CI/CD pipel...](/rules/nextjs/nextjs-deployment-devops)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![APIMatic MCP](https://2052727.fs1.hubspotusercontent-na1.net/hubfs/2052727/cropped-cropped-apimaticio-favicon-1-32x32.png)
### APIMatic MCP

Official

APIMatic MCP Server is used to validate OpenAPI specifications using [APIMatic](https://www.apimatic.io/). The server processes OpenAPI files and returns validation summaries by leveraging APIMatic's API.](/mcp/apimatic-mcp)[![Azure DevOps](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/1062064-Products-1.2-24x24)
### Azure DevOps

Official

Interact with Azure DevOps services like repositories, work items, builds, releases, test plans, and code search.](/mcp/azure-devops)[![Netdata](https://www.netdata.cloud/favicon-32x32.png)
### Netdata

Official

Discovery, exploration, reporting and root cause analysis using all observability data, including metrics, logs, systems, containers, processes, and network connections](/mcp/netdata)
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


