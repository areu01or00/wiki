---
title: "ReMMD: Realistic Multilingual Multi-Image Agentic Verification for Multimodal Misinformation Detection"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [multimodal, misinformation, agentic-verification, multilingual, cs.AI, benchmark]
sources: ["https://arxiv.org/abs/2606.24112"]
---

# ReMMD: Realistic Multilingual Multi-Image Agentic Verification for Multimodal Misinformation Detection

## Overview
ReMMD is a benchmark + verifier pair for *realistic* multimodal misinformation detection: viral posts combine long multilingual narratives, several images, mixed provenance, and subtle text–image framing errors, but existing benchmarks isolate short captions, single images, binary labels, or one manipulation source. ReMMD closes that gap with **ReMMDBench** (500 samples, 2,756 images, five monolingual languages, two cross-lingual settings, three text-length tiers, multi-image posts, five-way veracity labels, eight distortion labels, evidence provenance, and rationales) and **ReMMD-Agent**, a *persistent-memory verifier* that decomposes posts into atomic points, builds a reusable evidence set, and predicts structured L1/L2/L3 outputs.

## Key Facts
- **Authors**: Dang, Chenhao; Zhu, Dantong; Yang, Jun; He, Conghui; Li, Weijia
- **Year**: 2026
- **Date**: 2026-06-23
- **arXiv**: [2606.24112](https://arxiv.org/abs/2606.24112)
- **Subjects**: Artificial Intelligence (cs.AI)

## Key Contributions
- **ReMMDBench**: a benchmark matching the *actual distribution* of viral misinformation — multi-image posts, multilingual + cross-lingual settings, three text-length tiers, five-way veracity labels, eight distortion labels, evidence provenance, and rationales (500 samples, 2,756 images in total).
- **ReMMD-Agent**: a persistent-memory verifier that decomposes posts into *atomic points*, builds a *reusable evidence set* across those points, and predicts structured L1/L2/L3 outputs — shifting the verification paradigm from end-to-end single-shot classification to compositional evidence accumulation.
- **Strong empirical performance**: across proprietary systems, open LVLMs, MMD-Agent, and T2-Agent baselines, ReMMD-Agent obtains the best five-way veracity performance, with **41.80% accuracy and 39.12% macro-F1** using GPT-5.2.
- **Cost reduction as a first-class result**: ReMMD-Agent reduces cost by **17.5%** relative to MMD-Agent and **79.9%** relative to T2-Agent — the persistent-memory evidence set amortizes search across the post's atomic points rather than re-querying per point.
- Companion project page at `dang-ai.github.io/ReMMD` for benchmark and verifier access.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered; complements the recent Agents' Last Exam and AGORA benchmark entries on this page by *also* framing verification as an agentic, evidence-accumulation problem — but in the multimodal-multilingual misinformation setting rather than workplace document reasoning or general cross-domain exam tasks.
