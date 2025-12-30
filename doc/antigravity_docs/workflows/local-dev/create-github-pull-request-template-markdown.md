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
# Create GitHub PR Template

GitGitHubTeamDocumentationDownloadCopy Workflow---
description: Standardize pull request descriptions for better code reviews
---

1. \*\*Create Template Directory\*\*:
 - GitHub looks for templates in `.github/` folder.
 // turbo
 - Run `mkdir -p .github`

2. \*\*Create Pull Request Template\*\*:
 - Create the template file with structured content.
 ```markdown\n ## Description\n Briefly describe what this PR does.\n \n ## Type of Change\n - [ ] Bug fix\n - [ ] New feature\n - [ ] Breaking change\n - [ ] Documentation update\n \n ## Testing\n - [ ] I have tested these changes locally\n - [ ] I have added/updated tests\n - [ ] All tests pass\n \n ## Screenshots (if applicable)\n \n ## Checklist\n - [ ] My code follows the project's style guidelines\n - [ ] I have performed a self-review\n - [ ] I have commented complex code\n - [ ] I have updated documentation\n - [ ] No new warnings generated\n \n ## Related Issues\n Closes #\n` ``\n - Save this as` .github/PULL\_REQUEST\_TEMPLATE.md`\n
3. **Commit and Push**:
 - Add the template to your repository.
 // turbo
 - Run` git add .github/PULL\_REQUEST\_TEMPLATE.md && git commit -m \"Add PR template\" && git push `4. **Test It**:
 - Create a new PR and the template will auto-populate.

5. **Pro Tips**:
 - Customize the template for your team's workflow.
 - Add a link to your contributing guidelines.
 - Use multiple templates for different PR types (create` .github/PULL\_REQUEST\_TEMPLATE/` folder).By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `create-github-pull-request-template-markdown.md`
4. In Antigravity, type `/create_github_pull_request_template_markdown` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Setup Husky Git Hooks

GitAutomationQuality+1--- description: Automate code quality checks with pre-commit and pre-push hooks --- 1. \*\*Install Husky\*\*: - Install husky and lint-staged. // turbo - Run `npm install --save-dev husky lint-staged` 2. \*\*Initialize Husky\*\*: - Set up git hooks. // turbo - Run `npx husky init` 3. \*...](/workflows/local-dev/setup-husky-git-hooks-pre-commit-linting)[### Kill Port 3000

DevOpsTerminalProcess--- description: Instantly find and kill the process hogging your dev port --- 1. \*\*The Best Way (Cross-Platform)\*\*: - Kill it in one command using npx. Works on Mac, Windows, and Linux. // turbo - Run `npx kill-port 3000` 2. \*\*Mac/Linux Manual Method\*\*: - Find PID: `lsof -ti:3000` ...](/workflows/local-dev/kill-process-on-port-3000-terminal-command)[### Generate .env from Example

ConfigEnvironmentSetup--- description: Safely create a local .env file from .env.example --- 1. \*\*Check for .env.example\*\*: - Ensure the example file exists. // turbo - Run `test -f .env.example && echo "✅ Found .env.example" || echo "❌ .env.example not found"` 2. \*\*Copy to .env.local\*\*: - Create your local...](/workflows/local-dev/generate-local-env-file-from-example)
## Recommended Rules

[View more rules →](/rules)[### Git Feature Branch Workflow

WorkflowsGitVersion ControlCreate a workflow to start new feature branches synchronized with main. Workflow File: .agent/workflows/start\_feature.md ```markdown --- description...](/rules/antigravity-workflows/git-feature-branch-workflow)[### CI/CD Pipelines (GitHub Actions, GitLab CI)

CI/CDGitHub ActionsGitLab CIYou are an expert in CI/CD pipelines, specifically GitHub Actions and GitLab CI. Key Principles: - Fail fast and provide feedback - Automate everythi...](/rules/devops-infrastructure/ci-cd-pipelines-automation)[### GitOps & ArgoCD Expert

GitOpsArgoCDKubernetesYou are an expert in GitOps methodology and ArgoCD. Key Principles: - Git as the single source of truth - Declarative infrastructure and applications...](/rules/devops-infrastructure/gitops-argocd-expert)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![Detailer](https://detailer.ginylil.com/favicon.ico)
### Detailer

Official

Instantly generate rich, AI-powered documentation for your GitHub repositories. Designed for AI agents to gain deep project context before taking action.](/mcp/detailer)[![GreptimeDB](https://greptime.com/favicon.ico)
### GreptimeDB

Official

Provides AI assistants with a secure and structured way to explore and analyze data in [GreptimeDB](https://github.com/GreptimeTeam/greptimedb).](/mcp/greptimedb)[G
### GitMCP

Community

gitmcp.io is a generic remote MCP server to connect to ANY GitHub repository or project documentation effortlessly](/mcp/gitmcp)
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


