---
title: "AutoDojo: Adaptive Black-Box Attacks Reveal the Limits of IPI Defenses and Task-Specification Effects in LLM Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [adversarial-attack, indirect-prompt-injection, black-box-attack, llm-agent-security]
sources: ["https://arxiv.org/abs/2606.15057"]
---

# AutoDojo: Adaptive Black-Box Attacks Reveal the Limits of IPI Defenses and Task-Specification Effects in LLM Agents

## Overview
AutoDojo provides a comprehensive empirical evaluation of automated indirect prompt injection (IPI) attacks against LLM agents, systematically categorizing the landscape of IPI defenses (prompt-based, detection-based, and system-level) and revealing fundamental limits of each category. It adapts both white-box (GCG) and black-box (TAP) attack methods to the agentic setting, evaluating across 80 task pairs spanning four domains to establish benchmark boundaries for IPI defense research.

## Key Facts
- **Authors**: Ma, Xinhang
- **Year**: 2026
- **arXiv**: [2606.15057](https://arxiv.org/abs/2606.15057)
- **Discovered**: 2026-06-29

## Key Contributions
- First comprehensive taxonomy of IPI defenses revealing fundamental limits of each category
- Adapts GCG (white-box) and TAP (black-box) attack methods to agentic settings
- Evaluates across 80 task pairs spanning four domains in the AgentDojo framework
- Demonstrates that system-level defenses (control/data isolation) are necessary but not sufficient against sophisticated IPI attacks

## Related Papers
- [[the-defense-trilemma-why-prompt-injection-defense-wrappers-fail-2604.06436]] — Defense Trilemma: structural analysis of why IPI wrapper defenses fail; AutoDojo extends this with empirical evaluation of adaptive attacks revealing specific failure points
- [[what-if-prompt-injection-never-left-exploring-cross-session-stored-prompt-injection-in-agentic-systems-2606.04425]] — Cross-session stored prompt injection: extends IPI persistence across sessions; AutoDojo focuses on same-session adaptive black-box attacks rather than cross-session persistence
- [[jailbreakopt-tool-assisted-iterative-jailbreak-prompt-optimization-2606.11425]] — JailbreakOPT: tool-assisted iterative jailbreak optimization; AutoDojo differs by focusing on indirect prompt injection (vs direct jailbreak) and empirical defense evaluation (vs attack optimization)
