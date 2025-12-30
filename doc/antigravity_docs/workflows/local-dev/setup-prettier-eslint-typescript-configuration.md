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
# Setup Prettier & ESLint from Scratch

ESLintPrettierCode QualitySetupDownloadCopy Workflow---
description: Configure linting and formatting (ESLint 9 Flat Config)
---

1. \*\*Install Dependencies\*\*:
 - Install ESLint, Prettier, and configs.
 // turbo
 - Run `npm install --save-dev eslint @eslint/js typescript-eslint prettier eslint-config-prettier eslint-plugin-react-hooks eslint-plugin-react-refresh globals`

2. \*\*Create `eslint.config.js` (Flat Config)\*\*:
 - The new standard for ESLint 9.
```
import js from '@eslint/js';
   import globals from 'globals';
   import reactHooks from 'eslint-plugin-react-hooks';
   import reactRefresh from 'eslint-plugin-react-refresh';
   import tseslint from 'typescript-eslint';

   export default tseslint.config(
     { ignores: ['dist', '.next'] },
     {
       extends: [js.configs.recommended, ...tseslint.configs.recommended],
       files: ['**/*.{ts,tsx}'],
       languageOptions: {
         ecmaVersion: 2020,
         globals: globals.browser,
       },
       plugins: {
         'react-hooks': reactHooks,
         'react-refresh': reactRefresh,
       },
       rules: {
         ...reactHooks.configs.recommended.rules,
         'react-refresh/only-export-components': [
           'warn',
           { allowConstantExport: true },
         ],
       },
     },
   );
```

3. \*\*Create `.prettierrc`\*\*:
```
{
     "semi": true,
     "singleQuote": true,
     "tabWidth": 2,
     "trailingComma": "es5",
     "printWidth": 100,
     "plugins": ["prettier-plugin-tailwindcss"]
   }
```

4. \*\*Add Scripts\*\*:
```
{
     "scripts": {
       "lint": "eslint .",
       "lint:fix": "eslint . --fix",
       "format": "prettier --write ."
     }
   }
```

5. \*\*Pro Tips\*\*:
 - Install VS Code extensions: ESLint, Prettier.
 - Enable "Format on Save" in VS Code settings.
 - ESLint 9 is a major change; old `.eslintrc` files are deprecated.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `setup-prettier-eslint-typescript-configuration.md`
4. In Antigravity, type `/setup_prettier_eslint_typescript_configuration` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Fix Lint Errors

LintingESLintPrettier+1--- description: Automatically fix linting and formatting issues across the project --- 1. \*\*Run ESLint Fix\*\*: - Attempt to automatically fix all fixable ESLint errors. // turbo - Run `npm run lint -- --fix` 2. \*\*Run Prettier\*\*: - Format all files in the project to ensure consistent st...](/workflows/local-dev/fix-eslint-prettier-linting-errors-automatically)[### Generate .env from Example

ConfigEnvironmentSetup--- description: Safely create a local .env file from .env.example --- 1. \*\*Check for .env.example\*\*: - Ensure the example file exists. // turbo - Run `test -f .env.example && echo "✅ Found .env.example" || echo "❌ .env.example not found"` 2. \*\*Copy to .env.local\*\*: - Create your local...](/workflows/local-dev/generate-local-env-file-from-example)[### Setup Husky Git Hooks

GitAutomationQuality+1--- description: Automate code quality checks with pre-commit and pre-push hooks --- 1. \*\*Install Husky\*\*: - Install husky and lint-staged. // turbo - Run `npm install --save-dev husky lint-staged` 2. \*\*Initialize Husky\*\*: - Set up git hooks. // turbo - Run `npx husky init` 3. \*...](/workflows/local-dev/setup-husky-git-hooks-pre-commit-linting)
## Recommended Rules

[View more rules →](/rules)[### 🔄 Refactoring Agent - Safe Code Improvement

Agentic AIRefactoringClean CodeYou are an expert refactoring agent specialized in safely improving code quality without changing behavior. Apply systematic reasoning to identify ref...](/rules/agentic-ai/refactoring-agent)[### Strong Reasoner & Planner Agent (Official Google Template)

Agentic AIReasoningPlanningYou are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses. 📋 Source: Google Gemin...](/rules/agentic-ai/strong-reasoner-planner-agent)[### 🤖 AI Prompt Engineer Agent - LLM Expert

Agentic AIPrompt EngineeringLLMYou are an expert AI prompt engineer agent specialized in crafting effective prompts for Large Language Models. Apply systematic reasoning to design p...](/rules/agentic-ai/ai-prompt-engineer-agent)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![Codacy](https://app.codacy.com/static/images/favicon-16x16.png)
### Codacy

Official

Interact with [Codacy](https://www.codacy.com) API to query code quality issues, vulnerabilities, and coverage insights about your code.](/mcp/codacy)[![Composio](https://platform.composio.dev/favicon.ico)
### Composio

Official

Use [Composio](https://composio.dev) to connect 100+ tools. Zero setup. Auth built-in. Made for agents, works for humans.](/mcp/composio)[![Dot (GetDot.ai)](https://eu.getdot.ai/favicon.ico)
### Dot (GetDot.ai)

Official

Fetch, analyze or visualize data from your favorite database or data warehouse (Snowflake, BigQuery, Redshift, Databricks, Clickhouse, ...) with [Dot](https://getdot.ai), your AI Data Analyst. This remote MCP server is a one-click integration for user that have setup Dot.](/mcp/dot-getdot-ai)
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


