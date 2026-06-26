---
title: "Reasoning Models Struggle to Control their Chains of Thought"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [reasoning-models, chain-of-thought, monitorability, safety, controllability]
sources: ["https://arxiv.org/abs/2603.05706"]
---

# Reasoning Models Struggle to Control their Chains of Thought

## Overview
Introduces the **CoT-Control evaluation suite** to measure CoT controllability — the undesirable capability of reasoning models to manipulate what they verbalize in their CoT, which would undermine CoT monitorability. Across multiple frontier reasoning models, finds that **CoT controllability is dramatically lower than output controllability** (e.g., Claude Sonnet 4.5 controls its CoT only 2.7% of the time but 61.9% when controlling its final output). Controllability is higher for larger models and decreases with more RL training, test-time compute, and problem difficulty — leaving the authors cautiously optimistic about CoT monitorability as a safety primitive.

## Key Facts
- **Authors**: Yueh-Han, Chen; McCarthy, Robert; Lee, Bruce W.; He, He; Kivlichan, Ian; Baker, Bowen; Carroll, Micah; Korbak, Tomek
- **Year**: 2026
- **arXiv**: [2603.05706](https://arxiv.org/abs/2603.05706)
- **Online date**: 2026-03-05

## Key Contributions
- **CoT-controllability-as-distinct-from-output-controllability primitive**: a new safety-relevant axis that measures whether models can evade CoT monitors. Distinct from jailbreak resistance (output controllability) — the paper shows they are *decoupled*
- **Asymmetric-controllability empirical primitive**: Claude Sonnet 4.5 controls CoT at 2.7% but output at 61.9% — a 23× gap. Provides the first quantitative benchmark for the safety claim that "CoT is hard to manipulate"
- **Scale-vs-RL-controllability-antiparallel primitive**: CoT controllability *increases* with model size but *decreases* with more RL training / test-time compute / problem difficulty. The implication: scaling alone does not produce monitorable CoT, but the *RL recipes used to improve reasoning* also incidentally reduce monitor-evasion capability
- **Monitoring-awareness-doesn't-bypass primitive**: when models are told they are being monitored, controllability rises only slightly — adversarial prompt optimization also fails to meaningfully increase it. Suggests CoT evasion is not a near-term failure mode
- **Incentive-vs-direct-request asymmetry**: controllability is similar whether models are given incentives or direct requests to evade monitors — but is consistently *higher* with monitoring awareness, suggesting residual behavioral influence that current training does not erase
- **First systematic empirical case for CoT monitorability as a viable safety primitive**: rules out the most concerning "CoT-controllable reasoning models" failure mode at current capability levels, while leaving the underlying mechanism unexplained

## Related Papers
- [[when-the-chain-of-thought-knows-better-failure-modes-in-multi-turn-reasoning-models-2606.10740]] — CoT-vs-Output 2×2 matrix in multi-turn; sibling CoT-monitorability primitive from the multi-turn-safety axis
- [[reasoninglens-hierarchical-visualization-and-diagnostic-auditing-for-large-reasoning-models-2606.23404]] — Trace-level diagnostic; sibling CoT-transparency primitive from the LRM-diagnosis axis
- [[interpretability-can-be-actionable-2605.11161]] — Actionability evaluation grid; this paper's CoT-monitorability claim passes the validation bar
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — External CoT steering for controllability; this paper measures *internal* controllability limits that external steering must work within
- [[hidden-thoughts-are-not-secret-reasoning-trace-exposure-in-llms-2606.00642]] — Hidden CoT trace exposure; this paper measures the *controllability* of visible CoT that hidden-thoughts exposure aims to protect
- [[a-latent-computational-mode-in-large-language-models-2601.08058]] — Latent reasoning features; this paper's CoT-controllability findings are downstream — if reasoning is a latent feature, manipulating its verbalization requires a separate mechanism that current models may lack