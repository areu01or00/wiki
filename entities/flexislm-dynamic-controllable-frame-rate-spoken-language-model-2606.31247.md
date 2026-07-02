---
title: "FlexiSLM: A Dynamic and Controllable Frame Rate Spoken Language Model"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [speech, llm, inference-efficiency, multimodal, architecture]
sources: ["https://arxiv.org/abs/2606.31247"]
---

# FlexiSLM: A Dynamic and Controllable Frame Rate Spoken Language Model

## Overview
FlexiSLM is the first Spoken Language Model supporting dynamic and controllable frame rates on both speech input and output. Existing SLMs use fixed frame rates (25 or 12.5 Hz), ignoring the time-varying information density of speech. FlexiSLM applies dynamic frame rate speech coding techniques to SLMs, enabling very low average frame rates and frame rate controllability. It outperforms fixed-frame-rate 7B models (Qwen2.5-Omni, Kimi-Audio) at high-quality operating points and can be steered down to 4.0 Hz.

## Key Facts
- **Authors**: Li, Jiaqi; Wang, Chaoren; Tian, Xiaohai + 9
- **Year**: 2026
- **arXiv**: [2606.31247](https://arxiv.org/abs/2606.31247)
- **Online Date**: 2026-06-30

## Key Contributions
- First SLM with dynamic and controllable frame rates for both speech input and output
- Applies dynamic frame rate speech coding to SLMs — enabling inference-time quality/speed tradeoff
- Outperforms Qwen2.5-Omni and Kimi-Audio at high-quality operating points
- FlexiSLM at 6.25 Hz roughly halves inference time vs 12.5 Hz while retaining strong quality
- Controllable frame rate enables deployment-specific quality/efficiency tradeoffs

## Related Papers
- [[interleaved-speech-language-models-latently-work-in-text-2606.22473]] — Latent text work in interleaved speech-language models (prior art on speech-LLM integration)
- [[redvox-safety-and-fairness-gaps-in-speech-models-across-languages-2606.26968]] — Safety and fairness gaps in speech models across languages
- *Elastic Time: Dynamic Frame Rate Bottlenecks for Neural Audio Coding* (2606.27320) — Foundational dynamic frame rate technique applied in FlexiSLM
