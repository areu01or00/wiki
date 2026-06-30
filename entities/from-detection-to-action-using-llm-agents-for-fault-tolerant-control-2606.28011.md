---
title: "From Detection to Action: Using LLM Agents for Fault-Tolerant Control"
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [agent, llm, fault-tolerant-control, multi-agent]
sources: ["https://arxiv.org/abs/2606.28011"]
---

# From Detection to Action: Using LLM Agents for Fault-Tolerant Control

## Overview
This paper proposes an agentic LLM framework for active Fault-Tolerant Control (FTC) that transforms fault detection outputs into constraint-aware recovery actions grounded in plant-specific knowledge. The approach uses a multi-agent workflow decomposing operator duties (monitoring, planning, action synthesis, simulation, validation, reprompting) coupled with a Digital Process Plant Twin (DPPT) providing plant data, models, and simulation services.

## Key Facts
- **Authors**: Javal Vyas, Milapji Singh Gill, Artan Markaj, Felix Gehlhoff, Mehmet Mercangöz
- **Year**: 2026 (arXiv 2606.28011, submitted June 2026)
- **arXiv**: [2606.28011](https://arxiv.org/abs/2606.28011)

## Key Contributions
- **Multi-Agent LLM Fault-Tolerant Control Framework**: First framework coupling LLM agents with Digital Process Plant Twin (DPPT) for active FTC — decomposes fault recovery into monitoring, planning, action synthesis, simulation, validation, and reprompting sub-tasks across specialized agents
- **Constraint-Aware Recovery Actions**: Recovery actions grounded in plant-specific physical constraints via DPPT simulation, ensuring recovered controller respects actuator limits and physical invariants
- **Pre-execution Validation**: DPPT enables pre-execution simulation of recovery actions before plant deployment, catching secondary failures before they occur
- **Application**: Industrial control systems with active fault detection and dynamic reconfiguration requirements

## Related Papers
- [[emergent-concepts]] — Parent page for emergent-concept discoveries
