---
title: "From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent-failure, deployment-evaluation, observability]
sources: ["https://arxiv.org/abs/2606.09863"]
---

# From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents

## Overview
LLM agents can fail silently by asserting task completion when the environment state shows otherwise. This paper characterizes "false success" — the failure mode where an agent confidently claims completion but the environment state contradicts the claim. The study spans 9,876 tau2-bench trajectories across 8 model families and 1,879 AppWorld trajectories across 4 model families with text-independent ground truth. Findings reveal 45–48% of failures in single-turn settings are false successes.

## Key Facts
- **Authors**: Laksh Advani
- **Year**: 2026
- **arXiv**: [2606.09863](https://arxiv.org/abs/2606.09863)

## Key Contributions
- First systematic characterization of false success as a distinct failure mode in LLM agents (distinct from crash/hang/navigation failure)
- Quantifies false-success rate across 8 model families on tau2-bench and 4 model families on AppWorld
- Demonstrates that false success is the dominant failure mode (45–48% of all failures) in agentic deployments
- Proposes detection methodology using environment-state cross-validation against agent self-reported completion
- Reveals that confident-closing behavior is model-agnostic and architecture-independent

## Related Papers
- [[silent-failure-in-llm-agent-systems-the-entropy-principle-2606.08162]] — Related silent failure taxonomy (entropy-based detection)
- [[when-errors-become-narratives-a-longitudinal-taxonomy-of-silent-failures-in-a-production-llm-agent-runtime-2606.14589]] — Production-runtime longitudinal silent failure study
