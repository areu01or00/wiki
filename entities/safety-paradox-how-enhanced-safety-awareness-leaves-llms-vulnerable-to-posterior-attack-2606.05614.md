---
title: "Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [architecture, llm]
sources: ["https://arxiv.org/abs/2606.05614"]
---

# Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack

## Overview

Large language models (LLMs) are rigorously aligned to refuse harmful requests, a process that inherently cultivates a latent capacity to evaluate and recognize unsafe content. In this work, we reveal that this advanced safety awareness inadvertently introduces a fatal vulnerability. We introduce Posterior Attack, a single-query jailbreak that bypasses guardrails by prompting the model to generate the exact harmful response its internal classifier would normally flag as unsafe. Through extensive empirical evaluation across 30 open-source LLMs (up to 35B parameters in size) and frontier commercial models, we demonstrate that Posterior Attack achieves attack success rates exceeding 90% across most tested models.

## Key Facts
- **Authors**: Hoang, Long P. and Le, Hai V. and Xu, Shaoyang et al.
- **Year**: 2026
- **arXiv**: [2606.05614](https://arxiv.org/abs/2606.05614)

## Key Contributions
- **Posterior Attack** — a single-query jailbreak that prompts the model to emit the EXACT harmful response its internal classifier would flag, bypassing guardrails
- First paper to formalize the **safety paradox**: the more rigorously a model is aligned to recognize unsafe content, the more exploitable that recognition becomes
- Evaluated across 30 open-source LLMs (up to 35B) + frontier commercial models — >90% attack success rate on most tested models
- Distinct from Geometry-of-Refusal (linear-instability framing) and What-Intermediate-Layers-Know (entropy-detection framing) — Posterior Attack is a *causal exploitation* of safety awareness as a side channel

## Related Papers
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]]
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]]
- [[do-thinking-tokens-help-with-safety-2606.25013]]
- [[deeper-is-not-always-better-mitigating-the-alignment-tax-via-confident-layer-decoding-2606.21906]]
