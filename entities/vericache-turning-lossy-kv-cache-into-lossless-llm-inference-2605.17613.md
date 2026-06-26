---
title: "VeriCache: Turning Lossy KV Cache into Lossless LLM Inference"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [inference, kv-cache, compression, systems, long-context, llm, quantization]
sources: ["https://arxiv.org/abs/2605.17613"]
---

# VeriCache: Turning Lossy KV Cache into Lossless LLM Inference

## Overview
This paper addresses a critical failure mode of KV-cache compression methods (token dropping, quantization) for LLM serving: while accuracy degradation is minimal for short outputs, the outputs increasingly diverge from full-KV-cache outputs as more tokens are decoded, leading to catastrophic failures in code generation and tool calling. VeriCache is presented as the first inference framework that guarantees the same output as full-KV-cache decoding while preserving the high throughput of lossy compression — turning lossy KV-cache compression into lossless inference through a draft-and-verify mechanism that uses the lossy cache for fast drafting and the full cache for verification.

## Key Facts
- **Authors**: Jiayi Yao, Samuel Shen, Kuntai Du, Shaoting Feng, Dongjoo Seo, Rui Zhang, Yuyang Huang, et al.
- **Year**: 2026
- **arXiv**: [2605.17613](https://arxiv.org/abs/2605.17613) ([pdf](https://arxiv.org/pdf/2605.17613))
- **Date published**: 2026-05-17
- **Subjects**: cs.LG, cs.DC, cs.CL
- **Methodology**: Draft-and-verify inference framework that uses a lossy compressed KV cache for fast token drafting and a full KV cache for verification, supporting a range of lossy compression techniques (quantization and token dropping); verified to produce identical outputs to full-KV-cache decoding.

## Key Contributions
- **Identifies catastrophic-failure regime of lossy KV-cache compression**: accuracy degradation is non-uniform — minimal for short outputs but divergent for long-horizon tasks (code generation, tool calling) where it manifests as catastrophic failures, not graceful degradation.
- **Draft-and-verify mechanism for lossless inference**: rather than rejecting lossy compression, the framework exploits its throughput advantage for drafting and uses the full cache only for verification, achieving lossless output at lossy-compression throughput.
- **Compression-agnostic design**: works with both quantization-based and token-dropping lossy KV-cache methods, making it a general-purpose wrapper for existing compression techniques rather than a single-method optimization.
- **Targets the deployment-bottleneck regime**: the long-context inference problem is the most acute deployment bottleneck for modern LLMs (agentic tool-use, code generation), and VeriCache directly addresses the divergence-failure mode that prevents lossy methods from being deployed in production.

## Related Papers
- [[emergent-concepts]] — parent meta-page that catalogued this paper as part of the inference-systems / KV-cache-management / lossless-recovery theme.
- [[efficientrollout-system-aware-self-speculative-decoding-for-rl-rollouts-2606.18967]] — sibling inference-systems paper from this run; both target inference latency but VeriCache addresses serving-time lossless recovery while EfficientRollout addresses RL-rollout-time latency.
- [[jetspec-breaking-the-scaling-ceiling-of-speculative-decoding-with-parallel-tree-2606.18394]] — sibling inference-efficiency paper from Run 54; both use speculative/draft-verify-style mechanisms but JetSpec drafts from a parallel tree while VeriCache verifies against the full KV cache.
- [[discretizing-reward-models-2606.21795]] — sibling paper from this run focused on reward-model quality in RL post-training; orthogonal axis (RL training vs inference serving) but both address failure modes in modern LLM pipelines that emerge only at scale.