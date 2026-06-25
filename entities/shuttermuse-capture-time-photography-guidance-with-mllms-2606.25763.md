---
title: "ShutterMuse: Capture-Time Photography Guidance with MLLMs"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [mllm, photography, capture-time-guidance, benchmark, post-hoc-crop, subject-pose, interactive-assistant]
sources: ["https://arxiv.org/abs/2606.25763"]
---

# ShutterMuse: Capture-Time Photography Guidance with MLLMs

## Overview
Real-world photography needs capture-time guidance for both camera framing and subject pose — yet existing aesthetic-cropping benchmarks evaluate only post-hoc crop prediction (the photographer asks "what should this frame look like" after the shot) and ignore subject-side pose recommendations (asking the subject "how should you pose given this scene"), leaving the capture-time guidance capabilities of multimodal LLMs underexplored. ShutterMuse introduces CaptureGuide-Bench, a two-task benchmark covering photographer-side composition decision and refinement *plus* subject-side scene-conditioned pose recommendation, and surfaces a structural capability gap: general-purpose MLLMs make composition decisions but lack precise refinement localization, specialized aesthetic-cropping models localize crops but only do refinement, and neither provides actionable pose guidance. The authors train ShutterMuse on CaptureGuide-Dataset (130K samples with textual rationales and structured visual annotations) via supervised + reinforcement fine-tuning, achieving the best overall photographer-side performance among evaluated baselines and competitive subject-side pose recommendation at substantially lower inference cost.

## Key Facts
- **Authors**: Li, Jiayu; Fang, Yixiao; Hu, Tianyu; Cheng, Wei; Huang, Ping; Fan, Zheheng; Yu, Gang; Ma, Xingjun
- **Year**: 2026
- **arXiv**: [2606.25763](https://arxiv.org/abs/2606.25763)
- **Date**: 2026/06/24
- **Dataset size**: 130K samples (CaptureGuide-Dataset)
- **Benchmark**: CaptureGuide-Bench (photographer-side composition + subject-side pose recommendation)

## Key Contributions
- **CaptureGuide-Bench — two-axis capture-time guidance benchmark** — explicitly splits the guidance problem into (a) photographer-side composition decision and refinement, and (b) subject-side scene-conditioned pose recommendation, surfacing the subject-side axis that prior post-hoc benchmarks leave under-evaluated as a structurally distinct capability rather than a secondary concern.
- **Structural capability-gap diagnosis** — the empirical finding that *general-purpose MLLMs* make composition decisions but lack precise refinement localization, while *specialized aesthetic-cropping models* localize crops but only do refinement, demonstrates that composition decision and crop localization are *dissociable capabilities* — a finding that reshapes MLLM evaluation for vision-language deployment in creative/professional contexts.
- **CaptureGuide-Dataset with textual rationales + structured visual annotations** — the 130K-sample training set provides both the visual grounding (annotations) and the explanatory substrate (rationales) needed for the MLLM to internalize *why* a crop or pose is recommended, supporting reinforcement fine-tuning with grounded reward signals rather than blind preference learning.
- **ShutterMuse unified MLLM (SFT + RFT training)** — trained to handle both photographer-side and subject-side tasks with one model, achieving best photographer-side performance and competitive subject-side accuracy at substantially lower inference cost than task-specialized pipelines.
- **Methodological lens: post-hoc → capture-time guidance** — reorients the MLLM-as-assistant framing from retrospective critique (the canonical aesthetic-cropping setup) to prospective guidance (decisions and pose recommendations during the photo session), validating MLLMs as interactive assistants for live creative workflows.

## Related Papers
- [[emergent-concepts]] — Parent thematic cluster for emergent-concept discoveries in this wiki
- [[iv-cot-implicit-visual-chain-of-thought-structure-aware-text-to-image-2606.24849]] — IV-CoT decomposes T2I conditioning into structural-to-semantic cascade; ShutterMuse decomposes photography guidance into composition-vs-localization and photographer-vs-subject, sharing the multi-axis-decomposition discipline
- [[are-text-to-image-models-inductivist-turkeys-counterfactual-benchmark-causal-2606.24548]] — Counterfactual T2I evaluation (CF-World) for causal-reasoning diagnosis; ShutterMuse's CaptureGuide-Bench applies the same eval-as-discipline principle to photography guidance
- [[diffusionbench-holistic-evaluation-diffusion-transformers-2606.24888]] — DiffusionBench extends multi-axis-diagnostic evaluation to DiT surface; ShutterMuse applies the same discipline to creative-assistant MLLM evaluation (composition × localization × pose)