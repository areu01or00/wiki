---
title: "AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agent, os-harness, aosp, agent-infrastructure, security, mobile]
sources: ["https://arxiv.org/abs/2606.23449"]
---

# AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction

## Overview
AOHP (Android Open Harness Project) is an OS-level agent harness built on top of AOSP that treats AI agents as first-class OS actors rather than applications. It introduces three agent-oriented system mechanisms — personalized service composition, efficient agent interfaces, and secure information flow — and reports large gains over conventional Android execution paths (+21.12% task-completion rate, −51.55% token cost) on a benchmark of challenging OS-agent tasks.

## Key Facts
- **Authors**: Zhao, Shanhui; Liu, Jiacheng; Liu, Guohong; Yan, Jichao; Ye, Jialei
- **Year**: 2026
- **arXiv**: [2606.23449](https://arxiv.org/abs/2606.23449)
- **Subjects**: cs.AI

## Key Contributions
- Argues that current end-user OSes (including Android) are application-centric and lack native agent abstractions, forcing agents to compensate with brittle prompt-level workarounds that drive up token cost and surface area for security risks.
- Builds AOHP on AOSP as an open testbed for "agent-native" OS research, preserving the Android ecosystem while exposing agents as first-class actors (personalized service composition, efficient agent interfaces, secure information flow).
- Reports a +21.12 percentage-point lift in task-completion rate and a 51.55% reduction in token cost on challenging OS-agent benchmarks, with explicit security-policy compliance evaluation.
- Positions OS-level primitives (process isolation, intent flow, permission policy) as a research substrate for the next generation of tool-using agents, complementing higher-level agent-loop work.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this discovery is recorded; complements the agent-benchmarking literature (Tmax, PhoneBuddy) by attacking the OS substrate rather than the agent loop.
- [[when-lower-privileges-suffice-investigating-over-privileged-tool-selection-in-llm-agents-2606.20023]] — Over-Privileged Tool Selection: AOHP's secure-information-flow mechanism is an OS-level analog of the privilege-minimization finding, and the two together sketch a stack from syscall up to tool-selection policy.
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — Both works evaluate agents on multi-application, security-sensitive workflows; AOHP supplies a substrate, EnterpriseClawBench measures an instance on top of it.