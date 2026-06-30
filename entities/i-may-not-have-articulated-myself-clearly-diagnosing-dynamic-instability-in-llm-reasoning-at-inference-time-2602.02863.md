---
title: "\"I May Not Have Articulated Myself Clearly\": Diagnosing Dynamic Instability in LLM Reasoning at Inference Time"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, inference, diagnostics, reliability]
sources: ["https://arxiv.org/abs/2602.02863"]
---

# "I May Not Have Articulated Myself Clearly": Diagnosing Dynamic Instability in LLM Reasoning at Inference Time

## Overview
This paper studies a failure mode that standard end-of-generation reasoning evaluations miss entirely: process-level breakdowns where an LLM "loses the thread" mid-reasoning, rather than producing a wrong final answer. The authors define a dynamic instability signal combining consecutive-step distributional shift (JSD — Jensen-Shannon Divergence between token distributions at consecutive reasoning steps) and token-level uncertainty (entropy). Using only inference-time observables available in standard APIs (token log probabilities), they detect when a reasoning chain is becoming unstable — before it produces a catastrophically wrong answer.

## Key Facts
- **Authors**: Reasoning Instability Authors
- **Year**: 2026
- **arXiv**: [2602.02863](https://arxiv.org/abs/2602.02863)

## Key Contributions
- Dynamic instability signal: JSD (consecutive-step distributional shift) + entropy (token-level uncertainty) — both computable from standard API logprobs without fine-tuning
- Detects reasoning breakdowns mid-chain — before the wrong final answer is produced — enabling early-stopping or intervention
- First paper to define and operationalize "mid-reasoning" instability detection using only inference-time observables
- Open-sources the instability detection pipeline for integration into production reasoning systems

## Related Papers
- [[reasoninglens-hierarchical-visualization-and-diagnostic-auditing-for-large-reasoning-models-2606.23404]] — ReasoningLens — hierarchical visualization and diagnostic auditing for reasoning models; complements this paper's instability detection with interpretable layer-wise breakdowns of where reasoning breaks down
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — Geometry of Refusal — linear instability in safety-aligned LLMs; both papers probe geometric signatures of reasoning failure, but this paper focuses on mid-chain instability rather than refusal geometry
- [[reflect-intervention-supported-error-attribution-for-silent-failures-in-llm-agent-traces-2606.09071]] — Reflect — intervention-supported error attribution for silent failures; this paper's instability detection provides the signal that Reflect's intervention framework acts upon
