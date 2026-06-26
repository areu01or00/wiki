---
title: "SWE-Marathon: Can Agents Autonomously Complete Ultra-Long-Horizon Software Work?"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [architecture, llm]
sources: ["https://arxiv.org/abs/2606.07682"]
---

# SWE-Marathon: Can Agents Autonomously Complete Ultra-Long-Horizon Software Work?

## Overview

AI agents are increasingly expected to complete long-horizon workflows that require sustained progress over hours, millions of tokens, and complex environments. Yet current agent benchmarks largely evaluate short-form tasks, such as single pull requests, small tickets, or 5-10 minute exercises, limiting our ability to measure agents' capabilities in planning, long-context understanding, and memory use. We introduce SWE-Marathon, a benchmark of 20 long-horizon tasks spanning software engineering and adjacent technical domains. Each task consists of a unique executable environment, a human-curated task spec, and a validator that determines completion against the spec. Tasks are calibrated to require on the order of 4+ hours of agent work and 1M+ tokens of context consumption to complete, against a baseline of a state-of-the-art software engineering agent.

## Key Facts
- **Authors**: Desai, Rishi and Hu, Jesse and Cabezas, Joan et al.
- **Year**: 2026
- **arXiv**: [2606.07682](https://arxiv.org/abs/2606.07682)

## Key Contributions
- First benchmark to calibrate agent tasks at the **4+ hour / 1M+ token** scale — prior benchmarks stop at single-PR or 5-10 minute exercises
- 20 long-horizon tasks across software engineering + adjacent technical domains, each with unique executable environment + human-curated task spec + completion validator
- Calibration against a state-of-the-art software-engineering agent baseline sets a meaningful 'completion frontier' that prior short-form benchmarks cannot measure
- Surfaces the load-bearing gaps in agent planning, long-context understanding, and memory use that hour-scale tasks expose but minute-scale tasks hide

## Related Papers
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]]
- [[worldlines-benchmarking-and-modeling-long-horizon-stateful-2606.18847]]
- [[memgui-agent-end-to-end-long-horizon-mobile-gui-agent-proactive-context-2606.19926]]
- [[foresight-failure-detection-long-horizon-robotic-manipulation-2606.23085]]
