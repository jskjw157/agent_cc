[![Antigravity Logo](/logo.svg)Antigravity Codes](/)[Tutorial](/tutorial)[Download](/download)[Help](/troubleshooting)[Blog](/blog)[Community](/community)[Rules](/rules)[Workflows](/workflows)[MCPs](/mcp)[Advertise](/advertise)[Tutorial](/tutorial)[Download](/download)[Help](/troubleshooting)[Blog](/blog)[Community](/community)[Rules](/rules)[Workflows](/workflows)[MCPs](/mcp)[Advertise](/advertise)[MCP Servers](/mcp)/Awesome MCP Servers by wong2A
# Awesome MCP Servers by wong2

Community

(\*\*[website](https://mcpservers.org)\*\*) - A curated list of MCP servers by \*\*[wong2](https://github.com/wong2)\*\*

[View Source](https://github.com/wong2/awesome-mcp-servers)Share
#### Community Server

This server is maintained by the community. Please review the source code before connecting it to your agent.

Awesome MCP Servers by wong2 is not a server itself, but rather a meticulously curated and maintained directory dedicated to listing Minecraft Protocol (MCP) servers. For developers, this resource serves as an invaluable central hub for discovering, evaluating, and connecting with a diverse array of MCP servers, spanning various functionalities from game development and testing environments to community-driven projects. It aggregates essential information, providing a streamlined pathway to understanding the landscape of available servers and reducing the overhead of manual research.

The core value proposition for developers lies in its efficiency and reliability. Instead of sifting through fragmented online sources, developers can leverage this curated list to quickly identify servers relevant to their specific needs—whether that's finding a stable server for testing new mods, exploring different game modes, or researching server architecture. It eliminates much of the guesswork and vetting process, presenting a trusted collection maintained by wong2 and accessible via mcpservers.org. This resource empowers developers to accelerate their development cycles, foster community engagement, and enhance their understanding of the MCP ecosystem with ease.

Read More[Ad SlotAvailable📢 Advertise Your Tool Here🚀 Reach 16K+ AI developers•Learn more →](/advertise)
## What You Can Do

Discovering new Minecraft Protocol servers for game development and testing environments.Finding specific types of MCP servers for modding, particular game modes, or architectural research.Researching the broader MCP server ecosystem to identify trends and active projects.Programmatically parsing the list (e.g., from its GitHub repository) for data analysis or automated server discovery scripts.Identifying potential servers for community building, hosting, or educational purposes within the MCP landscape.
## Setup Guide

1Visit the official repository at the URL provided above2Review the README.md file for specific installation instructions3Install the MCP server using npm, pip, or the recommended package manager4Configure the server with your API keys or credentials (if required)5Add the server to your MCP client configuration (e.g., Antigravity, Cursor, Claude)6Restart your MCP client to load the new server7Test the connection by invoking a tool or resource from the server
## How to Connect in Antigravity

To connect to a custom MCP server in Antigravity:

1Open the MCP store via the "..." dropdown at the top of the editor's agent panel.2Click on "Manage MCP Servers"3Click on "View raw config"4Modify the `mcp_config.json` with your custom MCP server configuration.

Here is an example configuration compatible with MCP-enabled editors like **Antigravity**, **Windsurf**, Claude Desktop, and Cursor:

```
{
  "mcpServers": {
    "supabase-mcp-server": {
      "command": "npx",
      "args": [
        "-y",
        "@supabase/mcp-server-supabase@latest",
        "--access-token",
        "add-token-here"
      ],
      "env": {}
    },
    "github-mcp-server": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "ghcr.io/github/github-mcp-server"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "add-your-token-here"
      }
    }
  }
}
```

This configuration defines two servers: one running via `npx` (Supabase) and another via `docker` (GitHub). Make sure to replace the placeholder tokens with your actual API keys.

For a detailed step-by-step walkthrough, check out our [MCP Tutorial](/blog/antigravity-mcp-tutorial).

## How to Connect in Cursor

To add this MCP server to Cursor:

1Open **Cursor Settings** (File > Preferences > Cursor Settings).2Navigate to **Features** > **MCP Servers**.3Click on **"Add new MCP server"**.4Enter the Name, Command, and Arguments as specified in the configuration above.

For more details, refer to the [official Cursor MCP documentation](https://cursor.com/docs/context/mcp).

### Maintained By

wong2 (Community Maintained)

A community-maintained project by wong2, offering a curated list of Minecraft Protocol (MCP) servers for developers and enthusiasts.

[Visit Website](https://mcpservers.org)
### Tags

[tools](/mcp?search=tools)[productivity](/mcp?search=productivity)[data-analysis](/mcp?search=data-analysis)[api](/mcp?search=api)[Ad SlotAvailable Now📢 Advertise Your Tool Here🚀 Reach 16K+ AI developers•Learn more →](/advertise)
## Related Servers

[AActivityPub MCPA comprehensive MCP server that enables LLMs to explore and interact with the Fediverse through ActivityPub protocol, supporting actor discovery, timeline fetching, instance exploration, and WebFinger resolution across decentralized social networks.](/mcp/activitypub-mcp)[AAdobe Commerce— MCP to interact with Adobe Commerce GraphQL API, including orders, products, customers, etc.](/mcp/adobe-commerce)[AAI EnduranceAI-powered training platform for runners, cyclists, and triathletes with over 20 tools for workout management, activity analysis, performance predictions, and recovery tracking.](/mcp/ai-endurance)[AAirbnbProvides tools to search Airbnb and get listing details.](/mcp/airbnb)[AAlgorandA comprehensive MCP server for tooling interactions (40+) and resource accessibility (60+) plus many useful prompts for interacting with the Algorand blockchain.](/mcp/algorand)[AAmadeus(by donghyun-chae) - An MCP server to access, explore, and interact with Amadeus Flight Offers Search API for retrieving detailed flight options, including airline, times, duration, and pricing data.](/mcp/amadeus)[Browse all MCP Servers](/mcp)
## Explore More Resources

### ⚡ Rules

[View All Rules](/rules)[### Security & Penetration Testing

SecurityTestingPenTestYou are an expert in Security Testing and Penetration Testing. Key Principles: - Think like an attacker - Defense in Depth - Shift Left (Security ear...](/rules/testing-quality-assurance/security-penetration-testing)[### 🔄 Refactoring Agent - Safe Code Improvement

Agentic AIRefactoringClean CodeYou are an expert refactoring agent specialized in safely improving code quality without changing behavior. Apply systematic reasoning to identify ref...](/rules/agentic-ai/refactoring-agent)[### 📦 Code Migration Agent - Safe Upgrade Expert

Agentic AIMigrationUpgradeYou are an expert code migration agent specialized in safely upgrading frameworks, languages, and dependencies. Apply systematic reasoning to plan and...](/rules/agentic-ai/code-migration-agent)[### Web Forms & Validation Expert

FormsValidationUXYou are an expert in web forms and form validation. Key Principles: - Implement proper form UX - Use HTML5 validation attributes - Provide clear erro...](/rules/web-development/web-forms-validation)
### 🔄 Workflows

[View All Workflows](/workflows)[### Setup Local Database (Postgres)

DatabasePostgresLocal Development--- description: Quick setup for a local Postgres database using Docker --- 1. \*\*Install Docker Desktop\*\*: - If you don't have Docker installed, d...](/workflows/integrations/setup-local-postgres-database-docker-compose)[### Setup RBAC

SecurityAuthorizationRBAC--- description: Role-based permissions --- 1. \*\*Define Roles\*\*: ```prisma enum Role { USER ADMIN MODERATOR } ``` 2. \*\*Pr...](/workflows/production/setup-role-based-access-control-rbac)[### Nuke & Reinstall

npmTroubleshootingDependencies--- description: The nuclear option for when dependencies are completely broken --- 1. \*\*Remove node\_modules\*\*: - Delete the existing `node\_module...](/workflows/emergency/nuke-node-modules-and-reinstall-dependencies)[### Pre-Flight Check

CI/CDTestingBuild--- description: Run type checking, linting, and build verification before pushing --- 1. \*\*Type Check\*\*: - Ensure there are no TypeScript errors....](/workflows/local-dev/run-pre-flight-check-type-lint-build)[🪐 Antigravity.Codes](/)

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


