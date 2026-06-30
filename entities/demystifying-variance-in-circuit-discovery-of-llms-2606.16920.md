---
title: "Demystifying Variance in Circuit Discovery of LLMs"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [mechanistic-interpretability, llm, circuit-discovery]
sources: ["https://arxiv.org/abs/2606.16920"]
---

# Demystifying Variance in Circuit Discovery of LLMs

## Overview
Circuit discovery is a key technique in mechanistic interpretability to pinpoint the model components that are crucial for performing a given task. This paper analyzes variance in circuit discovery methods, showing that the current state-of-the-art method (EAP-IG) suffers from substantial variability across runs while maintaining good (un)faithfulness metrics.

## Key Facts
- **arXiv**: [2606.16920](https://arxiv.org/abs/2606.16920)
- **Date**: 2026-06

## Key Contributions
- Systematic analysis of variance in circuit discovery methods for LLMs
- Demonstrates that EAP-IG, while state-of-the-art on faithfulness metrics, exhibits substantial run-to-run variability
- Proposes understanding of why circuit discovery produces inconsistent results across different random seeds or ablations

## Related Papers
- [[emergent-concepts]] — Parent chain for emergent concept discovery
