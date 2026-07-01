---
title: "Calibrating Overconfidence Without Sacrificing Confidence: Probe-Conditioned Head Intervention for LLMs"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [calibration, uncertainty, llm-safety]
sources: ["https://arxiv.org/abs/2606.09876"]
---

# Calibrating Overconfidence Without Sacrificing Confidence: Probe-Conditioned Head Intervention for LLMs

## Overview
Standard LLM calibration remedies act globally or at the score level, reducing unwarranted confidence but also eroding warranted confidence on correct answers. This paper introduces Probe-Conditioned Head Intervention (PCHI) — a targeted, layer-specific approach that surgically corrects overconfidence in specific attention heads identified by probing, without broad confidence erosion on correct outputs.

## Key Facts
- **Authors**: Li, Ke; Zhang, Chongzhe; Zeng, Zifan + 3
- **Year**: 2026
- **arXiv**: [2606.09876](https://arxiv.org/abs/2606.09876)

## Key Contributions
- Proposes probe-conditioned head intervention — identifies overconfident attention heads via probing, applies targeted intervention only to those heads
- Demonstrates that global calibration (temperature scaling, Platt scaling) erodes warranted confidence on correct answers while removing overconfidence
- PCHI achieves better calibration-accuracy tradeoff: removes overconfidence on wrong answers while preserving confidence on correct answers
- Provides layer-wise analysis showing overconfidence is not uniformly distributed across Transformer layers

## Related Papers
- [[just-how-sure-are-you-improving-verbalized-uncertainty-calibration-in-llms-2606.27023]] — Verbalized uncertainty calibration (orthogonal approach: explicit verbalization vs. internal probing)
- [[calibrating-the-evaluator-does-probability-calibration-mitigate-preference-coupling-in-llm-agent-feedback-loops-2606.31371]] — Preference coupling in agent feedback loops (structural companion: calibration in agentic RL loops)
- [[from-reasoning-traces-to-reusable-modules-understanding-compositional-generalization-in-language-model-reasoning-2606.18089]] — Compositional generalization mechanisms in LM reasoning (separate primitive class: reasoning decomposition vs. confidence targeting)
