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
# Setup Semantic Versioning

VersioningReleasesGitAutomationDownloadCopy Workflow---
description: Automate version bumps and changelog generation
---

1. \*\*Install semantic-release\*\*:
 - Automate versioning based on commit messages.
 // turbo
 - Run `npm install --save-dev semantic-release @semantic-release/changelog @semantic-release/git`

2. \*\*Configure Commit Convention\*\*:
 - Use Conventional Commits.
```
# Format: <type>(<scope>): <description>
   feat: add dark mode support
   fix: resolve hydration error
   docs: update README
   chore: upgrade dependencies
```

3. \*\*Create Release Config\*\*:
 - Create `.releaserc.json`.
```
{
     "branches": ["main"],
     "plugins": [
       "@semantic-release/commit-analyzer",
       "@semantic-release/release-notes-generator",
       "@semantic-release/changelog",
       "@semantic-release/npm",
       "@semantic-release/github",
       ["@semantic-release/git", {
         "assets": ["CHANGELOG.md", "package.json"],
         "message": "chore(release): ${nextRelease.version} [skip ci]"
       }]
     ]
   }
```

4. \*\*Setup GitHub Actions\*\*:
 - Automate releases on merge to main.
```
# .github/workflows/release.yml
   name: Release
   on:
     push:
       branches: [main]
   jobs:
     release:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - uses: actions/setup-node@v3
         - run: npm ci
         - run: npx semantic-release
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

5. \*\*Commit with Convention\*\*:
 - Follow the format.
```
git commit -m "feat: add user authentication"
   # Will bump MINOR version (0.1.0 -> 0.2.0)

   git commit -m "fix: resolve login bug"
   # Will bump PATCH version (0.2.0 -> 0.2.1)

   git commit -m "feat!: redesign API\n\nBREAKING CHANGE: API endpoints changed"
   # Will bump MAJOR version (0.2.1 -> 1.0.0)
```

6. \*\*Pro Tips\*\*:
 - Use Commitizen for interactive commit messages: `npx cz`.
 - CHANGELOG.md is auto-generated, don't edit manually.
 - Releases create Git tags automatically.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `setup-semantic-versioning-automated-releases.md`
4. In Antigravity, type `/setup_semantic_versioning_automated_releases` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Setup Vercel Cron Jobs

VercelCronAutomation--- description: Create and test scheduled tasks in Next.js --- 1. \*\*Create Cron Config\*\*: - Add `crons` to `vercel.json`. ```json { "crons": [ { "path": "/api/cron/daily-report", "schedule": "0 10 \* \* \*" } ] } ``` 2. \*\*Create API Route\*\*: ...](/workflows/devops/setup-vercel-cron-jobs-scheduled-tasks)[### Analyze Bundle Size

PerformanceNext.jsOptimization--- description: Visualize and reduce your production build size --- 1. \*\*Install Analyzer\*\*: - Install the Next.js bundle analyzer. // turbo - Run `npm install @next/bundle-analyzer` 2. \*\*Configure next.config.js\*\*: - Wrap your config. ```js const withBundleAnalyzer = require('@...](/workflows/devops/analyze-nextjs-bundle-size-optimization)[### Database Migration Rollback

DatabasePrismaEmergency--- description: Revert the last database migration if something goes wrong --- 1. \*\*Identify Migration\*\*: - Check migration status. // turbo - Run `npx prisma migrate status` 2. \*\*Resolve Migration\*\*: - Mark a failed migration as resolved (if stuck). // turbo - Run `npx prisma m...](/workflows/devops/rollback-prisma-database-migration-emergency)
## Recommended Rules

[View more rules →](/rules)[### Python Automation & Scripting Expert

PythonAutomationScriptingYou are an expert in Python automation and scripting. Key Principles: - Write robust, error-resistant scripts - Implement proper logging - Handle edg...](/rules/python/python-automation-and-scripting-expert)[### Python DevOps & Infrastructure Automation

PythonDevOpsInfrastructureYou are an expert in Python for DevOps, infrastructure automation, and CI/CD. Key Principles: - Automate repetitive tasks - Use infrastructure as cod...](/rules/python/python-devops-and-infrastructure)[### CI/CD Pipelines (GitHub Actions, GitLab CI)

CI/CDGitHub ActionsGitLab CIYou are an expert in CI/CD pipelines, specifically GitHub Actions and GitLab CI. Key Principles: - Fail fast and provide feedback - Automate everythi...](/rules/devops-infrastructure/ci-cd-pipelines-automation)
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


