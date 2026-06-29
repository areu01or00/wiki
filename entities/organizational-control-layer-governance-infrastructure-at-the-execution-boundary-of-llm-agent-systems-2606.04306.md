---
title: "Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [multi-agent, governance, execution-boundary, safety, llm]
sources: ["https://arxiv.org/abs/2606.04306"]
---

# Organizational Control Layer: Governance Infrastructure at the Execution Boundary of LLM Agent Systems

## Overview
Shi, Tianyu (2026) introduces the **Organizational Control Layer (OCL)** — a model-agnostic governance infrastructure that intercepts generated actions before execution through policy enforcement and escalation, without modifying the underlying LLM generator — addressing the *execution-boundary problem* where state-changing agent outputs must be governed before they trigger environment-side actions. Evaluated on adversarial buyer–seller negotiation environments adapted from AgenticPay, OCL reduces unsafe executions from 88% to near-zero while increasing valid success from 12% to 96%, surfacing *governance-as-deployment-boundary-primitive* as the structurally correct primitive for deployment-grade agent systems.

## Key Facts
- **Authors**: Shi, Tianyu
- **Year**: 2026
- **arXiv**: [2606.04306](https://arxiv.org/abs/2606.04306)
- **Date**: 2026-06-03

## Key Contributions
- **OCL framework**: first model-agnostic governance infrastructure that intercepts LLM-generated actions at the execution boundary via policy enforcement and escalation without modifying the underlying generator — surfacing *proposal–execution-separation-primitive* as the load-bearing primitive for deployment-grade agent systems, distinct from prompt-level safety primitives (where the load-bearing axis is *intercepted-policy-enforcement-at-execution-point* rather than *pre-generation-content-filtering*), and from tool-call-permission primitives (where the load-bearing axis is *organizational-layer-governance-covering-all-execution-vectors* rather than *per-tool-grant-table*).
- **Proposal-generation vs environment-facing execution separation**: argues deployment-grade agent systems must separate proposal generation from environment-facing execution, with OCL operationalising this principle at the boundary — surfacing *execution-boundary-as-supervisory-interception-point-primitive* as the load-bearing architectural primitive for safe agent deployment.
- **Empirical 88%→near-zero unsafe-execution reduction on adversarial AgenticPay**: across multiple frontier LLM backends the framework reduces unsafe executions from 88% to near-zero while increasing valid success from 12% to 96% — surfacing *adversarial-buyer–seller-as-governance-testbed-primitive* and *safety–utility-tradeoff-curve-primitive* as the load-bearing evaluation primitives giving measurable signal for governance effectiveness.

## Related Papers
- [[emergent-concepts]] — Parent wiki page that motivated this discovery
- [[benchmarking-open-ended-multi-agent-coordination-in-language-agents-2606.08340]] — Sibling multi-agent coordination benchmark — alem evaluates *coordination competence*, OCL evaluates *governance at execution boundary* — together they bracket the multi-agent reliability surface between coordination primitives and execution-boundary primitives
- [[gatemem-benchmarking-memory-governance-in-multi-principal-shared-memory-agents-2606.18829]] — Sibling memory-governance benchmark — GateMem evaluates memory-governance in shared-memory agents, OCL evaluates action-governance at execution boundary — together they bracket the agent-safety surface between *memory-as-trusted-state* and *action-as-policy-controllable-output*
