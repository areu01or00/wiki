---
title: "Benchmarking Open-Ended Multi-Agent Coordination in Language Agents"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [multi-agent, coordination, benchmark, llm]
sources: ["https://arxiv.org/abs/2606.08340"]
---

# Benchmarking Open-Ended Multi-Agent Coordination in Language Agents

## Overview
Tessera et al. (2026) introduce **alem**, a JAX-based benchmark for *open-ended* multi-agent coordination built on Craftax-like dynamics. Alem embeds procedurally generated coordination tasks, soft specialisation, communication, and controllable coordination difficulty into a long-horizon survival world with exploration, crafting, trading, and combat — addressing the structural gap in agent evaluation where existing benchmarks rarely test long-horizon coordination demands together. Evaluating 13 modern LLMs zero-shot within homogeneous teams (with trained MARL agents as reference points) shows current LLM agents average only ~6% normalised return, but their failures are not uniform: on the hardest coordination setting, zero-shot Gemini-3.1-Pro-High approaches MARL agents trained for one billion steps, while GPT-5.4-High achieves strong base-task reward but much lower coordination reward — surfacing *coordination as a distinct bottleneck* for frontier LLM agents, separate from single-agent capabilities.

## Key Facts
- **Authors**: Tessera, Kale-ab Abebe; Szecsenyi, Andras; Barker, Cameron; Rutherford, Alexander; Paglieri, Davide; Scannell, Aidan; Gouk, Henry; Crowley, Elliot J.; Rocktäschel, Tim; Storkey, Amos
- **Year**: 2026
- **arXiv**: [2606.08340](https://arxiv.org/abs/2606.08340)
- **Date**: 2026-06-06

## Key Contributions
- **alem benchmark**: first benchmark that isolates *long-horizon open-ended multi-agent coordination* as a measurable bottleneck distinct from single-agent capability, built on JAX/Craftax-like dynamics with procedurally generated coordination tasks, soft specialisation, and controllable coordination difficulty.
- **Coordination-as-distinct-bottleneck finding**: ablation across 13 LLMs shows that individual task competence (GPT-5.4-High base-task reward) does not imply coordination competence (low coordination reward on hardest setting), while Gemini-3.1-Pro-High closes the gap to 1B-step-trained MARL agents only on the coordination axis — establishing that *coordination* is a separable primitive from *task competence*.
- **Communication as largest contributor**: ablations surface communication as the dominant driver of coordination reward, with memory and reasoning providing secondary gains when used to maintain multi-step plans — providing the first controlled testbed for measuring each of these contributions in isolation.

## Related Papers
- [[emergent-concepts]] — Parent wiki page that motivated this discovery
- [[the-hitchhikers-guide-to-agentic-ai-from-foundations-to-systems-2606.24937]] — Sibling foundational agentic-AI survey that organises the multi-agent systems landscape alem now provides the empirical coordination primitive for
- [[deep-research-in-physical-sciences-a-multi-agent-framework-and-comprehensive-benchmark-2606.18648]] — Sibling multi-agent deep-research benchmark — Deep-Research evaluates *task-completion* in scientific reasoning workflows, alem evaluates *coordination competence* in open-ended survival workflows — together they bracket the multi-agent evaluation surface between task-completion and open-ended coordination
- [[llm-based-scientific-peer-review-methods-benchmarks-reliability-challenges-2606.25057]] — Sibling peer-review methodology — Scientific-Peer-Review benchmarks human-mediated trace evaluation, alem benchmarks machine-mediated long-horizon coordination — together they bracket the multi-agent reliability surface between peer-evaluation and long-horizon coordination