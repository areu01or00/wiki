---
title: "Look Light, Think Heavy: What Multimodal Chain-of-Thought Reasoning Can and Cannot Do"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [multimodal, chain-of-thought, reasoning, evaluation, llm, llava]
sources: ["https://arxiv.org/abs/2606.22565"]
---

# Look Light, Think Heavy: What Multimodal Chain-of-Thought Reasoning Can and Cannot Do

## Overview
This paper audits the actual capability gains of chain-of-thought (CoT) prompting in the multimodal setting, asking where it helps, where it hurts, and what its failure modes are. The authors find that CoT in multimodal LLMs behaves like "look light, think heavy" — the visual front-end processes minimal information while the textual reasoning chain carries the load — which means the multimodal-CoT gain is largely a textual-reasoning gain gated on accurate visual grounding. The contribution is a clean, granular capability map of multimodal CoT that distinguishes genuine multimodal reasoning from text-only reasoning dressed up with images.

## Key Facts
- **Authors**: Jin, Zhuoran; Zhu, Kejian; Yuan, Hongbang; Hao, Yupu; Cao, Pengfei; Chen, Yubo; Liu, Kang; Zhao, Jun
- **Year**: 2026 (revised 2026-06-21)
- **arXiv**: [2606.22565](https://arxiv.org/abs/2606.22565)
- **Subjects**: cs.CL

## Key Contributions
- Audits chain-of-thought prompting in multimodal LLMs and shows that its gain is concentrated in the textual-reasoning chain rather than in multimodal fusion — i.e. CoT helps *despite* weak visual grounding, not because of strong multimodal reasoning.
- Identifies task categories where multimodal CoT helps (math, logic, multi-step text reasoning over an image) and where it hurts or fails (visual-detail-sensitive tasks, perceptual grounding).
- Provides a diagnostic protocol for evaluating whether a multimodal reasoning improvement is genuinely multimodal or text-only reasoning riding on a fixed visual feature.
- Challenges the implicit narrative that multimodal CoT is a step toward integrated multimodal reasoning, reframing it as a tool that exposes — rather than solves — the multimodal-reasoning bottleneck.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 as a fresh 2026 contribution to multimodal reasoning evaluation.