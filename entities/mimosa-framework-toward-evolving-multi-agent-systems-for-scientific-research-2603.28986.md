---
title: "Mimosa Framework: Toward Evolving Multi-Agent Systems for Scientific Research"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [multi-agent, scientific-research, workflow, autonomous-agents]
sources: ["https://arxiv.org/abs/2603.28986"]
---

# Mimosa Framework: Toward Evolving Multi-Agent Systems for Scientific Research

## Overview
Mimosa is an evolving multi-agent framework that automatically synthesizes task-specific multi-agent workflows and iteratively refines them through experimental feedback. It uses the Model Context Protocol (MCP) for dynamic tool discovery, generates workflow topologies via a meta-orchestrator, executes subtasks through code-generating agents, and scores executions with an LLM-based judge whose feedback drives workflow refinement. On ScienceAgentBench, Mimosa achieves 43.1% success rate with DeepSeek-V3.2, surpassing single-agent baselines and static multi-agent configurations.

## Key Facts
- **Authors**: Martin Legrand, Tao Jiang, Matthieu Feraud, Benjamin Navet, Yousouf Taghzouti, Fabien Gandon, Elise Dumont, Louis-Félix Nothias
- **Year**: 2026
- **arXiv**: [2603.28986](https://arxiv.org/abs/2603.28986)
- **Submitted**: 30 Mar 2026
- **Subjects**: cs.AI, cs.LG, cs.MA

## Key Contributions
- MCP-based dynamic tool discovery: Model Context Protocol enables dynamic tool lookup at runtime rather than fixed toolset
- Meta-orchestrator workflow topology generation: generates and iteratively refines multi-agent workflow graphs via experimental feedback
- LLM-based judge feedback loop: drives workflow refinement through scored execution feedback
- Heterogeneous model response: reveals that workflow evolution benefits depend on the underlying execution model's capabilities
- Open-source fully logged execution traces for auditability and replication

## Related Papers
- [[from-reaction-to-anticipation-proactive-failure-recovery-through-agentic-task-graph-for-robotic-manipulation-2605.11951]] — AgentChord's three-role choreography (Composer/Arranger/Conductor) vs Mimosa's meta-orchestrator represent two distinct multi-agent role-decomposition paradigms: reactive task-graph enrichment vs proactive workflow synthesis
- [[how-much-coordination-gain-is-real-a-paired-noise-floor-protocol-for-multi-agent-llm-benchmarks-2606.20695]] — Mimosa's LLM-judge scoring mechanism is directly relevant to the noise-floor critique; whether Mimosa's gains vs static configurations survive paired noise-floor replication would test whether workflow evolution adds genuine coordination value
