---
source: https://code.claude.com/docs/en/network-config
title: Enterprise network configuration - Claude Code Docs
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

# Enterprise network configuration

Configure Claude Code for enterprise environments with proxy servers, custom Certificate Authorities (CA), and mutual Transport Layer Security (mTLS) authentication.

Claude Code supports various enterprise network and security configurations through environment variables. This includes routing traffic through corporate proxy servers, trusting custom Certificate Authorities (CA), and authenticating with mutual Transport Layer Security (mTLS) certificates for enhanced security.

All environment variables shown on this page can also be configured in [`settings.json`](/docs/en/settings).

## 

​

Proxy configuration

### 

​

Environment variables

Claude Code respects standard proxy environment variables:

Copy

Ask AI
    
    
    # HTTPS proxy (recommended)
    export HTTPS_PROXY=https://proxy.example.com:8080
    
    # HTTP proxy (if HTTPS not available)
    export HTTP_PROXY=http://proxy.example.com:8080
    
    # Bypass proxy for specific requests - space-separated format
    export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
    # Bypass proxy for specific requests - comma-separated format
    export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
    # Bypass proxy for all requests
    export NO_PROXY="*"
    

Claude Code does not support SOCKS proxies.

### 

​

Basic authentication

If your proxy requires basic authentication, include credentials in the proxy URL:

Copy

Ask AI
    
    
    export HTTPS_PROXY=http://username:password@proxy.example.com:8080
    

Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.

For proxies requiring advanced authentication (NTLM, Kerberos, etc.), consider using an LLM Gateway service that supports your authentication method.

## 

​

Custom CA certificates

If your enterprise environment uses custom CAs for HTTPS connections (whether through a proxy or direct API access), configure Claude Code to trust them:

Copy

Ask AI
    
    
    export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
    

## 

​

mTLS authentication

For enterprise environments requiring client certificate authentication:

Copy

Ask AI
    
    
    # Client certificate for authentication
    export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem
    
    # Client private key
    export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem
    
    # Optional: Passphrase for encrypted private key
    export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE="your-passphrase"
    

## 

​

Network access requirements

Claude Code requires access to the following URLs:

  * `api.anthropic.com` \- Claude API endpoints
  * `claude.ai` \- WebFetch safeguards
  * `statsig.anthropic.com` \- Telemetry and metrics
  * `sentry.io` \- Error reporting

Ensure these URLs are allowlisted in your proxy configuration and firewall rules. This is especially important when using Claude Code in containerized or restricted network environments.

## 

​

Additional resources

  * [Claude Code settings](/docs/en/settings)
  * [Environment variables reference](/docs/en/settings#environment-variables)
  * [Troubleshooting guide](/docs/en/troubleshooting)

Was this page helpful?

[Microsoft Foundry](/docs/en/microsoft-foundry)[LLM gateway](/docs/en/llm-gateway)

⌘I