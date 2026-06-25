---
title: "Safe Few-Step Generation via Velocity Editing"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [flow-matching, t2i-safety, velocity-editing, training-free, concept-removal, few-step-distillation, posterior-steering]
sources: ["https://arxiv.org/abs/2606.23267"]
---

# Safe Few-Step Generation via Velocity Editing

## Overview
Flow matching has emerged as a strong paradigm for state-of-the-art text-to-image generation at small sampling-step counts (4–8 steps via MeanFlow/Rectified Flow variants), but adapting safety and concept-removal methods to this regime remains an open problem because prior safety methods rely on iterative trajectory steering across many denoising steps or on CLIP-centric prompt-embedding manipulation — design assumptions that break down when (a) the sampling budget is too small to permit iterative correction and (b) modern context-aware text encoders render embedding-level interventions ineffective. VESFlow proposes a training-free safety method tailored to few-step flow matching that directly edits the *velocity field* via a safe-conditional posterior, steering the trajectory toward safe outputs while leaving the conditioning prompt unchanged; VESFlow+ extends this by also pushing the velocity *away from* the unsafe direction and adds a risk-score filter that bypasses velocity editing on benign prompts to reduce compute. Evaluated on Ring-A-Bell and MMA-Diffusion attacks against a 4-step MeanFlow backbone, VESFlow+ reduces attack success rate (NudeNet) to 6.3% / 6.8% while preserving benign-prompt fidelity.

## Key Facts
- **Authors**: Choi, Yujin; Yoon, Jaehong
- **Year**: 2026
- **arXiv**: [2606.23267](https://arxiv.org/abs/2606.23267)
- **Date**: 2026/06/22
- **Method**: VESFlow (Velocity Editing for Safety in Flow matching) + VESFlow+
- **Backbone**: 4-step MeanFlow
- **Attack success rate (NudeNet)**: 6.3% on Ring-A-Bell, 6.8% on MMA-Diffusion
- **Training**: training-free (no fine-tuning required)

## Key Contributions
- **Velocity-field editing as the canonical safety primitive for flow matching** — leverages the structural fact that flow-matching models learn the marginal velocity field, so safety can be injected as a safe-conditional posterior edit on velocity rather than via the iterative-trajectory or CLIP-embedding primitives that prior safety work assumed.
- **VESFlow: training-free safety for extremely-few-step sampling** — addresses the design-assumption breakdown where prior methods require many denoising steps or work via embedding manipulation, both of which fail under 4-step MeanFlow. VESFlow is the first safety method validated at this sampling budget.
- **VESFlow+: dual-direction velocity steering** — extends VESFlow to also push velocity *away* from the unsafe direction (not just toward the safe direction), yielding stronger concept removal at the cost of slightly more compute per edit.
- **Risk-score-based benign-prompt bypass** — observations that VESFlow leaves outputs unchanged on benign prompts motivate a risk score that detects safe prompts and bypasses velocity editing entirely, reducing compute on the dominant benign traffic while preserving full safety on the risky minority.
- **Empirical validation across two attack benchmarks at 4-step MeanFlow** — Ring-A-Bell (6.3% ASR) and MMA-Diffusion (6.8% ASR) demonstrate that the velocity-edit primitive is competitive with prior training-required safety methods without requiring fine-tuning, validating training-free safety as a load-bearing alternative for flow-matching T2I.

## Related Papers
- [[emergent-concepts]] — Parent thematic cluster for emergent-concept discoveries in this wiki
- [[exploring-the-design-space-of-reward-backpropagation-for-flow-matching-2606.11075]] — FlowBP addresses reward-gradient-bottleneck pathology in flow-matching alignment (training-side intervention); VESFlow addresses safety on the same flow-matching surface (inference-side intervention) — direct training/inference complement
- [[tropt-an-open-framework-for-unifying-and-advancing-discrete-text-optimization-2606.23496]] — TROPT unifies discrete-text-trigger optimizers used for LLM jailbreaks; VESFlow provides the T2I-flow-matching counterpart that ships the open optimization/reward substrate safety work needs
- [[fedot-ownership-verification-leakage-tracing-watermarks-federated-ldms-2606.22875]] — FedOT addresses ownership-verification + leakage-tracing security for federated LDMs; VESFlow addresses output-stage safety via velocity editing, complementary generative-model security surfaces