---
title: "ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End?"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [llm-agent, operations-research, benchmark, end-to-end-evaluation, execution-grounded, agentic-decision-making]
sources: ["https://arxiv.org/abs/2606.19787"]
---

# ORAgentBench: Can LLM Agents Solve Challenging Operations Research Tasks End to End?

## Overview
Introduces ORAgentBench, an execution-grounded benchmark for evaluating autonomous LLM agents on challenging end-to-end operations research (OR) tasks — addressing the structural under-evaluation of LLM agents on realistic OR work where existing OR evaluations decouple modeling from solving, rely on pre-formalized or text-only instances, and rarely test the full workflow from operational artifacts to validated decisions. The benchmark contains 107 human-reviewed tasks and surfaces *end-to-end-execution-as-evaluation-surface* as the load-bearing primitive for OR-agent evaluation.

## Key Facts
- **Authors**: Li, Jiajun; Cai, Mingshu; Li, Yixuan; Ding, Yu; Hou, Ran; et al. (8 authors)
- **Year**: 2026
- **Date**: 2026-06-18
- **arXiv**: [2606.19787](https://arxiv.org/abs/2606.19787)
- **Categories**: cs.AI, cs.CL, cs.LG

## Key Contributions
- Provides the first execution-grounded OR benchmark for LLM agents — 107 human-reviewed tasks covering the full workflow from operational artifacts to validated decisions, where prior OR evaluations decoupled modeling from solving or relied on text-only instances.
- Surfaces *end-to-end-execution-as-evaluation-surface* as the structurally important primitive for OR-agent evaluation: the gap between "model can formalize an OR problem" and "agent can solve it end-to-end from artifacts" is the binding constraint the benchmark exposes.
- Methodology-level contribution to agent evaluation — execution-grounded benchmarks (vs text-only or pre-formalized) reveal capability profiles that decoupled evaluations systematically miss, and OR is a particularly high-value domain for this discipline because OR decisions are high-stakes, model-formalizations routinely fail silently, and verification against ground-truth solutions is unambiguous.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this discovery was logged
- [[naturebench-can-coding-agents-match-the-published-sota-of-nature-family-papers-2606.24530]] — Sibling SOTA-replication benchmark: NatureBench tests whether coding agents can match published Nature-family SOTA, ORAgentBench tests whether agents can match published OR-methodology SOTA — together they bracket the SOTA-replication-discipline across high-stakes scientific domains where execution-grounded validation is unambiguous
- [[beyond-static-leaderboards-predictive-validity-evaluation-llm-agents-2606.19704]] — Sibling agent-evaluation methodology: Beyond-Static-Leaderboards argues aggregate scoring is structurally inadequate, ORAgentBench demonstrates the specific execution-grounded alternative in a domain where aggregate scoring would systematically overstate agent capability
- [[tropt-an-open-framework-for-unifying-and-advancing-discrete-text-optimization-2606.23496]] — Sibling open-source evaluation substrate: TROPT unifies discrete text optimizers for adversarial evaluation, ORAgentBench is a complementary domain-specific benchmark providing the execution-grounded evaluation surface those optimizers would be measured against in the OR regime