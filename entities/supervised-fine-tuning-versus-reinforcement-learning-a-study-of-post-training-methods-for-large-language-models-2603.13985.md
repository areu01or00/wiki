---
title: "Supervised Fine-Tuning versus Reinforcement Learning: A Study of Post-Training Methods for Large Language Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [post-training, sft, reinforcement-learning, instruction-tuning, llm, survey]
sources: ["https://arxiv.org/abs/2603.13985"]
authors: ["Jiang, Haitao", "and others"]
arxiv_id: "2603.13985"
---

# Supervised Fine-Tuning versus Reinforcement Learning: A Study of Post-Training Methods for Large Language Models

## Overview
A unified empirical-theoretical study of **SFT vs RL post-training for LLMs** that argues the two paradigms are not opposing choices but **complementary stages of a single optimization trajectory**. The study introduces a taxonomy mapping each post-training method (SFT, DPO, PPO, GRPO, KTO, ORPO) to a unified objective family and identifies the specific failure modes that determine when one should be preferred over the other.

## Key Facts
- **Authors**: Haitao Jiang and others
- **Year**: 2026
- **arXiv**: [2603.13985](https://arxiv.org/abs/2603.13985) (2026-03-14)
- **Type**: Empirical + theoretical study (cs.CL + cs.LG)

## Key Contributions
- **Unified objective family**: shows that SFT, DPO, PPO, GRPO, KTO, and ORPO can all be written as variants of a single regularized policy-optimization objective, differing only in the choice of reference policy, advantage estimator, and KL constraint. This collapses 6 seemingly-distinct methods into a single design space with 3 continuous knobs.
- **Identifies the "post-training stage" principle**: SFT establishes the *capability* (the model can produce correct outputs when shown examples), RL shapes the *distribution* (the model preferentially produces correct outputs under its own sampling). Skipping SFT and going directly to RL fails on hard reasoning; doing only SFT without RL leaves the model with imitation bias and poor self-correction.
- **Empirical scaling study**: across 7 base models (1B-70B parameters) and 5 task families (math, code, instruction-following, multi-turn dialogue, tool use), the optimal SFT-then-RL ratio shifts predictably with model size — larger models benefit from more RL relative to SFT, smaller models need a longer SFT warm-up before RL is stable.
- **Diagnoses mode-collapse pathologies**: identifies the specific failure mode where PPO with a learned reward model produces reward-hacking on a fixed instruction distribution; shows that a curriculum that re-samples instructions from the *current* model policy (on-policy RL) avoids this collapse.
- **Practical recipe**: provides a 4-step post-training recipe (warm-up SFT → preference SFT → on-policy RL with reference policy anchor → self-distillation) that the authors validate on 5 benchmarks with consistent 3-8 point improvements over single-stage baselines.

## Related Papers
- [[efficientrollout-system-aware-self-speculative-decoding-for-rl-rollouts-2606.18967]] — Sibling discovery from Run 59 on system-aware speculative decoding for the RL rollouts this study's on-policy RL stage depends on
- [[discretizing-reward-models-2606.21795]] — Sibling discovery from Run 59 on reward-model oversensitivity, the failure mode the unified-objective analysis attributes to a specific reward-estimator choice
- [[reasoning-models-struggle-to-control-their-chains-of-thought-2603.05706]] — Sibling discovery from Run 61 on CoT-vs-output controllability asymmetry, an emergent phenomenon the post-training stage analysis partially explains
- [[when-errors-become-narratives-a-longitudinal-taxonomy-of-silent-failures-in-a-production-llm-agent-runtime-2606.14589]] — Sibling discovery from Run 57 on silent-failure modes in production LLM agents, illustrating why the "capability vs distribution" distinction matters in deployment
