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
# Setup Husky Git Hooks

GitAutomationQualityCI/CDDownloadCopy Workflow---
description: Automate code quality checks with pre-commit and pre-push hooks
---

1. \*\*Install Husky\*\*:
 - Install husky and lint-staged.
 // turbo
 - Run `npm install --save-dev husky lint-staged`

2. \*\*Initialize Husky\*\*:
 - Set up git hooks.
 // turbo
 - Run `npx husky init`

3. \*\*Create Pre-Commit Hook\*\*:
 - Run linting on staged files before commit.
 // turbo
 - Run `npx husky add .husky/pre-commit "npx lint-staged"`

4. \*\*Configure lint-staged\*\*:
 - Add to `package.json`.
```
{
     "lint-staged": {
       "*.{ts,tsx}": [
         "eslint --fix",
         "prettier --write"
       ],
       "*.{json,md}": [
         "prettier --write"
       ]
     }
   }
```

5. \*\*Create Pre-Push Hook (Optional)\*\*:
 - Run tests before pushing.
 // turbo
 - Run `npx husky add .husky/pre-push "npm test"`

6. \*\*Advanced: Commit Message Validation\*\*:
 - Install commitlint.
 // turbo
 - Run `npm install --save-dev @commitlint/cli @commitlint/config-conventional`
 - Create commitlint.config.js:
```
module.exports = { extends: ['@commitlint/config-conventional'] };
```

 - Add hook:
 // turbo
 - Run `npx husky add .husky/commit-msg "npx commitlint --edit $1"`

7. \*\*Pro Tips\*\*:
 - Skip hooks if needed: `git commit --no-verify`.
 - Hooks run locally, so they're fast feedback loops.
 - Combine with CI/CD for double protection.
 - If husky commands fail, manually create files in `.husky/` directory.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `setup-husky-git-hooks-pre-commit-linting.md`
4. In Antigravity, type `/setup_husky_git_hooks_pre_commit_linting` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Pre-Flight Check

CI/CDTestingBuild+1--- description: Run type checking, linting, and build verification before pushing --- 1. \*\*Type Check\*\*: - Ensure there are no TypeScript errors. // turbo - Run `npx tsc --noEmit` 2. \*\*Lint Check\*\*: - Verify code quality rules. // turbo - Run `npm run lint` 3. \*\*Build Verificat...](/workflows/local-dev/run-pre-flight-check-type-lint-build)[### Create GitHub PR Template

GitGitHubTeam+1--- description: Standardize pull request descriptions for better code reviews --- 1. \*\*Create Template Directory\*\*: - GitHub looks for templates in `.github/` folder. // turbo - Run `mkdir -p .github` 2. \*\*Create Pull Request Template\*\*: - Create the template file with structured cont...](/workflows/local-dev/create-github-pull-request-template-markdown)[### Fix Lint Errors

LintingESLintPrettier+1--- description: Automatically fix linting and formatting issues across the project --- 1. \*\*Run ESLint Fix\*\*: - Attempt to automatically fix all fixable ESLint errors. // turbo - Run `npm run lint -- --fix` 2. \*\*Run Prettier\*\*: - Format all files in the project to ensure consistent st...](/workflows/local-dev/fix-eslint-prettier-linting-errors-automatically)
## Recommended Rules

[View more rules →](/rules)[### CI/CD Pipelines (GitHub Actions, GitLab CI)

CI/CDGitHub ActionsGitLab CIYou are an expert in CI/CD pipelines, specifically GitHub Actions and GitLab CI. Key Principles: - Fail fast and provide feedback - Automate everythi...](/rules/devops-infrastructure/ci-cd-pipelines-automation)[### Python DevOps & Infrastructure Automation

PythonDevOpsInfrastructureYou are an expert in Python for DevOps, infrastructure automation, and CI/CD. Key Principles: - Automate repetitive tasks - Use infrastructure as cod...](/rules/python/python-devops-and-infrastructure)[### 🚀 DevOps & CI/CD Agent - Pipeline Expert

Agentic AIDevOpsCI/CDYou are an expert DevOps and CI/CD agent specialized in designing and implementing robust deployment pipelines and infrastructure. Apply systematic re...](/rules/agentic-ai/devops-cicd-agent)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[G
### GitHub Repos Manager MCP Server

Community

Token-based GitHub automation management. No Docker, Flexible configuration, 80+ tools with direct API integration.](/mcp/github-repos-manager-mcp-server)[![Alibaba Cloud AnalyticDB for PostgreSQL](https://github.com/aliyun/alibabacloud-adbpg-mcp-server/blob/master/images/AnalyticDB.png)
### Alibaba Cloud AnalyticDB for PostgreSQL

Official

An MCP server to connect to [AnalyticDB for PostgreSQL](https://github.com/aliyun/alibabacloud-adbpg-mcp-server) instances, query and analyze data.](/mcp/alibaba-cloud-analyticdb-for-postgresql)[![AltTester®](https://alttester.com/app/themes/alttester-sage-theme/public/images/logo-alttester.038ec8.png)
### AltTester®

Official

Use AltTester® capabilities to connect and test your Unity or Unreal game. Write game test automation faster and smarter, using [AltTester](https://alttester.com) and the AltTester® MCP server.](/mcp/alttester)
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


