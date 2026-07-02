---
title: "The Galaxy's Guide to the Tokenizer: A Benchmark for Scientific Foundation Models"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [tokenization, scientific-AI, benchmark, representation-geometry]
sources: ["https://arxiv.org/abs/2606.25610"]
---

# The Galaxy's Guide to the Tokenizer: A Benchmark for Scientific Foundation Models

## Overview
Tokenization is central to adapting scientific data for transformer-based foundation models, yet its impact on learned representations remains poorly understood. This paper compares four tokenization strategies — Affine, AIM, JetFormer, and VQ-VAE — within a unified transformer framework for astronomical imaging using 640,000 galaxy images from the DESI Legacy Survey. The benchmark isolates tokenizer design as a critical, underexplored axis of scientific foundation model quality.

## Key Facts
- **Authors**: Sanjaripour, Sogol; Smith, Michael J.; Pérez-Carrasco, Manuel + 3 others
- **Year**: 2026
- **arXiv**: [2606.25610](https://arxiv.org/abs/2606.25610)

## Key Contributions
- Introduces a controlled benchmark isolating tokenizer choice as a determinant of downstream scientific representations in astronomy
- Shows that tokenizer design materially affects learned representation geometry — not just token count or compression ratio
- First systematic comparison of discrete (VQ-VAE) vs continuous (Affine, AIM) tokenization strategies for scientific imaging at scale

## Related Papers
- [[mingram-a-minimalist-unigram-tokenizer-with-high-compression-and-competitive-morphological-fidelity-2606.27019]] —Tokenizer efficiency and morphological fidelity in language models
