---
title: "PACT: Preserving Anchored Cores in Task-vectors for Model Merging"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [model-merging, task-arithmetic, task-vectors, weight-space, lora, merging, llm]
sources: ["https://arxiv.org/abs/2606.18627"]
---

# PACT: Preserving Anchored Cores in Task-vectors for Model Merging

## Overview
Shi, Ningyuan; Zhou, Zhipeng; Wang, Hao; Miao, Chunyan; Zhao, Peilin (2026) introduce **PACT**, identifying and preserving *Load-Bearing Wall (LBW)* dimensions — task-critical knowledge that remains embedded in the pre-trained weights rather than being fully transferred into task vectors — by characterizing LBW from both scalar-weight and subspace perspectives, aligning task-vector orthogonal complements with the pre-trained-weight subspace, and removing the aligned subspace components before applying existing model-merging algorithms; PACT consistently enhances mainstream task-arithmetic approaches (Ties-Merging, AdaMerging) and establishes new state-of-the-art performance across multiple benchmarks, surfacing *anchored-task-core-preservation-primitive* as the structurally correct primitive for training-free model merging.

## Key Facts
- **Authors**: Shi, Ningyuan; Zhou, Zhipeng; Wang, Hao; Miao, Chunyan; Zhao, Peilin
- **Year**: 2026
- **arXiv**: [2606.18627](https://arxiv.org/abs/2606.18627)
- **Date**: 2026-06-17 (online 2026-06-23)

## Key Contributions
- **Load-Bearing Wall (LBW) dimension identification**: identifies task-critical knowledge that remains embedded in pre-trained weights rather than being fully transferred into task vectors, characterizing LBW from both scalar-weight and subspace perspectives to cover the major paradigms of existing model-merging methods — surfacing *pre-trained-anchor-knowledge-primitive* as the load-bearing diagnostic primitive exposing the structural failure of task-vector-only merging.
- **Task-vector orthogonality alignment with pre-trained subspace**: aligns the orthogonal complements of task vectors with the subspace of the pre-trained weights, then removes the aligned subspace components before applying existing merging algorithms — surfacing *subspace-orthogonal-complement-removal-primitive* as the structurally correct task-vector-cleaning primitive for merging, distinct from interference-aware reweighting (where the load-bearing axis is *anchored-core-preservation-via-subspace-alignment* rather than *task-vector-sign-magnitude-redistribution*), and from sparse-merging primitives (where the load-bearing axis is *pre-trained-weight-residual-knowledge-removal-from-task-vector* rather than *low-magnitude-update-truncation*).
- **Efficient randomized-SVD variant for scalability**: develops a scalable variant using randomized SVD for large models, making PACT deployable on practical architectures — surfacing *randomized-svd-subspace-estimation-primitive* as the load-bearing engineering primitive making anchored-core-preservation practical at frontier-model scale.
- **Seamless integration with existing merging methods**: PACT can be combined with Ties-Merging, AdaMerging, and other mainstream task-arithmetic approaches, consistently enhancing their performance and establishing new state-of-the-art — surfacing *drop-in-task-vector-cleaning-primitive* as the load-bearing *compositionality-primitive* making PACT a general pre-processing step rather than a standalone algorithm.
- **Empirical SOTA across multiple benchmarks**: extensive experiments across vision and language benchmarks demonstrate consistent enhancement over mainstream approaches — surfacing *cross-domain-validity-primitive* as the load-bearing *generalization-primitive* showing that LBW-pre-processing benefits both vision and language merging tasks.

## Related Papers
- [[emergent-concepts]] — Parent wiki page that motivated this discovery
- [[revisiting-parameter-based-knowledge-editing-in-llms-2606.00570]] — Sibling parameter-editing primitive — Revisiting-Parameter-Based-Knowledge-Editing analyzes *what parameter editing can/cannot do*, PACT analyzes *what task-vector merging misses about pre-trained anchors* — together they bracket weight-space intervention from parameter-side knowledge editing to parameter-side model merging
- [[a-theoretical-model-for-task-routing-in-mixture-of-expert-transformers-2606.14398]] — Sibling theoretical-MoE primitive — task-routing-theory provides theoretical support for *localized knowledge circuits*, PACT identifies *anchored knowledge that resists localization* — together they bracket model-internal-knowledge from localized (router-reachable) to anchored (router-resistant) forms
- [[energy-based-fine-tuning-of-language-models-2603.12248]] — Sibling training-free fine-tuning primitive — Energy-Based-Fine-Tuning explores *post-training energy landscapes*, PACT explores *post-training weight-space anchors* — together they bracket training-time-free fine-tuning objectives with weight-space-merge-time correction primitives