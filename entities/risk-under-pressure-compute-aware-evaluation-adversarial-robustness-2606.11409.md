---
title: "Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [adversarial-robustness, evaluation, safety, llm]
sources: ["https://arxiv.org/abs/2606.11409"]
---

# Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models

## Overview
Standard adversarial robustness evaluations of LLMs report attack success rate (ASR) under fixed query budgets, implicitly treating all attacks as equally costly. This paper introduces **compute-aware evaluation** based on computational pressure — the cumulative FLOPs required to find a successful jailbreak — revealing that ASR at fixed budget systematically misleads about true attacker cost-effort tradeoffs. The framework enables more realistic comparison of adversarial robustness across models and attack strategies.

## Key Facts
- **Authors**: Malikeh Ehghaghi, Boglárka Ecsedi, Marsha Chechik, Colin Raffel
- **Year**: 2026
- **arXiv**: [2606.11409](https://arxiv.org/abs/2606.11409)

## Key Contributions
- Introduces **computational pressure** as a cost metric for adversarial attacks, measured in cumulative FLOPs rather than query count
- Demonstrates that ASR-at-fixed-budget obscures order-of-magnitude differences in attack computational cost across different attack strategies
- Provides a framework for compute-aware evaluation that enables fairer comparison of robustness across models and defense methods
- Applies the framework to show that leading jailbreak attacks have highly skewed cost-efficiency ratios that standard metrics miss

## Related Papers
- [[layer-wise-perturbations-via-sparse-autoencoders-for-adversarial-text-generation-2508.10404]] — SFPF (Run 127) introduced SAE-guided adversarial feature perturbation; Risk Under Pressure is the **evaluation methodology** counterpart — how to measure whether those perturbations actually increase attacker cost
- [[signature-in-code-backdoor-detection-how-far-are-we-2510.13992]] — Signature Code Backdoor (Run 127) evaluated spectral-signature defenses for code models; Risk Under Pressure is the **compute-aware evaluation framework** applied to adversarial robustness
- [[disentangling-adversarial-prompts-semantic-graph-defense-2605.27823]] — APD (this run) is a defense mechanism; Risk Under Pressure is the **evaluation methodology** for whether defenses genuinely increase attacker cost
