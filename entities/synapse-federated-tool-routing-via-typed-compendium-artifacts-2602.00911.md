---
title: "Synapse: Federated Tool Routing via Typed Compendium Artifacts"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [collaborative-learning, federated, tool-routing, typed-artifacts, multi-agent]
sources: ["https://arxiv.org/abs/2602.00911"]
---

# Synapse: Federated Tool Routing via Typed Compendium Artifacts

## Overview
Synapse introduces typed federated artifacts as the unit of collaboration in federated LLM training — schema-validated objects whose declared field structure makes per-field differential privacy, schema-aware merging, and cross-architectural transfer first-class operations rather than heuristic approximations. The framework is instantiated for federated tool routing across heterogeneous LLM clients, addressing communication-cost, schema-heterogeneity, and tool-usage-diversity challenges that have limited prior federated LLM work.

## Key Facts
- **Authors**: Abhijit Chakraborty, Sandipan De, Yash Shah, Chahana Dahal, Vivek Gupta
- **Year**: 2026
- **arXiv**: [2602.00911](https://arxiv.org/abs/2602.00911)
- **Online date**: 2026-06-04

## Key Contributions
- **Typed federated artifacts**: schema-validated objects with declared field structure — replaces flat units (weights, prompts, raw examples) that carry no type signature on which privacy, conflict resolution, or cross-model transfer can dispatch as well-defined operations
- **Per-field differential privacy**: differential privacy applied per-schema-field rather than at the unit level, enabling fine-grained privacy budget allocation
- **Schema-aware merging**: cross-client compendium merging via schema operations rather than heuristic averaging — supports heterogeneous client schemas
- **Cross-architectural transfer**: typed artifacts transfer across model architectures as first-class operations, not post-hoc heuristics
- **SYNAPSE instantiation**: federated tool-routing compendium for cross-client LLM tool routing; addresses communication-cost, heterogeneity, tool-usage-diversity challenges
- **Adaptive text masking + noise injection** in decentralized framework to maintain utility while reducing information leakage
- **Compendium-as-evidence primitive**: typed artifacts double as evidence records for downstream retrieval and replay, treating compendium entries as both knowledge transfer units and audit-trace units

## Related Papers
- [[a-technical-taxonomy-of-llm-agent-communication-protocols-2606.19135]] — Taxonomy of LLM agent communication protocols that Synapse's typed-artifact schema extends into the federated setting
- [[cooperative-llm-agents-with-uncertainty-aware-task-allocation-2606.28182]] — Sibling Run 92 pick — LLawCo cooperative-laws primitive for embodied cooperation alignment, complements Synapse's typed federated routing
- [[multi-agent-transactive-memory-knowledge-sharing-across-heterogeneous-agent-populations-2606.19911]] — Sibling Run 92 pick — population-of-agents memory infrastructure that Synapse's federated routing can dispatch to