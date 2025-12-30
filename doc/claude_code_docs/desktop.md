---
source: https://code.claude.com/docs/en/desktop
title: Claude Code on desktop - Claude Code Docs
---

Skip to main content

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/light.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=536eade682636e84231afce2577f9509)![dark logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/dark.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=0766b3221061e80143e9f300733e640b)](/docs)

[Getting started](/docs/en/overview)[Build with Claude Code](/docs/en/sub-agents)[Deployment](/docs/en/third-party-integrations)[Administration](/docs/en/setup)[Configuration](/docs/en/settings)[Reference](/docs/en/cli-reference)[Resources](/docs/en/legal-and-compliance)

##### Getting started

  * [Overview](/docs/en/overview)
  * [Quickstart](/docs/en/quickstart)
  * [Common workflows](/docs/en/common-workflows)

##### Outside of the terminal

  * [Claude Code on the web](/docs/en/claude-code-on-the-web)
  * [Claude Code on desktop](/docs/en/desktop)
  * [Chrome extension (beta)](/docs/en/chrome)
  * [Visual Studio Code](/docs/en/vs-code)
  * [JetBrains IDEs](/docs/en/jetbrains)
  * [GitHub Actions](/docs/en/github-actions)
  * [GitLab CI/CD](/docs/en/gitlab-ci-cd)
  * [Claude Code in Slack](/docs/en/slack)

Outside of the terminal

# Claude Code on desktop

Run Claude Code tasks locally or on secure cloud infrastructure with the Claude desktop app

![Claude Code on desktop interface](https://mintcdn.com/claude-code/zEGbGSbinVtT3BLw/images/desktop-interface.png?fit=max&auto=format&n=zEGbGSbinVtT3BLw&q=85&s=c4e9dc9737b437d36ab253b75a1cc595)

## 

​

Claude Code on desktop (Preview)

The Claude desktop app provides a native interface for running multiple Claude Code sessions on your local machine and seamless integration with Claude Code on the web.

## 

​

Features

Claude Code on desktop provides:

  * **Parallel local sessions with`git` worktrees**: Run multiple Claude Code sessions simultaneously in the same repository, each with its own isolated `git` worktree
  * **Include files listed in your`.gitignore` in your worktrees**: Automatically copy files in your `.gitignore`, like `.env`, to new worktrees using `.worktreeinclude`
  * **Launch Claude Code on the web** : Kick off secure cloud sessions directly from the desktop app

## 

​

Installation

Download and install the Claude Desktop app from [claude.ai/download](https://claude.ai/download)

Local sessions are not available on Windows arm64 architectures.

## 

​

Using Git worktrees

Claude Code on desktop enables running multiple Claude Code sessions in the same repository using Git worktrees. Each session gets its own isolated worktree, allowing Claude to work on different tasks without conflicts. The default location for worktrees is `~/.claude-worktrees` but this can be configured in your settings on the Claude desktop app.

If you start a local session in a folder that does not have Git initialized, the desktop app will not create a new worktree.

### 

​

Copying files ignored with `.gitignore`

When Claude Code creates a worktree, files ignored via `.gitignore` aren’t automatically available. Including a `.worktreeinclude` file solves this by specifying which ignored files should be copied to new worktrees. Create a `.worktreeinclude` file in your repository root:

Copy

Ask AI
    
    
    .env
    .env.local
    .env.*
    **/.claude/settings.local.json
    

The file uses `.gitignore`-style patterns. When a worktree is created, files matching these patterns that are also in your `.gitignore` will be copied from your main repository to the worktree.

Only files that are both matched by `.worktreeinclude` AND listed in `.gitignore` are copied. This prevents accidentally duplicating tracked files.

### 

​

Launch Claude Code on the web

From the desktop app, you can kick off Claude Code sessions that run on Anthropic’s secure cloud infrastructure. This is useful for: To start a web session from desktop, select a remote environment when creating a new session. For more details, see [Claude Code on the web](/docs/en/claude-code-on-the-web).

## 

​

Bundled Claude Code version

Claude Code on desktop includes a bundled, stable version of Claude Code to ensure a consistent experience for all desktop users. The bundled version is required and downloaded on first launch even if a version of Claude Code exists on the computer. Desktop automatically manages version updates and cleans up old versions.

The bundled Claude Code version in Desktop may differ from the latest CLI version. Desktop prioritizes stability while the CLI may have newer features.

## 

​

Environment configuration

For local environments, Claude Code on desktop automatically extracts your `$PATH` environment variable from your shell configuration. This allows local sessions to access development tools like `yarn`, `npm`, `node`, and other commands available in your terminal without additional setup.

### 

​

Custom environment variables

Select “Local” environment, then to the right, select the settings button. This will open a dialog where you can update local environment variables. This is useful for setting project-specific variables or API keys that your development workflows require. Environment variable values are masked in the UI for security reasons.

Environment variables must be specified as key-value pairs, in [`.env` format](https://www.dotenv.org/). For example:

Copy

Ask AI
    
    
    API_KEY=your_api_key
    DEBUG=true
    
    # Multiline values - wrap in quotes
    CERT="-----BEGIN CERT-----
    MIIE...
    -----END CERT-----"
    

## 

​

Enterprise configuration

Organizations can disable local Claude Code use in the desktop application with the `isClaudeCodeForDesktopEnabled` [enterprise policy option](https://support.claude.com/en/articles/12622667-enterprise-configuration#h_003283c7cb). Additionally, Claude Code on the web can be disabled in your [admin settings](https://claude.ai/admin-settings/claude-code).

## 

​

Related resources

  * [Claude Code on the web](/docs/en/claude-code-on-the-web)
  * [Claude Desktop support articles](https://support.claude.com/en/collections/16163169-claude-desktop)
  * [Enterprise Configuration](https://support.claude.com/en/articles/12622667-enterprise-configuration)
  * [Common workflows](/docs/en/common-workflows)
  * [Settings reference](/docs/en/settings)

Was this page helpful?

[Claude Code on the web](/docs/en/claude-code-on-the-web)[Chrome extension (beta)](/docs/en/chrome)

⌘I