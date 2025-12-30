---
source: https://code.claude.com/docs/en/analytics
title: Analytics - Claude Code Docs
---

Skip to main content

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/light.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=536eade682636e84231afce2577f9509)![dark logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/dark.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=0766b3221061e80143e9f300733e640b)](/docs)

[Getting started](/docs/en/overview)[Build with Claude Code](/docs/en/sub-agents)[Deployment](/docs/en/third-party-integrations)[Administration](/docs/en/setup)[Configuration](/docs/en/settings)[Reference](/docs/en/cli-reference)[Resources](/docs/en/legal-and-compliance)

##### Administration

  * [Advanced installation](/docs/en/setup)
  * [Identity and Access Management](/docs/en/iam)
  * [Security](/docs/en/security)
  * [Data usage](/docs/en/data-usage)
  * [Monitoring](/docs/en/monitoring-usage)
  * [Costs](/docs/en/costs)
  * [Analytics](/docs/en/analytics)
  * [Create and distribute a plugin marketplace](/docs/en/plugin-marketplaces)

Administration

# Analytics

View detailed usage insights and productivity metrics for your organization’s Claude Code deployment.

Claude Code provides an analytics dashboard that helps organizations understand developer usage patterns, track productivity metrics, and optimize their Claude Code adoption.

Analytics are currently available only for organizations using Claude Code with the Claude API through the Claude Console.

## 

​

Access analytics

Navigate to the analytics dashboard at [console.anthropic.com/claude-code](https://console.anthropic.com/claude-code).

### 

​

Required roles

  * **Primary Owner**
  * **Owner**
  * **Billing**
  * **Admin**
  * **Developer**

Users with **User** , **Claude Code User** or **Membership Admin** roles cannot access analytics.

## 

​

Available metrics

### 

​

Lines of code accepted

Total lines of code written by Claude Code that users have accepted in their sessions.

  * Excludes rejected code suggestions
  * Doesn’t track subsequent deletions

### 

​

Suggestion accept rate

Percentage of times users accept code editing tool usage, including:

  * Edit
  * Write
  * NotebookEdit

### 

​

Activity

**users** : Number of active users in a given day (number on left Y-axis) **sessions** : Number of active sessions in a given day (number on right Y-axis)

### 

​

Spend

**users** : Number of active users in a given day (number on left Y-axis) **spend** : Total dollars spent in a given day (number on right Y-axis)

### 

​

Team insights

**Members** : All users who have authenticated to Claude Code

  * API key users are displayed by **API key identifier**
  * OAuth users are displayed by **email address**

**Spend this month:** Per-user total spend for the current month. **Lines this month:** Per-user total of accepted code lines for the current month.

## 

​

Using analytics effectively

### 

​

Monitor adoption

Track team member status to identify:

  * Active users who can share best practices
  * Overall adoption trends across your organization

### 

​

Measure productivity

Tool acceptance rates and code metrics help you:

  * Understand developer satisfaction with Claude Code suggestions
  * Track code generation effectiveness
  * Identify opportunities for training or process improvements

## 

​

Related resources

  * [Monitoring usage with OpenTelemetry](/docs/en/monitoring-usage) for custom metrics and alerting
  * [Identity and access management](/docs/en/iam) for role configuration

Was this page helpful?

[Costs](/docs/en/costs)[Create and distribute a plugin marketplace](/docs/en/plugin-marketplaces)

⌘I