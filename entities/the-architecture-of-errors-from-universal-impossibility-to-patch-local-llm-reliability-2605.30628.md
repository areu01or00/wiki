---
title: "The Architecture of Errors: From Universal Impossibility to Patch-Local LLM Reliability"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reliability, failure-modes, taxonomy, impossibility-theorem, patch-local]
sources: ["https://arxiv.org/abs/2605.30628"]
---

# The Architecture of Errors: From Universal Impossibility to Patch-Local LLM Reliability

## Overview
Formalizes the transition from universal LLM reliability (impossible) to patch-local reliability (achievable under catalogue-saturation), with two propositions and one corollary separating the worst-case-mode negative result from the patch-local positive result. Distinguishes L1-L4 levels of failure objects (events → modes → tail-population → patch catalogue) to anchor the discussion of intervention-coverage vs mode-discovery.

## Key Facts
- **Authors**: Mikhail L. Arbuzov, Lee Mosbacker, Sisong Bei, Ziwei Dong, Dmitri Kalaev, Alexey Shvets
- **Year**: 2026
- **arXiv**: [2605.30628](https://arxiv.org/abs/2605.30628)
- **Submitted**: 28 May 2026
- **Subjects**: cs.CL, cs.AI, cs.LG
- **Pages**: 25

## Key Contributions
- **Proposition 1 (worst-case-mode negative result)**: no finite intervention dictionary covers every distinguishable failure mode of an unbounded domain — universal reliability is not a finite-library problem.
- **Corollary 1 (inverse-discovery implication)**: the logarithmic upper bound on mode discovery cannot accommodate linearly more distinct tail modes without exponentially more observed hard-failure events.
- **Proposition 2 (patch-local positive result)**: under log active-mode exposure and head-heavy coverage, a sufficient per-hard-decision intervention budget grows polylogarithmically in sequence length and becomes domain-constant once the patch catalogue saturates.
- **L1-L4 ontological stratification** of error objects: failure events, modes, tail-population, patch catalogue — keeping these distinct is the load-bearing primitive for the rest of the framework.
- **Patch-local reframing**: deployed systems operate inside operationally bounded patches (legal review, medical RAG, code repair, customer-support agents, contract extraction) where empirical failures are sparse, repetitive, and concentrated in a small recurring catalogue — reliability becomes a catalogue-discovery and intervention-coverage problem rather than an exponential token-length problem.

## Related Papers
- [[llm-based-scientific-peer-review-methods-benchmarks-reliability-challenges-2606.25057]] — Sibling reliability-challenges taxonomy from Run 73 meta-probe
- [[uncertainty-quantification-for-hallucination-detection-in-llms-2510.12040]] — Failure-mode detection via uncertainty quantification (Run 63 pick)
- [[hallucination-in-world-models-is-predictable-and-preventable-2606.27326]] — Failure-mode taxonomy for world models (Run 72 pick)
