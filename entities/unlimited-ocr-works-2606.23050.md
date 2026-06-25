---
title: "Unlimited OCR Works"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [ocr, document-ai, attention, kv-cache, long-context, efficient-inference]
sources: ["https://arxiv.org/abs/2606.23050"]
---

# Unlimited OCR Works

## Overview
End-to-end OCR models (exemplified by DeepSeek OCR) thrust OCR back into the spotlight by using an LLM as the decoder to leverage language prior, but the LLM decoder's KV cache grows with output sequence length, making long-document transcription slow and memory-hungry. Unlimited OCR replaces all attention layers in the OCR decoder with Reference Sliding Window Attention (R-SWA), which keeps a constant KV cache throughout decoding while reducing attention compute cost. Combined with DeepSeek OCR's high encoder compression, R-SWA enables transcribing dozens of pages in a single forward pass under a standard 32K context window. R-SWA is positioned as a general parsing-attention mechanism that extends beyond OCR to ASR and translation.

## Key Facts
- **Authors**: Yin, Youyang; Liu, Huanhuan; YY, Xie; Qunyi; Liu, Chaorun; et al.
- **Year**: 2026
- **arXiv**: [2606.23050](https://arxiv.org/abs/2606.23050)
- **Date**: 2026/06/22

## Key Contributions
- **Reference Sliding Window Attention (R-SWA)** — replaces standard attention layers in the OCR decoder with a sliding-window variant that references a fixed-size cached context while processing new tokens, eliminating KV cache growth with output length. Reduces attention compute cost and keeps memory bounded across the entire decoding trajectory.
- **Constant-KV-cache long-document transcription** — combined with DeepSeek OCR's high encoder compression, R-SWA enables transcribing dozens of pages of documents in a single forward pass under the standard 32K maximum context length. No second-pass stitching or sliding-window post-processing required at the document level.
- **Human parsing working memory analogy** — frames R-SWA as emulating human parsing working memory: bounded recency-based attention rather than unbounded accumulation. The framing argues that LLM-decoder KV growth is an implementation artifact, not a fundamental parsing requirement.
- **General-purpose parsing-attention primitive** — R-SWA is not OCR-specific; the authors explicitly note applicability to ASR (long audio transcription) and translation (long-document translation) where similar KV-cache growth bottlenecks arise.
- **Open code + model weights release** — code and model weights publicly released, allowing replication and downstream use as a drop-in attention replacement.

## Related Papers
- [[emergent-concepts]] — Parent thematic cluster for emergent-concept discoveries in this wiki
- [[deli-auto-research]] — Autonomous-research themed discoveries (long-document OCR is a common bottleneck in research-assistant pipelines that ingest papers)
- [[ml-paper-writing]] — Paper-writing craft (R-SWA follows the "diagnose bottleneck → propose drop-in primitive → validate on primary + adjacent task" framing pattern documented for ML writing)