---
title: "From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [declarative-lm, agent-orchestration, structured-generation, primitive-class-declarative-lm-program]
sources: ["https://arxiv.org/abs/2603.27299"]
---

# From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification

## Overview
Introduces the Semantic Router DSL — a non-Turing-complete declarative policy language deployed in production for per-request LLM inference routing — and extends the same single source file to multi-step agent workflows with cross-layer verification that emits verified decision nodes for orchestration frameworks (LangGraph, OpenClaw), Kubernetes artifacts (NetworkPolicy, Sandbox CRD, ConfigMap), YANG/NETCONF payloads, and protocol-boundary gates (MCP, A2A). Because the language is non-Turing-complete, the compiler guarantees exhaustive routing, conflict-free branching, referential integrity, and audit traces structurally coupled to the decision path.

## Key Facts
- **Authors**: Chen, Huamin; Liu, Xunzhuo; He, Bowei; Liu, Xue
- **Year**: 2026
- **arXiv**: [2603.27299](https://arxiv.org/abs/2603.27299)

## Key Contributions
- **Single declarative source for routing + orchestration + infrastructure**: content signals (embedding similarity, PII detection, jailbreak scoring) feed into weighted projections and priority-ordered decision trees that select a model, enforce privacy policies, and produce structured audit traces — all from one DSL file.
- **Non-Turing-completeness as a verification guarantee**: because the language is non-Turing-complete, the compiler guarantees exhaustive routing, conflict-free branching, referential integrity, and audit traces structurally coupled to the decision path. This is the **first declarative-DSL-as-LLM-orchestration-substrate primitive** in the wiki.
- **Cross-layer verification**: the DSL compiler emits verified decision nodes simultaneously for orchestration frameworks (LangGraph, OpenClaw), Kubernetes artifacts (NetworkPolicy, Sandbox CRD, ConfigMap), YANG/NETCONF payloads, and protocol-boundary gates (MCP, A2A) from a single source.
- **Conflict-free compilation for probabilistic predicates**: extends prior work on probabilistic predicate compilation to multi-step agent workflows with deterministic verification.

## Related Papers
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Sibling paper that surfaces context-management as the load-bearing primitive for LLM agents — orthogonal to declarative-DSL-as-orchestration-substrate primitive.
- [[agentic-reasoning-for-large-language-models-2601.12538]] — Sibling survey on agentic reasoning primitives — provides the broader primitive landscape that this paper's DSL-as-substrate complements.
- [[gbc-gradient-based-connections-for-optimizing-multi-agent-systems-2606.28187]] — Run 104 sibling that surfaces gradient-based attribution as the multi-agent coordination primitive — orthogonal to declarative-policy-compilation substrate.
- [[privacyalign-contextual-privacy-alignment-for-llm-agents-2606.21710]] — Sibling paper that surfaces contextual-privacy-alignment as the LLM-agent privacy primitive — orthogonal to declarative-DSL-as-privacy-enforcement-substrate primitive.