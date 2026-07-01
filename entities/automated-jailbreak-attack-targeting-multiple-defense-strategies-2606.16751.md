---
title: "Automated Jailbreak Attack Targeting Multiple Defense Strategies"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [safety, jailbreak, adversarial-prompt, red-teaming, multi-defense]
sources: ["https://arxiv.org/abs/2606.16751"]
---

# Automated Jailbreak Attack Targeting Multiple Defense Strategies

## Overview
This paper presents UNIATTACK, an adversarial testing framework that systematically constructs effective black-box jailbreak attack prompts against multi-layered defense mechanisms. Unlike prior approaches that rely on static templates or iterative model-specific tuning, UNIATTACK extracts minimal high-impact attack features from existing attacks, optimizes them via a specialized attacker LLM, and composes them into flexible templates through automated refinement. The framework enables one-shot attacks that generalize across multiple models and safety categories, requiring only 0.03%-4.96% of the cost of baseline approaches.

## Key Facts
- **Authors**: Wang, Qi; Wan, Chengcheng; He, Weijia + 4
- **Year**: 2026
- **arXiv**: [2606.16751](https://arxiv.org/abs/2606.16751)
- **Date**: 2026-06-15

## Key Contributions
- Proposes feature-centric attack construction: extracts minimal high-impact attack features from diverse existing attacks
- Introduces specialized attacker LLM for optimizing attack features and composing flexible attack templates
- Achieves 64.63%-248.82% ASR improvement over baselines on models with multi-layered defenses
- Reduces attack cost to 0.03%-4.96% of baseline methods; open-source artifact available

## Related Papers
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — Adaptive jailbreak architecture (orthogonal: adaptive architecture vs. automated feature extraction)
- [[compositional-jailbreaking-empirical-analysis-mutator-chain-interactions-aligned-llms-2605.15598]] — Compositional jailbreaking (orthogonal: chain interaction analysis vs. multi-defense optimization)
