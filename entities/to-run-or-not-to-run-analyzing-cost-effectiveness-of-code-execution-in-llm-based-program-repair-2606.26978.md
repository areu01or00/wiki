---
title: "To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [code-generation, llm-agents, program-repair, tool-use, cost-effectiveness]
sources: ["https://arxiv.org/abs/2606.26978"]
---

# To Run or Not to Run: Analyzing the Cost-Effectiveness of Code Execution in LLM-Based Program Repair

## Overview
This paper systematically studies the cost-effectiveness of the "generate-run-revise" paradigm in LLM-based program repair agents. It conducts a two-stage empirical analysis to determine when code execution actually improves patch quality enough to justify its time and expense — providing a decision framework for when to invoke execution in agentic code修复 loops.

## Key Facts
- **Authors**: Lin, Zhu, Zhou, Wang, Sun, Yang, Lo, Li
- **Year**: 2026
- **arXiv**: [2606.26978](https://arxiv.org/abs/2606.26978)

## Key Contributions
- First systematic cost-effectiveness analysis of code execution in LLM program repair agents
- Two-stage empirical framework: when does execution improve pass@1 vs when is it wasted compute
- Decision framework for selective execution invocation (avoiding costly test runs that don't help)
- Quantifies the trade-off between execution rounds, patch quality improvement, and total cost
- Findings applicable to agentic code修复 loops (SWE-agent, CodeAgent, etc.)

## Related Papers
- [[how-much-static-structure-do-code-agents-need-a-study-of-deterministic-anchoring-2606.26979]] — Deterministic Anchoring: structural facts as plain-text comments discipline probabilistic code exploration; complementary (static structure reduces execution variance vs this paper studies execution cost)
- [[llm-as-code-agentic-programming-for-agent-harness-2606.15874]] — LLM-as-Code: agentic programming paradigm; broader context for code agents
