---
source: https://code.claude.com/docs/en/overview
title: Claude Code overview - Claude Code Docs
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

Getting started

# Claude Code overview

Learn about Claude Code, Anthropic’s agentic coding tool that lives in your terminal and helps you turn ideas into code faster than ever before.

## 

​

Get started in 30 seconds

Prerequisites:

  * A [Claude.ai](https://claude.ai) (recommended) or [Claude Console](https://console.anthropic.com/) account

**Install Claude Code:** To install Claude Code, use one of the following methods:

  * Native Install (Recommended)

  * Homebrew

  * NPM

**macOS, Linux, WSL:**

Copy

Ask AI
    
    
    curl -fsSL https://claude.ai/install.sh | bash
    

**Windows PowerShell:**

Copy

Ask AI
    
    
    irm https://claude.ai/install.ps1 | iex
    

**Windows CMD:**

Copy

Ask AI
    
    
    curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
    

Copy

Ask AI
    
    
    brew install --cask claude-code
    

If you have [Node.js 18 or newer installed](https://nodejs.org/en/download/):

Copy

Ask AI
    
    
    npm install -g @anthropic-ai/claude-code
    

**Start using Claude Code:**

Copy

Ask AI
    
    
    cd your-project
    claude
    

You’ll be prompted to log in on first use. That’s it! [Continue with Quickstart (5 minutes) →](/docs/en/quickstart)

Claude Code automatically keeps itself up to date. See [advanced setup](/docs/en/setup) for installation options, manual updates, or uninstallation instructions. Visit [troubleshooting](/docs/en/troubleshooting) if you hit issues.

## 

​

What Claude Code does for you

  * **Build features from descriptions** : Tell Claude what you want to build in plain English. It will make a plan, write the code, and ensure it works.
  * **Debug and fix issues** : Describe a bug or paste an error message. Claude Code will analyze your codebase, identify the problem, and implement a fix.
  * **Navigate any codebase** : Ask anything about your team’s codebase, and get a thoughtful answer back. Claude Code maintains awareness of your entire project structure, can find up-to-date information from the web, and with [MCP](/docs/en/mcp) can pull from external data sources like Google Drive, Figma, and Slack.
  * **Automate tedious tasks** : Fix fiddly lint issues, resolve merge conflicts, and write release notes. Do all this in a single command from your developer machines, or automatically in CI.

## 

​

Why developers love Claude Code

  * **Works in your terminal** : Not another chat window. Not another IDE. Claude Code meets you where you already work, with the tools you already love.
  * **Takes action** : Claude Code can directly edit files, run commands, and create commits. Need more? [MCP](/docs/en/mcp) lets Claude read your design docs in Google Drive, update your tickets in Jira, or use _your_ custom developer tooling.
  * **Unix philosophy** : Claude Code is composable and scriptable. `tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"` _works_. Your CI can run `claude -p "If there are new text strings, translate them into French and raise a PR for @lang-fr-team to review"`.
  * **Enterprise-ready** : Use the Claude API, or host on AWS or GCP. Enterprise-grade [security](/docs/en/security), [privacy](/docs/en/data-usage), and [compliance](https://trust.anthropic.com/) is built-in.

## 

​

Next steps

## [QuickstartSee Claude Code in action with practical examples](/docs/en/quickstart)## [Common workflowsStep-by-step guides for common workflows](/docs/en/common-workflows)## [TroubleshootingSolutions for common issues with Claude Code](/docs/en/troubleshooting)## [IDE setupAdd Claude Code to your IDE](/docs/en/vs-code)

## 

​

Additional resources

## [About Claude CodeLearn more about Claude Code on claude.com](https://claude.com/product/claude-code)## [Build with the Agent SDKCreate custom AI agents with the Claude Agent SDK](https://docs.claude.com/en/docs/agent-sdk/overview)## [Host on AWS or GCPConfigure Claude Code with Amazon Bedrock or Google Vertex AI](/docs/en/third-party-integrations)## [SettingsCustomize Claude Code for your workflow](/docs/en/settings)## [CommandsLearn about CLI commands and controls](/docs/en/cli-reference)## [Reference implementationClone our development container reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer)## [SecurityDiscover Claude Code’s safeguards and best practices for safe usage](/docs/en/security)## [Privacy and data usageUnderstand how Claude Code handles your data](/docs/en/data-usage)

Was this page helpful?

[Quickstart](/docs/en/quickstart)

⌘I