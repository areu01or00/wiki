---
title: "MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agentic-ai, adversarial-ai, red-teaming, prompt-injection, web-agents, security]
sources: ["https://arxiv.org/abs/2602.09222"]
---

# MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks

## Overview
MUZZLE is an automated agentic red-teaming framework that adaptively evaluates the security of web agents against indirect prompt injection attacks. It uses the agent's own trajectory to automatically identify high-salience injection surfaces and iteratively refines context-aware malicious instructions targeting confidentiality, integrity, and availability violations. The framework discovers 44 new attacks across 4 web applications with 10 adversarial objectives, including 3 cross-application prompt injection attacks and an agent-tailored phishing scenario.

## Key Facts
- **Authors**: Georgios Syros, Evan Rose, Brian Grinstead, Christoph Kerschbaumer, William Robertson, Cristina Nita-Rotaru, Alina Oprea
- **Year**: 2026 (submitted Feb 9, 2026; revised Jun 14, 2026)
- **arXiv**: [2602.09222](https://arxiv.org/abs/2602.09222)
- **Subjects**: Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)

## Key Contributions
- **Adaptive attack surface identification**: Uses agent trajectories to automatically identify high-salience injection surfaces, removing the need for manually selected attack surfaces
- **Iterative attack refinement**: Adapts attack strategy based on observed execution trajectory and refines attacks using feedback from failed executions
- **Cross-application prompt injection**: Discovers 3 novel cross-application prompt injection attacks that span multiple web applications
- **Agent-tailored phishing**: Identifies a novel agent-specific phishing scenario not captured by prior evaluation frameworks
- **Multi-LLM evaluation**: Tests across diverse LLMs and agent scaffolds, demonstrating generalizability of the framework

## Related Papers
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — AJAR: Adaptive Jailbreak Architecture for Red-teaming — sibling adaptive attack framework in the wiki; AJAR focuses on jailbreak architecture while MUZZLE focuses on indirect prompt injection in web agents
- [[adaptive-evaluation-out-of-band-defenses-against-prompt-injection-in-llm-agents-2606.26479]] — Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents — concurrent work on evaluating out-of-band prompt injection defenses
- [[what-if-prompt-injection-never-left-exploring-cross-session-stored-prompt-injection-in-agentic-systems-2606.04425]] — Cross-Session Stored Prompt Injection in Agentic Systems — explores persistent prompt injection via stored memory, orthogonal to MUZZLE's web agent attack surface
