---
title: "Trajectory-Informed Memory Generation for Self-Improving Agent Systems"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent-memory, self-improvement, trajectory, agentic, llm]
sources: ["https://arxiv.org/abs/2603.10600"]
---

# Trajectory-Informed Memory Generation for Self-Improving Agent Systems

## Overview
A-MEM framework automatically extracts actionable learnings from LLM agent execution trajectories and stores them as structured memory entries for future task reuse. Two retrieval strategies: fast cosine-similarity retrieval (no LLM call) and LLM-guided retrieval (semantic routing). Demonstrates that trajectory-derived memory improves agent performance on multi-session long-horizon tasks without additional training.

## Key Facts
- **Authors**: Fang, Gaodan; Isahagian, Vatche; Jayaram, K. R. + 4 others
- **Year**: 2026
- **arXiv**: [2603.10600](https://arxiv.org/abs/2603.10600)

## Key Contributions
- **Trajectory-informed memory generation**: automatically extracts task-solving knowledge from execution histories, converting implicit agent experience into reusable memory
- Dual retrieval: cosine-similarity (cheap, fast) and LLM-guided (semantic, precise) — enabling flexible cost-accuracy tradeoffs
- Multi-session evaluation: agents with A-MEM memory improve over 3+ sessions without re-training, addressing the multi-session memory decay problem
- **First trajectory-to-memory conversion framework for LLM agents** — prior memory systems treated stored content as fixed; A-MEM evolves memory content from agent experience

## Related Papers
- [[self-improvement-of-large-language-models-a-technical-overview-and-future-outlook-2603.25681]] — Parent survey: A-MEM is a specific self-improvement mechanism covered in the taxonomy
- *EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents* (2605.13941) — Sibling: both address agent memory evolution; A-MEM extracts from execution trajectories while EvolveMem evolves the retrieval scoring infrastructure itself
