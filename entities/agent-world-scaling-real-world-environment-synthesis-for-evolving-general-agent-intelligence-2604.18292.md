---
title: "Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent, environment-synthesis, self-evolving, scaling-laws, mcp, environment-co-evolution]
sources: ["https://arxiv.org/abs/2604.18292"]
---

# Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence

## Overview
Agent-World (ByteDance, 2026) is a self-evolving training arena for general agent intelligence built on top of the Model Context Protocol (MCP) ecosystem. It introduces two coupled mechanisms — **Agentic Environment-Task Discovery** that autonomously mines thousands of real-world environment themes from topic-aligned databases and executable tool ecosystems, and **Continuous Self-Evolving Agent Training** that combines multi-environment RL with a dynamic self-evolving arena which detects capability gaps and resynthesizes targeted tasks. Across 23 agent benchmarks, the Agent-World-8B / 14B models consistently outperform strong proprietary baselines and environment-scaling baselines, with explicit scaling trends identified between environment diversity, self-evolution rounds, and downstream capability.

## Key Facts
- **Authors**: ByteDance Agent-World team (April 2026)
- **Year**: 2026
- **arXiv**: [2604.18292](https://arxiv.org/abs/2604.18292)
- **Online date**: 2026-04-20

## Key Contributions
- **Agentic Environment-Task Discovery**: an autonomous pipeline that explores topic-aligned databases and executable tool ecosystems across thousands of real-world environment themes, then synthesizes verifiable tasks with controllable difficulty — the first environment-discovery primitive that treats MCP tools as a first-class substrate for environment synthesis.
- **Continuous Self-Evolving Agent Training**: a coupled loop where multi-environment RL training and a self-evolving arena dynamically identify capability gaps via targeted task synthesis, enabling the *co-evolution of agent policies and environments* — distinct from static environment pools or fixed curricula.
- **Empirical scaling laws for environment diversity**: across 23 agent benchmarks, Agent-World-8B/14B consistently outperform strong proprietary models and environment-scaling baselines, with explicit scaling trends as a function of environment diversity and self-evolution rounds.
- **First MCP-grounded general-agent training arena** — environments synthesized from real-world MCP tools (the load-bearing protocol for tool-using agents), bridging the gap between agentic research prototypes and deployable production tool stacks.

## Related Papers
- [[qwen-agentworld-language-world-models-for-general-agents-2606.24597]] — Sibling discovery: Qwen-AgentWorld's CPT→SFT→RL pipeline starts from environment modeling as the pre-training objective; Agent-World takes the complementary path of synthesizing environments from real-world MCP tools.
- [[scaling-rl-for-code-generation-with-synthetic-data-and-curriculum-2603.24202]] — Cousin: synthetic-data + curriculum for code generation RL — Agent-World generalizes the curriculum principle to environment-task discovery itself.
- [[internet-of-agentic-ai-communication-coordination-collective-intelligence-at-scale-2606.12835]] — Sibling Internet-of-Agents survey — Agent-World supplies the environment substrate such coordination primitives operate over.