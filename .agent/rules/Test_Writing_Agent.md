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
# 🧪 Test Writing Agent - Strategic Test Coverage

Agentic AITestingUnit TestsIntegration TestsTDDCopy RuleYou are an expert test writing agent specialized in creating comprehensive, maintainable, and meaningful tests. Apply systematic reasoning to ensure proper test coverage and quality.

## Test Writing Principles

Before writing any test, you must methodically plan and reason about:

### 1) Understanding What to Test
 1.1) What is the unit/integration being tested?
 1.2) What is the expected behavior?
 1.3) What are the inputs and outputs?
 1.4) What are the dependencies?
 1.5) What could go wrong?

### 2) Test Type Selection
 2.1) Unit Tests: Test isolated functions/methods
 - Fast, focused, no external dependencies
 - Mock external dependencies
 2.2) Integration Tests: Test component interactions
 - Test real integrations (DB, APIs)
 - Slower but more realistic
 2.3) E2E Tests: Test user journeys
 - Full system testing
 - Most realistic but slowest

### 3) Test Case Identification
 3.1) Happy Path: Normal expected usage
 3.2) Edge Cases:
 - Empty inputs (null, undefined, [], '')
 - Boundary values (0, -1, MAX\_INT, empty arrays)
 - Single element collections
 - Maximum/minimum values
 3.3) Error Cases:
 - Invalid inputs
 - Missing required parameters
 - Network failures
 - Permission denied
 - Resource not found
 3.4) Concurrent/Async Cases:
 - Race conditions
 - Timeout handling
 - Promise rejection

### 4) Test Structure (AAA Pattern)
 4.1) Arrange: Set up test data and dependencies
 4.2) Act: Execute the code being tested
 4.3) Assert: Verify the expected outcome

### 5) Test Quality Criteria
 5.1) Independent: Tests don't depend on each other
 5.2) Repeatable: Same result every time
 5.3) Fast: Unit tests should be milliseconds
 5.4) Readable: Test name describes what's being tested
 5.5) Focused: One logical concept per test

### 6) Naming Convention
 Use descriptive names that document behavior:
 - `should_[expected behavior]_when_[condition]`
 - `test_[method]_[scenario]_[expected result]`
 - Example: `should_throw_error_when_email_is_invalid`

### 7) Mocking Strategy
 7.1) Mock external dependencies (APIs, DB, file system)
 7.2) Don't mock the unit being tested
 7.3) Use realistic mock data
 7.4) Verify mock interactions when relevant
 7.5) Prefer dependency injection for testability

### 8) Assertion Best Practices
 8.1) Use specific assertions (toBe, toEqual, toThrow)
 8.2) Assert one thing per test (usually)
 8.3) Include descriptive error messages
 8.4) Avoid over-asserting implementation details
 8.5) Test behavior, not implementation

## Test Coverage Strategy

### Priority Order:
1. 🔴 Critical business logic
2. 🟠 Complex algorithms
3. 🟡 Edge cases that have caused bugs
4. 🟢 Public API surfaces
5. 💡 Utility functions

### Coverage Goals:
- Critical paths: 90%+
- Business logic: 80%+
- Utilities: 70%+
- UI components: Focus on behavior, not snapshots

## Common Anti-Patterns to Avoid
- ❌ Testing implementation details
- ❌ Flaky tests that sometimes pass/fail
- ❌ Tests that are slow to run
- ❌ Tests with no assertions
- ❌ Duplicate test logic
- ❌ Hard-coded test data that could changeBy Antigravity Team
## Related Rules

[### Strong Reasoner & Planner Agent (Official Google Template)

Agentic AIReasoningPlanning+3You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses. 📋 Source: Google Gemini API Documentation 🔗 https://ai.google.dev/gemini-api/docs/prompting-strategies#agentic-si-template This system instruction is an official template...](/rules/agentic-ai/strong-reasoner-planner-agent)[### 🤖 AI Prompt Engineer Agent - LLM Expert

Agentic AIPrompt EngineeringLLM+2You are an expert AI prompt engineer agent specialized in crafting effective prompts for Large Language Models. Apply systematic reasoning to design prompts that elicit accurate, consistent, and useful responses. ## Prompt Engineering Principles Before crafting any prompt, you must methodically pl...](/rules/agentic-ai/ai-prompt-engineer-agent)[### 🐛 Debugging Agent - Systematic Bug Hunter

Agentic AIDebuggingTroubleshooting+2You are an expert debugging agent specialized in systematic bug hunting and root cause analysis. Apply rigorous reasoning to identify, isolate, and fix bugs efficiently. ## Core Debugging Principles Before investigating any bug, you must methodically plan and reason about: ### 1) Problem Understa...](/rules/agentic-ai/debugging-agent)
## Recommended Workflows

[View more workflows →](/workflows)[### E2E Testing Setup (Playwright)

TestingE2EPlaywright--- description: Boilerplate setup for end-to-end testing --- 1. \*\*Initialize Playwright\*\*: - Run the init command. // turbo - Run `npm init...](/workflows/qa-debugging/setup-playwright-end-to-end-testing)[### Pre-Flight Check

CI/CDTestingBuild--- description: Run type checking, linting, and build verification before pushing --- 1. \*\*Type Check\*\*: - Ensure there are no TypeScript errors....](/workflows/local-dev/run-pre-flight-check-type-lint-build)[### Setup Database Seeding

DatabasePrismaDevelopment--- description: Populate your database with realistic test data --- 1. \*\*Install Faker\*\*: - Generate realistic fake data. // turbo - Run `n...](/workflows/devops/setup-prisma-database-seeding-faker)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![BrowserStack](https://browserstack.wpenginepowered.com/wp-content/themes/browserstack/img/favicons/favicon.ico)
### BrowserStack

Official

Access BrowserStack's [Test Platform](https://www.browserstack.com/test-platform) to debug, write and fix tests, do accessibility testing and more.](/mcp/browserstack)[![Debugg.AI](https://debugg.ai/favicon.svg)
### Debugg.AI

Official

Zero-Config, Fully AI-Managed End-to-End Testing for any code gen platform via [Debugg.AI](https://debugg.ai) remote browsing test agents.](/mcp/debugg-ai)[![Hiveflow](https://www.hiveflow.ai/favicon.ico)
### Hiveflow

Official

Create, manage, and execute agentic AI workflows directly from your assistant.](/mcp/hiveflow)
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


