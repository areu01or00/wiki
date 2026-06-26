---
title: "Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [agentic-rl, tool-use, training-stability, supervisory-signal, sft-rl-interleaving, llm]
sources: ["https://arxiv.org/abs/2606.26027"]
---

# Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It

## Overview

Hao, Yupu; Jin, Zhuoran; Liao, Huanxuan; Liu, Kang; Zhao, Jun observe that recent agentic reinforcement learning (RL) methods for multi-step tool use show promise but frequently deliver **catastrophic collapse** — a sudden, unpredictable drop where tool-invocation structure fails even though the underlying tool-use capability is intact, merely obscured by format-level pathologies. They trace the failure mode to **unexpected probability spikes in specific control tokens** (i.e., format-level rather than capability-level degradation) and demonstrate that a structured set of supervisory signals (off-policy supervision, hint-based guidance, erroneous-example supervision) applied under either synchronous or **interleaved SFT+RL** schemes can substantially improve training stability while restoring tool-execution structure. The load-bearing primitive is **interleaved-SFT-as-stabilizer-for-RL-collapse** — recognizing that agentic RL instability is not a capability gap but a format-distribution pathology that supervised anchors can repair.

## Key Facts
- **Authors**: Hao, Yupu; Jin, Zhuoran; Liao, Huanxuan; Liu, Kang; Zhao, Jun
- **Year**: 2026
- **Date**: 2026-06-24
- **arXiv**: [2606.26027](https://arxiv.org/abs/2606.26027)
- **Code released**

## Key Contributions
- Articulates the **catastrophic-collapse failure mode of agentic tool-use RL** — where models abruptly lose tool-invocation structure during training even though their underlying capability is preserved, surfacing a format-level pathology distinct from capability-level training failures
- Identifies **control-token probability spikes** as the structural cause — the collapse is a format-distribution pathology, not a capability degradation, so the underlying tool-use skill remains intact but obscured by spurious control-token mass
- Investigates a **diverse set of supervisory signals** (off-policy supervision, hint-based guidance, erroneous-example supervision) under both synchronous and interleaved training schemes, providing the structural taxonomy of fixes the field has been missing
- Demonstrates that **interleaving supervised fine-tuning (SFT) with RL** substantially improves stability, but exhibits degraded performance under format and content out-of-distribution (OOD) evaluation — surfacing the OOD-format generalization cost of stabilization
- Analyzes the impact of **learning rates and generalization across settings** — making the stability-vs-OOD trade-off explicit so future work can tune rather than rediscover it
- First paper in the wiki that frames **agentic-RL collapse as a format-distribution pathology** amenable to interleaved-SFT supervision, distinct from Run 44's OPID (which targets skill-density in on-policy distillation, not RL-training collapse)

## Related Papers
- [[opid-on-policy-skill-distillation-for-agentic-reinforcement-learning-2606.26790]] — Run 44 sibling: on-policy skill-conditioned distillation for agentic RL (different failure mode — OPID is post-training-distillation, this paper is RL-training-time collapse)
- [[dont-blindly-trust-it-how-unreliable-feedback-breaks-tool-using-llm-agents-2606.21409]] — feedback-reliability-as-deployment-condition for tool-using agents (Run 38)
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — long-horizon planning evaluation for tool-use agents
- [[constraint-tax-in-open-weight-llms-an-empirical-study-of-tool-calling-suppression-under-structured-output-constraints-2606.25605]] — tool-calling pathology under structured-output constraints
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — agent-native memory design survey
- [[learning-from-your-own-mistakes-constructing-learnable-micro-reflective-trajectories-for-self-distillation-2606.18844]] — trajectory-aware self-correction RL
- [[emergent-concepts]] (parent wiki page) — meta-cluster for emergent-concept paper discoveries