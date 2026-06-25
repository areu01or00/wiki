---
title: "Critique of Agent Model"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agent-architecture, agency, epistemology, agent-evaluation, audit, xing]
sources: ["https://arxiv.org/abs/2606.23991"]
---

# Critique of Agent Model

## Overview
Eric Xing, Mingkai Deng, and Jinyu Hou deliver an epistemic audit of "agent" as a term of art in current LLM systems, arguing that genuine agency requires goal/identity/decision/self-regulation/learning structures to be internalized within the system itself rather than assembled through external scaffolding — and propose the Goal-Identity-Configurator (GIC) architecture for what they call "agentive" systems. The piece lands at a moment when the field has been marketing LLM-toolchains as "coding agents" and "AI co-scientists" while simultaneously entertaining speculative "machine agency" risk narratives, and Xing et al. argue both framings collapse without a precise distinction between *agentic* (engineered workflows) and *agentive* (endogenous capability) systems.

## Key Facts
- **Authors**: Eric Xing, Mingkai Deng, Jinyu Hou
- **Year**: 2026
- **arXiv**: [2606.23991](https://arxiv.org/abs/2606.23991)
- **Subjects**: cs.AI, cs.LG, cs.MA, cs.RO
- **Submitted**: 2026-06-22

## Key Contributions
- A five-dimension framework for classifying agent architectures (goal, identity, decision-making, self-regulation, learning), grounded in Cartesian agency-internalism and science-fiction portrayals of autonomous beings.
- A sharp terminological distinction between *agentic* systems (competence in engineered workflows) and *agentive* systems (capabilities arising endogenously, including social interaction) — defining the boundary between systems designed for prescribed tasks and those capable of open-world operation.
- The Goal-Identity-Configurator (GIC) reference architecture for a general-purpose agentive system, combining hierarchical goal decomposition, identity evolution, simulative reasoning grounded in a separately trained world model, learned self-regulation, and self-directed learning from both real and simulated experience.
- An auditability/controllability/safety discussion for agentive systems that possess greater autonomy while remaining under human oversight — proposing internalized self-regulation as the load-bearing primitive for safe scaling beyond prescribed-task regimes.

## Related Papers
- [[emergent-concepts]] — Parent meta-page on emergent-concept discoveries; this entry was discovered via emergent-concept search on 2026-06-25 (LLM-agent epistemology / agency-internalism / GIC architecture theme)
- [[causal-discovery-in-the-era-of-agents-2606.23608]] — Sibling entry on epistemological audit of LLM-augmented work; both papers surface the same gap between surface capabilities and underlying mechanism in the agent setting
- [[capable-but-careless-do-computer-use-agents-follow-contextual-integrity-2606.23189]] — Sibling entry on agent-capability audit; Critique of Agent Model pushes the audit question one level deeper from "do agents follow rules" to "do agents have the structures required to follow rules internally"
- [[agent-orchestration]] — Parent meta-page on agent-system organization; GIC's internalism framing is the architecture-side counterpart to the orchestration-side scaffold-thickening trend
