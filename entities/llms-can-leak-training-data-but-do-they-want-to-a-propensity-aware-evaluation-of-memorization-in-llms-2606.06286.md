---
title: "LLMs Can Leak Training Data But Do They Want To? A Propensity-Aware Evaluation of Memorization in LLMs"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [memorization, training-data, propensity, privacy, evaluation]
sources: ["https://arxiv.org/abs/2606.06286"]
authors: ["Barmina, Gianluca", "Schneider-Kamp, Peter", "Poech, Lukas Galke"]
year: 2026
---

# LLMs Can Leak Training Data But Do They Want To? A Propensity-Aware Evaluation of Memorization in LLMs

## Overview
Reframes LLM memorization evaluation from *capability* (can the model be forced to reproduce training data?) to *propensity* (does the model reproduce training data under ordinary non-adversarial use?). Introduces **PropMe**, a propensity-aware evaluation framework that contrasts prefix-based capability attacks with non-adversarial prompting, together with **SimpleTrace** — a deterministic tracing pipeline built on infini-gram that attributes generations to large-scale training corpora and computes verbatim, near-verbatim, and propensity-transformed memorization metrics.

## Key Facts
- **Authors**: Barmina, Gianluca; Schneider-Kamp, Peter; Poech, Lukas Galke
- **Year**: 2026
- **arXiv**: [2606.06286](https://arxiv.org/abs/2606.06286)
- **Online date**: 2026-06-04

## Key Contributions
- **Propensity vs capability distinction** — surfaces a structural gap between *what a model can leak under adversarial elicitation* and *what it does leak under ordinary use*; capability attacks elicit substantially stronger memorization signals than generic or dataset-specific prompts, while propensity scores remain low overall
- **SimpleTrace infini-gram pipeline** — deterministic attribution of model generations to large-scale training corpora across verbatim, near-verbatim, and propensity-transformed memorization metrics
- **Propensity metric transformation** — a generic transformation that, applied to existing memorization functions, yields propensity metrics without requiring new measurement primitives
- **Continual-pretraining reduces memorization** — DFM Decoder (continually pre-trained from Comma) shows reduced memorization and memorization propensity for Common Pile, empirically confirming that later training emphasizing partially different data reduces memorization capability
- **Audit implication** — memorization audits should report both capability *and* propensity; the paper encourages the community to adopt this dual reporting standard

## Related Papers
- [[emergent-concepts]] — Parent wiki page
- [[fedot-ownership-verification-leakage-tracing-watermarks-federated-ldms-2606.22875]] — Sibling memorization-leakage work (federated LDM ownership-verification watermarking); orthogonal axis (FedOT addresses *detection-and-attribution* of leakage, PropMe addresses *measurement-distinction* between capability and propensity)
- [[privacyalign-contextual-privacy-alignment-for-llm-agents-2606.21710]] — Sibling privacy-alignment work for LLM agents; complements PropMe's *memorization-as-leakage* framing with *agent-action-as-contextual-privacy* framing
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Sibling memory-system-evaluation work from the same HF-daily pool (2026-06-25); orthogonal axis (Are-We-Ready-For-An-Agent-Native-Memory-System addresses *system-level memory evaluation as data-management*, PropMe addresses *model-level memorization-evaluation as propensity* — together they bracket the *LLM-memorization-vs-system-memory* surface between model-side propensity and system-side memory-management primitives)

---
*Run 71 — Rule 38 NEGATIVE-RESULT-PROBE escape hatch (axis: training data memorization boundaries / propensity-as-memorization-willingness primitive).*
