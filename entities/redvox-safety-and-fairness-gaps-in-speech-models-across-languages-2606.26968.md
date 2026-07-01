---
title: "RedVox: Safety and Fairness Gaps in Speech Models Across Languages"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [speech-model, safety, fairness, multilingual, benchmark, audio-LLM]
sources: ["https://arxiv.org/abs/2606.26968"]
---

# RedVox: Safety and Fairness Gaps in Speech Models Across Languages

## Overview
RedVox is a multilingual safety and fairness benchmark for audio and speech models built on real voices, covering unsafe and unfair stereotypical requests across five languages (English, French, Italian, Spanish, and German). The paper surveys safety reporting practices across state-of-the-art speech model releases, finding that only 8% document any multilingual analysis, and evaluates eight models finding persistent vulnerabilities that worsen in non-English languages and are amplified by spoken input.

## Key Facts
- **Authors**: Unknown (arXiv 2606.26968)
- **Year**: 2026
- **arXiv**: [2606.26968](https://arxiv.org/abs/2606.26968)

## Key Contributions
- First multilingual speech safety and fairness benchmark covering real voices across five languages with unsafe/stereotypical request coverage
- Documents that only 8% of state-of-the-art speech model releases perform any multilingual safety analysis
- Finds vulnerabilities persist under non-adversarial conditions, worsen in non-English languages, and amplify when request is spoken (not typed)
- Eight models evaluated including state-of-the-art speech-capable models
- First documentation of unique personal and privacy challenges in collecting naturalistic speech safety data with human participants

## Related Papers
- [[do-thinking-tokens-help-with-safety-2606.25013]] — Do thinking tokens help with safety? (orthogonal — safety via thinking tokens in text; RedVox addresses spoken-input safety amplification specifically)
- [[evalsafetygap-hybrid-survey-and-conceptual-framework-for-llm-evaluation-safety-failures-2606.30219]] — EvalSafetyGap survey on LLM safety failures (orthogonal — text LLM safety failures; RedVox addresses speech/audio modality safety gaps)
- [[interleaved-speech-language-models-latently-work-in-text-2606.22473]] — Interleaved speech-language models (related — both address speech model capabilities, but Interleaved addresses generation; RedVox addresses safety/fairness benchmarking)
- [[governance-decay-how-context-compaction-silently-erases-safety-constraints-in-long-horizon-llm-agents-2606.22528]] — Governance decay erodes safety constraints (orthogonal — safety in long-horizon text agents; RedVox addresses speech model safety across languages)
