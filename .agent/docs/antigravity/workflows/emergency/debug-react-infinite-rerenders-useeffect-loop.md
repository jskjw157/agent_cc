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
# Debugging Infinite Re-renders

ReactDebuggingPerformanceHooksDownloadCopy Workflow---
description: Track down and fix infinite loops in useEffect and component rendering
---

1. \*\*Check `useEffect` Dependencies\*\*:
 - The most common culprit is a `useEffect` that updates a state variable which is also in its dependency array.
 - \*\*Bad Pattern:\*\*
```
useEffect(() => {
       setCount(count + 1);
     }, [count]); // Depends on 'count' -> Infinite Loop!
```

 - \*\*Fix:\*\* Use the functional update form or remove the dependency if not needed.

2. \*\*Unstable Object References\*\*:
 - If you pass an object or array as a dependency, React compares it by reference. Creating a new object on every render causes the effect to run every time.
 - \*\*Fix:\*\* Wrap the object in `useMemo` or move it outside the component.
```
const options = useMemo(() => ({ id: 1 }), []);
```

3. \*\*Use `useTraceUpdate` Hook\*\*:
 - Copy this hook to debug exactly which prop is changing.
```
function useTraceUpdate(props) {
     const prev = useRef(props);
     useEffect(() => {
       const changedProps = Object.entries(props).reduce((ps, [k, v]) => {
         if (prev.current[k] !== v) ps[k] = [prev.current[k], v];
         return ps;
       }, {});
       if (Object.keys(changedProps).length > 0) {
         console.log('Changed props:', changedProps);
       }
       prev.current = props;
     });
   }
```

4. \*\*Pro Tips\*\*:
 - Install the \*\*eslint-plugin-react-hooks\*\* package. It will automatically warn you about missing or circular dependencies.By Antigravity Team
### How to Use This Workflow

1. Click **"Download"** above
2. In your project, create the directory: `.agent/workflows/`
3. Save the file as `debug-react-infinite-rerenders-useeffect-loop.md`
4. In Antigravity, type `/debug_react_infinite_rerenders_useeffect_loop` or just describe what you want to do

[Learn more about workflows →](/blog/workflows)

## Related Workflows

[### Fix Next.js Hydration Errors

Next.jsDebuggingHydration+1--- description: Systematically debug and fix 'Text content does not match server-rendered HTML' errors --- 1. \*\*Check for Invalid HTML Nesting\*\*: - The most common cause is invalid HTML, like a `<div>` inside a `<p>` tag. - \*\*React 19 Update:\*\* React 19 provides much better hydration error d...](/workflows/emergency/fix-nextjs-hydration-error-text-content-mismatch)[### Nuke & Reinstall

npmTroubleshootingDependencies+1--- description: The nuclear option for when dependencies are completely broken --- 1. \*\*Remove node\_modules\*\*: - Delete the existing `node\_modules` folder to clear installed packages. // turbo - Run `rm -rf node\_modules` 2. \*\*Remove Lock File\*\*: - Delete `package-lock.json`, `yarn.loc...](/workflows/emergency/nuke-node-modules-and-reinstall-dependencies)
## Recommended Rules

[View more rules →](/rules)[### React Hooks Best Practices

ReactHooksBest PracticesYou are an expert in React Hooks. Key Principles: - Follow Rules of Hooks strictly - Use custom hooks for reusable logic - Optimize dependency arrays...](/rules/react/react-hooks-best-practices)[### React Performance Optimization

ReactPerformanceOptimizationYou are an expert in React performance optimization. Key Principles: - Measure before optimizing - Minimize re-renders - Optimize bundle size - Use c...](/rules/react/react-performance-optimization)[### React Hook Generator Workflow

WorkflowsReactHooksScaffold custom React hooks with standard boilerplate code. Workflow File: .agent/workflows/create\_hook.md ```markdown --- description: Create a new...](/rules/antigravity-workflows/react-hook-generator-workflow)
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


