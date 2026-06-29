---
title: "JailbreakOPT: Tool-Assisted Iterative Jailbreak Prompt Optimization"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [adversarial-attack, jailbreak, tool-augmented-attack, llm-security]
sources: ["https://arxiv.org/abs/2606.11425"]
---

# JailbreakOPT: Tool-Assisted Iterative Jailbreak Prompt Optimization

## Overview
JailbreakOPT organizes diverse atomic jailbreak prompts into an attack taxonomy and uses tool-assisted framework for improving iterative single-turn jailbreak prompt optimization. It resolves the trade-off between static hand-crafted prompts (expressive but inflexible) and prior iterative methods (adaptive but requiring many target queries). The framework significantly improves attack success rate while reducing query complexity.

## Key Facts
- **Authors**: Shi, Ge
- **Year**: 2026
- **arXiv**: [2606.11425](https://arxiv.org/abs/2606.11425)
- **Discovered**: 2026-06-29

## Key Contributions
- Tool-assisted framework organizing atomic jailbreak prompts into a structured attack taxonomy
- Iterative prompt optimization that adapts to target model defenses without exhaustive querying
- Significantly higher jailbreak success rate than prior single-turn methods with fewer target queries
- Bridges the gap between static hand-crafted jailbreaks and fully stochastic optimization approaches

## Related Papers
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — AJAR: adaptive jailbreak via MCP service interfaces; JailbreakOPT differs by organizing prompts into a taxonomy rather than using external tool-service interfaces
- [[agentic-adversarial-rewriting-exposes-nlp-pipeline-vulnerabilities-2604.23483]] — Agentic Adversarial Rewriting: black-box constraint perturbation pipeline; JailbreakOPT differs by focusing on prompt optimization rather than constraint rewriting
- [[metis-learning-to-jailbreak-llms-via-self-evolving-metacognitive-policy-optimization-2605.10067]] — Metis: POMDP-based metacognitive jailbreaking; JailbreakOPT differs by using tool-organized prompt taxonomy rather than self-evolving policy optimization
