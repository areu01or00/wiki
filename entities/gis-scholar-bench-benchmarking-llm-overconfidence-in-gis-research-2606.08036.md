---
title: "GIScholarBench: Benchmarking LLM Overconfidence in GIS Research"
created: 2026-07-02
updated: 2026-07-02
type: entity
domain-specific-benchmark
tags: [benchmarking, calibration, domain-specific, GIS]
sources: ["https://arxiv.org/abs/2606.08036"]
---

# GIScholarBench: Benchmarking LLM Overconfidence in GIS Research

## Overview
LLMs deployed in academic research workflows require high factual precision, exposing a systematic overconfidence weakness. GIScholarBench evaluates LLM overconfidence in Geographic Information Science research tasks — a domain requiring precise spatial factual knowledge — and finds that overconfidence manifests differently across task forms: factual overgeneration in retrieval, unreliable citation expansion, and overconfidence in output completeness during ideation.

## Key Facts
- **Authors**: Li, Zongrng; Yang, Mingzheng; Zou, Lei + 8
- **Year**: 2026
- **arXiv**: [2606.08036](https://arxiv.org/abs/2606.08036)

## Key Contributions
- Introduces GIScholarBench: a domain-specific benchmark for LLM overconfidence in GIS (Geographic Information Science) research tasks
- Documents three distinct overconfidence failure modes: (1) factual overgeneration in retrieval, (2) unreliable citation expansion, (3) overconfidence in output completeness
- Finds overconfidence is task-invariant (systematic) but form-varying across task types — consistent with general calibration findings but domain-specified
- Establishes that domain-specific knowledge boundaries (e.g., geospatial precision) are particularly prone to confident hallucination

## Related Papers
- [[calibrating-overconfidence-without-sacrificing-confidence-probe-conditioned-head-intervention-for-llms-2606.09876]] — Probe-conditioned head intervention for overconfidence (companion: PCHI addresses the overconfidence failure mode that GIScholarBench diagnoses)
- [[calibrating-the-evaluator-does-probability-calibration-mitigate-preference-coupling-in-llm-agent-feedback-loops-2606.31371]] — Calibrating the evaluator (sibling: both address calibration in research/scholarly workflows)
- [[just-how-sure-are-you-improving-verbalized-uncertainty-calibration-in-llms-2606.27023]] — Verbalized uncertainty calibration (orthogonal approach to the same overconfidence problem)
