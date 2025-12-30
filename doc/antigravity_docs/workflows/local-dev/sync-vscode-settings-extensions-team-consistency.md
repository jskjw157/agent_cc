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
# VS Code Settings Sync

VS CodeDXConfigDownloadCopy Workflow---
description: Standardize VS Code settings across the team
---

1. \*\*Create settings.json\*\*:
 - Create `.vscode/settings.json` for workspace-specific settings.
 // turbo
 - Run `mkdir -p .vscode && printf '{\n "editor.formatOnSave": true,\n "editor.defaultFormatter": "esbenp.prettier-vscode",\n "editor.codeActionsOnSave": {\n "source.fixAll.eslint": true\n }\n}' > .vscode/settings.json`

2. \*\*Create extensions.json\*\*:
 - Recommend extensions for the team.
 // turbo
 - Run `printf '{\n "recommendations": [\n "dbaeumer.vscode-eslint",\n "esbenp.prettier-vscode",\n "bradlc.vscode-tailwindcss"\n ]\n}' > .vscode/extensions.json`

3. \*\*Pro Tips\*\*:
 - Commit the `.vscode` folder (excluding user-specific files) to git.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `sync-vscode-settings-extensions-team-consistency.md`
4. In Antigravity, type `/sync_vscode_settings_extensions_team_consistency` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Generate .env from Example

ConfigEnvironmentSetup--- description: Safely create a local .env file from .env.example --- 1. \*\*Check for .env.example\*\*: - Ensure the example file exists. // turbo - Run `test -f .env.example && echo "✅ Found .env.example" || echo "❌ .env.example not found"` 2. \*\*Copy to .env.local\*\*: - Create your local...](/workflows/local-dev/generate-local-env-file-from-example)[### Generate TypeScript Types from API

TypeScriptAPICodegen+1--- description: Auto-generate type-safe API client from OpenAPI/Swagger spec --- 1. \*\*Get Your API Schema\*\*: - Most APIs expose OpenAPI spec at `/swagger.json` or `/openapi.json`. - Download it or use the URL directly. 2. \*\*Install openapi-typescript\*\*: - Best tool for generating types. ...](/workflows/local-dev/generate-typescript-types-from-openapi-schema)[### Kill Port 3000

DevOpsTerminalProcess--- description: Instantly find and kill the process hogging your dev port --- 1. \*\*The Best Way (Cross-Platform)\*\*: - Kill it in one command using npx. Works on Mac, Windows, and Linux. // turbo - Run `npx kill-port 3000` 2. \*\*Mac/Linux Manual Method\*\*: - Find PID: `lsof -ti:3000` ...](/workflows/local-dev/kill-process-on-port-3000-terminal-command)
## Recommended Rules

[View more rules →](/rules)[### Google Cloud Platform Expert

GCPGoogle CloudCloudYou are an expert in Google Cloud Platform (GCP) services and architecture. Key Principles: - Leverage Google's global infrastructure - Use managed o...](/rules/devops-infrastructure/google-cloud-platform-expert)[### Monitoring & Observability (Prometheus, Grafana)

MonitoringObservabilityPrometheusYou are an expert in Monitoring and Observability using Prometheus and Grafana. Key Principles: - Monitor the four golden signals (Latency, Traffic, ...](/rules/devops-infrastructure/monitoring-observability-prometheus-grafana)[### GitOps & ArgoCD Expert

GitOpsArgoCDKubernetesYou are an expert in GitOps methodology and ArgoCD. Key Principles: - Git as the single source of truth - Declarative infrastructure and applications...](/rules/devops-infrastructure/gitops-argocd-expert)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[A
### Algolia

Official

Use AI agents to provision, configure, and query your [Algolia](https://algolia.com) search indices.](/mcp/algolia)[![Chiki StudIO](https://cdn.chiki.studio/brand/logo.png)
### Chiki StudIO

Official

Create your own configurable MCP servers purely via configuration (no code), with instructions, prompts, and tools support.](/mcp/chiki-studio)[![Cloudflare](https://cdn.simpleicons.org/cloudflare)
### Cloudflare

Official

Deploy, configure & interrogate your resources on the Cloudflare developer platform (e.g. Workers/KV/R2/D1)](/mcp/cloudflare)
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


