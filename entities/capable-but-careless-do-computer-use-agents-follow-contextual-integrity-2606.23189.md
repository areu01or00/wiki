---
title: "Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity?"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agent-safety, computer-use-agents, contextual-integrity, privacy, evaluation, benchmark]
sources: ["https://arxiv.org/abs/2606.23189"]
---

# Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity?

## Overview
Computer-use agents (CUAs) act on a user's behalf across personal applications such as email, calendars, and to-do lists, and this cross-application access creates a privacy risk that has been largely overlooked: when an agent works in one context, it can pull in information from another that is inappropriate in that context. This paper introduces AgentCIBench, an evaluation harness that turns this risk into executable, deterministically scored scenarios targeting three common failure modes — visual co-location (prohibited items sitting next to the task target in the UI), task-ambiguity overshare (dense personal state dumped in response to under-specified prompts), and recipient misalignment (content sent to an addressee for whom it is inappropriate). Across 15 frontier agents, 11 leak on more than 50% of scenarios with an average leakage of 67.9%, and the failures persist when agents act end-to-end in the environment to complete the task.

## Key Facts
- **Authors**: Anmol Goel, Iryna Gurevych
- **Year**: 2026
- **arXiv**: [2606.23189](https://arxiv.org/abs/2606.23189) ([pdf](https://arxiv.org/pdf/2606.23189))
- **Date published**: 2026-06-22
- **Subjects**: cs.AI
- **Methodology**: AgentCIBench — executable, deterministically-scored contextual-integrity scenarios; evaluation of 15 frontier computer-use agents across three failure modes (visual co-location, task-ambiguity overshare, recipient misalignment); both prompt-response and end-to-end-environment evaluation.

## Key Contributions
- **AgentCIBench**: an evaluation harness that turns contextual-integrity risks into executable, deterministically-scored scenarios — releasing it as a pre-deployment safety check.
- **Three structured failure modes**: visual co-location, task-ambiguity overshare, and recipient misalignment, each isolating a distinct mechanism by which an agent leaks across context boundaries.
- **High failure rate across frontier agents**: 11 of 15 evaluated CUAs leak on more than 50% of scenarios, with average leakage 67.9%; failures persist end-to-end in the environment, ruling out prompt-only-vs-act-in-environment explanation.
- **Position as pre-deployment safety check**: contextual-disclosure testing should be a release gate for computer-use agents, parallel to refusal-classifier and capability-evaluation testing.

## Related Papers
- [[when-lower-privileges-suffice-investigating-over-privileged-tool-selection-in-llm-agents-2606.20023]] — sibling paper on agent-safety alignment, focused on privilege escalation in tool selection; together these papers cover the two under-evaluated axes of agent autonomy: what tool to use (privilege) and what information to disclose (context).
- [[agents-last-exam-2606.05405]] — capability-focused agent benchmark; complements this paper by addressing the *capability side* of the same agent class while this paper addresses the *safety side*.
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — workplace-focused agent benchmark with authentic session data; the workplace setting here is exactly the high-stakes context where AgentCIBench's failures would matter most.
- [[counsel-a-meta-evaluation-dataset-for-agentic-tasks-2606.21627]] — meta-evaluation for agentic tasks; the meta-evaluation framing (how do we know whether an evaluation is good?) applies equally to capability benchmarks like EnterpriseClawBench and safety benchmarks like AgentCIBench.
- [[emergent-concepts]] — parent meta-page that catalogued this paper as part of the LLM agent-safety / privacy / contextual-integrity theme.