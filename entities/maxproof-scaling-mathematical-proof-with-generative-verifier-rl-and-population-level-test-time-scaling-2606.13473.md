---
title: "MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [math, llm, test-time-scaling, verifier, training-rl]
sources: ["https://arxiv.org/abs/2606.13473"]
---

# MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling

## Overview
Population-level test-time scaling framework for competition-level mathematical proof that trains three proof-oriented capabilities (proof generation, proof verification, critique-conditioned proof repair) using a defense-in-depth generative verifier engineered for low false-positive rate. At test time, the model acts as generator + verifier + refiner + ranker, searches over a population of candidate proofs, and returns one final proof through tournament selection.

## Key Facts
- **Authors**: Chen, Jiacheng; Zhang, Xinyu; Zhang, Shunkai; Wang, Yanmohan; Li, Lin; Qin, Tiancheng; Wang, Qin; Zhu, Zhengmao; Li, Tianle
- **Year**: 2026
- **arXiv**: [2606.13473](https://arxiv.org/abs/2606.13473)
- **Citation date**: 2026-06-11

## Key Contributions
- Unifies three proof capabilities (generation + verification + critique-conditioned repair) into a single model trained with defense-in-depth generative-verifier RL
- Population-level test-time scaling that uses the model in four roles simultaneously (generator / verifier / refiner / ranker)
- Tournament selection over candidate proofs as the test-time aggregation primitive
- Establishes generative-verifier-as-RL-signal as a load-bearing primitive for mathematical-proof scaling
- Bridges training-time RL and test-time population scaling via shared verifier architecture (vs. separate verifier models)

## Related Papers
- [[off-the-shelf-llms-as-process-scorers-training-free-prm-alternative-chunk-level-guided-generation-2606.01682]] — training-free PRM alternative; sibling primitive showing off-the-shelf LLM as scorer without reward-model training
- [[measuring-epistemic-resilience-of-llms-under-misleading-medical-context-2606.12291]] — epistemic robustness under misleading context; sibling primitive from Run 72 with orthogonal adversarial surface
- [[a-survey-of-on-policy-distillation-for-large-language-models-2604.00626]] — first OPD survey in the wiki; sibling primitive establishing on-policy distillation as capability-transfer primitive
