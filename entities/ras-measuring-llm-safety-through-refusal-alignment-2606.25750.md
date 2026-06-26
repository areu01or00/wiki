---
title: "RAS: Measuring LLM Safety Through Refusal Alignment"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [safety, llm-evaluation, refusal-alignment, measurement, cs.CL]
sources: ["https://arxiv.org/abs/2606.25750"]
---

# RAS: Measuring LLM Safety Through Refusal Alignment

## Overview
Refusal Alignment Score (RAS) — a measurement paradigm that evaluates LLM safety by quantifying how closely the model's *internal refusal representation* aligns with its *external refusal behavior*, decoupling safety evaluation from expensive output-level judging. Argues that output-level safety evaluation is expensive, judge-sensitive, and tied to fixed safety taxonomies, while refusal-alignment provides a model-internal, judge-free, taxonomy-agnostic safety signal — RAS directly correlates with downstream safety outcomes while being significantly cheaper to compute than output-level evaluation pipelines.

## Key Facts
- **Authors**: Huang, Chang-Chieh; Chen, Yan-Lun; Yu, Chia-Mu; Lee, Wei-Bin
- **Year**: 2026
- **arXiv**: [2606.25750](https://arxiv.org/abs/2606.25750)
- **Submitted**: 2026-06-24

## Key Contributions
- Introduces *Refusal Alignment Score (RAS)* — measures safety by the alignment between internal refusal representations and external refusal behavior, decoupling safety evaluation from output-level judging
- Argues output-level safety evaluation is *expensive*, *judge-sensitive*, and *tied to fixed safety taxonomies* — RAS addresses all three by being model-internal and taxonomy-agnostic
- Direct correlation with downstream safety outcomes at significantly lower evaluation cost than output-judging pipelines
- Surfaces *refusal-representation-alignment* as the load-bearing primitive for cheap scalable safety measurement in the deployment regime where output-judging is structurally too expensive
- Complements the mechanistic-geometry-of-refusal work (Run 39) by providing a *measurement* angle on the same refusal-direction concept — together they bracket the refusal-discipline surface between *linear-feature mechanism* (Geometry of Refusal) and *measurement score* (RAS)

## Related Papers
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Geometry of Refusal (06-21) — mechanistic linear-feature view of refusal, sibling refusal-mechanism surface — together they bracket the refusal-discipline surface between *linear-feature mechanism* (Geometry of Refusal) and *refusal-alignment measurement score* (RAS)
- [[safety-paradox-how-enhanced-safety-awareness-leaves-llms-vulnerable-to-posterior-attack-2606.05614]] — Safety Paradox Posterior Attack (06-04) — exploits safety-awareness as a side channel, sibling safety-evaluation surface — together they bracket the safety-evaluation surface between *exploit-via-safety-awareness* (Safety Paradox) and *measure-via-refusal-alignment* (RAS)
- [[do-thinking-tokens-help-with-safety-2606.25013]] — Do Thinking Tokens Help with Safety (06-23) — reasoning-time safety audit, sibling safety-mechanism surface — together they bracket the safety-mechanism surface between *reasoning-time audit* (Thinking-Tokens) and *refusal-representation measurement* (RAS)
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Detecting Jailbreaks from Entropy Dynamics (06-24) — jailbreak-detection via internal entropy, sibling safety-detection surface — together they bracket the safety-detection surface between *entropy-dynamics detection* (Detection paper) and *refusal-alignment detection* (RAS)