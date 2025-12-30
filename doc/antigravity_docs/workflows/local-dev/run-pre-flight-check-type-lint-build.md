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
# Pre-Flight Check

CI/CDTestingBuildQualityDownloadCopy Workflow---
description: Run type checking, linting, and build verification before pushing
---

1. \*\*Type Check\*\*:
 - Ensure there are no TypeScript errors.
 // turbo
 - Run `npx tsc --noEmit`

2. \*\*Lint Check\*\*:
 - Verify code quality rules.
 // turbo
 - Run `npm run lint`

3. \*\*Build Verification\*\*:
 - Ensure the project builds successfully for production.
 // turbo
 - Run `npm run build`

4. \*\*Pro Tips\*\*:
 - Use a pre-push git hook (using `husky`) to run this automatically.
 - If the build fails locally, it will definitely fail in production.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `run-pre-flight-check-type-lint-build.md`
4. In Antigravity, type `/run_pre_flight_check_type_lint_build` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Setup Husky Git Hooks

GitAutomationQuality+1--- description: Automate code quality checks with pre-commit and pre-push hooks --- 1. \*\*Install Husky\*\*: - Install husky and lint-staged. // turbo - Run `npm install --save-dev husky lint-staged` 2. \*\*Initialize Husky\*\*: - Set up git hooks. // turbo - Run `npx husky init` 3. \*...](/workflows/local-dev/setup-husky-git-hooks-pre-commit-linting)[### Fix Lint Errors

LintingESLintPrettier+1--- description: Automatically fix linting and formatting issues across the project --- 1. \*\*Run ESLint Fix\*\*: - Attempt to automatically fix all fixable ESLint errors. // turbo - Run `npm run lint -- --fix` 2. \*\*Run Prettier\*\*: - Format all files in the project to ensure consistent st...](/workflows/local-dev/fix-eslint-prettier-linting-errors-automatically)[### Setup Environment Variables Per Branch

DevOpsEnvironmentVercel+1--- description: Configure different env vars for dev, staging, and production --- 1. \*\*Local Development (.env.local)\*\*: - Create `.env.local` for local overrides (never commit this). ```bash # .env.local DATABASE\_URL=postgresql://localhost:5432/mydb API\_URL=http://localhost:3001 ...](/workflows/local-dev/setup-environment-variables-per-branch-vercel)
## Recommended Rules

[View more rules →](/rules)[### 🚀 DevOps & CI/CD Agent - Pipeline Expert

Agentic AIDevOpsCI/CDYou are an expert DevOps and CI/CD agent specialized in designing and implementing robust deployment pipelines and infrastructure. Apply systematic re...](/rules/agentic-ai/devops-cicd-agent)[### Python Testing Best Practices

PythonTestingQuality AssuranceYou are an expert in Python testing with pytest and testing best practices. Key Principles: - Write tests before or alongside code (TDD/BDD) - Aim fo...](/rules/python/python-testing-best-practices)[### Next.js Testing Strategies Expert

Next.jsTestingJestYou are an expert in Next.js testing strategies and best practices. Key Principles: - Test Server and Client Components differently - Use Jest for un...](/rules/nextjs/nextjs-testing-strategies)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![Jenkins](https://jenkins.io/images/logos/jenkins/jenkins.svg)
### Jenkins

Official

Official Jenkins MCP Server plugin enabling AI assistants to manage builds, check job statuses, retrieve logs, and integrate with CI/CD pipelines through standardized MCP interface.](/mcp/jenkins)[![Alpaca](https://files.alpaca.markets/webassets/favicon-32x32.png)
### Alpaca

Official

Alpaca's MCP server lets you trade stocks and options, analyze market data, and build strategies through [Alpaca's Trading API](https://alpaca.markets/)](/mcp/alpaca)[![Azure DevOps](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/1062064-Products-1.2-24x24)
### Azure DevOps

Official

Interact with Azure DevOps services like repositories, work items, builds, releases, test plans, and code search.](/mcp/azure-devops)
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


