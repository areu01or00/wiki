---
title: "When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [llm, agents, reliability, silent-failure, longitudinal-study, production-systems, taxonomy]
sources: ["https://arxiv.org/abs/2606.14589"]
---

# When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime

## Overview
An eight-week longitudinal study of silent failures in a personal-assistant LLM agent runtime in continuous production since March 2026 (40 scheduled jobs, 8 LLM providers, 4,286 unit tests, 827 governance checks). The paper documents 22 incidents with full root-cause postmortems in which one meta-pattern — a failure whose error signal never reaches a human in actionable form — manifested at least 28 times, and derives a five-class mechanism-oriented taxonomy.

## Key Facts
- **Authors**: Wu, Wei
- **Year**: 2026
- **arXiv**: [2606.14589](https://arxiv.org/abs/2606.14589)

## Key Contributions
- Derives a five-class, mechanism-oriented taxonomy: (A) environment and platform quirks, (B) design-assumption mismatches, (C) error swallowing and dilution, (D) chained hallucination and fabrication, (E) operational omission and forensic blind spots
- Identifies Class D ("chained hallucination and fabrication") as unique to LLM systems and the most dangerous: the system does not merely fail to report an error — the LLM transforms it into fluent, plausible narrative delivered to the user
- Coines the term "fail-plausible" — gray failure's differential observability escalated by LLMs' natural-language fluency
- **First paper in the wiki** to coin "fail-plausible" as a distinct LLM-specific failure mode and surface the LLM-as-narrator threat model in production agent runtimes

## Related Papers
- [[silent-failure-in-llm-agent-systems-the-entropy-principle-2606.08162]] — Sibling discovery from same run: mechanism-level entropy lens that complements this paper's taxonomy-first framing
- [[where-llm-agents-fail-and-how-they-can-learn-from-failures-2509.25370]] — Sibling discovery from same run: modular AgentErrorTaxonomy (memory/reflection/planning/action/system) that complements this paper's mechanism-oriented production framing
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — surfaces evaluation-side failure modes for long-horizon tool-use agents
- [[foresight-failure-detection-long-horizon-robotic-manipulation-2606.23085]] — failure-detection primitive for embodied long-horizon tasks