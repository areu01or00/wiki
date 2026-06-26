---
title: "Confidence-Aware Tool Orchestration for Robust Video Understanding"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [video-reasoning, evidence-reliability, tool-orchestration, grpo, perception]
sources: ["https://arxiv.org/abs/2606.26904"]
---

# Confidence-Aware Tool Orchestration for Robust Video Understanding

## Overview
He, Choi, Yoon (2026) identify the *Blind Trust Problem* — video reasoning language models implicitly assume every input frame is equally reliable, causing frontier models to suffer 15-30 percentage-point accuracy drops on real-world embodied benchmarks under realistic perturbations (motion blur, glare, occlusion) while remaining unaware their visual evidence has been degraded — and propose Robust-TO, an agentic video understanding framework that explicitly integrates per-frame trustworthiness into every stage of reasoning. Robust-TO organizes heterogeneous visual perception tools under a unified evidence interface where each tool receives a sub-query derived from the original question and a set of trustworthy frames selected by a reliability-relevance score, returning evidence in a shared format (concrete prediction, temporal grounding, calibrated reliability score); the calibrated scores guide a three-tier synthesis process and define a confidence-cost GRPO reward jointly optimizing correctness, evidence reliability, and efficiency. Robust-TO achieves 56.4% average accuracy on clean inputs (surpassing the strongest open-source baseline by 10.6 pp and outperforming Gemini-2.5-Pro at 46.2%) and maintains 54.3% under five corruption types — the smallest clean-to-corrupted drop among compared methods.

## Key Facts
- **Authors**: Yangfan He; Yujin Choi; Jaehong Yoon
- **Year**: 2026
- **arXiv**: [2606.26904](https://arxiv.org/abs/2606.26904)
- **Date**: 2026-06-25

## Key Contributions
- **Blind-Trust-Problem diagnosis**: surfaces that frame-level evidence degradation is invisible to current video reasoning models, with accuracy drops of 15-30 pp on embodied benchmarks under realistic perturbations — naming the load-bearing failure mode of *uniform-reliability-assumption* in multimodal reasoning where perception confidence is collapsed into a single trust value.
- **Unified evidence interface with calibrated reliability scores**: each perception tool returns evidence in a shared format including a *calibrated reliability score* — surfacing *calibrated-confidence-as-evidence-attribute* as the structurally correct primitive for multi-tool perception pipelines, replacing the implicit uniform-trust assumption with explicit per-evidence reliability weights.
- **Confidence-cost GRPO reward**: introduces a GRPO reward that jointly optimizes correctness, evidence reliability, and efficiency, providing a training-time primitive for *reliability-aware reasoning* that is neither pure accuracy-maximization nor pure efficiency-maximization but a Pareto-shaped combination where the cost of acquiring evidence is balanced against its reliability contribution.

## Related Papers
- [[emergent-concepts]] — Parent wiki page that motivated this discovery
- [[remmd-realistic-multilingual-multi-image-agentic-verification-for-multimodal-misinformation-detection-2606.24112]] — Sibling multimodal agentic-verification work — REMMD verifies multimodal misinformation via agentic pipelines, Robust-TO verifies *visual-evidence reliability* via calibrated scores in video reasoning — together they bracket the multimodal-verification surface between misinformation-detection and visual-evidence-reliability primitives
- [[capable-but-careless-do-computer-use-agents-follow-contextual-integrity-2606.23189]] — Sibling agentic-capability-with-carefulness surface — Capable-But-Careless audits *rule-following* under contextual integrity, Robust-TO audits *evidence-reliability-weighting* under perturbation — together they bracket the agentic-carefulness surface between contextual-rule-following and perception-evidence-reliability
- [[the-verification-horizon-no-silver-bullet-for-coding-agent-rewards-2606.26300]] — Sibling verification-fidelity work — Verification-Horizon argues no fixed reward stays faithful for coding agents, Robust-TO operationalizes *per-evidence reliability scores* as a calibrated alternative — together they bracket the verification-fidelity surface between reward-stability ceilings and calibrated-evidence reliability primitives