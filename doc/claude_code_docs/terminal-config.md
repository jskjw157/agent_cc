---
source: https://code.claude.com/docs/en/terminal-config
title: Optimize your terminal setup - Claude Code Docs
---

Skip to main content

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/light.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=536eade682636e84231afce2577f9509)![dark logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/dark.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=0766b3221061e80143e9f300733e640b)](/docs)

[Getting started](/docs/en/overview)[Build with Claude Code](/docs/en/sub-agents)[Deployment](/docs/en/third-party-integrations)[Administration](/docs/en/setup)[Configuration](/docs/en/settings)[Reference](/docs/en/cli-reference)[Resources](/docs/en/legal-and-compliance)

##### Configuration

  * [Settings](/docs/en/settings)
  * [Terminal configuration](/docs/en/terminal-config)
  * [Model configuration](/docs/en/model-config)
  * [Memory management](/docs/en/memory)
  * [Status line configuration](/docs/en/statusline)

Configuration

# Optimize your terminal setup

Claude Code works best when your terminal is properly configured. Follow these guidelines to optimize your experience.

### 

​

Themes and appearance

Claude cannot control the theme of your terminal. That’s handled by your terminal application. You can match Claude Code’s theme to your terminal any time via the `/config` command. For additional customization of the Claude Code interface itself, you can configure a [custom status line](/docs/en/statusline) to display contextual information like the current model, working directory, or git branch at the bottom of your terminal.

### 

​

Line breaks

You have several options for entering line breaks into Claude Code:

  * **Quick escape** : Type `\` followed by Enter to create a newline
  * **Keyboard shortcut** : Set up a keybinding to insert a newline

#### 

​

Set up Shift+Enter (VS Code or iTerm2):

Run `/terminal-setup` within Claude Code to automatically configure Shift+Enter.

#### 

​

Set up Option+Enter (VS Code, iTerm2 or macOS Terminal.app):

**For Mac Terminal.app:**

  1. Open Settings → Profiles → Keyboard
  2. Check “Use Option as Meta Key”

**For iTerm2 and VS Code terminal:**

  1. Open Settings → Profiles → Keys
  2. Under General, set Left/Right Option key to “Esc+“

### 

​

Notification setup

Never miss when Claude completes a task with proper notification configuration:

#### 

​

iTerm 2 system notifications

For iTerm 2 alerts when tasks complete:

  1. Open iTerm 2 Preferences
  2. Navigate to Profiles → Terminal
  3. Enable “Silence bell” and Filter Alerts → “Send escape sequence-generated alerts”
  4. Set your preferred notification delay

Note that these notifications are specific to iTerm 2 and not available in the default macOS Terminal.

#### 

​

Custom notification hooks

For advanced notification handling, you can create [notification hooks](/docs/en/hooks#notification) to run your own logic.

### 

​

Handling large inputs

When working with extensive code or long instructions:

  * **Avoid direct pasting** : Claude Code may struggle with very long pasted content
  * **Use file-based workflows** : Write content to a file and ask Claude to read it
  * **Be aware of VS Code limitations** : The VS Code terminal is particularly prone to truncating long pastes

### 

​

Vim Mode

Claude Code supports a subset of Vim keybindings that can be enabled with `/vim` or configured via `/config`. The supported subset includes:

  * Mode switching: `Esc` (to NORMAL), `i`/`I`, `a`/`A`, `o`/`O` (to INSERT)
  * Navigation: `h`/`j`/`k`/`l`, `w`/`e`/`b`, `0`/`$`/`^`, `gg`/`G`
  * Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)

Was this page helpful?

[Settings](/docs/en/settings)[Model configuration](/docs/en/model-config)

⌘I