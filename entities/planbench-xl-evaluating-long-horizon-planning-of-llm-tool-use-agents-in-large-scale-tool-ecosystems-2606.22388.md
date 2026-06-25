---
title: "PlanBench-XL: Evaluating Long-Horizon Planning of LLM Tool-Use Agents in Large-Scale Tool Ecosystems"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agent-benchmark, tool-use, long-horizon-planning, llm-agents, evaluation, cs.AI]
sources: ["https://arxiv.org/abs/2606.22388"]
---

# PlanBench-XL: Evaluating Long-Horizon Planning of LLM Tool-Use Agents in Large-Scale Tool Ecosystems

## Overview
PlanBench-XL is an interactive benchmark of 327 retail tasks over 1,665 tools that tests whether LLM tool-use agents can *iteratively* retrieve usable tools, invoke them to uncover intermediate evidence for subsequent calls, and reach a final goal under **retrieval-limited tool visibility** — i.e., agents do not see the whole tool catalog at once and must discover what they need. The benchmark further features an optional *blocking mechanism* that simulates real-world unpredictability through missing, failing, or distracting tool functions, forcing agents to detect disrupted paths and adapt at runtime rather than rely on a fixed plan.

## Key Facts
- **Authors**: Liu, Jiayu; Lin, Qihan; Qian, Cheng; Wang, Rui; Acikgoz, Emre Can; Yang, Xiaocheng; Liu, Jiateng; Wang, Zhenhailong; Chen, Xiusi; Ji, Heng; Hakkani-Tür, Dilek
- **Year**: 2026
- **Date**: 2026-06-21
- **arXiv**: [2606.22388](https://arxiv.org/abs/2606.22388)
- **Subjects**: Artificial Intelligence (cs.AI)

## Key Contributions
- **Scale matched to realistic tool ecosystems**: 327 retail tasks spanning 1,665 tools — orders of magnitude larger than prior tool-use benchmarks where agents see the whole catalog or a small fixed subset.
- **Retrieval-limited tool visibility** as the default evaluation mode: agents must iteratively discover which tools are relevant, infer implicit sub-goals from intermediate evidence, and plan over a horizon much longer than a single tool call.
- **Optional blocking mechanism** that injects missing / failing / distracting tool functions mid-run, simulating real-world tool unreliability and forcing *runtime adaptation* rather than reliance on a pre-computed plan.
- **Empirical headroom signal**: GPT-5.4 achieves 51.90% accuracy in block-free settings but collapses to **11.36%** under the most severe blocking condition — establishing that current leading LLMs are far from solved on long-horizon, large-scale tool planning.
- Failure-mode diagnosis: agents are especially vulnerable when failures lack explicit error signals or when recovery requires longer alternative tool-use paths — a recipe for the next generation of *adaptive-planning* agent architectures.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered; complements the recent Agents' Last Exam and AGORA benchmark entries on this page by isolating a distinct axis — *long-horizon planning under tool retrieval limits and runtime blocking* — where current frontier models still collapse by ~40 points absolute accuracy when tool environments become unreliable.
