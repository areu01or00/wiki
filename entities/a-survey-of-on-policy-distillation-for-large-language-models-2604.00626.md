---
title: "A Survey of On-Policy Distillation for Large Language Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [knowledge-distillation, post-training, on-policy-distillation, llm, survey]
sources: ["https://arxiv.org/abs/2604.00626"]
authors: ["Song, Mingyang", "and others"]
arxiv_id: "2604.00626"
---

# A Survey of On-Policy Distillation for Large Language Models

## Overview
First systematic survey of **on-policy distillation (OPD)** as an alternative to static SFT for transferring frontier LLM capabilities to smaller, deployable students. The survey identifies the structural weakness of static teacher-text imitation (the student never observes its own errors) and argues that on-policy sampling with teacher feedback is the load-bearing primitive for capability transfer in reasoning-intensive, long-horizon, and tool-use settings.

## Key Facts
- **Authors**: Mingyang Song and others
- **Year**: 2026
- **arXiv**: [2604.00626](https://arxiv.org/abs/2604.00626) (v1: 2026-04-01, v3: 2026-05-18, online 2026-06-18)
- **Type**: Survey (cs.CL + cs.LG)

## Key Contributions
- **Frames the static-vs-on-policy divide**: standard KD pipelines (train student on teacher-generated completions) carry a *structural* weakness — the student never sees its own rollout errors, so capability transfer degrades sharply on tasks that exceed the teacher's distribution (long chain-of-thought, multi-turn tool use, agent trajectories).
- **Taxonomy of on-policy distillation methods**: organizes 30+ OPD techniques by (a) feedback signal type (reward model, teacher rollouts, self-critique), (b) update mechanism (rejection sampling, importance-weighted SFT, PPO-style policy gradient), and (c) data-flow (single-turn vs multi-turn, single-teacher vs mixture-of-teachers).
- **Identifies the failure mode of "imitation collapse"**: when the student is trained only on teacher *successful* traces, the gap between teacher and student rollouts widens at deployment time, producing compounding errors on out-of-distribution tasks. OPD closes this gap by training on what the student itself can produce.
- **Provides an empirical comparison framework**: synthesizes results across MATH, HumanEval, MMLU-Pro, AgentBench, and tool-use benchmarks, showing OPD consistently outperforms static KD by 5-15 absolute points on reasoning tasks while remaining compute-competitive.
- **Open problems**: (i) extending OPD to multi-modal and embodied settings, (ii) teacher-student scaling laws (when does OPD break down as student shrinks), (iii) combining OPD with RLHF/DPO without reward-hacking pathologies.

## Related Papers
- [[discretizing-reward-models-2606.21795]] — Sibling discovery from Run 59 on reward-model oversensitivity as a structural failure mode that OPD's on-policy sampling is designed to mitigate
- [[efficientrollout-system-aware-self-speculative-decoding-for-rl-rollouts-2606.18967]] — Sibling discovery from Run 59 on system-aware speculative decoding for non-stationary RL rollouts, the deployment substrate OPD-trained students require
- [[danceopd-on-policy-generative-field-distillation-2606.27377]] — Recent same-paradigm paper on on-policy distillation (different domain — generative fields rather than LLMs) showing the OPD principle generalizes beyond text
- [[tropt-an-open-framework-for-unifying-and-advancing-discrete-text-optimization-2606.23496]] — Sibling discovery on discrete text optimization that intersects with OPD's textual-gradient subfield
