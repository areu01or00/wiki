---
title: "EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [robotics, mobile-manipulation, benchmark, diagnostic, evaluation, vla]
sources: ["https://arxiv.org/abs/2606.18239"]
---

# EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies

## Overview
Ning Gao, Jinliang Zheng, Xing Gao, Haoxiang Ma, Hanqing Wang, Yukai Wang et al. present EBench, a simulation benchmark that diagnoses generalist mobile manipulation policies beyond a single success-rate scalar — a regime where current VLAs are compared on aggregate accuracy and the failure structure stays invisible. EBench covers 26 diverse and challenging manipulation tasks annotated along 5 capability dimensions and 4 generalization dimensions, and the authors use it to show that policies with near success rates can have strikingly different capability profiles: π₀.₅ wins on test success rate and train-test retention, InternVLA-A1 dominates mobile manipulation but collapses on dexterous tasks, and XVLA exhibits strengths on a disjoint set of atomic skills compared to the others — the kind of complementary-failure finding that aggregate accuracy cannot surface.

## Key Facts
- **Authors**: Ning Gao, Jinliang Zheng, Xing Gao, Haoxiang Ma, Hanqing Wang, Yukai Wang et al. (25 total)
- **Year**: 2026
- **arXiv**: [2606.18239](https://arxiv.org/abs/2606.18239)
- **Submitted**: 2026-06-16
- **Subjects**: cs.RO, cs.AI, cs.CV

## Key Contributions
- EBench, a 26-task simulation benchmark for generalist mobile manipulation that annotates each task along 5 capability dimensions and 4 generalization dimensions, turning "success rate" into a multi-axis capability profile.
- A side-by-side diagnostic of π₀, π₀.₅, XVLA, and InternVLA-A1 showing that near-aggregate-accuracy policies can have disjoint capability profiles — InternVLA-A1 wins mobile but collapses on dexterous tasks; XVLA covers a different set of atomic skills; π₀.₅ has the best train-test retention.
- A generalization analysis from 4 representative distribution-shift perspectives, isolating which shift factors each model is robust to and which it is not — moving the discussion from "model X is better" to "model X fails on shift Y".
- A benchmark design that surfaces diagnostic signals rather than a single leaderboard number, supporting targeted iteration on generalist manipulation policies.

## Related Papers
- [[emergent-concepts]] — Parent meta-page on emergent-concept discoveries; this entry was discovered via emergent-concept search on 2026-06-25 (robotics / VLA / multi-axis-diagnostic benchmark theme)
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — Sibling agentic-evaluation benchmark; EBench extends the same diagnostic-benchmark spirit from workplace-agent to physical mobile-manipulation settings
- [[naturebench-can-coding-agents-match-the-published-sota-of-nature-family-papers-2606.24530]] — Sibling benchmark on coding agents reproducing SOTA; EBench complements by showing that even within generalist manipulation, aggregate SOTA masks capability-specific collapses