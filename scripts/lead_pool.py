#!/usr/bin/env python3
"""Rotation pool for the hero lead text in src/main/resources/templates/index.html.

Each entry is a self-contained lead paragraph in the voice of the existing copy:
full-stack training with a playful security twist, ranging from straight tech
highlights to outright satire of the industry. The hourly workflow picks a
random entry that differs from the one currently on main and swaps it in.
"""

LEADS = [
    "Master the full stack without becoming a corporate robot. Learn modern web technologies, cloud infrastructure, and AI integration\u2014plus enough security awareness to spot vulnerabilities before the crooks do. (Not that we're encouraging you to think like one. Mostly.)",
    "Build like a pro, ship like a rebel. From React Server Components and edge rendering to WebAssembly and streaming SSR, you'll harness the newest web platform features while learning to harden them against real-world attacks.",
    "Modern web tech moves fast\u2014so do you. Train on HTTP/3, view transitions, container queries, and CSS anchor positioning, then flip to the dark side of the stack to understand the vulnerabilities crooks exploit every day.",
    "Full-stack fluency with a security mindset. Explore AI-assisted development, serverless patterns, and progressive enhancement, and discover how the same browser APIs that delight users can be abused when developers drop their guard.",
    "Learn the web platform from every angle: performance budgets, Core Web Vitals, type-safe end-to-end stacks, and secrets management\u2014because knowing how crooks chain small misconfigurations into breaches is what separates engineers from targets.",
    "The modern stack is your weapon of choice. TypeScript everywhere, React Server Components at the edge, local-first data sync, and AI copilots in your editor\u2014paired with the offensive insight to see your app the way an attacker would.",
    "One curriculum, every layer. Spec-driven development, HTTP/3 and QUIC, WebGPU rendering, and AI agents wired into CI/CD\u2014plus the security awareness to spot the OWASP Top 10 creeping into your code before anyone else does.",
    "Engineers who understand both sides build the safest apps. Master new web capabilities like declarative shadow DOM and passkeys while studying how crooks weaponize weak secrets, stale dependencies, and over-permissive IAM.",
    "From markup to mega-scale. Practice with modern SSR frameworks, containerized delivery, and Kubernetes on EKS\u2014then stress-test your instincts against injection, SSRF, and supply-chain attacks in the same afternoon.",
    "Where new web tech meets street smarts. Bento grids, WebSockets, streaming responses, and AI-powered search are the fun part; learning how crooks bypass naive rate limits and leak data through APIs is the part they don't teach.",
    "Learn to ship code that survives contact with reality: CI/CD pipelines, observability, infrastructure as code—then watch in horror as a crook waltzes past all of it through the S3 bucket you set to 'public' for a demo in 2023.",
    "It works on your machine? Delightful. Practice containerized delivery, immutable infrastructure, and blue-green deploys—then accept that crooks also have a staging environment, and yours is accidentally exposed to the internet.",
    "Hype-driven development is a crook's favorite framework. Cut through the buzzwords with type-safe APIs, real performance budgets, and dependency audits—because nothing says 'supply-chain attack' like installing a package whose name you can't pronounce.",
    "Move fast and break things—preferably not the customers' things. Train on edge rendering, streaming SSR, and Kubernetes on EKS, with enough security awareness to know that 'admin/admin' remains the most successful credential in history.",
    "Become the engineer your standups think you are. Design event-driven architectures, zero-downtime deploys, and self-healing clusters—plus the humility to know that 'temporary fix' is a lie both crooks and tech leads like to tell.",
    "Let the AI write your code, then read it like a crook would. Modern tooling, AI-assisted development, and ruthless code review—because trusting a machine that hallucinates package names is exactly how supply-chain attacks get their start.",
]
