---
title: "LLM Reasoning Is Latent, Not the Chain of Thought"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, latent-representation, theory]
sources: ["https://arxiv.org/abs/2604.15726"]
---

# LLM Reasoning Is Latent, Not the Chain of Thought

## Overview
A position paper arguing that LLM reasoning should be studied as latent-state trajectory formation rather than as faithful surface chain-of-thought (CoT). The authors formalize three competing hypotheses — H1 (latent-state trajectories mediate reasoning), H2 (surface CoT mediates reasoning), and H0 (gains are from generic serial compute) — and evaluate recent empirical, mechanistic, and survey evidence, finding strongest support for H1 as the default working hypothesis.

## Key Facts
- **Authors**: Wenshuo Wang (single author)
- **Year**: 2026
- **arXiv**: [2604.15726](https://arxiv.org/abs/2604.15726)
- **Submitted**: 17 Apr 2026

## Key Contributions
- Formalizes three hypotheses for what mediates LLM reasoning: H1 (latent-state trajectories), H2 (surface CoT), H0 (generic serial compute)
- Uses compute-audited worked exemplars that factorize surface traces, latent interventions, and matched budget expansions
- Finds current evidence most strongly supports H1 (latent-state dynamics) over H2 (surface CoT)
- Recommends the field should (1) treat latent-state dynamics as the default object of study and (2) evaluate reasoning with designs that disentangle surface traces, latent states, and serial compute
- Position held: surface CoT is epiphenomenal — what matters is what happens in transformer latent space, not the textual reasoning trace

## Related Papers
- [[a-latent-computational-mode-in-large-language-models-2601.08058]] — Related latent computational mode framing for LLM reasoning
- [[formalizing-latent-thoughts-four-axioms-of-thought-representation-in-llms-2606.27378]] — Axiomatic formalization of latent thought representations
- [[between-the-layers-lies-the-truth-uncertainty-estimation-via-intra-layer-local-information-scores-2603.22299]] — Intra-layer uncertainty signals as a probe into latent reasoning states
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Test-time compute allocation for reasoning LLMs
