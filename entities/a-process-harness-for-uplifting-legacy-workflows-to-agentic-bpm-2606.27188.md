---
title: "A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agentic-workflow, business-process-management, multi-agent-systems, llm-governance]
sources: ["https://arxiv.org/abs/2606.27188"]
---

# A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO

## Overview
The process harness is a new mechanism for embedding agentic capabilities into legacy deterministic workflow engines without replacing them. A policy-governed agentic layer intercepts designated control points to contribute reasoning, adaptation, and oversight, while the engine retains structural authority. The Task-Decision-Flow (TDF) model formalizes three agent types — TaskAgent, DecisionAgent, and FlowAgent — each operating under explicit policy from the process FRAME.

## Key Facts
- **Authors**: Fabiana Fournier, Lior Limonad
- **Year**: 2026
- **arXiv**: [2606.27188](https://arxiv.org/abs/2606.27188)
- **Submitted**: 25 Jun 2026
- **Subjects**: Artificial Intelligence (cs.AI)

## Key Contributions
- **Process harness architecture**: Places a policy-governed agentic layer around legacy workflow engines without replacement — the engine keeps structural authority while agents contribute reasoning at designated control points
- **TDF model**: Task-Decision-Flow schema and execution semantics decomposing LLM reasoning across three policy-governed agent types
- **CUGA FLO realization**: Loan approval workflow demonstrating all three agent types and hook-driven regulatory override
- **Normative vs imperative reconciliation**: Agents handle normative requirements (policy-framed autonomy) while engines enforce imperative requirements (structural compliance)

## Related Papers
- [[towards-direct-latent-space-synthesis-for-parallel-branches-in-llm-agent-workflows-2606.14672]] — Latent space synthesis for parallel agent workflow branches, complementary to the process harness interception model
- [[benchmarking-open-ended-multi-agent-coordination-in-language-agents-2606.08340]] — Multi-agent coordination benchmarking relevant to the TaskAgent/DecisionAgent/FlowAgent tripartite architecture
- [[coordination-as-an-architectural-layer-for-llm-based-multi-agent-systems-2605.03310]] — Coordination as architectural layer for multi-agent systems, foundational to the TDF model
