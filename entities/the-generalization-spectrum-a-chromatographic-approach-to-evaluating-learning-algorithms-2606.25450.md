---
title: "The Generalization Spectrum: A Chromatographic Approach to Evaluating Learning Algorithms"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [evaluation, generalization, learning-algorithms, per-sample]
sources: ["https://arxiv.org/abs/2606.25450"]
---

# The Generalization Spectrum: A Chromatographic Approach to Evaluating Learning Algorithms

## Overview
This paper proposes a *chromatographic* evaluation framework that decomposes an algorithm's aggregate test-set performance into a *per-sample generalization spectrum* — a continuous profile showing how learning from each individual example transfers to others. Rather than reducing learning to a single i.i.d. accuracy number, the spectrum exposes the structural generalization properties of the algorithm and surfaces failure modes hidden by aggregate metrics.

## Key Facts
- **Authors**: Zhang, Jinghan; Cheng, Zerui; Chen, Shiqi; Zhang, Ge
- **Year**: 2026
- **arXiv**: [2606.25450](https://arxiv.org/abs/2606.25450)

## Key Contributions
- Argues that traditional i.i.d. test-set evaluation reduces learning algorithms to a single aggregate score, obscuring per-sample generalization behavior.
- Introduces a *generalization spectrum* that characterizes how learning from each individual example transfers to others — akin to how chromatography separates a mixture into a continuous profile of constituents.
- Enables algorithm comparison on the *structure* of generalization (which examples transfer to which) rather than on aggregate accuracy alone.

## Related Papers
- [[emergent-concepts]] — Parent discovery chain that surfaced this paper
- [[act-as-a-real-researcher-aarri-bench-frontier-llms-agentic-research-lifecycle-2606.07462]] — Sibling on agentic-research evaluation; AARRI evaluates full research lifecycle while this paper focuses on per-sample generalization profile of underlying learning algorithms
- [[foresci-evaluating-llm-agents-for-forward-looking-ai-research-judgment-2606.00644]] — Sibling on temporally-controlled research-judgment evaluation; complementary angle on evaluation primitives for LLM-era learning systems