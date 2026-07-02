---
title: "Don't Go Breaking My LLM: The Impact of Pruning Attention Layers on Explanation Faithfulness and Confidence Calibration"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [model-compression, pruning, calibration, interpretability]
sources: ["https://arxiv.org/abs/2606.24970"]
---

# Don't Go Breaking My LLM: The Impact of Pruning Attention Layers on Explanation Faithfulness and Confidence Calibration

## Overview
Pruning Large Language Models reduces memory and inference costs by removing parts of the network, producing smaller models that retain most of their accuracy. This paper studies the so-far-neglected impact of attention-layer pruning on two critical properties beyond accuracy: explanation faithfulness (whether the model's post-hoc explanations align with its actual reasoning) and confidence calibration (whether predicted probabilities match empirical accuracy). The authors find that pruning up to 33% of attention layers preserves accuracy but degrades faithfulness and calibration non-linearly — small pruning budgets are safe, but beyond a threshold, both faithfulness and calibration collapse faster than accuracy. The paper provides the first systematic evidence that compression's standard evaluation metric (accuracy) is insufficient for deployment in high-stakes settings where explanations or calibrated uncertainty are required.

## Key Facts
- **Authors**: Tropeano, Pietro; Maistro, Maria; Ruotsalo, Tuukka + 1
- **Year**: 2026
- **arXiv**: [2606.24970](https://arxiv.org/abs/2606.24970)

## Key Contributions
- First systematic study of attention pruning impact on explanation faithfulness and confidence calibration (beyond accuracy)
- Empirical finding that faithfulness and calibration degrade non-linearly with pruning — accuracy is an insufficient proxy for deployment safety
- Identification of a critical pruning threshold (approximately 33% of attention layers) beyond which calibration collapses
- Analysis of the tradeoff between compression efficiency and interpretability/reliability guarantees
- Framework for compression evaluation that includes faithfulness and calibration metrics alongside accuracy

## Related Papers
- [[prune-you-generate-online-rollout-pruning-faster-better-2603.24840]] — Online rollout pruning for faster, better LLM serving (compression context)
- [[calibrating-the-evaluator-does-probability-calibration-mitigate-preference-coupling-in-llm-agent-feedback-loops-2606.31371]] — Calibration of evaluator models in feedback loops (calibration theory)
- [[calibration-collapse-under-sycophancy-fine-tuning-reward-hacking-2604.10585]] — Calibration collapse under sycophancy and fine-tuning (calibration failure mode)
