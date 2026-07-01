---
title: "FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [multi-agent, workflow-steering, security, planner-executor, vulnerability]
sources: ["https://arxiv.org/abs/2605.11514"]
---

# FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems

## Overview
FlowSteer studies the attack surface introduced when LLM-based multi-agent systems adopt planner-executor architectures — planners convert natural language prompts into subtasks, roles, dependencies, and routing paths at planning time. The attack surface is in workflow formation: prompts can shape agent organization without modifying MAS infrastructure. The paper demonstrates that an attacker who controls the planner prompt can redirect multi-agent coordination at runtime by shaping how tasks get decomposed, assigned, and routed.

## Key Facts
- **Authors**: Li, Fanxiao; Wu, Jiaying; Fu, Tingchao + 3
- **Year**: 2026
- **arXiv**: [2605.11514](https://arxiv.org/abs/2605.11514)

## Key Contributions
- First identification of planner-executor architecture as an attack surface in multi-agent LLM systems
- Demonstrates that workflow-formation prompts can redirect multi-agent coordination without modifying infrastructure
- Prompt-only attack vector that requires no code changes or API modifications
- Provides taxonomy of planning-time vulnerabilities distinct from execution-time attacks

## Related Papers
- [[toward-secure-llm-agents-threat-surfaces-attacks-defenses-and-evaluation-2606.10749]] — The security framework from this paper systematizes the attack surface that FlowSteer identifies; FlowSteer's planner-executor vulnerability is a specific instance of the broader control-flow threat category
- [[tool-use-enables-undetectable-steganography-in-multi-agent-llm-systems-2606.28425]] — Steganography paper from Run 298; FlowSteer's planning-time attack surface provides the infrastructure that enables covert channel embedding in multi-agent tool calls
