---
title: "Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [reasoning-trace, privacy, extraction-attack, prompt-injection, cot, distillation]
sources: ["https://arxiv.org/abs/2606.00642"]
---

# Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs

## Overview

Lu, Yu-An; Tsai, Ci-Yang; Tsai, Yu-Lin; Popa, Raluca Ada; Yu, Chia-Mu observe that **deployed reasoning models routinely hide raw internal traces** from end users, exposing only summaries and final answers under the assumption that interface-level trace-hiding prevents users from obtaining the reasoning supervision signal that distillation pipelines depend on. They demonstrate that this assumption is **structurally false** — their **Reasoning Exposure Prompting (REP)** attack uses shadow-model-generated demonstrations wrapped in **auxiliary code-like formats** (e.g., pseudo-code, JSON scaffolds, function-call syntax) to elicit richer reasoning traces from victim models, substantially increasing similarity between user-visible outputs and the model's internal reasoning state across victim models, distillation regimes, and reasoning datasets. The load-bearing primitive is **reasoning-trace-as-attack-extractable-asset** — interface-level trace hiding does not constitute a security boundary because the prompting format itself can be engineered to make the model volunteer its traces.

## Key Facts
- **Authors**: Lu, Yu-An; Tsai, Ci-Yang; Tsai, Yu-Lin; Popa, Raluca Ada; Yu, Chia-Mu
- **Year**: 2026
- **Date**: 2026-05-30
- **arXiv**: [2606.00642](https://arxiv.org/abs/2606.00642)

## Key Contributions
- Articulates the **interface-vs-internal-trace gap in deployed reasoning models** — where interface-level trace hiding is treated as equivalent to security boundary enforcement, but the gap between them is structural and exploitable
- Introduces **Reasoning Exposure Prompting (REP)** — a lightweight in-context elicitation method using shadow-model-generated demonstrations wrapped in auxiliary code-like formats (pseudo-code, JSON scaffolds, function-call syntax) that elicits victim-model traces without modifying weights or breaking the API surface
- Demonstrates **substantial similarity increase** between REP-conditioned exposed traces and victim-model internal traces across multiple reasoning datasets, victim models, and student distillation regimes
- Shows that **interface-level hiding preserves neither distillation privacy nor reasoning-signal control** — the prompting format itself can be engineered to volunteer the very traces the interface was supposed to hide
- Surfaces **code-like-format-as-extraction-amplifier** — auxiliary structural framing (the prompts themselves, not the questions) reliably pushes reasoning models to volunteer more of their internal reasoning, inverting the deployment assumption that trace hiding is sufficient protection
- First paper in the wiki that frames **reasoning-trace exposure as an extraction-attack surface** (distinct from Run 42's evidence-tracing-provenance work, which is forward-tracing of decisions; this paper is backward-extraction of internal reasoning traces via prompting)

## Related Papers
- [[llm-based-scientific-peer-review-methods-benchmarks-reliability-challenges-2606.25057]] — Run 40 sibling: scientific peer review reliability (different reliability axis — peer review is human-mediated trace hiding, this paper is interface-mediated trace hiding)
- [[from-agent-traces-to-trust-a-survey-of-evidence-tracing-and-execution-provenance-in-llm-agents-2606.04990]] — Run 42 sibling: evidence tracing is forward-tracing decisions to source material, this paper is backward-extraction of internal reasoning via prompting
- [[ras-measuring-llm-safety-through-refusal-alignment-2606.25750]] — refusal-alignment-safety-measurement (different vulnerability surface — RAS measures over-rejection, this paper is reasoning-trace extraction via prompting format)
- [[privacyalign-contextual-privacy-alignment-for-llm-agents-2606.21710]] — contextual privacy alignment for agents (training-time alignment, not interface-time extraction)
- [[taro-token-level-adaptive-routing-llm-test-time-alignment-2603.18411]] — Run 46 sibling: token-level routing as test-time alignment (different alignment primitive — TARo is routing-based alignment, this paper is extraction-side attack on aligned reasoning)
- [[emergent-concepts]] (parent wiki page) — meta-cluster for emergent-concept paper discoveries