---
title: "Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle (AARRI-Bench)"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [benchmark, agent, evaluation, research, llm]
sources: ["https://arxiv.org/abs/2606.07462"]
---

# Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle (AARRI-Bench)

## Overview
AARRI-Bench is the first installment of the AARR (Act As a Real Researcher) benchmark series, designed to evaluate whether LLM agents can emulate the professionalism, thoroughness, and nuanced scientific judgment of human researchers in granular research-lifecycle scenarios — not just macro-level execution. The benchmark targets field sensitivity, research ethics, and nuanced scientific judgment, surfacing subtle-but-critical failures that macro-capability benchmarks miss.

## Key Facts
- **Authors**: Wang, Jiayu; Lv, Weijiang; Fu, Bowen; Fu, Jing; Song, Jiayi; Zhang, Lingyu; Xue, Lanxuan; Chen, Luodi; Xin, Zepeng; Li, Kaiyu; Cao, Xiangyong
- **Year**: 2026
- **arXiv**: [2606.07462](https://arxiv.org/abs/2606.07462)
- **Date**: 2026-06-05
- **Project URL**: https://github.com/AARR-bench/AARRI-bench

## Key Contributions
- Introduces the AARR benchmark series paradigm, in which agents are evaluated on their ability to *act like a real researcher* — researcher-role-mimicry as an evaluation surface distinct from macro-task-completion benchmarks.
- AARRI-Bench (Intern-level variant) reveals that even the best configuration (Mini-SWE-Agent + Claude Opus 4.7) achieves only 68.3% success rate, frequently overlooking subtle details obvious to human researchers.
- Frames research behavior — not just agent scaffolding — as the load-bearing variable for advancing researcher-grade AI agents.
- Provides data + evaluation harness for granular research-lifecycle scenarios spanning field sensitivity, research ethics, and nuanced scientific judgment.

## Related Papers
- [[connect-the-dots-training-llms-for-long-lifecycle-agents-with-cross-domain-generalization-via-reinforcement-learning-2606.20002]] — Sibling lifecycle-spanning agent work, but on cross-domain generalization rather than researcher-role-mimicry as evaluation surface.
- [[llm-based-scientific-peer-review-methods-benchmarks-reliability-challenges-2606.25057]] — Sibling survey on operational infrastructure for LLM-mediated scientific review, complementary to AARRI's lifecycle-as-evaluation angle.
- [[beyond-static-leaderboards-predictive-validity-evaluation-llm-agents-2606.19704]] — Sibling methodology paper on predictive validity of agent benchmarks; complements AARRI's researcher-role-mimicry paradigm.
- [[emergent-concepts]] — Parent wiki page tracking emergent-concept discoveries including this benchmark.