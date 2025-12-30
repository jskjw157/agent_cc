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
# Implement Feature Flags

Feature FlagsDeploymentA/B TestingDevOpsDownloadCopy Workflow---
description: Safely release features with toggles for gradual rollouts
---

1. \*\*Simple Approach: Environment Variables\*\*:
 - Use env vars for basic flags.
```
// lib/features.ts
   export const features = {
     newDashboard: process.env.NEXT_PUBLIC_FEATURE_NEW_DASHBOARD === 'true',
     aiChat: process.env.NEXT_PUBLIC_FEATURE_AI_CHAT === 'true',
   };
```

2. \*\*Use in Components\*\*:
 - Conditionally render features.
```
import { features } from '@/lib/features';

   export default function Dashboard() {
     if (features.newDashboard) {
       return <NewDashboard />;
     }
     return <OldDashboard />;
   }
```

3. \*\*Advanced: Vercel Edge Config\*\*:
 - Dynamic flags without redeployment.
 // turbo
 - Run `npm install @vercel/edge-config`
```
import { get } from '@vercel/edge-config';

   export async function getFeatureFlags() {
     const flags = await get('features');
     return flags || {};
   }
```

4. \*\*Production-Ready: LaunchDarkly/PostHog\*\*:
 - Install SDK.
 // turbo
 - Run `npm install launchdarkly-react-client-sdk`
```
import { useLDClient, useFlags } from 'launchdarkly-react-client-sdk';

   function MyComponent() {
     const { newFeature } = useFlags();

     if (newFeature) {
       return <NewFeature />;
     }
     return <OldFeature />;
   }
```

5. \*\*Gradual Rollout Pattern\*\*:
 - Enable for percentage of users.
```
function isFeatureEnabled(userId: string, rolloutPercent: number) {
     const hash = userId.split('').reduce((a, b) => a + b.charCodeAt(0), 0);
     return (hash % 100) < rolloutPercent;
   }

   const showNewUI = isFeatureEnabled(user.id, 25); // 25% rollout
```

6. \*\*Pro Tips\*\*:
 - Always have a kill switch for new features.
 - Log feature flag usage for analytics.
 - Clean up old flags after full rollout.
 - Use flags for A/B testing experiments.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `implement-feature-flags-gradual-rollout.md`
4. In Antigravity, type `/implement_feature_flags_gradual_rollout` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Implement Blue-Green Deployment

DeploymentDevOpsZero-Downtime--- description: Zero-downtime deploys --- 1. \*\*Setup Two Environments\*\*: - Blue: Current (v1.0) - Green: New (v1.1) 2. \*\*Route Traffic Gradually\*\*: ```ts const rolloutPercent = await get('green\_rollout') || 0; if (Math.random() \* 100 < rolloutPercent) { return NextResponse.rew...](/workflows/devops/implement-blue-green-deployment-strategy)[### Setup Preview Deployments

CI/CDGitHub ActionsDeployment--- description: Auto-deploy PRs --- 1. \*\*Create GitHub Action\*\*: ```yaml name: Preview on: pull\_request: types: [opened, synchronize] jobs: deploy: runs-on: ubuntu-latest steps: - uses: actions/checkout@v4 - uses: actions/setup-node@v4 ...](/workflows/devops/setup-github-actions-preview-deployments)[### Deploy to Vercel Preview

VercelDeploymentCI/CD--- description: Push current branch to a Vercel preview URL --- 1. \*\*Install Vercel CLI\*\*: - Ensure you have the CLI. // turbo - Run `npm i -g vercel` 2. \*\*Deploy\*\*: - Deploy the current directory. // turbo - Run `vercel` 3. \*\*Pro Tips\*\*: - Use `vercel --prod` to deploy to p...](/workflows/devops/deploy-branch-to-vercel-preview-environment)
## Recommended Rules

[View more rules →](/rules)[### Next.js Deployment & DevOps Expert

Next.jsDeploymentDevOpsYou are an expert in Next.js deployment and DevOps practices. Key Principles: - Use Vercel for optimal Next.js hosting - Implement proper CI/CD pipel...](/rules/nextjs/nextjs-deployment-devops)[### MLOps & Model Deployment

MLOpsDeploymentDevOpsYou are an expert in MLOps (Machine Learning Operations) and Model Deployment. Key Principles: - Treat ML as software (Version Control, CI/CD) - Auto...](/rules/ai-machine-learning/mlops-model-deployment)[### Database Migration Strategies

MigrationsDevOpsDatabaseYou are an expert in database migrations and schema evolution. Key Principles: - Treat database changes as code - Version control all migrations - En...](/rules/database-data/database-migration-strategies)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![Azure DevOps](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/1062064-Products-1.2-24x24)
### Azure DevOps

Official

Interact with Azure DevOps services like repositories, work items, builds, releases, test plans, and code search.](/mcp/azure-devops)[![ConfigCat](https://configcat.com/favicon.ico)
### ConfigCat

Official

Enables AI tools to interact with [ConfigCat](https://configcat.com), a feature flag service for teams. Supports managing ConfigCat feature flags, configs, environments, products and organizations. Helps to integrate ConfigCat SDK, implement feature flags and remove zombie (stale) flags.](/mcp/configcat)[![DeployHQ](https://deployhq.com/assets/favicon-357ebe39b58f28869358da83948e76e7cadfb0791c97af34abfe346f5e3ef634.png)
### DeployHQ

Official

MCP server for DeployHQ API integration, enabling AI assistants to manage deployments, list projects, and monitor deployment status.](/mcp/deployhq)
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


