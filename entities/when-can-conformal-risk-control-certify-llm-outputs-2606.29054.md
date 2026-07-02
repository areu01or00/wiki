---
title: "When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [calibration, safety, formal-methods, llm]
sources: ["https://arxiv.org/abs/2606.29054"]
---

# When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation

## Overview
This paper addresses the critical gap between LLM capability and formal reliability guarantees in structured generation tasks (NER, JSON extraction, QA, classification). The authors characterize when conformal risk control (CRC) can and cannot provide PAC-style coverage guarantees for LLM outputs, identifying fundamental impossibility results and adaptive remedies. Standard heuristic abstention policies are shown to miss user-specified risk targets by 7.5-12.5%.

## Key Facts
- **Authors**: Kotte, Varun
- **Year**: 2026
- **arXiv**: [2606.29054](https://arxiv.org/abs/2606.29054)

## Key Contributions
- First formal characterization of when conformal risk control can certify LLM output reliability
- Identifies impossibility conditions: CRC fails when LLM calibration is simultaneously overconfident AND the task loss is non-decomposable
- Proposes adaptive CRC variants that recover coverage under distribution shift
- Demonstrates 7.5-12.5% gap between heuristic abstention and formally guaranteed risk bounds
- Bridges conformal prediction theory with LLM deployment constraints

## Related Papers
- [[calibration-collapse-under-sycophancy-fine-tuning-reward-hacking-2604.10585]] — Documents how reward hacking and sycophancy produce the overconfident calibration that makes standard CRC impossible
- [[calibrating-the-evaluator-does-probability-calibration-mitigate-preference-coupling-in-llm-agent-feedback-loops-2606.31371]] — Companion work on calibration in agentic feedback loops where this paper's impossibility results apply most acutely
- [[calibration-is-not-control-llm-agent-oversight-needs-intervention-2606.21399]] — Foundational context: calibration is necessary but insufficient for LLM agent control
