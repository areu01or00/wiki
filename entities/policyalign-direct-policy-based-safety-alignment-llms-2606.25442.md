---
title: "PolicyAlign: Direct Policy-Based Safety Alignment for Large Language Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [safety, alignment, policy-direct, on-policy-distillation, llm]
sources: ["https://arxiv.org/abs/2606.25442"]
---

# PolicyAlign: Direct Policy-Based Safety Alignment for Large Language Models

## Overview

Wu, Chang; Fang, Junfeng; Jiang, Houcheng; Tang, Kai; Cheng, Pengyu; Jiang, Xiaoxi; Jiang, Guanjun; Wang, Xiang observe that real-world LLM deployment confronts safety requirements specified as **natural-language policies** — often without corresponding high-quality supervision data, since policy updates outpace the data-collection pipeline. They propose **PolicyAlign**, a direct framework that first synthesizes policy-violating instructions from a stated safety policy and then performs **on-policy self-distillation** to internalize policy-guided behavior, supplemented by **Policy-Sensitive Filtering** that selects the instructions where the policy induces the largest behavioral shift. The approach bypasses reward-modeling and preference-pair construction entirely, generalizes to medical / legal / financial safety scenarios, and maintains low over-refusal plus preserved general capabilities — making **policy-natural-language as the safety specification surface** the load-bearing primitive.

## Key Facts

- **Authors**: Wu, Chang; Fang, Junfeng; Jiang, Houcheng; Tang, Kai; Cheng, Pengyu; Jiang, Xiaoxi; Jiang, Guanjun; Wang, Xiang
- **Year**: 2026
- **Date**: 2026-06-24
- **arXiv**: [2606.25442](https://arxiv.org/abs/2606.25442)
- **Code released**

## Key Contributions

- Articulates the **policy-vs-supervision-data mismatch** in real-world LLM safety: emerging safety requirements arrive as natural-language policies, but data-driven alignment methods (RLHF, DPO, Constitutional AI) need curated preference pairs or demonstrations — creating a latency gap
- Introduces **PolicyAlign** — a 2-stage direct alignment framework: (1) **policy-violating instruction synthesis** from a stated safety policy, (2) **on-policy self-distillation** to internalize policy-guided behavior — bypassing reward modeling entirely
- Introduces **Policy-Sensitive Filtering** — selects instructions where the policy induces the largest behavioral shift in the base model, improving training stability and data efficiency
- Demonstrates **low over-refusal + preserved general capabilities** (a common safety alignment failure mode is refusal collapse on benign queries)
- Generalizes across **medical / legal / financial** safety scenarios — vertical-domain transfer without retraining
- First framework in the wiki that explicitly treats **natural-language policy as the safety-alignment specification surface**, decoupling safety updates from the data-annotation pipeline

## Related Papers

- [[safety-paradox-how-enhanced-safety-awareness-leaves-llms-vulnerable-to-posterior-attack-2606.05614]] — safety awareness as a vulnerability surface (Run 41)
- [[ras-measuring-llm-safety-through-refusal-alignment-2606.25750]] — refusal alignment as safety-measurement primitive (Run 42)
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — mechanistic geometry of safety alignment (Run 39)
- [[privacyalign-contextual-privacy-alignment-for-llm-agents-2606.21710]] — contextual privacy alignment for agents
- [[do-thinking-tokens-help-with-safety-2606.25013]] — thinking-tokens-as-safety-instrument
- [[deeper-is-not-always-better-mitigating-the-alignment-tax-via-confident-layer-decoding-2606.21906]] — alignment tax mitigation via confident-layer decoding
- [[opid-on-policy-skill-distillation-for-agentic-reinforcement-learning-2606.26790]] — on-policy skill distillation for agentic RL (Run 44)
- [[renio-reweighting-negative-trajectory-importance-for-llm-on-policy-distillation-2606.23104]] — on-policy trajectory reweighting
- [[policytrim-boosting-intrinsic-policy-efficiency-vla-models-2606.22540]] — intrinsic policy efficiency for VLA
- [[mobileforge-annotation-free-adaptation-mobile-gui-agents-hierarchical-feedback-policy-optimization-2606.19930]] — annotation-free hierarchical policy optimization (Run 36)
- [[polar-factorizing-extent-mode-latent-actions-robot-policy-2606.21139]] — extent-mode latent-action factorization
- [[v-zero-answer-label-free-on-policy-distillation-contrastive-evidence-2606.25319]] — label-free on-policy distillation