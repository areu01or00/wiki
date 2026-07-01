---
title: "Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [safety-mechanisms, jailbreak, attention-heads, mechanistic-interpretability]
sources: ["https://arxiv.org/abs/2606.28153"]
---

# Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models

## Overview
Jailbreak attacks bypass LLM safety alignment, yet their mechanisms remain poorly understood. This paper provides mechanistic evidence that attacks do not comprehensively eliminate safety features, but instead selectively suppress specific attention heads. The authors identify two functionally differentiated types of harmful features and show that adversarial attacks exploit head-level suppression rather than wholesale safety erasure.

## Key Facts
- **Authors**: Yin, Yanchen; Han, Dongqi; Li, Linghui
- **Year**: 2026
- **arXiv**: [2606.28153](https://arxiv.org/abs/2606.28153)
- **Date**: 2026-06-26

## Key Contributions
- Identifies two functionally differentiated types of harmful features under jailbreak attacks
- Shows selective attention head suppression as the mechanistic substrate of jailbreak bypass
- Demonstrates that safety features are not eliminated but geometrically reshaped by attacks
- Provides evidence for attention head specialization in safety-critical vs harmful content processing

## Related Papers
- [[the-compliance-trap-how-structural-constraints-degrade-frontier-ai-metacognition-2605.02398]] — Compliance Trap paper from prior run surfaces metacognitive degradation under adversarial pressure; this paper provides the mechanistic attention-head substrate for that macro-level phenomenon
