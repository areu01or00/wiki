---
title: "SCATR: Simple Calibrated Test-Time Ranking"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [test-time-compute, calibration, ranking, llm-reasoning, inference-efficiency]
sources: ["https://arxiv.org/abs/2604.16535"]
---

# SCATR: Simple Calibrated Test-Time Ranking

## Overview
Test-time scaling (TTS) improves LLMs by allocating additional inference compute — typically via generating multiple candidate responses and selecting the best through a Best-of-N (BoN) strategy. The effectiveness of BoN hinges on the scoring function. SCATR introduces a simple calibrated ranking approach that learns to rank multiple candidate responses at test time using calibrated confidence scores, enabling principled uncertainty-aware selection without requiring process-level rewards.

## Key Facts
- **Authors**: Divya Shyamal, Marta Knežević, Lan Tran, Chanakya Ekbote, Vijay Lingam, Paul Pu Liang
- **Year**: 2026
- **arXiv**: [2604.16535](https://arxiv.org/abs/2604.16535)

## Key Contributions
- **Calibrated BoN ranking**: Learnable scoring function for Best-of-N ranking that produces calibrated confidence scores for each candidate response
- **Parallel scaling with calibration**: Handles the standard parallel-scaling TTS paradigm (generating multiple responses simultaneously) with a principled scoring approach
- **Process reward model integration**: Leverages PRM-learned scores but without requiring per-step rewards at inference time
- **First in wiki**: First calibrated test-time ranking framework for LLM reasoning under the parallel-scaling TTS paradigm

## Related Papers
- [[process-supervision-of-confidence-margin-for-calibrated-llm-reasoning-2604.23333]] — Calibrated confidence margin process supervision (orthogonal: per-step margin vs per-candidate ranking)
- [[reward-under-attack-analyzing-the-robustness-and-hackability-of-process-reward-models-2603.06621]] — Robustness analysis of PRMs under adversarial attacks (PRM reliability axis)
- [[evirank-evidence-based-confidence-estimation-for-llm-based-ranking-2606.04727]] — Evidence-based confidence estimation for LLM ranking
