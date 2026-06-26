---
title: "Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [memory, long-horizon, agent, reinforcement-learning, self-supervised]
sources: ["https://arxiv.org/abs/2605.30159"]
---

# Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents

## Overview
Introduces **MMPO** (Metacognitive Memory Policy Optimization), a self-supervised training objective that targets the *clarity of the induced belief* over latent task state — not just sparse trajectory success — when training memory-augmented LLM agents for long-horizon tasks. The method uses **Belief Entropy** as a fine-grained proxy for memory quality and explicitly penalizes summaries that induce high epistemic uncertainty.

## Key Facts
- **Authors**: Liu, Ziyan; Hao, Zhezheng; Chen, Yeqiu; Wang, Hong; Hou, Jingren; Ding, Ruiyi; Yang, Yongkang; Ji, Wence; Xia, Wei; Liu, Feng
- **Year**: 2026
- **arXiv**: [2605.30159](https://arxiv.org/abs/2605.30159)

## Key Contributions
- Frames memory optimization as a **belief-clarity** problem rather than a sparse outcome-reward problem, formalizing the *epistemic-uncertainty-penalization* objective for memory policies.
- Introduces **Belief Entropy**, a self-supervised proxy that probes how uncertain the model remains about the latent task state given its current memory, enabling dense, memory-specific supervision without environment reward.
- Proposes **MMPO**, which combines outcome-based RL with explicit summary-quality penalties; empirically maintains **97.1% performance at 1.75M-token context windows** on diverse long-horizon tasks.

## Related Papers
- [[emergent-concepts]] — Parent discovery surface for emergent-concept exploration runs.
- [[why-multi-step-tool-use-reinforcement-learning-collapses-and-how-supervisory-signals-fix-it-2606.26027]] — Companion work on diagnosing RL pathologies via supervisory signal design.