---
title: "Attribution-Guided Continual Learning for Large Language Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [continual-learning, catastrophic-forgetting, llm-finetuning, parameter-importance, gradient-modulation]
sources: ["https://arxiv.org/abs/2605.05285"]
---

# Attribution-Guided Continual Learning for Large Language Models

## Overview
Large language models (LLMs) suffer from catastrophic forgetting in continual learning: after learning new tasks sequentially, performance on earlier tasks degrades. Existing remedies — data replay, parameter freezing, and regularization — lack semantic awareness of internal knowledge distribution in LLMs and cannot distinguish parameters that should be preserved from those that should adapt. Liu, Wan, Xu, Zhang, Xie, and Xiong propose an attribution-guided continual fine-tuning framework that estimates task-specific, element-wise parameter importance per Transformer layer and modulates gradients so that parameters important to prior tasks receive smaller updates while less relevant parameters remain plastic for new tasks.

## Key Facts
- **Authors**: Liu, Yazheng; Wan, Yuxuan; Xu, Rui; Zhang, Xi; Xie, Sihong; Xiong, Hui
- **Year**: 2026
- **arXiv**: [2605.05285](https://arxiv.org/abs/2605.05285)
- **Category**: cs.CL, cs.LG
- **Date**: 2026-05-06

## Key Contributions
- Identifies the structural *semantic-blindness* failure mode of existing continual-learning remedies for LLMs: data replay, parameter freezing, and regularization lack semantic awareness of internal knowledge distribution and cannot distinguish parameters that should be preserved from those that should adapt to new tasks.
- Proposes an *attribution-guided continual fine-tuning framework* that estimates task-specific, element-wise parameter importance in each Transformer layer and uses these importance scores to *modulate gradients* during training.
- Surfaces *gradient-modulation-by-importance* as the load-bearing mechanism: parameters important to previous tasks receive smaller updates (preservation), while parameters less relevant to prior tasks remain plastic (adaptation).
- Demonstrates that the method consistently outperforms baselines on continual learning benchmarks, achieving better retention of old tasks while maintaining competitive performance on new tasks.
- Provides a unifying view: existing continual-learning methods (replay, freezing, regularization) are special cases of gradient modulation where importance is estimated coarsely (entire-parameter or uniform), and attribution-guided modulation generalizes them with finer-grained, task-specific, element-wise importance scores.

## Related Papers
- [[distill-once-adapt-life-long-dataset-distillation-continual-2606.20196]] — Sibling continual-test-time-adaptation work — Distill-Once-Adapt-Life-Long uses *dataset distillation* to produce stable source anchors for continual test-time adaptation, Attribution-Guided uses *element-wise parameter importance* for continual fine-tuning — together they bracket the continual-learning surface between *source-anchor-based continual adaptation* (Distill-Once-Adapt-Life-Long) and *importance-modulated continual fine-tuning* (Attribution-Guided))
- [[emergent-concepts]] (parent wiki page) entries on this page by surfacing *gradient-modulation-by-element-wise-parameter-importance* as the structurally correct primitive for LLM continual learning where the failure mode of *semantic-blindness-in-replay-freezing-regularization* is structurally invisible to uniform-coefficient continual learning methods but becomes tractable when per-layer, per-element parameter importance is estimated via attribution and used to modulate gradients during fine-tuning — bridging replay, freezing, and regularization as special cases of finer-grained gradient modulation.