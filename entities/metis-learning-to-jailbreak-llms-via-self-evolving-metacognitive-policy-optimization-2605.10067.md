---
title: "Metis: Learning to Jailbreak LLMs via Self-Evolving Metacognitive Policy Optimization"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [safety, red-teaming, adversarial]
sources: ["https://arxiv.org/abs/2605.10067"]
---

# Metis: Learning to Jailbreak LLMs via Self-Evolving Metacognitive Policy Optimization

## Overview
Red teaming for LLM vulnerabilities has scaled via automated methods, but existing approaches rely on static heuristics or stochastic search and remain brittle against advanced safety alignment. Metis reformulates jailbreaking as inference-time policy optimization within an adversarial POMDP, using a self-evolving metacognitive loop that performs causal diagnosis of a target's defense logic and generates targeted jailbreak strategies through structured reflection.

## Key Facts
- **arXiv**: [2605.10067](https://arxiv.org/abs/2605.10067)
- **Date**: 2026/05/11 (submission), 2026/05/21 (online)

## Key Contributions
- **Metacognitive POMDP jailbreaking**: models the jailbreak-target interaction as a Partially Observable Markov Decision Process with the attacker as a meta-cognitive agent that reasons about the target's defense logic
- **Self-evolving causal diagnosis**: the metacognitive loop performs causal diagnosis of defense mechanisms — identifying which safety layers are active, which are exploitable, and which compose to create emergent vulnerabilities
- **Structured reflection**: generates jailbreak strategies through structured self-examination rather than random perturbation, substantially higher success rate than stochastic baselines against strong safety-aligned models
- **Orthogonal to prior Rule 86 axes**: AJAR exploits MCP service interfaces, Agentic Adversarial Rewriting operates under black-box constraints; Metis learns to defeat any defense via metacognitive policy optimization

## Related Papers
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — Rule 86 sibling: adaptive jailbreak via MCP service orchestration
- [[agentic-adversarial-rewriting-exposes-nlp-pipeline-vulnerabilities-2604.23483]] — Rule 86 sibling: black-box two-agent semantic perturbation
- [[jailbreaking-llms-vlms-mechanisms-evaluation-unified-defense-2601.03594]] — Rule 86 sibling: comprehensive jailbreak taxonomy
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Jailbreak detection via entropy dynamics in intermediate layers
