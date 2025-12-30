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
# Setup Vercel Cron Jobs

VercelCronAutomationDownloadCopy Workflow---
description: Create and test scheduled tasks in Next.js
---

1. \*\*Create Cron Config\*\*:
 - Add `crons` to `vercel.json`.
```
{
     "crons": [
       {
         "path": "/api/cron/daily-report",
         "schedule": "0 10 * * *"
       }
     ]
   }
```

2. \*\*Create API Route\*\*:
 - Create the endpoint at `src/app/api/cron/daily-report/route.ts`.
```
import { NextResponse } from 'next/server';

   export async function GET(request: Request) {
     // Verify the request is from Vercel Cron
     const authHeader = request.headers.get('authorization');
     if (authHeader !== Bearer ${process.env.CRON_SECRET}) {
       return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
     }

     // Your cron job logic here
     console.log('Daily report cron executed');

     return NextResponse.json({ success: true });
   }
```

3. \*\*Set Environment Variable\*\*:
 - Add `CRON_SECRET` to your `.env.local` and Vercel project settings.
 - Generate a secure random string: `openssl rand -base64 32`

4. \*\*Pro Tips\*\*:
 - Vercel sends an `Authorization: Bearer <token>` header with cron requests.
 - Test locally by manually calling the endpoint with the correct header.
 - Cron expressions use UTC timezone.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `setup-vercel-cron-jobs-scheduled-tasks.md`
4. In Antigravity, type `/setup_vercel_cron_jobs_scheduled_tasks` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Deploy to Vercel Preview

VercelDeploymentCI/CD--- description: Push current branch to a Vercel preview URL --- 1. \*\*Install Vercel CLI\*\*: - Ensure you have the CLI. // turbo - Run `npm i -g vercel` 2. \*\*Deploy\*\*: - Deploy the current directory. // turbo - Run `vercel` 3. \*\*Pro Tips\*\*: - Use `vercel --prod` to deploy to p...](/workflows/devops/deploy-branch-to-vercel-preview-environment)[### Setup Semantic Versioning

VersioningReleasesGit+1--- description: Automate version bumps and changelog generation --- 1. \*\*Install semantic-release\*\*: - Automate versioning based on commit messages. // turbo - Run `npm install --save-dev semantic-release @semantic-release/changelog @semantic-release/git` 2. \*\*Configure Commit Convention...](/workflows/devops/setup-semantic-versioning-automated-releases)[### Analyze Bundle Size

PerformanceNext.jsOptimization--- description: Visualize and reduce your production build size --- 1. \*\*Install Analyzer\*\*: - Install the Next.js bundle analyzer. // turbo - Run `npm install @next/bundle-analyzer` 2. \*\*Configure next.config.js\*\*: - Wrap your config. ```js const withBundleAnalyzer = require('@...](/workflows/devops/analyze-nextjs-bundle-size-optimization)
## Recommended Rules

[View more rules →](/rules)[### Python Automation & Scripting Expert

PythonAutomationScriptingYou are an expert in Python automation and scripting. Key Principles: - Write robust, error-resistant scripts - Implement proper logging - Handle edg...](/rules/python/python-automation-and-scripting-expert)[### Python DevOps & Infrastructure Automation

PythonDevOpsInfrastructureYou are an expert in Python for DevOps, infrastructure automation, and CI/CD. Key Principles: - Automate repetitive tasks - Use infrastructure as cod...](/rules/python/python-devops-and-infrastructure)[### Test Automation Frameworks

AutomationTestingArchitectureYou are an expert in designing and building Test Automation Frameworks. Key Principles: - Maintainability and Scalability - Reusability of code - Rep...](/rules/testing-quality-assurance/test-automation-frameworks)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![AltTester®](https://alttester.com/app/themes/alttester-sage-theme/public/images/logo-alttester.038ec8.png)
### AltTester®

Official

Use AltTester® capabilities to connect and test your Unity or Unreal game. Write game test automation faster and smarter, using [AltTester](https://alttester.com) and the AltTester® MCP server.](/mcp/alttester)[![Appium MCP Server](https://appium.io/docs/en/latest/assets/images/appium-logo-horiz.png)
### Appium MCP Server

Official

MCP server for Mobile Development and Automation | iOS, Android, Simulator, Emulator, and Real Devices](/mcp/appium-mcp-server)[![GoLogin MCP server](https://api.gologin.com/favicon.ico)
### GoLogin MCP server

Official

Manage your GoLogin browser profiles and automation directly through AI conversations!](/mcp/gologin-mcp-server)
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


