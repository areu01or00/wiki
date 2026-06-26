---
title: "MammoExpert: Benchmarking Chain-of-Thought Reasoning in Mammography Diagnosis"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [medical-imaging, chain-of-thought, multimodal-reasoning, benchmark, mammography, interpretable-diagnosis]
sources: ["https://arxiv.org/abs/2606.21119"]
---

# MammoExpert: Benchmarking Chain-of-Thought Reasoning in Mammography Diagnosis

## Overview
Addresses the structural *public-mammography-datasets-lack-structured-diagnostic-reasoning-annotations-and-pathological-subtype-coverage* failure mode of medical-imaging AI development where breast cancer detection relies on mammography with millions of examinations conducted annually, but available high-quality public datasets are limited in both scale and annotation richness. Presents the *first* mammography dataset with Chain-of-Thought reasoning annotations across three diagnostic phases (primal observation → factual assessment → diagnostic synthesis), covering 67 WHO-classified histopathology subtypes with 42 radiographic features per exam annotated by nine senior radiologists.

## Key Facts
- **Authors**: Dai, Di; Liu, Bo; Li, Youcheng; Yu, Haojun; Bian, Zhouhang; Wu, Quanlin; Wang, Dong; Meng, Sichen; Xuan, Hongye; Lan, Zijie
- **Year**: 2026
- **arXiv**: [2606.21119](https://arxiv.org/abs/2606.21119) (online: 2026-06-19)

## Key Contributions
- **MammoExpert dataset** — 2,379 mammography images covering 67 WHO-classified histopathology subtypes with 42 radiographic features per exam, annotated by nine senior radiologists
- **Three-phase CoT reasoning schema** — primal observation → factual assessment → diagnostic synthesis (decomposes expert radiologist reasoning into structured stages)
- Empirical demonstration that combining public dataset CBIS-DDSM with MammoExpert yields **7.1% classification accuracy improvement**; training to learn CoT reasoning achieves another **4% gain** on MammoExpert test set
- Cross-dataset generalization — full approach yields **6.9% gain on INBreast** and **6.7% on Vindr**
- Establishes CoT-reasoning-annotated medical-imaging benchmark for interpretable breast lesion diagnosis

## Related Papers
- [[emergent-concepts]] — Parent meta-page that led to this discovery
- [[large-language-model-reasoning-failures-2602.06176]] — Survey distinguishing embodied/non-embodied reasoning modalities with failure-scope axis; MammoExpert is a concrete instance of *application-specific limitations* in the embodied-vision medical-imaging sub-mode, demonstrating that CoT reasoning can recover domain-expert diagnostic structure
- [[reasoning-models-struggle-to-control-their-chains-of-thought-2603.05706]] — CoT controllability study on reasoning models (23× asymmetry between CoT and output controllability); MammoExpert's *learn-to-reason* training paradigm is the complementary primitive that targets faithful CoT generation in domain-expert-annotated settings