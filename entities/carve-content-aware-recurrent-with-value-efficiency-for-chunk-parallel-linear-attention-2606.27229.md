---
title: "CARVE: Content-Aware Recurrent with Value Efficiency for Chunk-Parallel Linear Attention"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [architecture, recurrent-model, linear-attention, llm]
sources: ["https://arxiv.org/abs/2606.27229"]
---

# CARVE: Content-Aware Recurrent with Value Efficiency for Chunk-Parallel Linear Attention

## Overview
CARVE resolves three coupled defects in delta-rule recurrent architectures (GDN-2) through a single principle: erase only on the key axis. The state-of-the-art delta-rule recurrent model decides what to erase without consulting what is stored — the gate sees only the arriving token, not the memory it is about to modify. CARVE reuses the recurrent output tensor as a free content signal for the erase gate, and replaces the per-value write-gate projection with a single scalar per head.

## Key Facts
- **Authors**: (from arxiv abstract extraction — needs author field)
- **Year**: 2026
- **arXiv**: [2606.27229](https://arxiv.org/abs/2606.27229)

## Key Contributions
- Resolves three coupled defects in GDN-2 delta-rule architecture through content-aware key-axis erase gating
- Proves necessary and sufficient condition for WY-form triangular chunk solver validity
- Achieves WikiText perplexity 15.72 (4.5-sigma vs. GDN-2); leads all recurrent baselines on nine reasoning benchmarks
- Sets state-of-the art on all RULER retrieval probes at 0.4% throughput overhead, 13% lower peak memory, 19% fewer parameters
- Six formal theorems covering memory capacity, Lyapunov stability, gradient flow, expressivity separation, Pareto-optimal chunk size, and hybrid optimality

## Related Papers
- [[emergent-concepts]] — Parent topic node for emergent LLM research
