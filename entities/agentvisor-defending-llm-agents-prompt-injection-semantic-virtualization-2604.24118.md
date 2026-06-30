---
title: "AgentVisor: Defending LLM Agents Against Prompt Injection via Semantic Virtualization"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agentic-ai, adversarial-ai, defense, prompt-injection, semantic-virtualization, security]
sources: ["https://arxiv.org/abs/2604.24118"]
---

# AgentVisor: Defending LLM Agents Against Prompt Injection via Semantic Virtualization

## Overview
AgentVisor is a defense framework that enforces semantic privilege separation for LLM agents by treating the target agent as an untrusted guest and intercepting tool calls via a trusted semantic visor. Drawing inspiration from operating system virtualization, it introduces a rigorous audit protocol grounded in classic OS security primitives to systematically mitigate both direct and indirect prompt injection attacks. The one-shot self-correction mechanism transforms security violations into constructive feedback, enabling agents to recover from attacks. Experiments show AgentVisor reduces attack success rate to 0.65% while incurring only a 1.45% average decrease in utility.

## Key Facts
- **Authors**: Zonghao Ying, Haozheng Wang, Jiangfan Liu, Quanchen Zou, Aishan Liu, Jian Yang, Yaodong Yang, Xianglong Liu
- **Year**: 2026 (submitted Apr 27, 2026)
- **arXiv**: [2604.24118](https://arxiv.org/abs/2604.24118)
- **Subjects**: Cryptography and Security (cs.CR)

## Key Contributions
- **Semantic privilege separation**: Novel defense framework that treats the LLM agent as an untrusted guest, inspired by OS virtualization security primitives
- **Trusted semantic visor**: Intercepts tool calls through a trusted intermediary that applies OS-inspired audit protocols
- **One-shot self-correction**: Transforms security violations into constructive feedback, enabling autonomous recovery from attacks
- **Dual injection coverage**: Mitigates both direct prompt injection (user input) and indirect prompt injection (external content) attacks
- **Minimal utility loss**: Achieves 0.65% attack success rate with only 1.45% average utility decrease, superior to existing defense methods

## Related Papers
- [[muzzle-adaptive-agentic-red-teaming-web-agents-indirect-prompt-injection-attacks-2602.09222]] — MUZZLE: Adaptive Agentic Red-Teaming Against Indirect Prompt Injection — sibling paper; MUZZLE is the attacker's perspective (red-teaming), AgentVisor is the defender's perspective (semantic virtualization)
- [[the-defense-trilemma-why-prompt-injection-defense-wrappers-fail-2604.06436]] — The Defense Trilemma: Why Prompt Injection Defense Wrappers Fail — prior art on why wrapper-based defenses are insufficient; AgentVisor addresses this by moving beyond wrapper approaches to semantic isolation
- [[defending-against-adaptive-prompt-injection-attacks-via-reasoning-enabled-task-alignment-2606.15441]] — Reasoning-Enabled Task Alignment Defense — another defense approach using reasoning-enabled alignment; AgentVisor uses OS virtualization metaphor instead
