---
title: "From Text to Talk: Audio-Language Model Needs Non-Autoregressive Joint Training"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [audio-language-model, non-autoregressive, multimodal-llm, absorbing-diffusion, modality-aware-attention, speech-to-speech]
sources: ["https://arxiv.org/abs/2509.20072"]
---

# From Text to Talk: Audio-Language Model Needs Non-Autoregressive Joint Training

## Overview
Proposes Text-to-Talk (TtT), a unified audio-text framework that integrates autoregressive text generation with non-autoregressive audio diffusion in a single Transformer. By leveraging the any-order AR property of absorbing discrete diffusion, TtT provides a unified training objective for text and audio, with modality-aware attention enforcing causal decoding for text and bidirectional modeling within audio spans.

## Key Facts
- **Authors**: Liu, Tianqiao; Li, Xueyi; Wang, Hao; Li, Haoxuan; Chen, Zhichao; Luo, Weiqi; Liu, Zitao
- **Year**: 2025
- **arXiv**: [2509.20072](https://arxiv.org/abs/2509.20072)
- **Category**: cs.CL, cs.SD, cs.AI, eess.AS
- **Date**: 2025-09-24

## Key Contributions
- Identifies a structural asymmetry in multimodal training: *text depends on target-target relations* (autoregressive) whereas *audio depends mainly on source-target relations* (non-autoregressive) — surfacing *modality-relation-asymmetry-as-load-bearing-primitive* where the load-bearing contribution is recognizing that the AR-vs-NAR choice is *modality-dependent* not architectural.
- Proposes *Text-to-Talk (TtT)*, a unified audio-text framework that integrates AR text generation with NAR audio diffusion in a *single Transformer* — surfacing *single-transformer-multimodal-unification primitive* as the load-bearing *architectural-unification primitive* for speech-to-speech conversational systems.
- Leverages the *any-order AR property of absorbing discrete diffusion* to provide a unified training objective for text and audio — surfacing *absorbing-discrete-diffusion-as-unifying-formalism primitive* as the load-bearing *training-objective-unification primitive* that bridges AR and NAR paradigms.
- Designs a *modality-aware attention mechanism* that enforces *causal decoding for text* while allowing *bidirectional modeling within audio spans* — surfacing *modality-aware-attention-as-decoupling-primitive* where the load-bearing primitive is per-position causal-vs-bidirectional selection based on modality.
- Introduces *three training strategies* that reduce train-test discrepancies — surfacing *train-test-discrepancy-reduction-as-practical-primitive* for hybrid generation paradigms.
- Employs *block-wise diffusion* during inference to synthesize audio in parallel while flexibly handling variable-length outputs — surfacing *block-wise-diffusion-as-parallel-inference-primitive* for NAR audio with length flexibility.
- Provides *comprehensive experiments on Audio-QA, ASR, AA* benchmarks — surfacing *benchmark-coverage-as-validation-primitive* for hybrid multimodal systems.

## Related Papers
- [[look-light-think-heavy-what-multimodal-chain-of-thought-reasoning-can-and-cannot-do-2606.22565]] — Sibling multimodal-CoT work — Look-Light-Think-Heavy evaluates *multimodal chain-of-thought reasoning*, TtT provides *the unified AR+NAR training paradigm* for multimodal models that such reasoning operates within — together they bracket the multimodal-LLM surface between *multimodal-CoT reasoning evaluation* (Look-Light-Think-Heavy) and *hybrid audio+text training* (TtT).
- [[causal-rcm-a-unified-teacher-forcing-and-self-forcing-open-recipe-for-autoregressive-diffusion-distillation-in-streaming-video-generation-and-interactive-world-models-2606.25473]] — Sibling autoregressive-diffusion-distillation work — Causal-rCM unifies *teacher-forcing and self-forcing recipes for autoregressive diffusion distillation*, TtT provides *the AR+NAR hybrid training paradigm* such recipes target — together they bracket the AR+NAR-diffusion surface between *unified training recipes for AR-diffusion* (Causal-rCM) and *hybrid AR-text + NAR-audio training* (TtT).
- [[shuttermuse-capture-time-photography-guidance-with-mllms-2606.25763]] — Sibling MLLM-application work — ShutterMuse applies *MLLMs* for capture-time photography guidance, TtT provides *the AR+NAR hybrid training paradigm* for multimodal conversational systems — together they bracket the multimodal-LLM surface between *photography-guidance application* (ShutterMuse) and *hybrid audio+text training* (TtT).
- [[a-latent-computational-mode-in-large-language-models-2601.08058]] — Sibling Run 61 SAE-reasoning work — Latent-Computational-Mode identifies *latent-reasoning features* with single-feature causal steering, TtT provides *the AR+NAR hybrid training paradigm* where such latent features can also surface in audio — together they bracket the LLM-internals surface between *single-feature-reasoning-steering* (Latent-Computational-Mode) and *hybrid-modality-training* (TtT).
- [[dart-diffusion-inspired-speculative-decoding-for-fast-llm-inference-2601.19278]] — Sibling Run 61 diffusion-parallel-decoding work — DART uses *diffusion-inspired parallel logit prediction* for fast inference, TtT uses *block-wise diffusion* for parallel audio synthesis — together they bracket the diffusion-decoding surface between *parallel-text-decoding* (DART) and *parallel-audio-synthesis* (TtT).
- [[emergent-concepts]] (parent wiki page) entries on this page by surfacing *modality-relation-asymmetry-as-load-bearing-primitive* as the structurally correct primitive for multimodal training where the failure mode of *forcing AR-on-audio or NAR-on-text* is structurally invisible to single-modality evaluations but becomes tractable when text-vs-audio relation structure (target-target vs source-target) is recognized and *modality-aware attention* with *absorbing-discrete-diffusion* is used to enforce causal decoding for text and bidirectional modeling within audio spans — bridging AR and NAR paradigms under a single unified training objective with parallel block-wise inference.
