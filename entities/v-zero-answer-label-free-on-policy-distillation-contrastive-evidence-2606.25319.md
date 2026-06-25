---
title: "V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [multimodal-llm, visual-reasoning, on-policy-distillation, post-training, contrastive-learning, evidence-grounding]
sources: ["https://arxiv.org/abs/2606.25319"]
---

# V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning

## Overview
Sun, Yi, Deng, Zhou, Jia, Zhao, Yuan, Lv, and Wang address the prohibitive cost of post-training multimodal LLMs (MLLMs) for fine-grained visual reasoning — where existing methods rely on reinforcement learning with hand-designed verifiable rewards or supervised fine-tuning on large-scale annotated reasoning traces — by proposing V-Zero, an answer-label-free framework that uses On-Policy Distillation (OPD) augmented with Contrastive Evidence Gating: the student model is trained on its own sampled trajectories, evaluated against a question-relevant regional crop paired with a negative visual view, with a contrastive gate controlling the flow of dense token-level distillation signal — yielding 5×+ speedups over SFT and 10×+ speedups over RL baselines while preserving strong generalization.

## Key Facts
- **Authors**: Sun, Haoxiang; Yi, Zhihang; Deng, Langxuan; Zhou, Yuhao; Jia, Peiqi; Zhao, Jian; Yuan, Li; Lv, Jiancheng; Wang, Tao
- **Year**: 2026
- **arXiv**: [2606.25319](https://arxiv.org/abs/2606.25319)
- **Date**: 2026-06-24
- **Code**: https://github.com/eVI-group-SCU/V-Zero

## Key Contributions
- Diagnoses the post-training cost structure of fine-grained visual-reasoning MLLMs — RL-with-verifiable-rewards needs costly exploration + hand-designed rules, SFT needs heavy textual-supervision annotation — and identifies On-Policy Distillation (learning from the student's own trajectories) as the natural label-free alternative that avoids both external answer labels and dense annotation.
- Revisits OPD through a negative-free stop-gradient alignment lens, showing that while OPD provides effective token-level correction, its ceiling is constrained by the absence of trajectory-level discrimination — a structural diagnosis that motivates the contrastive gating addition.
- Proposes V-Zero, an answer-label-free framework with Contrastive Evidence Gating that pairs a question-relevant regional crop with a negative visual view during training to evaluate student-sampled trajectories and gate dense token-level distillation — using contrastive regional evidence as the trajectory-quality signal that bare OPD lacks.
- Demonstrates consistent gains on multiple visual reasoning benchmarks while preserving strong generalization, with 5×+ speedups over SFT and 10×+ speedups over RL baselines — surfacing a deployment-relevant design pattern: contrastive regional grounding can replace hand-designed verifiers and full trajectory supervision in MLLM post-training.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[distilling-examples-into-task-instructions-enhanced-in-context-2606.15641]] — Sibling label-minimization work in the in-context-learning surface; both replace verbose supervision with compact, learned signals — V-Zero replaces annotated answer labels with contrastive regional grounding, while the Call Playbook paper distills few-shot examples into structured criteria + task descriptions.
- [[distill-once-adapt-life-long-dataset-distillation-continual-2606.20196]] — Sibling dataset-distillation work on the continual-adaptation side; both papers replace raw-data supervision with compact learned signals — V-Zero replaces annotated answer labels with contrastive regional grounding, while DO-ALL replaces raw source data with synthetic anchors for stable online adaptation.