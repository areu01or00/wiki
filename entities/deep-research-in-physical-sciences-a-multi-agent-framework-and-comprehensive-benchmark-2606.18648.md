---
title: "Deep Research in Physical Sciences: A Multi-Agent Framework and Comprehensive Benchmark"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [deep-research, multi-agent, scientific-reasoning, benchmark, physical-sciences, evaluation]
sources: ["https://arxiv.org/abs/2606.18648"]
---

# Deep Research in Physical Sciences: A Multi-Agent Framework and Comprehensive Benchmark

## Overview
Yigeng Jiang, Tengchao Yang, Taoyong Cui, Jiaxing Wan, Yuan Wang, Weida Wang et al. introduce PhySciBench — a benchmark of 200 expert-curated questions balanced between physics and chemistry across six task categories reflecting real-world scientific workflows — and evaluate state-of-the-art models and agent systems on it, surfacing limited performance (the strongest baseline, Gemini Deep Research, reaches only 33.5% accuracy). The authors analyse failure cases to identify three recurrent deficiencies (fragility in extended reasoning chains, limited knowledge transfer across steps, and a lack of physics-grounded self-verification) and propose DelveAgent, a modular multi-agent framework with an adaptive planning loop, dual-granularity memory, and a hierarchical physics-grounded reflection mechanism that improves accuracy by up to 7.5 percentage points across four scientific benchmarks while reducing inference costs to approximately one-third of the strongest baseline.

## Key Facts
- **Authors**: Yigeng Jiang, Tengchao Yang, Taoyong Cui, Jiaxing Wan, Yuan Wang, Weida Wang et al. (28 total)
- **Year**: 2026
- **arXiv**: [2606.18648](https://arxiv.org/abs/2606.18648)
- **Submitted**: 2026-06-17
- **Subjects**: cs.AI, cs.CL, cs.MA

## Key Contributions
- PhySciBench, a 200-question benchmark balanced between physics and chemistry across six task categories that reflect real-world scientific workflows, and that current state-of-the-art deep-research agents fail (33.5% best accuracy) — a quantitative anchor for "deep research in the physical sciences" as a frontier agent task.
- A failure-mode analysis identifying three recurrent deficiencies in deep-research agents on physical-science tasks: fragility in extended reasoning chains, limited cross-step knowledge transfer, and absence of physics-grounded self-verification.
- DelveAgent, a modular multi-agent framework combining an adaptive planning loop, dual-granularity memory, and a hierarchical physics-grounded reflection mechanism — yielding up to 7.5pp accuracy gains at approximately one-third the inference cost of the strongest baseline.
- Empirical evidence that "physics-grounded self-verification" is the load-bearing primitive for deep-research agents in physical sciences — without it, the planning loop drifts even when the underlying LLM is capable.

## Related Papers
- [[emergent-concepts]] — Parent meta-page on emergent-concept discoveries; this entry was discovered via emergent-concept search on 2026-06-25 (deep-research / multi-agent scientific-reasoning / physical-sciences theme)
- [[naturebench-can-coding-agents-match-the-published-sota-of-nature-family-papers-2606.24530]] — Sibling deep-research benchmark in the Nature-family setting; PhySciBench complements by extending the same evaluation rigour to physics/chemistry and showing the Gemini Deep Research ceiling is similarly low
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — Sibling deep-research benchmark on workplace sessions; PhySciBench is the science-flank counterpart in the agent-evaluation wave
- [[autodata-an-agentic-data-scientist-to-create-high-quality-synthetic-data-2606.25996]] — Sibling entry on agentic data science; DelveAgent complements Autodata by attacking the agentic *evaluation* side of the deep-research loop in a domain where hallucination risk is structurally high