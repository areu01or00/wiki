---
title: "Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [llm-security, multi-agent-security, agentic-systems, threat-modeling]
sources: ["https://arxiv.org/abs/2606.10749"]
---

# Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation

## Overview
This survey systematizes the rapidly expanding attack surface of LLM agents, moving beyond unsafe text generation to systematize threats that arise when language-mediated reasoning couples with action selection, state management, and externally consequential execution. It provides the first comprehensive threat taxonomy for agentic LLM deployments, covering control-flow hijacking, tool privilege misuse, memory corruption, and multi-agent coordination attacks.

## Key Facts
- **Authors**: Ling, Yuchen; Yu, Shengcheng; Chen, Zhenyu + 1
- **Year**: 2026
- **arXiv**: [2606.10749](https://arxiv.org/abs/2606.10749)

## Key Contributions
- First comprehensive threat taxonomy for LLM agent deployments: threat surfaces, attack classes, defenses, and evaluation metrics
- Identifies control-flow redirection, tool privilege misuse, and memory corruption as distinct threat categories beyond traditional LLM risks
- Positions LLM agent security as a systems problem requiring co-design of reasoning + execution + state management
- First systematic security framework specifically targeting multi-agent LLM systems

## Related Papers
- [[tool-use-enables-undetectable-steganography-in-multi-agent-llm-systems-2606.28425]] — Tool-use steganography paper (Run 298); the security threat model in this paper provides the taxonomy that steganographic covert channels exploit
- [[flowsteer-prompt-only-workflow-steering-exposes-planning-time-vulnerabilities-in-multi-agent-llm-systems-2605.11514]] — FlowSteer paper (Run 299); the security framing in this paper extends to the workflow-formation attack surface that FlowSteer exposes
