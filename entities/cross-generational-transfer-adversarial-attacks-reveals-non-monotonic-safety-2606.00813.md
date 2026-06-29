---
title: "Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [safety-alignment, adversarial-attacks, alignment, llm]
sources: ["https://arxiv.org/abs/2606.00813"]
---

# Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs

## Overview
Safety alignment in LLMs does not improve monotonically across model generations. This paper studies four generations of Google's Gemma family (7B–31B) using MAP-Elites (quality-diversity evolution) as an automated red-teaming probe, revealing that Gemma 3 (12B) exhibits significantly higher attack success rate (68.7%) than both its predecessor Gemma 2 (45.5%) and successor Gemma 4 (33.9%). Replaying evolved attack archives across generations shows asymmetric cross-generational transfer — attacks from other generations transfer to Gemma 3 at 44–46% but only 10–20% to other generations — identifying Gemma 3 as a critical alignment regression. The findings reveal fundamental discontinuities in LLM safety alignment development.

## Key Facts
- **Authors**: Subhadip Mitra
- **Year**: 2026
- **arXiv**: [2606.00813](https://arxiv.org/abs/2606.00813)

## Key Contributions
- Reveals **non-monotonic safety alignment** across LLM model generations — Gemma 3 (12B) is a critical regression with 68.7% ASR vs. Gemma 2 (45.5%) and Gemma 4 (33.9%)
- Uses **MAP-Elites automated red-teaming** as a systematic probe across four Gemma generations
- Demonstrates **asymmetric cross-generational attack transfer** — Gemma 3 is uniquely vulnerable to attacks evolved on other generations, suggesting a specific alignment failure mode
- Provides evidence that safety improvements from one generation do not reliably transfer to the next, with implications for deployment and evaluation practices

## Related Papers
- [[risk-under-pressure-compute-aware-evaluation-adversarial-robustness-2606.11409]] — Risk Under Pressure (this run) provides **compute-aware evaluation methodology** for assessing cross-generational robustness; Cross-Generational Transfer provides the empirical finding of non-monotonic alignment
- [[disentangling-adversarial-prompts-semantic-graph-defense-2605.27823]] — APD (this run) is a defense mechanism; Cross-Generational Transfer reveals **why alignment regressions occur** and what makes specific generations uniquely vulnerable
- [[llm-driven-feature-level-adversarial-attacks-on-android-malware-detectors-2512.21404]] — LAMLAD (Run 127) is adversarial attack methodology; Cross-Generational Transfer studies **alignment regression as an attack surface** — misalignment enables adversarial transfer
