---
title: "Scaling Behavior of Single LLM-Driven Multi-Agent Systems"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [multi-agent, scaling, collective-intelligence, llm]
sources: ["https://arxiv.org/abs/2606.00655"]
---

# Scaling Behavior of Single LLM-Driven Multi-Agent Systems

## Overview
This paper investigates the fundamental scaling laws and collective dynamics that emerge when a single large language model drives multiple agents in a multi-agent system. Rather than scaling the model itself, the authors characterize how task complexity, agent count, and communication topology affect the emergent collective behavior of LLM-driven MAS. The work addresses a critical gap: while individual LLM scaling laws are well-studied, the scaling behavior of LLM-mediated collective intelligence remains poorly understood.

## Key Facts
- **Authors**: Li, Jialing; Gu, Zhouhong; Cai, Yin + 1
- **Year**: 2026
- **arXiv**: [2606.00655](https://arxiv.org/abs/2606.00655)

## Key Contributions
- First characterization of scaling laws for single-LLM-driven multi-agent collective behavior
- Identifies non-linear phase transitions in collective performance as agent count increases
- Characterizes optimal communication topologies for different task complexity regimes
- Reveals that single-LLM-driven MAS exhibits emergent behaviors not predictable from individual agent performance alone

## Related Papers
- [[argent-signaling-protocol-multi-agent-semantic-drift-2606.19356]] — Multi-agent semantic drift analysis; complements by showing that collective reasoning quality degrades in predictable ways as agent count scales
- [[benchmarking-open-ended-multi-agent-coordination-in-language-agents-2606.08340]] — Open-ended coordination benchmark; provides the evaluation substrate for the scaling behaviors characterized here
- [[beyond-individual-intelligence-surveying-collaboration-failure-attribution-and-self-evolution-in-llm-based-multi-agent-systems-2605.14892]] — Collaboration failure taxonomy; maps specific failure modes that emerge at scale in single-LLM-driven systems
