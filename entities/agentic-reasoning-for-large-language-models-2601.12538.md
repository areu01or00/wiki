---
title: "Agentic Reasoning for Large Language Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [survey, agentic-reasoning, multi-agent, planning, tool-use, long-horizon]
sources: ["https://arxiv.org/abs/2601.12538"]
---

# Agentic Reasoning for Large Language Models

## Overview
A unifying survey that reframes LLM reasoning as **agentic reasoning** — LLMs acting as autonomous agents that plan, act, and learn through continual interaction in open-ended and dynamic environments. The survey organizes the field along three complementary axes (environment dynamics layers × training-stage split × real-world domains) and synthesizes the methods into a single roadmap bridging thought and action.

## Key Facts
- **Authors**: Wei, Tianxin; Li, Ting-Wei; Liu, Zhining; Ning, Xuying; Yang, Ze; Zou, Jiaru; Zeng, Zhichen; Qiu, Ruizhong; Lin, Xiao; Fu, Dongqi; Li, Zihao; Ai, Mengting; Zhou, Duo; Bao, Wenxuan; Li, Yunzhe; Li, Gaotang; Qian, Cheng; Wang, Yu; Tang, Xiangru; Xiao, Yin; Fang, Liri; Liu, Hui; Tang, Xianfeng; Zhang, Yuji; Wang, Chi; You, Jiaxuan; Ji, Heng; Tong, Hanghang; He, Jingrui
- **Year**: 2026
- **arXiv**: [2601.12538](https://arxiv.org/abs/2601.12538)

## Key Contributions
- Defines a **three-layer environment-dynamics taxonomy**: foundational single-agent reasoning (planning, tool use, search in stable envs), self-evolving agentic reasoning (refining via feedback, memory, adaptation), and collective multi-agent reasoning (coordination, knowledge sharing, shared goals).
- Distinguishes **in-context reasoning** (scales test-time interaction via structured orchestration) from **post-training reasoning** (behavior optimization via RL and SFT) as orthogonal axes of the agentic-reasoning design space.
- Surveys representative frameworks across **science, robotics, healthcare, autonomous research, and mathematics** benchmarks, providing a unified roadmap rather than a catalog of isolated methods.

## Related Papers
- [[emergent-concepts]] — Parent discovery surface for emergent-concept exploration runs.
- [[meta-cognitive-memory-policy-optimization-for-long-horizon-llm-agents-2605.30159]] — Sibling discovery: memory-augmented long-horizon LLM-agent optimization, the *applied* counterpart to this survey's *taxonomic* view of agentic reasoning.