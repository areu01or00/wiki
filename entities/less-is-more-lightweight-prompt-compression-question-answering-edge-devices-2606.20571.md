---
title: "Less is More: Lightweight Prompt Compression for Question Answering Applications on Edge Devices"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [prompt-compression, rag, edge-ai, inference-efficiency, retrieval-augmented-generation]
sources: ["https://arxiv.org/abs/2606.20571"]
---

# Less is More: Lightweight Prompt Compression for Question Answering Applications on Edge Devices

## Overview
In agent-driven QA applications with RAG, the retrieved context often contains substantial redundant information due to noisy retrieval results and document-level granularity. Existing prompt compression methods rely on auxiliary small language models (SLMs) to estimate context importance, introducing significant memory and computational overhead that prevents edge deployment. CORE (Compression via Orthogonal Residual and Clue Estimation) is a two-stage sentence-level prompt compression method requiring no SLM: the first stage constructs answer and clue sets via NER and semantic matching; the second stage refines via orthogonal residual retrieval and spatial proximity filtering. On NVIDIA Jetson AGX Orin and Huawei Nova smartphone, CORE improves accuracy by ≥30.19% within a 2000-token budget while reducing memory by ≥50.47%, achieving ≥1.94× speedup and 95.74% energy reduction vs LLMLingua2.

## Key Facts
- **Authors**: Zihuai Xu, Ruofei Hou, Yang Xu, Hongli Xu, Yunming Liao, Ying Zhu
- **Year**: 2026
- **arXiv**: [2606.20571](https://arxiv.org/abs/2606.20571)

## Key Contributions
- **CORE method**: two-stage sentence-level prompt compression (answer set via NER + clue set via semantic matching; orthogonal residual retrieval refinement + spatial proximity filtering) — no auxiliary SLM required
- **Edge deployment**: NVIDIA Jetson AGX Orin edge device and Huawei Nova smartphone
- **Performance**: ≥30.19% accuracy improvement, ≥50.47% memory reduction, ≥1.94× speedup on edge device; 95.74% energy reduction vs LLMLingua2 on smartphone

## Related Papers
- [[hakari-bench-a-lightweight-benchmark-for-comparing-retrieval-architectures-and-efficiency-settings-under-unified-conditions-2606.22778]] — Retrieval architecture benchmarking (orthogonal: HakariBench evaluates retrieval architectures; CORE addresses prompt compression for retrieval noise)
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — Long-context retrieval and agentic memory (orthogonal: EvoEmbedding targets long-context retrieval representations; CORE targets lightweight compression for edge RAG)
