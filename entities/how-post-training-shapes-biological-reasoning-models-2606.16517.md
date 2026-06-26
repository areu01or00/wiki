---
title: "How Post-Training Shapes Biological Reasoning Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [biology, reasoning, post-training, llm, domain-specialization]
sources: ["https://arxiv.org/abs/2606.16517"]
---

# How Post-Training Shapes Biological Reasoning Models

## Overview
This paper presents a controlled study of how each post-training stage reshapes generalization in scientific reasoning models for biology, training and evaluating more than 100 biological reasoning models across genomics, transcriptomics, and proteins with controlled variation in backbone, continued pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL). The central finding is that biological reasoning does not improve monotonically with additional supervision or compute — each stage reshapes generalization in a distinct way, with SFT consistently increasing ID performance but causing OOD performance to peak early and decline, and RL, when applied to strong SFT checkpoints with aligned rewards, improving OOD performance and partially recovering generalization. The strongest ID-OOD trade-off comes from brief SFT, larger RL allocations, and asymmetric adaptation capacity across stages.

## Key Facts
- **Authors**: Fesser, Lukas; Zhang, Hanlin; Li, Michelle M.; Wang, Eric; Perozzi, Bryan; Azizi, Shekoofeh; Kakade, Sham M.; Zitnik, Marinka
- **Year**: 2026
- **arXiv**: [2606.16517](https://arxiv.org/abs/2606.16517)

## Key Contributions
- Provides a controlled empirical study of 100+ biological reasoning models across genomics, transcriptomics, and proteins with systematic variation in backbone, CPT, SFT, and RL, measuring both in-domain (ID) and out-of-domain (OOD) performance.
- Demonstrates that each post-training stage reshapes generalization distinctly rather than contributing uniform gains: CPT improves downstream performance by aligning models with biological language; SFT consistently increases ID performance but causes OOD performance to peak early and decline as models fit the training distribution; RL, when applied to strong SFT checkpoints with aligned rewards, improves OOD performance and partially recovers generalization.
- Shows that biological reasoning does not improve monotonically with additional supervision or compute — performance depends on how training stages are composed.
- Derives a practical post-training budget allocation rule: under fixed compute, the strongest ID-OOD trade-off comes from brief SFT, larger RL allocations, and asymmetric adaptation capacity across stages.

## Related Papers
- [[emergent-concepts]] — Parent emergent-concept run that surfaced this paper