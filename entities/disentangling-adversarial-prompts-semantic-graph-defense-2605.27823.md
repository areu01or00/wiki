---
title: "Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [adversarial-defense, safety, prompt-security, llm]
sources: ["https://arxiv.org/abs/2605.27823"]
---

# Disentangling Adversarial Prompts: A Semantic-Graph Defense for Robust LLM Security

## Overview
LLMs are increasingly vulnerable to adversarial prompts that exploit semantic ambiguities to bypass safety mechanisms. This paper proposes the **Adversarial Prompt Disentanglement (APD)** framework — a defense that proactively identifies and neutralizes malicious components in input prompts before LLM processing, using a semantic-graph representation to model relationships between prompt tokens and known attack patterns. APD demonstrates superior robustness across diverse adversarial prompt datasets, reducing harmful output generation by over 90% while preserving benign task performance.

## Key Facts
- **Authors**: Xiang Fang, Wanlong Fang
- **Year**: 2026
- **arXiv**: [2605.27823](https://arxiv.org/abs/2605.27823)

## Key Contributions
- Introduces **Adversarial Prompt Disentanglement (APD)** framework using semantic-graph representation to identify and neutralize malicious prompt components
- Proactively detects adversarial elements before LLM processing, unlike reactive defenses that work at output level
- Achieves >90% reduction in harmful output generation across adversarial prompt datasets while preserving benign task utility
- Addresses both jailbreaking and prompt injection attack vectors through unified semantic-graph analysis

## Related Papers
- [[risk-under-pressure-compute-aware-evaluation-adversarial-robustness-2606.11409]] — Risk Under Pressure (this run) provides the **compute-aware evaluation framework** for APD — measuring whether APD genuinely increases attacker cost beyond standard defenses
- [[layer-wise-perturbations-via-sparse-autoencoders-for-adversarial-text-generation-2508.10404]] — SFPF (Run 127) is adversarial **attack** via SAE-guided feature perturbation; APD is the **defense** counterpart — disentangling adversarial prompts at the input level
- [[signature-in-code-backdoor-detection-how-far-are-we-2510.13992]] — Signature Code Backdoor (Run 127) evaluated spectral-signature defenses for code models; APD is the **general-domain prompt disentanglement defense** for natural language
