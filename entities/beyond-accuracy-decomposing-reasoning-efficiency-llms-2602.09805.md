---
title: "Beyond Accuracy: Decomposing the Reasoning Efficiency of LLMs"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [reasoning, efficiency, benchmark, token]
sources: ["https://arxiv.org/abs/2602.09805"]
---

# Beyond Accuracy: Decomposing the Reasoning Efficiency of LLMs

## Overview
As reasoning LLMs trade tokens for accuracy through deliberation, search, and self-correction, a single accuracy score no longer reveals whether those tokens buy useful reasoning, recovery from hard instances, or mere verbosity. This paper introduces a trace-optional evaluation framework that decomposes reasoning efficiency into logic-limited, context-limited (truncation-driven), and verbosity-limited failure modes — providing a diagnostic decomposition that accuracy-per-token obscures.

## Key Facts
- **Authors**: Kaiser, Daniel; Frigessi, Arnoldo; Ramezani-Kebrya, Ali + 1
- **Year**: 2026
- **arXiv**: [2602.09805](https://arxiv.org/abs/2602.09805)
- **Date**: 2026-02-10

## Key Contributions
- **Three-way failure mode decomposition**: Separates logic-limited, context-limited (truncation-driven), and verbosity-limited reasoning failures — which appear identical under accuracy-per-token
- **Trace-optional evaluation**: Does not require full reasoning traces, enabling efficiency measurement without full decode capture
- **Efficiency and overhead rankings** are more stable across benchmark pairs than accuracy rankings — more robust for model comparison
- **Pareto analysis** over (token count, accuracy) pairs for identifying optimal reasoning investment per problem type
- **Distinct from OckBench**: This paper decomposes WHY tokens are wasted (failure mode taxonomy); OckBench measures HOW MUCH is wasted (token count benchmark) — complementary primitives

## Related Papers
- [[ockbench-measuring-the-efficiency-of-llm-reasoning-2511.05722]] — OckBench token efficiency benchmark (measures waste magnitude; this paper measures failure modes)
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — Planning efficiency in tool-use agents
- [[robust-reasoning-benchmark-2604.08571]] — Robustness of reasoning under distribution shift
