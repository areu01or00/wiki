---
title: "From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [survey, llm-agent, evidence-tracing, provenance, trust, audit, cs.CL]
sources: ["https://arxiv.org/abs/2606.04990"]
---

# From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents

## Overview
First systematic survey of *evidence tracing* and *execution provenance* for LLM-based agents — the discipline of reconstructing which observations, tool calls, retrievals, and intermediate reasoning steps justify each agent decision. Frames agent autonomy (planning, tool use, retrieval, memory access, environmental interaction, multi-agent collaboration) as a trust problem that execution-provenance infrastructure must solve, and inventories the techniques (trace reconstruction, lineage tracking, provenance-aware retrieval, audit primitives) needed to make agent behavior verifiable post-hoc.

## Key Facts
- **Authors**: Wang, Yiqi; Zhang, Jiaqi; Cai, Taotao; Liu, Zirui; Sun, Qingqiang
- **Year**: 2026
- **arXiv**: [2606.04990](https://arxiv.org/abs/2606.04990)
- **Submitted**: 2026-06-03

## Key Contributions
- First survey dedicated to evidence-tracing and execution-provenance infrastructure for LLM-based agents — establishes the *provenance primitive* as the load-bearing concept for post-hoc verification of agent decisions
- Conceptual framework linking agent autonomy (planning / tool use / retrieval / memory / environment / multi-agent) to the trust requirements that execution-provenance must satisfy
- Inventory of trace-reconstruction, lineage-tracking, provenance-aware retrieval, and audit primitives needed to make agent behavior verifiable
- Bridges the gap between agent-capability research and agent-deployment audit requirements — the structural axis that agent-trust certification systems (e.g., Pre-Deployment Assurance) implicitly assume but do not specify

## Related Papers
- [[toward-pre-deployment-assurance-enterprise-ai-agents-ontology-grounded-simulation-trust-certification-2606.04037]] — Pre-Deployment Assurance (06-02) — ontology-grounded certification framework, sibling trust-certification surface — together they bracket agent-trust between *pre-deployment scenario verification* (Pre-Deployment Assurance) and *post-hoc execution provenance* (this survey)
- [[trustmem-trustworthy-memory-consolidation-llm-agents-long-term-memory-2606.25161]] — TrustMem (06-23) — memory-transition verification, sibling reliability-primitive surface — together they bracket agent-trust between *transition-level reliability verification* (TrustMem) and *trace-level evidence reconstruction* (this survey)
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — CALVERT (06-21) — calibrated verifier telemetry, sibling verifier-integrity surface — together they bracket the verifier-integrity axis between *telemetry calibration* (CALVERT) and *post-hoc trace reconstruction* (this survey)
- [[dont-blindly-trust-it-how-unreliable-feedback-breaks-tool-using-llm-agents-2606.21409]] — Don't Blindly Trust It (06-19) — feedback-reliability controlled comparison, sibling observation-reliability surface — together they bracket the agent-observation-trust surface between *observation-input reliability* (Don't-Blindly-Trust) and *trace-output provenance* (this survey)