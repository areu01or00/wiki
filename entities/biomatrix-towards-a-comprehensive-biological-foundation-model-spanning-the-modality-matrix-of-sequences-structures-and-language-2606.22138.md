---
title: "BioMatrix: Towards a Comprehensive Biological Foundation Model Spanning the Modality Matrix of Sequences, Structures, and Language"
created: 2026-06-20
updated: 2026-06-20
type: entity
tags: [foundation-models, biology, multimodal, protein, molecule, cross-domain]
sources: ["https://arxiv.org/abs/2606.22138"]
---

# BioMatrix: Towards a Comprehensive Biological Foundation Model Spanning the Modality Matrix of Sequences, Structures, and Language

## Overview
We present BioMatrix, the first multimodal foundation model that natively integrates sequences, structures, and natural language for both molecules and proteins within a single decoder-only architecture. Existing biological foundation models pursue native multimodality and broad entity coverage separately: those that fuse multiple modalities under a shared objective remain confined to a single entity type, while those spanning multiple entity types either omit explicit structural modeling or rely on adapter-based designs in which the model cannot natively generate the very modalities it can read. BioMatrix closes this gap by mapping molecular sequences (supporting both SMILES and SELFIES notations), molecular structures, protein sequences, protein structures, and natural language into a.

## Key Facts
- **Authors**: Pei, Qizhi, Zhou, Zhimeng, Duan, Yi, et al.
- **Year**: 2026
- **Date**: 2026-06-20
- **arXiv**: [2606.22138](https://arxiv.org/abs/2606.22138)
- **Subjects**: Computation and Language (cs.CL)

## Key Contributions
- BioMatrix: the first decoder-only multimodal foundation model that natively integrates sequences, structures, and natural language for both molecules and proteins in a single architecture
- Unifies two previously disjoint biological-FM directions — native multimodality under a shared objective, and broad entity coverage — into one model
- Closes the structural-modeling gap in prior multi-entity biological FMs, which either omitted explicit structural modeling or relied on implicit representations
- Provides a single pre-trained substrate that can be fine-tuned for both molecule- and protein-centric downstream tasks across sequence, structure, and language modalities

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
