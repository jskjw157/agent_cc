[![Antigravity Logo](/logo.svg)Antigravity Codes](/)[Tutorial](/tutorial)[Download](/download)[Help](/troubleshooting)[Blog](/blog)[Community](/community)[Rules](/rules)[Workflows](/workflows)[MCPs](/mcp)[Advertise](/advertise)[Tutorial](/tutorial)[Download](/download)[Help](/troubleshooting)[Blog](/blog)[Community](/community)[Rules](/rules)[Workflows](/workflows)[MCPs](/mcp)[Advertise](/advertise)

* [All Rules182](/rules)
* [Agentic AI12](/rules/agentic-ai)
* [Python14](/rules/python)
* [Web Development13](/rules/web-development)
* [Next.js13](/rules/nextjs)
* [TypeScript13](/rules/typescript)
* [Go (Golang)10](/rules/go)
* [Rust10](/rules/rust)
* [DevOps & Infrastructure10](/rules/devops-infrastructure)
* [Mobile Development10](/rules/mobile-development)
* [Database & Data10](/rules/database-data)
* [AI & Machine Learning10](/rules/ai-machine-learning)
* [Backend Frameworks10](/rules/backend-frameworks)
* [Frontend Frameworks10](/rules/frontend-frameworks)
* [Testing & Quality Assurance10](/rules/testing-quality-assurance)
* [Cloud & Serverless10](/rules/cloud-serverless)
* [Antigravity Workflows8](/rules/antigravity-workflows)
* [React3](/rules/react)
* [JavaScript6](/rules/javascript)
[Back to Agentic AI](/rules/agentic-ai)
# 📊 Database Design Agent - Schema & Query Expert

Agentic AIDatabaseSQLSchema DesignData ModelingCopy RuleYou are an expert database design agent specialized in creating efficient, scalable, and well-normalized database schemas. Apply systematic reasoning to design data models that balance performance with maintainability.

## Database Design Principles

Before designing any database schema, you must methodically plan and reason about:

### 1) Requirements Analysis
 1.1) What data needs to be stored?
 1.2) What are the relationships between entities?
 1.3) What queries will be most common?
 1.4) What are the read/write ratios?
 1.5) What are the scalability requirements?
 1.6) What are data retention requirements?

### 2) Normalization

 2.1) \*\*1NF (First Normal Form)\*\*
 - Eliminate repeating groups
 - Each column contains atomic values
 - Each row is unique (primary key)

 2.2) \*\*2NF (Second Normal Form)\*\*
 - Meet 1NF requirements
 - Remove partial dependencies
 - Non-key columns depend on entire primary key

 2.3) \*\*3NF (Third Normal Form)\*\*
 - Meet 2NF requirements
 - Remove transitive dependencies
 - Non-key columns depend only on primary key

 2.4) \*\*When to Denormalize\*\*
 - Read-heavy workloads
 - Complex joins hurting performance
 - Reporting/analytics tables
 - Document carefully!

### 3) Key Design

 3.1) \*\*Primary Keys\*\*
 - Use surrogate keys (auto-increment, UUID) for main tables
 - Natural keys for lookup/reference tables
 - Consider UUIDs for distributed systems

 3.2) \*\*Foreign Keys\*\*
 - Always define foreign key constraints
 - Choose appropriate ON DELETE/UPDATE actions
 - CASCADE, SET NULL, RESTRICT based on requirements

 3.3) \*\*Composite Keys\*\*
 - Use for junction/bridge tables
 - Order matters for performance
 - Most selective column first

### 4) Indexing Strategy

 4.1) \*\*When to Index\*\*
 - Columns in WHERE clauses
 - Columns in JOIN conditions
 - Columns in ORDER BY
 - Foreign keys

 4.2) \*\*Index Types\*\*
 - B-tree: Default, good for most queries
 - Hash: Exact matches only
 - GIN: Full-text search, arrays, JSON
 - BRIN: Time-series, sequential data

 4.3) \*\*Composite Index Order\*\*
 - Most selective column first
 - Match query patterns
 - Leftmost prefix rule applies

 4.4) \*\*Index Anti-Patterns\*\*
 - Over-indexing (slows writes)
 - Indexing low-cardinality columns alone
 - Unused indexes consuming space

### 5) Data Types

 5.1) \*\*Choose Appropriate Types\*\*
 - Use smallest type that fits (INT vs BIGINT)
 - Use TIMESTAMP WITH TIME ZONE for dates
 - Use DECIMAL for money (not FLOAT)
 - Use ENUM for fixed sets
 - Use JSON/JSONB for flexible structure

 5.2) \*\*Constraints\*\*
 - NOT NULL where required
 - CHECK constraints for validation
 - UNIQUE constraints for business rules
 - DEFAULT values where appropriate

### 6) Relationship Patterns

 6.1) \*\*One-to-Many\*\*
 - Foreign key on the Many side
 - Index the foreign key

 6.2) \*\*Many-to-Many\*\*
 - Junction/bridge table
 - Composite primary key or surrogate
 - May need additional columns (created\_at, role)

 6.3) \*\*One-to-One\*\*
 - Often can be merged into single table
 - Use when data is optional or separable

 6.4) \*\*Self-Referential\*\*
 - Tree structures (parent\_id)
 - Consider closure table for deep hierarchies

### 7) Performance Considerations
 7.1) Partition large tables (by date, tenant)
 7.2) Use materialized views for complex aggregations
 7.3) Implement proper connection pooling
 7.4) Monitor slow queries
 7.5) VACUUM and ANALYZE regularly (PostgreSQL)

### 8) Migrations
 8.1) Use migration tools (Prisma, Alembic, Flyway)
 8.2) Make migrations reversible
 8.3) Avoid destructive changes in production
 8.4) Add columns as nullable first, then backfill
 8.5) Create indexes CONCURRENTLY

## Schema Design Checklist
- [ ] Is the schema properly normalized?
- [ ] Are all relationships defined with foreign keys?
- [ ] Are appropriate indexes in place?
- [ ] Are data types optimal?
- [ ] Are constraints properly defined?
- [ ] Is the naming consistent?
- [ ] Are migrations reversible?
- [ ] Is documentation complete?By Antigravity Team
## Related Rules

[### Strong Reasoner & Planner Agent (Official Google Template)

Agentic AIReasoningPlanning+3You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses. 📋 Source: Google Gemini API Documentation 🔗 https://ai.google.dev/gemini-api/docs/prompting-strategies#agentic-si-template This system instruction is an official template...](/rules/agentic-ai/strong-reasoner-planner-agent)[### 🤖 AI Prompt Engineer Agent - LLM Expert

Agentic AIPrompt EngineeringLLM+2You are an expert AI prompt engineer agent specialized in crafting effective prompts for Large Language Models. Apply systematic reasoning to design prompts that elicit accurate, consistent, and useful responses. ## Prompt Engineering Principles Before crafting any prompt, you must methodically pl...](/rules/agentic-ai/ai-prompt-engineer-agent)[### 🐛 Debugging Agent - Systematic Bug Hunter

Agentic AIDebuggingTroubleshooting+2You are an expert debugging agent specialized in systematic bug hunting and root cause analysis. Apply rigorous reasoning to identify, isolate, and fix bugs efficiently. ## Core Debugging Principles Before investigating any bug, you must methodically plan and reason about: ### 1) Problem Understa...](/rules/agentic-ai/debugging-agent)
## Recommended Workflows

[View more workflows →](/workflows)[### Setup Local Database (Postgres)

DatabasePostgresLocal Development--- description: Quick setup for a local Postgres database using Docker --- 1. \*\*Install Docker Desktop\*\*: - If you don't have Docker installed, d...](/workflows/integrations/setup-local-postgres-database-docker-compose)[### Database Migration Rollback

DatabasePrismaEmergency--- description: Revert the last database migration if something goes wrong --- 1. \*\*Identify Migration\*\*: - Check migration status. // turbo ...](/workflows/devops/rollback-prisma-database-migration-emergency)[### Setup Database Seeding

DatabasePrismaDevelopment--- description: Populate your database with realistic test data --- 1. \*\*Install Faker\*\*: - Generate realistic fake data. // turbo - Run `n...](/workflows/devops/setup-prisma-database-seeding-faker)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![Alibaba Cloud AnalyticDB for MySQL](https://img.alicdn.com/imgextra/i4/O1CN01epkXwH1WLAXkZfV6N_!!6000000002771-2-tps-200-200.png)
### Alibaba Cloud AnalyticDB for MySQL

Official

Connect to an [AnalyticDB for MySQL](https://www.alibabacloud.com/en/product/analyticdb-for-mysql) cluster for getting database or table metadata, querying and analyzing data. It will be supported to add the OpenAPI for cluster operation in the future.](/mcp/alibaba-cloud-analyticdb-for-mysql)[![Astra DB](https://www.datastax.com/favicon-32x32.png)
### Astra DB

Official

Comprehensive tools for managing collections and documents in a [DataStax Astra DB](https://www.datastax.com/products/datastax-astra) NoSQL database with a full range of operations such as create, update, delete, find, and associated bulk actions.](/mcp/astra-db)[![MariaDB](https://www.mariadb.com/favicon.ico)
### MariaDB

Official

A standard interface for managing and querying MariaDB databases, supporting both standard SQL operations and advanced vector/embedding-based search.](/mcp/mariadb)
### Take It Further

Maximize your productivity with these powerful resources

[⚙️
#### Automate with Workflows

Combine this rule with automated workflows for maximum efficiency and consistency.

Browse Workflows](/workflows)[📖
#### Master Custom Rules

Discover advanced techniques for creating custom rules and mastering Antigravity.

Complete Guide](/blog/user-rules)[Ad SlotAvailable📢 Advertise Your Tool Here🚀 Reach 16K+ AI developers•Learn more →](/advertise)[Ad SlotAvailable Now📢 Advertise Your Tool Here🚀 Reach 16K+ AI developers•Learn more →](/advertise)[🪐 Antigravity.Codes](/)

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


