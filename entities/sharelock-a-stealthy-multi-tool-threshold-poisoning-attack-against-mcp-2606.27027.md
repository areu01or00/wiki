---
title: "ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agentic-security, mcp, multi-agent, adversarial-attack]
sources: ["https://arxiv.org/abs/2606.27027"]
---

# ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP

## Overview
ShareLock is a multi-tool threshold poisoning attack targeting the Model Context Protocol (MCP), an open protocol that bridges LLMs with external tools in modern agent ecosystems. The attack exploits the interaction between an LLM agent and multiple MCP servers to inject malicious prompts through a stealthy multi-party threshold mechanism — none of the individual poisoned tools exceeds a detection threshold, but collectively they redirect the agent's behavior. This work formalizes the threat model for collaborative multi-tool agent ecosystems where trust boundaries are undefined across tool providers.

## Key Facts
- **Authors**: Liwei Liu, Tianzhu Han, Zijian Liu, Zishu Dong, Na Ruan
- **Year**: 2026
- **arXiv**: [2606.27027](https://arxiv.org/abs/2606.27027)

## Key Contributions
- Formalizes multi-tool threshold poisoning: individual tools appear benign but collectively redirect agent control flow
- Introduces ShareLock attack against MCP-based multi-agent tool ecosystems
- Demonstrates that per-tool safety evaluations miss collective-action attacks in open agent protocols
- Provides empirical evaluation on real MCP-enabled agent deployments

## Related Papers
- [[what-if-prompt-injection-never-left-exploring-cross-session-stored-prompt-injection-in-agentic-systems-2606.04425]] — Cross-session prompt injection (Run 124) — earlier work on persistent prompt injection in agentic systems
- [[fragfuse-bypassing-access-control-of-llm-agents-via-memory-based-query-fragmentation-and-fusion-2606.15609]] — FragFuse memory fragmentation attack (Run 131) — related memory-channel attack surface in multi-tool agents
- [[the-defense-trilemma-why-prompt-injection-defense-wrappers-fail-2604.06436]] — Prompt injection defense wrapper failures — systemic limitations in current IPI defenses
