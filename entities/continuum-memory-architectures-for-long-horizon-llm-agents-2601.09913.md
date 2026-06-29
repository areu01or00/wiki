---
title: "Continuum Memory Architectures for Long-Horizon LLM Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent-memory-architecture, continuum-memory, persistent-storage, selective-retention, associative-routing, temporal-chaining, higher-order-consolidation, rag-vs-cma, architectural-primitive, llm]
sources: ["https://arxiv.org/abs/2601.09913"]
---

# Continuum Memory Architectures for Long-Horizon LLM Agents

## Overview
Logan formalizes the **Continuum Memory Architecture (CMA)** — a class of systems that maintain and update internal state across interactions through five architectural requirements: persistent storage, selective retention, associative routing, temporal chaining, and consolidation into higher-order abstractions — arguing that standard RAG's treatment of memory as a stateless lookup table is the load-bearing structural limitation blocking long-horizon agents, and presenting empirical probes that demonstrate CMA is a necessary architectural primitive for tasks that require *accumulating, mutating, and disambiguating* memory rather than mere retrieval. The work surfaces the formal-architectural-primitive facet of agent-memory research — distinct from cognitive-mechanism or empirical-performance framings — by specifying what *must* hold architecturally for any long-horizon memory system to function, while honestly flagging open challenges around latency, drift, and interpretability.

## Key Facts
- **Authors**: Logan, Joe
- **Year**: 2026
- **arXiv**: [2601.09913](https://arxiv.org/abs/2601.09913)
- **Submitted**: 2026-01-14

## Key Contributions
- **Continuum Memory Architecture (CMA) primitive-formalization** that specifies five architectural requirements for long-horizon agent memory: persistent storage (state survives across turns), selective retention (forgetting rather than retaining), associative routing (retrieval conditioned on context), temporal chaining (recency-aware traversal), and consolidation into higher-order abstractions (rolling episodic events into semantic knowledge). Defining CMA as a *class of systems* rather than a single design is the contribution that lets downstream work situate itself relative to a primitive rather than compete on a benchmark.
- **RAG-vs-CMA structural diagnostic framework** that identifies four capabilities RAG structurally cannot provide — knowledge updates, temporal association, associative recall, contextual disambiguation — and demonstrates CMA's consistent advantages on empirical probes that isolate each capability, surfacing the *RAG-vs-CMA-as-load-bearing-memory-primitive* distinction rather than a benchmark-result one.
- **Architectural-primitive primitive** as the load-bearing *primitive-class primitive* where the contribution is to *name and require* a class of solutions (similar to how the Lake-Mercer framework names a class of online RL algorithms) rather than to present a single system — distinct from cognitive-mechanism primitive work (which import mechanisms from cognitive science) and from benchmark-comparison primitive work (which compares systems empirically).
- **Honest challenge enumeration** (latency, drift, interpretability) — surfaces the open problems with CMA-class systems so downstream work has a falsifiable target rather than an aspirational primitive.
- **Behavioral-advantages-not-architectural-blueprints contribution** that surfaces what a Continuum Memory Architecture *behaves like* under probes (knowledge-update consistency, temporal-association accuracy, associative-recall completeness, contextual-disambiguation precision) rather than committing to specific implementations.

## Related Papers
- [[memory-r2-fair-credit-assignment-for-long-horizon-memory-augmented-llm-agents-2605.21768]] — Sibling memory-augmented-agent entry; CMA formalizes the architectural primitive that Memory-R2 then applies to credit assignment, with CMA providing the memory substrate and Memory-R2 providing the credit-assignment policy over that substrate.
- [[hela-mem-hebbian-learning-and-associative-memory-for-llm-agents-2604.16839]] — Sibling associative-memory entry; CMA's persistent-storage-and-associative-routing requirement is structurally similar to HeLa-Mem's Hebbian-associative-memory primitive — CMA names the class, HeLa-Mem implements one instance with biological plasticity.
- [[human-inspired-memory-architecture-for-llm-agents-2605.08538]] — Sibling biological-cognitive-mechanism entry; CMA specifies *what architectural requirements must hold*, human-inspired architecture specifies *which biological mechanisms implement those requirements* — the two are complementary framings of the same problem space.
- [[emergent-concepts]] — Meta parent page for emergent-concept chains from run-89 AGENT-MEMORY-ARCHITECTURE-PROBE.
