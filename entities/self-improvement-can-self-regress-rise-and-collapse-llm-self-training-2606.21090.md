---
title: "Self-Improvement Can Self-Regress: The Rise-and-Collapse Failure Mode of LLM Self-Training"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [self-improvement, reinforcement-learning, failure-mode, post-training, agent]
sources: ["https://arxiv.org/abs/2606.21090"]
---

# Self-Improvement Can Self-Regress: The Rise-and-Collapse Failure Mode of LLM Self-Training

## Overview
This paper identifies a fundamental failure mode in LLM self-training: models that improve via REINFORCE post-training on code tasks first rise in capability and then collapse — sometimes to near-zero performance — within the same training campaign. The collapse is not cross-task catastrophic forgetting but within-task policy over-optimization on a fixed distribution. KL- and EWC-style constraints do not prevent it. The paper compares three control-loop interventions (CARE, ES, GRPO) and finds the answer is regime-dependent: on smaller models (Qwen-2.5-3B), CARE nearly doubles end-of-chain pass@1; on larger models (Qwen-2.5-7B), ES reaches 22.2%.

## Key Facts
- **Authors**: Jianzhe Lin et al.
- **Year**: 2026
- **arXiv**: [2606.21090](https://arxiv.org/abs/2606.21090)

## Key Contributions
- First identification of the rise-and-collapse failure mode in LLM self-training: pass@1 peaks within tens of gradient steps then falls back to near zero
- Controlled multi-seed testbed on Qwen-2.5-3B and Qwen-2.5-7B trained on competitive-programming tasks across 10 sequential 20-step campaigns
- CARE: between-campaign memory with capability posterior, transfer gate, and regression-aware belief revision
- ES: within-campaign early-stop rule rolling forward the peak checkpoint
- GRPO (group-relative reward normalization) raises the floor but does not remove the cliff
- Gemma-3-4B pilot shows the same signature, suggesting the phenomenon is not limited to Qwen

## Related Papers
- [[knowing-acting-probe-kapro-benchmarking-self-awareness-capability-of-llm-agents-2606.20661]] — KAPRO benchmark probes cognitive-behavioral alignment in LLM agents; Self-Improvement Self-Regress identifies a metacognitive failure mode where self-training collapses without self-awareness of the collapse trajectory
