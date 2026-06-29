---
title: "MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, test-time-compute, efficiency, stopping-rule, llm]
sources: ["https://arxiv.org/abs/2606.12935"]
---

# MARS: Margin-Adversarial Risk-controlled Stopping for Parallel LLM Test-time Scaling

## Overview
MARS addresses the computational overhead of parallel test-time scaling (sampling many reasoning traces and majority-voting) by introducing a margin-adversarial stopping rule. The key insight is that probing partial traces at intermediate checkpoints reveals an evolving aggregate vote without disrupting generation. MARS estimates which active traces are likely to change their answers and stops once the leader remains safe under a conservative bound on future vote movement. Saves 25-47% of self-consistency tokens while matching full-budget accuracy.

## Key Facts
- **Authors**: Wenbo Chen, Puheng Li, Mengyang Liu, Weijie Su, Tianpei Xie
- **Year**: 2026
- **arXiv**: [2606.12935](https://arxiv.org/abs/2606.12935)
- **Submitted**: 11 June 2026
- **Subjects**: Artificial Intelligence (cs.AI)

## Key Contributions
- Margin-adversarial stopping rule: estimates trace-level switch probabilities + adversarial bound on vote movement
- Phase-based approach: separates uncertainty sources (trace-level switch probability vs adversarial bound on where switching traces land)
- Saves 25-47% of self-consistency tokens, 14-29% on top of DeepConf Online (already filters/truncates weak traces)
- Guarantees with high probability that early-stopped answer matches full-budget vote
- Five-feature logistic model closely matches oracle switching behavior

## Related Papers
- [[grace-granularity-regulated-adaptive-computational-efficiency-for-optimal-verification-in-test-time-scaling-2606.19354]] — GRACE (this run pick; MARS provides the compute-optimal stopping criterion that GRACE's theory predicts — both address the "how much compute is enough" question from different angles)
- [[thinkbooster-a-unified-framework-for-seamless-test-time-scaling-2606.06915]] — ThinkBooster unified test-time scaling (sibling test-time compute paper; MARS's adaptive stopping is a practical complement to ThinkBooster's broader scaling framework)
- [[when-more-thinking-hurts-overthinking-in-llm-test-time-compute-2604.10739]] — Overthinking paper (Run 113 cross-reference; MARS's stopping rule directly addresses the overthinking/diminishing-returns problem identified in the overthinking literature)
