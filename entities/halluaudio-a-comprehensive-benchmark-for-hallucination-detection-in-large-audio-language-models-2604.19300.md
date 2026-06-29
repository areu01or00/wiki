---
title: "HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [hallucination, audio-language-model, benchmark, multimodal, modality-specific]
sources: ["https://arxiv.org/abs/2604.19300"]
---

# HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models

## Overview
First large-scale audio-domain hallucination benchmark for Large Audio-Language Models (LALMs), spanning speech, environmental sound, and music with 5K+ human-verified QA pairs across binary judgments, multi-choice reasoning, attribute verification, and open-ended QA. Goes beyond accuracy with a four-dimensional evaluation protocol (hallucination rate, yes/no bias, error-type analysis, refusal rate) revealing systemic deficiencies in acoustic grounding, temporal reasoning, and music attribute understanding.

## Key Facts
- **Authors**: Feiyu Zhao, Yiming Chen, Wenhuan Lu, Daipeng Zhang, Xianghu Yue, Jianguo Wei
- **Year**: 2026
- **arXiv**: [2604.19300](https://arxiv.org/abs/2604.19300)
- **Submitted**: 21 Apr 2026
- **Venue**: ACL 2026 (accepted)
- **Subjects**: cs.SD, cs.AI

## Key Contributions
- **Modality-first hallucination taxonomy** for audio: speech-grounded, environmental-sound-grounded, music-attribute-grounded — first benchmark to systematically cover all three audio sub-modalities.
- **5K+ human-verified QA pairs** with adversarial-prompt and mixed-audio-condition design to systematically induce hallucinations.
- **Four-dimensional evaluation protocol** (hallucination rate, yes/no bias, error-type analysis, refusal rate) — extends text/vision hallucination benchmarks with audio-specific bias and refusal-rate axes.
- **First large-scale LALM comparison** across open-source and proprietary models on speech, sound, and music — surfaces significant deficiencies in acoustic grounding and temporal reasoning.

## Related Papers
- [[audio-language-model-needs-non-autoregressive-joint-training-2509.20072]] — Audio-language training paradigm (Run 64 pick, sibling audio-domain entity)
- [[uncertainty-quantification-for-hallucination-detection-in-llms-2510.12040]] — Text-domain UQ for hallucination detection (Run 63 pick)
- [[hallucination-in-world-models-is-predictable-and-preventable-2606.27326]] — Failure-mode taxonomy for world models (Run 72 pick)
