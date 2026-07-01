---
title: "Theoretical Limits of Language Model Alignment"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [alignment, theory, safety-mechanisms, RLHF]
sources: ["https://arxiv.org/abs/2605.07105"]
---

# Theoretical Limits of Language Model Alignment

## Overview
Theoretical analysis establishing fundamental limits of LLM alignment — proving that ensembling mitigates reward hacking under specific conditions, and characterizing the tradeoff between alignment fidelity and model capability preservation. The work formalizes when alignment succeeds, when it degrades capabilities, and when reward hacking is theoretically unavoidable.

## Key Facts
- **Authors**: Paes, Lucas Monteiro; Mackraz, Natalie; Theobald, Barry-John + 1
- **Year**: 2026
- **arXiv**: [2605.07105](https://arxiv.org/abs/2605.07105)

## Key Contributions
- First formal bound connecting reward function distance to alignment degradation
- Proof that ensembling structurally mitigates reward hacking under the base model distance condition
- Characterization of when alignment and capability preservation are fundamentally at odds
- First theoretical-limits-of-alignment paper in the wiki

## Related Papers
- *Detecting Proxy Gaming in RL and LLM Alignment via Evaluator Stress Tests* (2507.05619) — Complementary empirical work on evaluator gaming detection; Theoretical Limits provides the formal foundation for why such detection is hard
