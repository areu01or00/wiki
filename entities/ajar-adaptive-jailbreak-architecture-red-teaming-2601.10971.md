---
title: "AJAR: Adaptive Jailbreak Architecture for Red-teaming"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [adversarial-ai, jailbreak, red-teaming]
sources: ["https://arxiv.org/abs/2601.10971"]
---

# AJAR: Adaptive Jailbreak Architecture for Red-teaming

## Overview
AJAR exposes multi-turn jailbreak algorithms as callable MCP services and orchestrates them inside a tool-aware runtime built on Petri. The framework integrates Crescendo, ActorAttack, and X-Teaming under a shared service interface. On 200 HarmBench validation behaviors, AJAR improves X-Teaming from 65.0% to 76.0% ASR and reproduces Crescendo more effectively than PyRIT (91.0% vs. 87.5% ASR). AJAR demonstrates that tool access reshapes rather than uniformly enlarges the attack surface — Crescendo drops from 91.0% to 78.0% with tools, while ActorAttack rises from 51.0% to 56.0%.

## Key Facts
- **arXiv**: [2601.10971](https://arxiv.org/abs/2601.10971)
- **Online Date**: 2026-01-16
- **Theme**: adaptive-multi-turn-jailbreak-red-teaming-MCP-agentic

## Key Contributions
-

## Related Papers
- [[risk-under-pressure-compute-aware-evaluation-adversarial-robustness-2606.11409]] — Compute-aware adversarial robustness evaluation from Run 128 Rule 85 sibling
- [[disentangling-adversarial-prompts-semantic-graph-defense-2605.27823]] — Semantic graph prompt disentanglement defense from Run 128 Rule 85 sibling
- [[cross-generational-transfer-adversarial-attacks-reveals-non-monotonic-safety-2606.00813]] — Non-monotonic cross-generational alignment transfer from Run 128 Rule 85 sibling
