---
title: "Teach-to-Reason: Competition-Guided Reasoning with a Self-Improving Teacher"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, chain-of-thought, distillation, self-improvement, competition, medical-vqa, reinforcement-learning]
sources: ["https://arxiv.org/abs/2606.25407"]
---

# Teach-to-Reason: Competition-Guided Reasoning with a Self-Improving Teacher

## Overview
This paper introduces *Teach-to-Reason* (T2R), a framework that uses comparison-based supervision to improve chain-of-thought (CoT) quality in language models. The key insight is that existing RL-based training relies on answer-level rewards that are too coarse to guide improvement in reasoning quality — the model can learn to produce correct answers without producing good reasoning. T2R introduces a self-improving Teacher that generates reference reasoning chains, and a competition-guided Reasoner that is optimized against progressively stronger Teacher-generated references. The Teacher is iteratively strengthened via self-competition, and the Reasoner is optimized against the improving Teacher.

## Key Facts
- **Authors**: Han, Xiao; Liu, Hao; Bao, Zhimin; Jiao, Jile; Wang, Yue; Guo, Hui; Mou, Xiaofeng; Xu, Yi
- **Year**: 2026
- **arXiv**: [2606.25407](https://arxiv.org/abs/2606.25407)
- **Online date**: 2026/06/24

## Key Contributions
- **Comparison-based CoT supervision**: First framework to use comparison-based supervision (Teacher vs. Reasoner reasoning chains) rather than answer-level rewards for CoT optimization — enabling the model to learn the *structure* of good reasoning, not just correct answers.
- **Self-improving Teacher**: A Teacher model that is iteratively strengthened via self-competition — as the Reasoner improves, the Teacher generates harder reference chains that push the Reasoner further, producing a co-evolutionary improvement dynamic.
- **Competition-guided optimization**: The Reasoner is optimized against Teacher-generated references using a contrastive loss that rewards reasoning chains that are closer to the Teacher's superior reasoning than to the Reasoner's own inferior outputs.
- **CXR VQA application**: Validated on chest X-ray visual question answering where medical reasoning quality (not just answer accuracy) is the primary evaluation target — demonstrating that comparison-based supervision produces more medically grounded reasoning chains than answer-level RL training.

## Related Papers
- [[a-verifiable-search-is-not-a-learnable-chain-of-thought-2606.21884]] — Related reasoning theory: both papers probe the limits of CoT distillation; this paper's competition-guided approach addresses the learnability failure identified in the verifiable search paper by using comparison-based rather than answer-level supervision.
- [[coft-counterfactual-conformal-decoding-fair-chain-of-thought-2605.30641]] — Related CoT fairness: both improve CoT quality through structural interventions; T2R's self-improving Teacher complements CFPO's conformal decoding approach.
