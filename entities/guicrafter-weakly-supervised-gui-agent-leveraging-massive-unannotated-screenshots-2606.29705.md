---
title: "GUICrafter: Weakly-Supervised GUI Agent Leveraging Massive Unannotated Screenshots"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [gui-agent, weakly-supervised, agent-learning, grounding]
sources: ["https://arxiv.org/abs/2606.29705"]
---

# GUICrafter: Weakly-Supervised GUI Agent Leveraging Massive Unannotated Screenshots

## Overview
GUI agents have emerged as a key paradigm for autonomous computer interaction, but their training requires large amounts of labeled GUI data — screenshots with action annotations — which is expensive and time-consuming to collect at scale. GUICrafter addresses this by developing a weakly-supervised approach that learns effective GUI agents from massive unannotated screenshot collections, dramatically reducing data collection cost.

## Key Facts
- **Authors**: Sunqi Fan, Lingshan Chen, Runqi Yin, Qingle Liu, Yongming Rao, Meng-Hao Guo, Shi-Min Hu
- **Year**: 2026
- **arXiv**: [2606.29705](https://arxiv.org/abs/2606.29705)

## Key Contributions
- **Weakly-supervised GUI agent learning**: Instead of requiring expensive human-annotated (screenshot, action) pairs, GUICrafter leverages the visual structure of unannotated screenshots (UI layouts, spatial relationships, visual affordances) to learn action proposals
- **Massive-scale pretraining**: Shows that pretraining on millions of unannotated screenshots from app stores and web interfaces produces GUI agents that transfer to new environments with minimal fine-tuning
- **Contrastive visual representation learning**: A core technical contribution is a visual representation learning objective that distinguishes actionable UI elements from decorative ones without labels
- **Strong downstream transfer**: Evaluated on Android, Web, and Desktop environments; achieves competitive performance with fully-supervised approaches using only a fraction of the labeled data

## Related Papers
- [[memgui-agent-end-to-end-long-horizon-mobile-gui-agent-proactive-context-2606.19926]] — MemGUI: end-to-end mobile GUI agent with proactive context management; fully supervised approach — GUICrafter's weakly-supervised paradigm is orthogonal and complementary
- [[mobileforge-annotation-free-adaptation-mobile-gui-agents-hierarchical-feedback-policy-optimization-2606.19930]] — MobileForge: annotation-free adaptation for mobile GUI agents; shares the annotation-free/weakly-supervised goal but MobileForge focuses on adaptation of existing agents while GUICrafter focuses on pretraining representation learning from scratch
