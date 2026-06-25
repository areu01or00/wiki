---
title: "Self-Compacting Language Model Agents"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agents, context-management, inference-efficiency, llm-agents, compaction]
sources: ["https://arxiv.org/abs/2606.23525"]
---

# Self-Compacting Language Model Agents

## Overview
This paper addresses a central failure mode of long-horizon LLM agents: accumulated agent traces — chains of thought interleaved with tool calls, retrieval results, and intermediate observations — eventually outgrow the context window or anchor subsequent generations to stale content. The authors introduce "self-compaction," an inference-time mechanism where the agent periodically summarizes, prunes, or compresses its own trace into a more compact representation without external intervention, and analyze the trade-offs between trace fidelity and continued task performance. The work formalizes compaction as a learned operation (vs. a hand-crafted prompt scaffold) and shows it can be triggered adaptively based on trace-growth and relevance signals.

## Key Facts
- **Authors**: Li, Tianjian; Zhang, Jingyu; Jurayj, William
- **Year**: 2026
- **arXiv**: [2606.23525](https://arxiv.org/abs/2606.23525)
- **Subjects**: cs.CL

## Key Contributions
- Formalizes "self-compaction" as an inference-time operation where the agent decides *when* and *what* to compress from its own running trace, distinguishing it from external summarization pipelines or hand-engineered scaffolds.
- Empirically demonstrates that without compaction, long-horizon agent traces exhibit *trace-anchoring degradation* — later generations become conditioned on stale or irrelevant intermediate observations, hurting downstream task accuracy — and quantifies the degradation curve across trace length.
- Compares three compaction policies (uniform periodic, relevance-triggered, learned) and shows relevance-triggered compaction recovers ~85% of the no-compaction accuracy on multi-step tool-use benchmarks while using <40% of the original trace tokens.
- Introduces "Accordion-thinking" as a self-regulated step-summary primitive that integrates with existing scaffolds without architectural changes, suggesting a drop-in upgrade path for production coding/research agents.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 as a fresh 2026 contribution to LLM agent context-management and inference-efficiency.
