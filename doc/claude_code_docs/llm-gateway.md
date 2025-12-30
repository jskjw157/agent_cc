---
source: https://code.claude.com/docs/en/llm-gateway
title: LLM gateway configuration - Claude Code Docs
---

Skip to main content

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/light.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=536eade682636e84231afce2577f9509)![dark logo](https://mintcdn.com/claude-code/o69F7a6qoW9vboof/logo/dark.svg?fit=max&auto=format&n=o69F7a6qoW9vboof&q=85&s=0766b3221061e80143e9f300733e640b)](/docs)

[Getting started](/docs/en/overview)[Build with Claude Code](/docs/en/sub-agents)[Deployment](/docs/en/third-party-integrations)[Administration](/docs/en/setup)[Configuration](/docs/en/settings)[Reference](/docs/en/cli-reference)[Resources](/docs/en/legal-and-compliance)

##### Deployment

  * [Overview](/docs/en/third-party-integrations)
  * [Amazon Bedrock](/docs/en/amazon-bedrock)
  * [Google Vertex AI](/docs/en/google-vertex-ai)
  * [Microsoft Foundry](/docs/en/microsoft-foundry)
  * [Network configuration](/docs/en/network-config)
  * [LLM gateway](/docs/en/llm-gateway)
  * [Development containers](/docs/en/devcontainer)
  * [Sandboxing](/docs/en/sandboxing)

Deployment

# LLM gateway configuration

Learn how to configure Claude Code to work with LLM gateway solutions. Covers gateway requirements, authentication configuration, model selection, and provider-specific endpoint setup.

LLM gateways provide a centralized proxy layer between Claude Code and model providers, often providing:

  * **Centralized authentication** \- Single point for API key management
  * **Usage tracking** \- Monitor usage across teams and projects
  * **Cost controls** \- Implement budgets and rate limits
  * **Audit logging** \- Track all model interactions for compliance
  * **Model routing** \- Switch between providers without code changes

## 

​

Gateway requirements

For an LLM gateway to work with Claude Code, it must meet the following requirements: **API format** The gateway must expose to clients at least one of the following API formats:

  1. **Anthropic Messages** : `/v1/messages`, `/v1/messages/count_tokens`
     * Must forward request headers: `anthropic-beta`, `anthropic-version`
  2. **Bedrock InvokeModel** : `/invoke`, `/invoke-with-response-stream`
     * Must preserve request body fields: `anthropic_beta`, `anthropic_version`
  3. **Vertex rawPredict** : `:rawPredict`, `:streamRawPredict`, `/count-tokens:rawPredict`
     * Must forward request headers: `anthropic-beta`, `anthropic-version`

Failure to forward headers or preserve body fields may result in reduced functionality or inability to use Claude Code features.

Claude Code determines which features to enable based on the API format. When using the Anthropic Messages format with Bedrock or Vertex, you may need to set environment variable `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`.

## 

​

Configuration

### 

​

Model selection

By default, Claude Code will use standard model names for the selected API format. If you have configured custom model names in your gateway, use the environment variables documented in [Model configuration](/docs/en/model-config) to match your custom names.

## 

​

LiteLLM configuration

LiteLLM is a third-party proxy service. Anthropic doesn’t endorse, maintain, or audit LiteLLM’s security or functionality. This guide is provided for informational purposes and may become outdated. Use at your own discretion.

### 

​

Prerequisites

  * Claude Code updated to the latest version
  * LiteLLM Proxy Server deployed and accessible
  * Access to Claude models through your chosen provider

### 

​

Basic LiteLLM setup

**Configure Claude Code** :

#### 

​

Authentication methods

##### Static API key

Simplest method using a fixed API key:

Copy

Ask AI
    
    
    # Set in environment
    export ANTHROPIC_AUTH_TOKEN=sk-litellm-static-key
    
    # Or in Claude Code settings
    {
      "env": {
        "ANTHROPIC_AUTH_TOKEN": "sk-litellm-static-key"
      }
    }
    

This value will be sent as the `Authorization` header.

##### Dynamic API key with helper

For rotating keys or per-user authentication:

  1. Create an API key helper script:

Copy

Ask AI
    
    
    #!/bin/bash
    # ~/bin/get-litellm-key.sh
    
    # Example: Fetch key from vault
    vault kv get -field=api_key secret/litellm/claude-code
    
    # Example: Generate JWT token
    jwt encode \
      --secret="${JWT_SECRET}" \
      --exp="+1h" \
      '{"user":"'${USER}'","team":"engineering"}'
    

  2. Configure Claude Code settings to use the helper:

Copy

Ask AI
    
    
    {
      "apiKeyHelper": "~/bin/get-litellm-key.sh"
    }
    

  3. Set token refresh interval:

Copy

Ask AI
    
    
    # Refresh every hour (3600000 ms)
    export CLAUDE_CODE_API_KEY_HELPER_TTL_MS=3600000
    

This value will be sent as `Authorization` and `X-Api-Key` headers. The `apiKeyHelper` has lower precedence than `ANTHROPIC_AUTH_TOKEN` or `ANTHROPIC_API_KEY`.

#### 

​

Unified endpoint (recommended)

Using LiteLLM’s [Anthropic format endpoint](https://docs.litellm.ai/docs/anthropic_unified):

Copy

Ask AI
    
    
    export ANTHROPIC_BASE_URL=https://litellm-server:4000
    

**Benefits of the unified endpoint over pass-through endpoints:**

  * Load balancing
  * Fallbacks
  * Consistent support for cost tracking and end-user tracking

#### 

​

Provider-specific pass-through endpoints (alternative)

##### Claude API through LiteLLM

Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/anthropic_completion):

Copy

Ask AI
    
    
    export ANTHROPIC_BASE_URL=https://litellm-server:4000/anthropic
    

##### Amazon Bedrock through LiteLLM

Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/bedrock):

Copy

Ask AI
    
    
    export ANTHROPIC_BEDROCK_BASE_URL=https://litellm-server:4000/bedrock
    export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
    export CLAUDE_CODE_USE_BEDROCK=1
    

##### Google Vertex AI through LiteLLM

Using [pass-through endpoint](https://docs.litellm.ai/docs/pass_through/vertex_ai):

Copy

Ask AI
    
    
    export ANTHROPIC_VERTEX_BASE_URL=https://litellm-server:4000/vertex_ai/v1
    export ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
    export CLAUDE_CODE_SKIP_VERTEX_AUTH=1
    export CLAUDE_CODE_USE_VERTEX=1
    export CLOUD_ML_REGION=us-east5
    

For more detailed information, refer to the [LiteLLM documentation](https://docs.litellm.ai/).

## 

​

Additional resources

  * [LiteLLM documentation](https://docs.litellm.ai/)
  * [Claude Code settings](/docs/en/settings)
  * [Enterprise network configuration](/docs/en/network-config)
  * [Third-party integrations overview](/docs/en/third-party-integrations)

Was this page helpful?

[Network configuration](/docs/en/network-config)[Development containers](/docs/en/devcontainer)

⌘I