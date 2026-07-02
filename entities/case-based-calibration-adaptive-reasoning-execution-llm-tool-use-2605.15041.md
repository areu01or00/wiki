---
title: "Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [calibration, tool-use, reasoning, agent]
sources: ["https://arxiv.org/abs/2605.15041"]
---

# Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use

## Overview
CAST (Case-based Calibration framework) approaches LLM tool use from a case-based reasoning perspective, treating historical execution cases as a calibration substrate for balancing reasoning depth with structural validity. The framework enables LLMs to select appropriate deliberation depth based on the similarity of the current problem to previously solved cases, avoiding both under- and over-thinking.

## Key Facts
- **Authors**: Pang, Renning; Lan, Tian; Liu, Leyuan + 3
- **Year**: 2026
- **arXiv**: [2605.15041](https://arxiv.org/abs/2605.15041)
- **Date**: 2026-05-14

## Key Contributions
- **Case-based calibration**: Uses historical tool-use cases as a reference set for estimating required reasoning depth on new tasks
- **Adaptive execution**: Dynamically adjusts reasoning depth based on case similarity — shallow for familiar patterns, deep for novel situations
- **Structural validity constraint**: Enforces strict format validity on tool calls before execution, reducing failed tool invocations
- **+5.85pp improvement** on BFCLv2 benchmark with **-26% reasoning length** reduction versus uncalibrated baseline
- **First case-based calibration framework** specifically targeting LLM tool-use reasoning depth — distinct from token-budget or accuracy-based approaches

## Related Papers
- [[calibrating-the-evaluator-does-probability-calibration-mitigate-preference-coupling-in-llm-agent-feedback-loops-2606.31371]] — Related calibration framing for LLM agents
- [[why-multi-step-tool-use-reinforcement-learning-collapses-and-how-supervisory-signals-fix-it-2606.26027]] — Tool use RL collapse failure mode
- [[taco-tool-augmented-credit-optimization-for-agentic-tool-use-2606.30251]] — Tool-augmented credit assignment
