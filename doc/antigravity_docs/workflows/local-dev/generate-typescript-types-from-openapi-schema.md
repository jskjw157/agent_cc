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
# Generate TypeScript Types from API

TypeScriptAPICodegenDXDownloadCopy Workflow---
description: Auto-generate type-safe API client from OpenAPI/Swagger spec
---

1. \*\*Get Your API Schema\*\*:
 - Most APIs expose OpenAPI spec at `/swagger.json` or `/openapi.json`.
 - Download it or use the URL directly.

2. \*\*Install openapi-typescript\*\*:
 - Best tool for generating types.
 // turbo
 - Run `npm install --save-dev openapi-typescript`

3. \*\*Generate Types\*\*:
 - Create types from schema URL.
 // turbo
 - Run `npx openapi-typescript https://api.example.com/openapi.json -o src/types/api.ts`

4. \*\*Use Generated Types\*\*:
 - Import and use in your API calls.
```
import type { paths } from './types/api';

   type UserResponse = paths['/users']['get']['responses']['200']['content']['application/json'];

   async function getUsers(): Promise<UserResponse> {
     const res = await fetch('/api/users');
     return res.json();
   }
```

5. \*\*Auto-Regenerate on Change\*\*:
 - Add script to package.json.
```
{
     "scripts": {
       "generate:types": "openapi-typescript https://api.example.com/openapi.json -o src/types/api.ts"
     }
   }
```

6. \*\*Alternative: tRPC\*\*:
 - For Next.js apps, use tRPC for end-to-end type safety.
 // turbo
 - Run `npm install @trpc/server @trpc/client @trpc/react-query @trpc/next`

7. \*\*Pro Tips\*\*:
 - Run `npm run generate:types` before starting development.
 - Commit generated types to git for team consistency.
 - Use `openapi-fetch` for a fully typed fetch wrapper.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `generate-typescript-types-from-openapi-schema.md`
4. In Antigravity, type `/generate_typescript_types_from_openapi_schema` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### VS Code Settings Sync

VS CodeDXConfig--- description: Standardize VS Code settings across the team --- 1. \*\*Create settings.json\*\*: - Create `.vscode/settings.json` for workspace-specific settings. // turbo - Run `mkdir -p .vscode && printf '{\n "editor.formatOnSave": true,\n "editor.defaultFormatter": "esbenp.prettier-vsco...](/workflows/local-dev/sync-vscode-settings-extensions-team-consistency)[### Kill Port 3000

DevOpsTerminalProcess--- description: Instantly find and kill the process hogging your dev port --- 1. \*\*The Best Way (Cross-Platform)\*\*: - Kill it in one command using npx. Works on Mac, Windows, and Linux. // turbo - Run `npx kill-port 3000` 2. \*\*Mac/Linux Manual Method\*\*: - Find PID: `lsof -ti:3000` ...](/workflows/local-dev/kill-process-on-port-3000-terminal-command)[### Generate .env from Example

ConfigEnvironmentSetup--- description: Safely create a local .env file from .env.example --- 1. \*\*Check for .env.example\*\*: - Ensure the example file exists. // turbo - Run `test -f .env.example && echo "✅ Found .env.example" || echo "❌ .env.example not found"` 2. \*\*Copy to .env.local\*\*: - Create your local...](/workflows/local-dev/generate-local-env-file-from-example)
## Recommended Rules

[View more rules →](/rules)[### NestJS TypeScript Backend Expert

TypeScriptNestJSBackendYou are an expert in NestJS backend development with TypeScript. Key Principles: - Use decorators with proper TypeScript types - Leverage dependency ...](/rules/typescript/nestjs-typescript-backend)[### GraphQL with TypeScript Expert

TypeScriptGraphQLAPIYou are an expert in GraphQL development with TypeScript. Key Principles: - Use GraphQL Code Generator for type safety - Type all resolvers and queri...](/rules/typescript/graphql-typescript-expert)[### TypeScript Node.js Backend Expert

TypeScriptNode.jsBackendYou are an expert in TypeScript Node.js backend development. Key Principles: - Use strict TypeScript configuration - Type all Express middleware and ...](/rules/typescript/typescript-nodejs-backend)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![ActionKit by Paragon](https://framerusercontent.com/images/LpSK1tSZweomrAHOMAj9Gea96lA.svg)
### ActionKit by Paragon

Official

Connect to 130+ SaaS integrations (e.g. Slack, Salesforce, Gmail) with Paragon’s [ActionKit](https://www.useparagon.com/actionkit) API.](/mcp/actionkit-by-paragon)[![AgentOps](https://github.com/AgentOps-AI/agentops/blob/main/docs/favicon.png)
### AgentOps

Official

Provide observability and tracing for debugging AI agents with [AgentOps](https://www.agentops.ai/) API.](/mcp/agentops)[![Airwallex Developer](https://www.airwallex.com/favicon.ico)
### Airwallex Developer

Official

Empowers AI coding agents with the tools they need to assist developers integrating with [Airwallex APIs](https://www.airwallex.com/docs/api/)](/mcp/airwallex-developer)
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


