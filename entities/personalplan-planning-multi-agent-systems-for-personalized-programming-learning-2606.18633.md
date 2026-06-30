---
title: "PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [multi-agent, planning, personalization, education, programming, llm]
sources: ["https://arxiv.org/abs/2606.18633"]
---

# PersonalPlan: Planning Multi-Agent Systems for Personalized Programming Learning

## Overview
PersonalPlan addresses the gap between generic LLM multi-agent planners and personalized programming education. The authors introduce MAP-PPL (Multi-Agent Plans for Personalized Programming Learning), a profile-conditioned multi-agent planning dataset with 3,043 query-profile-plan instances, and propose PersonalPlan, a two-stage MAS planner using hierarchical SFT with separate LoRA adapters for profile-aware task decomposition and step dependency planning, followed by Reward-Adaptive GRPO. Even 8B and 32B variants achieve state-of-the-art plan executability, personalization, and pedagogical quality.

## Key Facts
- **Authors**: Unknown (from arxiv 2606.18633)
- **Year**: 2026
- **arXiv**: [2606.18633](https://arxiv.org/abs/2606.18633)

## Key Contributions
- MAP-PPL dataset: 3,043 query-profile-plan instances from 1,730 Stack Overflow question groups and 2,738 learner profiles
- PersonalPlan two-stage planner: hierarchical SFT (separate LoRA adapters for profile-aware decomposition + step dependency planning) + Reward-Adaptive GRPO
- Profile-grounded pedagogical scaffolding: profile-conditioned decomposition ensures plans adapt to learner background
- Strong results at 8B/32B scale: state-of-the-art executability, personalization, and pedagogical quality vs. frontier LLMs and generic MAS frameworks

## Related Papers
- [[discobench-clarification-aware-deep-search-llm-search-agents-2606.27669]] — DiscoBench: Clarification-Aware Deep Search LLM Agents (related multi-agent planning and clarification/interaction)
- [[democratic-icai-debate-steering-principles-preferences-2606.28294]] — Democratic ICAI: Debating Our Way to Steering Principles from Preferences (related multi-agent preference elicitation)
- [[from-signals-to-transfer-probe-based-uncertainty-estimation-llm-2606.27679]] — From Signals to Transfer: Probe-Based Uncertainty Estimation (related transfer/probe methodology)
