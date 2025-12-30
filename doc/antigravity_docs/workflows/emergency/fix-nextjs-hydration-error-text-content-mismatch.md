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
[Back to 🚑 Emergency Room](/workflows/emergency)
# Fix Next.js Hydration Errors

Next.jsDebuggingHydrationReactDownloadCopy Workflow---
description: Systematically debug and fix 'Text content does not match server-rendered HTML' errors
---

1. \*\*Check for Invalid HTML Nesting\*\*:
 - The most common cause is invalid HTML, like a `<div>` inside a `<p>` tag.
 - \*\*React 19 Update:\*\* React 19 provides much better hydration error diffs. Check the console for the exact mismatch location.
 - \*\*Bad:\*\* `<p><div>Content</div></p>`
 - \*\*Good:\*\* `<div><div>Content</div></div>` or `<p><span>Content</span></p>`

2. \*\*Handle Random Values (Dates, Math.random)\*\*:
 - If you render data that changes between server and client (like `new Date()` or `Math.random()`), it will cause a mismatch.
 - \*\*Fix:\*\* Use a `useEffect` to set the value only on the client.
```
const [mounted, setMounted] = useState(false);
   useEffect(() => setMounted(true), []);
   if (!mounted) return null; // or a loading skeleton
```

3. \*\*Fix Browser-Only APIs\*\*:
 - Accessing `window` or `localStorage` during the initial render will fail on the server.
 - \*\*Fix:\*\* Ensure these are only accessed inside `useEffect` or event handlers.

4. \*\*Suppress Warning (Last Resort)\*\*:
 - If you absolutely cannot fix the mismatch (e.g., a timestamp that \*must\* be dynamic), you can suppress the warning on a specific element.
```
<div suppressHydrationWarning>
     {new Date().toLocaleTimeString()}
   </div>
```

5. \*\*Pro Tips\*\*:
 - Use the \*\*React DevTools\*\* Profiler to see exactly what props are changing.
 - Check your browser extensions; sometimes they inject HTML that messes with hydration (try Incognito mode).By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `fix-nextjs-hydration-error-text-content-mismatch.md`
4. In Antigravity, type `/fix_nextjs_hydration_error_text_content_mismatch` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Debugging Infinite Re-renders

ReactDebuggingPerformance+1--- description: Track down and fix infinite loops in useEffect and component rendering --- 1. \*\*Check `useEffect` Dependencies\*\*: - The most common culprit is a `useEffect` that updates a state variable which is also in its dependency array. - \*\*Bad Pattern:\*\* ```tsx useEffect(() =...](/workflows/emergency/debug-react-infinite-rerenders-useeffect-loop)[### Nuke & Reinstall

npmTroubleshootingDependencies+1--- description: The nuclear option for when dependencies are completely broken --- 1. \*\*Remove node\_modules\*\*: - Delete the existing `node\_modules` folder to clear installed packages. // turbo - Run `rm -rf node\_modules` 2. \*\*Remove Lock File\*\*: - Delete `package-lock.json`, `yarn.loc...](/workflows/emergency/nuke-node-modules-and-reinstall-dependencies)
## Recommended Rules

[View more rules →](/rules)[### 🐛 Debugging Agent - Systematic Bug Hunter

Agentic AIDebuggingTroubleshootingYou are an expert debugging agent specialized in systematic bug hunting and root cause analysis. Apply rigorous reasoning to identify, isolate, and fi...](/rules/agentic-ai/debugging-agent)[### Next.js App Router Best Practices

Next.jsApp RouterRoutingYou are an expert in Next.js App Router. Key Principles: - Use Server Components by default - Use Client Components only when necessary (interactivit...](/rules/nextjs/nextjs-app-router-best-practices)[### Next.js Performance Optimization

Next.jsPerformanceOptimizationYou are an expert in Next.js performance optimization. Key Principles: - Optimize images and fonts - Minimize client-side JavaScript - Use proper cac...](/rules/nextjs/nextjs-performance-optimization)
## Recommended MCP Servers

[View more MCP servers →](/mcp)[![AgentOps](https://github.com/AgentOps-AI/agentops/blob/main/docs/favicon.png)
### AgentOps

Official

Provide observability and tracing for debugging AI agents with [AgentOps](https://www.agentops.ai/) API.](/mcp/agentops)[![Chrome DevTools](https://www.google.com/chrome/static/images/favicons/favicon-32x32.png)
### Chrome DevTools

Official

Enable AI coding assistants to debug web pages directly in Chrome, providing runtime insights and debugging capabilities.](/mcp/chrome-devtools)[![Kuzu](https://kuzudb.com/favicon.ico)
### Kuzu

Official

This server enables LLMs to inspect database schemas and execute queries on the provided Kuzu graph database. See [blog](https://blog.kuzudb.com/post/2025-03-23-kuzu-mcp-server/)) for a debugging use case.](/mcp/kuzu)
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


