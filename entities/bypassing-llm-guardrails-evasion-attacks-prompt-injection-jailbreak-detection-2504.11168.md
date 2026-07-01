---
title: "Bypassing LLM Guardrails: An Empirical Analysis of Evasion Attacks against Prompt Injection and Jailbreak Detection Systems"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [safety, llm, jailbreak, guardrail, adversarial]
sources: ["https://arxiv.org/abs/2504.11168"]
---

# Bypassing LLM Guardrails: An Empirical Analysis of Evasion Attacks against Prompt Injection and Jailbreak Detection Systems

## Overview
This paper provides a systematic empirical analysis of how LLM guardrail systems can be bypassed via adversarial evasion techniques. The authors demonstrate two approaches: traditional character-injection methods and algorithmic Adversarial Machine Learning (AML) evasion techniques. Testing against six prominent protection systems including Microsoft's Azure Prompt Shield, the work reveals that safety classifiers trained on standard benchmarks dramatically overstate their robustness — with an 8.4-point AUC gap and large per-dataset drops when evaluated under Leave-One-Dataset-Out distribution shift.

## Key Facts
- **Authors**: Hackett, William; Birch, Lewis; Trawicki, Stefan + 2
- **Year**: 2025
- **arXiv**: [2504.11168](https://arxiv.org/abs/2504.11168)

## Key Contributions
- **Character-injection evasion**: Demonstrates that simple character-level perturbations (adding invisible characters, Unicode homoglyphs, space injection) can bypass prompt injection and jailbreak detection classifiers
- **Algorithmic AML evasion**: Uses adversarial machine learning techniques (projected gradient descent on the input encoding) to systematically find evasion examples that transfer across multiple guardrail systems
- **Leave-One-Dataset-Out evaluation**: The key methodological contribution — evaluates guardrail robustness under genuine distribution shift rather than within-distribution benchmark performance. Reveals 8.4-point AUC gap between benchmark and LODO evaluation
- **Dataset shortcut diagnosis**: Identifies that many features used by safety classifiers are dataset-specific shortcuts that don't generalize — a mechanistic interpretability finding with direct safety implications
- **Production guardrail vulnerability**: Tests against real deployed systems (Azure Prompt Shield, among others) — not just academic benchmarks

## Related Papers
- *What Intermediate Layers Know: Detecting Jailbreaks from Entropy Dynamics* (2606.25182) — Proposes a detection method using internal model entropy. This paper reveals the adversarial evasion techniques that detection methods must also defend against — both papers are essential reads for the safety-mechanisms researcher.
- *Robust Harmful Features Under Jailbreak Attacks* (2606.28153) — Mechanistically characterizes jailbreak mechanisms in LLM safety alignment. Complements this paper's evasion attack surface analysis by revealing why these mechanisms are brittle in deployment.
