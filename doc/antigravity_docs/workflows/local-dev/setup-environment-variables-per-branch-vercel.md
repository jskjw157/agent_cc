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
# Setup Environment Variables Per Branch

DevOpsEnvironmentVercelCI/CDDownloadCopy Workflow---
description: Configure different env vars for dev, staging, and production
---

1. \*\*Local Development (.env.local)\*\*:
 - Create `.env.local` for local overrides (never commit this).
```
# .env.local
   DATABASE_URL=postgresql://localhost:5432/mydb
   API_URL=http://localhost:3001
   NEXT_PUBLIC_APP_URL=http://localhost:3000
```

2. \*\*Shared Defaults (.env)\*\*:
 - Create `.env` for defaults (commit this).
```
# .env
   NEXT_PUBLIC_APP_NAME=MyApp
   NEXT_PUBLIC_MAX_UPLOAD_SIZE=5242880
```

3. \*\*Vercel Environment Setup\*\*:
 - In Vercel Dashboard → Project → Settings → Environment Variables.
 - Add variables for each environment:
 - \*\*Production\*\*: `main` branch
 - \*\*Preview\*\*: All other branches
 - \*\*Development\*\*: Local only

4. \*\*Access Branch-Specific Vars\*\*:
 - Vercel automatically injects `VERCEL_ENV`.
```
const apiUrl = process.env.VERCEL_ENV === 'production'
     ? 'https://api.myapp.com'
     : 'https://staging-api.myapp.com';
```

5. \*\*GitHub Actions Setup\*\*:
 - Use secrets for CI/CD.
```
# .github/workflows/test.yml
   env:
     DATABASE_URL: ${{ secrets.DATABASE_URL }}
     API_KEY: ${{ secrets.API_KEY }}
```

6. \*\*Pro Tips\*\*:
 - Prefix public vars with `NEXT_PUBLIC_` for client-side access.
 - Use `.env.example` as a template (commit).
 - Never log environment variables in production.
 - Use Vercel CLI to pull env vars: `vercel env pull .env.local`.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `setup-environment-variables-per-branch-vercel.md`
4. In Antigravity, type `/setup_environment_variables_per_branch_vercel` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Kill Port 3000

DevOpsTerminalProcess--- description: Instantly find and kill the process hogging your dev port --- 1. \*\*The Best Way (Cross-Platform)\*\*: - Kill it in one command using npx. Works on Mac, Windows, and Linux. // turbo - Run `npx kill-port 3000` 2. \*\*Mac/Linux Manual Method\*\*: - Find PID: `lsof -ti:3000` ...](/workflows/local-dev/kill-process-on-port-3000-terminal-command)[### Generate .env from Example

ConfigEnvironmentSetup--- description: Safely create a local .env file from .env.example --- 1. \*\*Check for .env.example\*\*: - Ensure the example file exists. // turbo - Run `test -f .env.example && echo "✅ Found .env.example" || echo "❌ .env.example not found"` 2. \*\*Copy to .env.local\*\*: - Create your local...](/workflows/local-dev/generate-local-env-file-from-example)[### Pre-Flight Check

CI/CDTestingBuild+1--- description: Run type checking, linting, and build verification before pushing --- 1. \*\*Type Check\*\*: - Ensure there are no TypeScript errors. // turbo - Run `npx tsc --noEmit` 2. \*\*Lint Check\*\*: - Verify code quality rules. // turbo - Run `npm run lint` 3. \*\*Build Verificat...](/workflows/local-dev/run-pre-flight-check-type-lint-build)
## Recommended Rules

[View more rules →](/rules)[### Next.js Deployment & DevOps Expert

Next.jsDeploymentDevOpsYou are an expert in Next.js deployment and DevOps practices. Key Principles: - Use Vercel for optimal Next.js hosting - Implement proper CI/CD pipel...](/rules/nextjs/nextjs-deployment-devops)[### 🚀 DevOps & CI/CD Agent - Pipeline Expert

Agentic AIDevOpsCI/CDYou are an expert DevOps and CI/CD agent specialized in designing and implementing robust deployment pipelines and infrastructure. Apply systematic re...](/rules/agentic-ai/devops-cicd-agent)[### Python DevOps & Infrastructure Automation

PythonDevOpsInfrastructureYou are an expert in Python for DevOps, infrastructure automation, and CI/CD. Key Principles: - Automate repetitive tasks - Use infrastructure as cod...](/rules/python/python-devops-and-infrastructure)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![Azure DevOps](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/1062064-Products-1.2-24x24)
### Azure DevOps

Official

Interact with Azure DevOps services like repositories, work items, builds, releases, test plans, and code search.](/mcp/azure-devops)[![CloudBees Unify](https://www.cloudbees.com/favicon.ico)
### CloudBees Unify

Official

Enable AI access to your [CloudBees Unify](https://www.cloudbees.com/unify) environment.](/mcp/cloudbees-unify)[![ConfigCat](https://configcat.com/favicon.ico)
### ConfigCat

Official

Enables AI tools to interact with [ConfigCat](https://configcat.com), a feature flag service for teams. Supports managing ConfigCat feature flags, configs, environments, products and organizations. Helps to integrate ConfigCat SDK, implement feature flags and remove zombie (stale) flags.](/mcp/configcat)
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


