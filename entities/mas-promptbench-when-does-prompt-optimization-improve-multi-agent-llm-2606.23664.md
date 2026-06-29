---
title: "MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems?"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [multi-agent, prompt-optimization, benchmarking, llm, agentic-ai]
sources: ["https://arxiv.org/abs/2606.23664"]
---

# MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems?

## Overview
MAS-PromptBench systematically studies system-prompt optimization across a broad range of multi-agent LLM system configurations — varying in task, workflow, communication protocol, and team size — benchmarking two prompt optimizers that extend single-agent methods to the MAS setting. The work reveals when and how much prompt optimization helps MAS performance, characterizing the sensitivity of gains to system configuration.

## Key Facts
- **Authors**: Juyang Bai, Laixi Shi et al.
- **Year**: 2026
- **arXiv**: [2606.23664](https://arxiv.org/abs/2606.23664)
- **Submitted**: 2026-06-22
- **Subjects**: Machine Learning (cs.LG); Multiagent Systems (cs.MA)

## Key Contributions
- **MAS prompt optimization taxonomy**: First systematic characterization of how prompt optimization behaves differently in multi-agent vs single-agent settings
- **Exponentially growing search space**: Identifies that MAS prompt optimization poses distinct challenges from single-LLM prompt optimization due to combinatorial explosion of agent role/behavior interactions
- **Configuration sensitivity analysis**: Reveals when and how much prompt optimization helps across diverse MAS setups — gains are non-uniform and highly sensitive to workflow and team size
- **Open challenges characterization**: Documents the open problems in MAS prompt optimization, providing a benchmark for future research

## Related Papers
- [[tap-file-based-protocol-heterogeneous-llm-agent-collaboration-2606.14445]] — Both study multi-agent LLM collaboration; MAS-PromptBench focuses on prompt optimization as the optimization surface while tap focuses on communication protocol infrastructure
- [[the-ringelmann-effect-in-multi-agent-llm-systems-a-scaling-law-for-effective-team-size-2606.02646]] — Both study team dynamics in multi-agent LLMs; Ringelmann Effect characterizes team size inefficiency while MAS-PromptBench characterizes prompt optimization sensitivity across configurations
