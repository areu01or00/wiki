---
title: "Physics Question Scene Graph: Fine-grained Evaluation of Physical Plausibility in Text-to-Video Generation"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [text-to-video, evaluation, physical-plausibility, benchmark, scene-graph, multimodal-evaluation]
sources: ["https://arxiv.org/abs/2606.25306"]
---

# Physics Question Scene Graph: Fine-grained Evaluation of Physical Plausibility in Text-to-Video Generation

## Overview
Pothiraj, Cho, Zhang, Stengel-Eskin, and Bansal address a structural evaluation gap in text-to-video (T2V) generation — where current models produce realistic-looking videos that nonetheless violate basic physical laws, and where existing evaluation methods cannot localize or specify *which* physical-law violation is occurring — and introduce Physics Question Scene Graph (PQSG), a hierarchical question-based evaluation pipeline that decomposes T2V physical-plausibility assessment into objects, actions, and physics-law-adherence sub-questions organized as a graph with logical dependencies between queries, validated against FinePhyEval (a dataset of human-annotated videos from Sora 2, Veo 3, and Wan 2.1) where PQSG achieves higher correlation with human judgment than prior work and ranks closed-source models above Wan 2.1 on physical realism.

## Key Facts
- **Authors**: Pothiraj, Atin; Cho, Jaemin; Zhang, Yue; Stengel-Eskin, Elias; Bansal, Mohit
- **Year**: 2026
- **arXiv**: [2606.25306](https://arxiv.org/abs/2606.25306)
- **Date**: 2026-06-24

## Key Contributions
- Diagnoses a structural evaluation gap in T2V: video generation models produce realistic-looking outputs that nonetheless violate basic physical laws, and the lack of granular evaluation methods means violations cannot be localized or specified — the field can produce visually plausible videos without knowing whether they are *physically* plausible.
- Introduces Physics Question Scene Graph (PQSG), a hierarchical question-based evaluation pipeline that decomposes T2V physical-plausibility assessment into objects, actions, and physics-law-adherence sub-questions, organized as a graph with logical dependencies between queries so that each question is contextually valid only after its prerequisite questions are satisfied.
- Validates PQSG against FinePhyEval, a dataset of physics-based prompts with corresponding videos from Sora 2, Veo 3, and Wan 2.1, each annotated across multiple categories by humans, and shows PQSG achieves higher correlation with human judgment than prior work while providing granular assessments of *which* qualities of the video violate physical plausibility constraints.
- Surfaces a methodology-level contribution to multimodal evaluation: scene-graph-structured question hierarchies with logical dependencies are a structurally stronger diagnostic of physical-law adherence than flat question lists, because flat questions can ask physics questions about objects that have not yet been verified to exist in the video — scene graphs enforce the dependency structure that mirrors the dependency structure of the underlying physical reasoning.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[diffusionbench-holistic-evaluation-diffusion-transformers-2606.24888]] — Sibling T2I / DiT evaluation-discipline work; both papers argue the canonical T2I / T2V evaluation surface (FID, CLIPScore, prompt-alignment) under-probes the underlying generative-modeling capability — DiffusionBench argues for multi-axis cost-scaled T2I eval, PQSG argues for graph-structured question-based physical-plausibility eval on the T2V surface.
- [[are-text-to-image-models-inductivist-turkeys-counterfactual-benchmark-causal-2606.24548]] — Sibling T2I causal-reasoning evaluation work; both papers probe *physical-world understanding* in generative models — Inductivist-Turkeys does this on the T2I surface via counterfactual prompts (Russell-turkey analogy), PQSG does it on the T2V surface via scene-graph-structured physics questions (objects → actions → physics-law-adherence).
- [[ebench-elemental-diagnosis-of-generalist-mobile-manipulation-policies-2606.18239]] — Sibling multi-axis-diagnostic-benchmark work; both replace single-axis aggregate scores with diagnostic evaluation that isolates *what underlying capability* the system has — EBench on the robotics surface (atomic skill profiles), PQSG on the T2V surface (physical-plausibility per question category).
