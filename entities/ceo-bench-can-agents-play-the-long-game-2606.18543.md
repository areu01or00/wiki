---
title: "CEO-Bench: Can Agents Play the Long Game?"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [agent-evaluation, long-horizon-planning, multi-decision-coordination, startup-simulation, benchmark]
sources: ["https://arxiv.org/abs/2606.18543"]
---

# CEO-Bench: Can Agents Play the Long Game?

## Overview
CEO-Bench evaluates language model agents on sustained, adaptive progress over time by simulating a 500-day startup operation. Agents manage pricing, marketing, budgeting, and other business functions through a programmable Python interface, facing the same challenges as human CEOs. Success demands analyzing noisy interconnected business databases, translating signals into strategy, and coordinating many decisions with programming. Only Claude Opus 4.8 and GPT-5.5 finish above the $1M starting balance; neither consistently turns a profit.

## Key Facts
- **Authors**: Chen, Haozhe; Narasimhan, Karthik; Liu, Zhuang
- **Year**: 2026
- **arXiv**: [2606.18543](https://arxiv.org/abs/2606.18543)

## Key Contributions
- First benchmark to evaluate agents on sustained adaptive progress over a 500-day simulated horizon (vs. isolated short-horizon tasks)
- Tests four capabilities: (1) navigating long horizons amid uncertainty, (2) acquiring information in noisy environments, (3) adapting to a changing world, (4) orchestrating multiple moving parts toward a coherent goal
- Strongest agents (Claude Opus 4.8, GPT-5.5) still fail to consistently turn a profit — ceiling on sustained multi-decision coordination remains low
- Introduces programmable Python interface as agent interaction modality for complex real-world simulation
- **First startup-simulation long-horizon agent benchmark in the wiki.**

## Related Papers
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — Long-horizon planning evaluation via tool-use ecosystems (orthogonal axis — CEO-Bench is economic simulation vs. PlanBench's tool-retrieval planning)
- [[memprobe-probing-longterm-agent-memory-via-hidden-userstate-recovery-2606.24595]] — Long-term memory probing for agents (orthogonal — CEO-Bench tests strategic memory vs. MEMPROBE's hidden state recovery)
- [[counsel-a-meta-evaluation-dataset-for-agentic-tasks-2606.21627]] — Meta-evaluation dataset for agentic tasks (parallel evaluation methodology)
