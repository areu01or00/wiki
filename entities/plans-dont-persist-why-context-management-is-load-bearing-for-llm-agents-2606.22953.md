---
title: "Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [llm, agents, context-management, planning, inference]
sources: ["https://arxiv.org/abs/2606.22953"]
---

# Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents

## Overview
Long-horizon agents depend on context management: systems compress, summarize, and evict old tokens so tasks can continue beyond finite windows. That is safe only when dropped information is no longer needed or has been internalized. Plans are the stress case: they are written early in an agent run, referenced many steps later, and frequently lost when context compression fires mid-task. Plans Don't Persist formalizes this failure mode, shows empirically that off-the-shelf summarization-based context managers systematically drop plan content while preserving surface-task tokens, and argues that *load-bearing* agent state (plans, contracts, retrieved evidence, prior commitments) needs explicit retention semantics rather than being treated as fungible with the rest of the trace. The paper proposes a small, plan-aware eviction policy that surfaces plan tokens as durable and recovers a substantial fraction of long-horizon task success.

## Key Facts
- **Authors**: Mehta, Aman; Datta, Anupam
- **Year**: 2026
- **arXiv**: [2606.22953](https://arxiv.org/abs/2606.22953)
- **Subjects**: cs.AI

## Key Contributions
- Identifies *plan-persistence* as a distinct axis of long-horizon agent failure, separate from context length, retrieval recall, or instruction following, and shows current summarization-based context managers fail it by ~30-40 percentage points.
- Formalizes a load-bearing-vs-fungible token taxonomy and shows that treating all tokens uniformly during eviction is the dominant source of plan-loss.
- Proposes a plan-aware eviction policy (mark plan tokens as durable, surface them across compression passes) and demonstrates a substantial recovery on long-horizon tool-use benchmarks without retraining the underlying model.
- Frames context management not as an inference-efficiency optimization but as a *correctness* substrate, opening a new evaluation axis for context-engineering work.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain; discovered via emergent-concept search on the agent-context-management axis
- [[self-compacting-language-model-agents-2606.23525]] — Companion: agent-driven inference-time self-compaction; this paper formalizes why plan tokens specifically resist generic compaction
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — Companion: PlanBench-XL evaluates long-horizon planning under retrieval-limited tool visibility; this paper isolates the *context-retention* axis of the same long-horizon failure surface
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Companion: argues agent memory needs systems-level treatment; this paper shows one specific system layer (context eviction) where current designs systematically destroy load-bearing state