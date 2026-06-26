---
title: "A Technical Taxonomy of LLM Agent Communication Protocols"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [llm-agent, multi-agent, communication-protocols, taxonomy, interoperability, distributed-agents]
sources: ["https://arxiv.org/abs/2606.19135"]
---

# A Technical Taxonomy of LLM Agent Communication Protocols

## Overview
Develops a technical taxonomy to classify and analyze LLM agent communication protocols, addressing the fragmented protocol landscape that presents a significant interoperability challenge for distributed multi-agent networks. Following an established iterative taxonomy-development method with five iterations across empirical-to-conceptual analysis, the work surfaces the load-bearing primitives that distinguish inter-agent protocols in the LLM-agent stack and proposes the meta-characteristic and ending conditions that future protocol designers should satisfy.

## Key Facts
- **Authors**: Sander, Linus; Gidey, Habtom Kahsay; Lenz, Alexander; Knoll, Alois
- **Year**: 2026
- **Date**: 2026-06-17
- **arXiv**: [2606.19135](https://arxiv.org/abs/2606.19135)
- **Categories**: cs.MA, cs.CL, cs.AI

## Key Contributions
- Provides the first systematic taxonomy of LLM agent communication protocols, defining the meta-characteristic (interoperability) and ending conditions for the protocol design space.
- Five iterative empirical-to-conceptual analysis rounds identify the structural axes along which protocols differentiate — message format, transport, discovery, state-synchronization, error-recovery — and the canonical design choices within each axis.
- Surfaces *communication-protocol-as-infrastructure* as a load-bearing primitive for distributed LLM-agent deployments where the canonical single-agent loop is structurally inadequate and robust communication between heterogeneous agents is the binding constraint.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this discovery was logged
- [[connect-the-dots-training-llms-for-long-lifecycle-agents-with-cross-domain-generalization-via-reinforcement-learning-2606.20002]] — Sibling long-lifecycle-agent work: Connect-the-Dots trains single agents for cross-domain generalization, Communication-Protocols-Taxonomy classifies the multi-agent infrastructure the long-lifecycle agents would compose with
- [[aohp-an-open-source-os-level-agent-harness-for-personalized-efficient-and-2606.23449]] — Sibling OS-level agent harness: AOHP provides the runtime substrate, Communication-Protocols-Taxonomy classifies the wire-level protocol layer the harness must speak
- [[critique-of-agent-model-2606.23991]] — Sibling agent epistemics: Critique-of-Agent-Model audits what counts as an agent, Communication-Protocols-Taxonomy surveys how agents talk to each other once the agency question is settled