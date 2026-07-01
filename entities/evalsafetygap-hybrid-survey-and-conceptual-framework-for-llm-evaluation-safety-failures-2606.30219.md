---
title: "EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [evaluation, safety, alignment, benchmark]
sources: ["https://arxiv.org/abs/2606.30219"]
---

# EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures

## Overview
This paper identifies a fundamental measurement problem at the intersection of LLM evaluation and AI safety: benchmark scores, reward-model signals, and safety metrics can improve while the latent properties they represent remain unverified. The authors synthesize 2018–2026 evidence across eight streams—benchmark validity, dynamic evaluation, LLM-as-judge reliability, safety evaluation, jailbreak/refusal robustness, reward hacking, mechanistic interpretability, and governance—and introduce the EvalSafetyGap as an organizing hypothesis. A ten-model audit reveals the association between capability and adversarial robustness is statistically indeterminate, and the open/closed safety gap is driven mainly by governance rather than behavioral robustness.

## Key Facts
- **arXiv**: [2606.30219](https://arxiv.org/abs/2606.30219)
- **Theme**: LLM evaluation / AI safety measurement / Goodhart's Law / benchmark validity / alignment

## Key Contributions
- EvalSafetyGap organizing hypothesis: compares evaluation-side vs. alignment-side proxy failures under optimization pressure
- Instability Decomposition and Alignment Trilemma as diagnostic tools
- Eight evidence streams synthesis covering 2018–2026 evaluation-safety literature
- Ten-model audit showing capability/robustness correlation is statistically indeterminate (Pearson r=+0.232, p=0.520)
- Evidence that the apparent safety gap is governance/disclosure-driven rather than behavioral

## Related Papers
- [[be-your-own-red-teamer-safety-alignment-via-self-play-and-reflective-experience-replay-2601.10589]] — Self-play red-teaming for safety alignment, orthogonal to eval-safety measurement gap framing
- [[ask-dont-judge-binary-questions-for-interpretable-llm-evaluation-and-self-improvement-2606.27226]] — Interpretable binary-question eval methodology, orthogonal measurement approach
