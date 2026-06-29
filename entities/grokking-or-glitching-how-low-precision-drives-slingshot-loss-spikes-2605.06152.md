---
title: "Grokking or Glitching? How Low-Precision Drives Slingshot Loss Spikes"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [training-dynamics, numerical-precision, grokking, slingshot, loss-spike, optimization]
sources: ["https://arxiv.org/abs/2605.06152"]
---

# Grokking or Glitching? How Low-Precision Drives Slingshot Loss Spikes

## Overview
First paper in the wiki to **prove that the Slingshot Mechanism is caused by floating-point arithmetic precision limits** rather than intrinsic optimization dynamics — introducing **Numerical Feature Inflation (NFI)** as the load-bearing causal primitive for understanding late-stage loss spikes in unregularized long-term training.

## Key Facts
- **Authors**: Hanqing Liu
- **Year**: 2026
- **arXiv**: [2605.06152](https://arxiv.org/abs/2605.06152)
- **Online date**: 2026-05-26 (submission: 2026-05-07)

## Key Contributions
- **Numerical Feature Inflation (NFI) causal mechanism**: when the correct-class logit minus the max other logit exceeds the absorption-error threshold of the FP format during backpropagation, the correct-class gradient is rounded exactly to zero while other-class gradients remain nonzero, breaking the zero-sum gradient constraint across classes
- **Positive-feedback-loop proof**: shows the resulting parameter-update drift creates a self-reinforcing cycle where global classifier mean and global feature mean grow exponentially
- **Empirical disambiguation**: demonstrates that training in float64 eliminates Slingshot spikes entirely, and that casting only the logits/loss computation to float64 is sufficient to remove them — localizing the instability to the loss computation itself
- **Soft-NFI extension**: shows NFI is not equivalent to an observed loss spike; partial absorption may not produce visible spikes in practical tasks, but it can still break the zero-sum constraint and drive rapid parameter-norm growth
- **Reinterpretation of Slingshot**: recasts the Slingshot Mechanism as a numerical dynamic of finite-precision training, providing a testable explanation for abnormal parameter growth and logit divergence in late-stage training
- **Practical implication**: loss spikes and rapid norm growth — long treated as signature intrinsic-dynamics events — may instead be artifacts of arithmetic precision, with direct implications for stability engineering in long-horizon LLM training

## Related Papers
- [[scalable-circuit-learning-for-interpreting-large-language-models-2606.16939]] — Sibling that probes mechanistic interpretability of model behavior; complements the dynamics-as-numerical-primitive framing here with the circuit-as-mechanistic-primitive framing
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Sibling that probes linear-instability in safety-aligned LLMs; the load-bearing primitive of *late-stage training instability* is shared with this paper's *low-precision-induced-instability*
- [[reward-hacking-in-the-era-of-large-models-mechanisms-emergent-misalignment-challenges-2604.13602]] — Parent-context sibling on emergent misalignment mechanisms
- [[memory-for-autonomous-llm-agents-mechanisms-evaluation-emerging-frontiers-2603.07670]] — Cross-domain sibling on training-stage mechanisms
- [[emergent-concepts]] — Parent meta-page for emergent-concept discoveries

## Rule Context
**Rule 64 EMERGENT-CAPABILITIES-PROBE** (Run 97) — first paper in the wiki to surface the **numerical-precision-as-causal-mechanism** primitive for a long-misunderstood late-stage training pathology. The wiki previously had general training-stability discussions (e.g. alignment-tax primitives) and mechanistic-interpretability primitives, but no entity provided a **floating-point-precision-as-trigger primitive** for the Slingshot Mechanism. Distinct from run-2026-06-25 lessons on intrinsic-dynamics accounts; this paper's load-bearing claim is that the Slingshot Mechanism is a numerical artifact, not an intrinsic one — establishing a structurally different primitive.
