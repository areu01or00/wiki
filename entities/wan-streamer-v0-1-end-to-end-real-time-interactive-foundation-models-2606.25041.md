---
title: "Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [streaming, multimodal, interactive-foundation-model, full-duplex, audio-visual, block-causal-attention, real-time-inference]
sources: ["https://arxiv.org/abs/2606.25041"]
---

# Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models

## Overview
Cascaded real-time interactive systems today are stitched together from separately-trained VAD, ASR, language, TTS, audio-driven animation, and video-generation modules — each adding pipeline latency, cross-module error accumulation, and turn-management handshakes that together prevent sub-second full-duplex audio-visual interaction. Wan-Streamer replaces this cascaded stack with a single Transformer trained end-to-end for native streaming: language, audio, and video are interleaved into one token sequence of mixed visual/audio/text inputs and outputs, coordinated by block-causal attention for incremental streaming, with causal encoders/decoders and low-latency multimodal token scheduling that supports 160 ms streaming units at 25 fps and ≈200 ms model-side response latency. The result is a unified interactive foundation model that learns perception, reasoning, generation, response timing, turn management, and cross-modal synchronization jointly, achieving ≈550 ms total interaction latency under 350 ms bidirectional network latency and positioning the architecture as a stepping stone toward sub-second duplex audio-visual communication.

## Key Facts
- **Authors**: Huang, Lianghua; Wu, Zhifan; Wang, Wei; Shi, Yupeng; Feng, Mengyang; He, Junjie; Xie, Chenwei; Liu, Yu; Zhou, Jingren; Wang, Ang; Zhang, Bang; Ai, Baole; Liang, Chen; Yu, Cheng; Zhong, Chongyang; Qi, Jinwei; Zhu, Kai; Li, Pandeng; Zhang, Peng; Zhang, Wenyuan; Cheng, Xinhua; Huang, Yitong; Zheng, Yun; Bi, Zoubin; et al.
- **Year**: 2026
- **arXiv**: [2606.25041](https://arxiv.org/abs/2606.25041)
- **Date**: 2026/06/23
- **Streaming unit**: 160 ms at 25 fps
- **Model-side latency**: ≈200 ms
- **Total interaction latency**: ≈550 ms (with 350 ms bidirectional network)

## Key Contributions
- **Native end-to-end streaming interaction** — replaces cascaded VAD+ASR+LLM+TTS+animation+video pipelines with a single Transformer that models language, audio, and video jointly as interleaved input/output tokens, eliminating pipeline latency and cross-module error accumulation as structural artifacts rather than engineering nuisances.
- **Block-causal attention for full-duplex coordination** — rethinks attention from the standard causal mask to a block-causal pattern that supports incremental streaming across modalities, allowing past context to inform new outputs without re-encoding or re-cascading through intermediate modules.
- **Streamability-redesigned stack** — causal encoders, causal decoders, block-causal attention, and low-latency multimodal token scheduling co-designed so that streaming units as short as 160 ms at 25 fps remain coherent — surfacing *streamability* as a first-class architectural constraint rather than a downstream optimization.
- **Joint learning of perception/reasoning/generation/timing/turn-management/synchronization** — a methodological contribution to interactive multimodal foundation models: response timing, turn management, and cross-modal synchronization are learned rather than rule-engineered, blurring the line between model and dialogue manager.
- **Sub-second duplex audio-visual interaction achieved at foundation-model scale** — the ≈200 ms model-side + ≈550 ms total interaction latency is a quantitative milestone for unified multimodal interactive systems, validating that sub-second full-duplex interaction does not require modular decomposition.

## Related Papers
- [[emergent-concepts]] — Parent thematic cluster for emergent-concept discoveries in this wiki
- [[causal-rcm-a-unified-teacher-forcing-and-self-forcing-open-recipe-for-autoregressive-diffusion-distillation-in-streaming-video-generation-and-interactive-world-models-2606.25473]] — Causal-rCM extends rCM (a recent diffusion-distillation framework) into the streaming-causal-attention regime required for interactive world models — the closest sibling on streaming video generation
- [[world-action-models-a-survey-2606.20781]] — WAM survey decomposing predictive-action models; Wan-Streamer's joint perception/reasoning/generation framing is the architectural unification that WAM's design-axis decomposition points toward
- [[domain-shuttle-freeform-open-domain-subject-driven-text-to-video-2606.26058]] — DomainShuttle addresses open-domain subject-driven T2V generation, complementary to Wan-Streamer's streaming interactive generation axis