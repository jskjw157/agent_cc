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
# Setup Database Seeding

DatabasePrismaDevelopmentTestingDownloadCopy Workflow---
description: Populate your database with realistic test data
---

1. \*\*Install Faker\*\*:
 - Generate realistic fake data.
 // turbo
 - Run `npm install --save-dev @faker-js/faker`

2. \*\*Create Seed Script\*\*:
 - Create `prisma/seed.ts`.
```
import { PrismaClient } from '@prisma/client';
   import { faker } from '@faker-js/faker';

   const prisma = new PrismaClient();

   async function main() {
     // Clear existing data
     await prisma.post.deleteMany();
     await prisma.user.deleteMany();

     // Create 10 users
     const users = await Promise.all(
       Array.from({ length: 10 }).map(() =>
         prisma.user.create({
           data: {
             email: faker.internet.email(),
             name: faker.person.fullName(),
             avatar: faker.image.avatar(),
           },
         })
       )
     );

     // Create 50 posts
     await Promise.all(
       Array.from({ length: 50 }).map(() =>
         prisma.post.create({
           data: {
             title: faker.lorem.sentence(),
             content: faker.lorem.paragraphs(3),
             authorId: faker.helpers.arrayElement(users).id,
           },
         })
       )
     );

     console.log('✅ Database seeded successfully');
   }

   main()
     .catch(console.error)
     .finally(() => prisma.$disconnect());
```

3. \*\*Configure package.json\*\*:
 - Add seed command.
```
{
     "prisma": {
       "seed": "ts-node --compiler-options {\"module\":\"CommonJS\"} prisma/seed.ts"
     },
     "scripts": {
       "db:seed": "prisma db seed"
     }
   }
```

4. \*\*Run Seed\*\*:
 - Populate your database.
 // turbo
 - Run `npm run db:seed`

5. \*\*Reset Database\*\*:
 - Wipe and re-seed.
 // turbo
 - Run `npx prisma migrate reset` (runs seed automatically)

6. \*\*Pro Tips\*\*:
 - Create different seed files for dev/staging/test.
 - Use deterministic seeds for consistent testing.
 - Seed only in development; never in production!
 - Consider using snapshots of production data (anonymized).By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `setup-prisma-database-seeding-faker.md`
4. In Antigravity, type `/setup_prisma_database_seeding_faker` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Database Migration Rollback

DatabasePrismaEmergency--- description: Revert the last database migration if something goes wrong --- 1. \*\*Identify Migration\*\*: - Check migration status. // turbo - Run `npx prisma migrate status` 2. \*\*Resolve Migration\*\*: - Mark a failed migration as resolved (if stuck). // turbo - Run `npx prisma m...](/workflows/devops/rollback-prisma-database-migration-emergency)[### Analyze Bundle Size

PerformanceNext.jsOptimization--- description: Visualize and reduce your production build size --- 1. \*\*Install Analyzer\*\*: - Install the Next.js bundle analyzer. // turbo - Run `npm install @next/bundle-analyzer` 2. \*\*Configure next.config.js\*\*: - Wrap your config. ```js const withBundleAnalyzer = require('@...](/workflows/devops/analyze-nextjs-bundle-size-optimization)[### Setup Vercel Cron Jobs

VercelCronAutomation--- description: Create and test scheduled tasks in Next.js --- 1. \*\*Create Cron Config\*\*: - Add `crons` to `vercel.json`. ```json { "crons": [ { "path": "/api/cron/daily-report", "schedule": "0 10 \* \* \*" } ] } ``` 2. \*\*Create API Route\*\*: ...](/workflows/devops/setup-vercel-cron-jobs-scheduled-tasks)
## Recommended Rules

[View more rules →](/rules)[### Next.js Database Integration Expert

Next.jsDatabasePrismaYou are an expert in Next.js database integration with Prisma and modern ORMs. Key Principles: - Use Prisma for type-safe database access - Implement...](/rules/nextjs/nextjs-database-integration)[### 📊 Database Design Agent - Schema & Query Expert

Agentic AIDatabaseSQLYou are an expert database design agent specialized in creating efficient, scalable, and well-normalized database schemas. Apply systematic reasoning ...](/rules/agentic-ai/database-design-agent)[### Python Testing Best Practices

PythonTestingQuality AssuranceYou are an expert in Python testing with pytest and testing best practices. Key Principles: - Write tests before or alongside code (TDD/BDD) - Aim fo...](/rules/python/python-testing-best-practices)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![Prisma](https://www.prisma.io/images/favicon-32x32.png)
### Prisma

Official

Create and manage Prisma Postgres databases](/mcp/prisma)[M
### MSSQL-MCP-Node

Community

(by mihai - dulgheru) – Node.js MCP server for Microsoft SQL Server featuring auto-detected single / multi-database configs, execute-SQL and schema tools, robust Zod validation, and optional Express endpoints for local testing](/mcp/mssql-mcp-node)[![Alibaba Cloud AnalyticDB for MySQL](https://img.alicdn.com/imgextra/i4/O1CN01epkXwH1WLAXkZfV6N_!!6000000002771-2-tps-200-200.png)
### Alibaba Cloud AnalyticDB for MySQL

Official

Connect to an [AnalyticDB for MySQL](https://www.alibabacloud.com/en/product/analyticdb-for-mysql) cluster for getting database or table metadata, querying and analyzing data. It will be supported to add the OpenAPI for cluster operation in the future.](/mcp/alibaba-cloud-analyticdb-for-mysql)
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


