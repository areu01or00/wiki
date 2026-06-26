---
title: "MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [4d-video-generation, multi-view, point-tracking, geometric-supervision, novel-view-synthesis, video-diffusion]
sources: ["https://arxiv.org/abs/2606.26087"]
---

# MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation

## Overview
MVTrack4Gen addresses the geometric-consistency bottleneck in novel-view video synthesis from a monocular reference video along a target camera trajectory. The method uses **multi-view point tracking** as a geometric-supervision signal to constrain 4D video generation, enforcing both geometric consistency (the same physical point projects to consistent 3D locations across views) and motion fidelity (the same dynamic point exhibits consistent trajectories across views) in a single diffusion-based generation pipeline. The work lands at a moment when T2V systems have largely converged on appearance-only evaluation, leaving the *geometric supervision* axis under-explored despite being load-bearing for the deployment regime where downstream applications (3D reconstruction, scene editing, simulation) require view-consistent 4D output rather than just per-frame realism.

## Key Facts
- **Authors**: Lee, JoungBin; Jung, Jaewoo; Lee, Jongmin; Kim, Tongmin; Kim, Hyunsung; Narihira, Takuya; + 5 more
- **Year**: 2026
- **arXiv**: [2606.26087](https://arxiv.org/abs/2606.26087)
- **Submitted**: 2026-06-24 (cs.CV)
- **Discovered via**: emergent-concept search on 2026-06-26 (4d-video-generation / multi-view-point-tracking / geometric-supervision / novel-view-synthesis / video-diffusion theme)
- **First-in-wiki surface**: 4D video generation + multi-view point tracking as geometric supervision (verified via `ls entities/ | grep -iE "(4d|multi-view|point-track|geometric)"` returning only Causal-rCM as a tangentially related match)

## Key Contributions
- Identifies a structural gap in 4D video generation: existing pipelines enforce appearance fidelity but lack an explicit geometric-consistency primitive that survives novel-view synthesis along arbitrary camera trajectories
- Proposes multi-view point tracking as a *geometric-supervision* signal: rather than using points as a conditioning input, the points are tracked across the generated views to provide a differentiable consistency loss between the model's multi-view output and the underlying 3D scene structure
- Demonstrates that point-tracking-derived geometric supervision improves both geometric consistency (lower reprojection error, better 3D reconstruction downstream) and motion fidelity (better temporal coherence of dynamic content) without requiring 3D ground truth at training time
- Surfaces *geometric-supervision-via-tracking* as a load-bearing primitive for 4D video generation: tracking-derived signals can stand in for expensive 3D ground truth while still constraining the multi-view output to be 3D-consistent

## Related Papers
- [[causal-rcm-a-unified-teacher-forcing-and-self-forcing-open-recipe-for-autoregressive-diffusion-distillation-in-streaming-video-generation-and-interactive-world-models-2606.25473]] — sibling streaming-video-generation distillation (Causal-rCM unifies teacher/self-forcing for AR diffusion distillation; MVTrack4Gen adds geometric supervision as a complementary axis to appearance-only distillation)
- [[domain-shuttle-freeform-open-domain-subject-driven-text-to-video-2606.26058]] — sibling T2V evaluation discipline (DomainShuttle surfaces in-domain/cross-domain S2V ambiguity; MVTrack4Gen surfaces view-consistency as a structurally distinct axis of T2V quality that complements the subject-driven axis)
- [[wan-streamer-v0-1-end-to-end-real-time-interactive-foundation-models-2606.25041]] — sibling multimodal video foundation (Wan-Streamer is end-to-end real-time interactive video; MVTrack4Gen is offline novel-view synthesis with geometric-supervision — together they bracket video foundation models on the latency/quality spectrum)
- [[world-action-models-a-survey-2606.20781]] — sibling embodied predictive-action survey (WAM surveys predictive-action methods; MVTrack4Gen is a *non-predictive* geometric-supervision primitive that could be a useful input to WAM-style downstream applications)
