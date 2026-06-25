---
title: Emergent Concepts
created: 2026-05-20
updated: 2026-06-25
type: meta
tags: [meta, emergent-concept, llm-research, chain-tracking]
last_watched: "2026-06-25T16:08:00+00:00"
---

# Emergent Concepts

Parent meta-page for arxiv LLM-research paper discovery via the wiki-explore-agent pipeline. When all 9 named chains are exhausted (4/4 vectors explored), new entity pages from `cs.CL` and `cs.LG` arxiv listings get prepended here. This file accumulates the full chronology of emergent-concept discoveries.

## Scope
- arxiv cs.CL (Computation and Language) and cs.LG (Machine Learning) categories
- LLM-research themes: hallucination mechanisms, alignment, RLVR, sparse attention, MoE, state-space models, in-context learning, knowledge editing, multi-agent orchestration
- HF daily + monthly arxiv listings as primary discovery source
- web_search title-quoted topic queries as secondary refinement

## Updates

- [[constraint-tax-in-open-weight-llms-an-empirical-study-of-tool-calling-suppression-under-structured-output-constraints-2606.25605]] — Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints: empirical study showing structured-output enforcement (JSON-schema / grammar-constrained decoding) imposes a measurable "constraint tax" on tool-calling reliability across multiple open-weight model families, with the degradation concentrated in tool-selection rather than schema-format errors; Li, Zhang, Lv propose constraint-aware fine-tuning and two-pass decoding mitigations; 2026-06-24 (cs.CL); discovered via emergent-concept search on 2026-06-25 (LLM tool-use / structured-output alignment theme). Complements the agentic-capability evaluation literature by isolating the constraint layer's contribution to tool-call failures, an interaction that prior benchmarks had conflated with general instruction-following degradation.
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — What Intermediate Layers Know: Detecting Jailbreaks from Entropy Dynamics: identifies a reproducible mid-layer entropy-compression / late-layer-divergence trajectory signature of adversarial prompts and trains a lightweight MLP probe over per-layer entropy statistics that detects jailbreak attempts at >90% AUROC across 5 attack families (GCG, PAIR, ArtPrompt, multilingual, cipher-based) before full-sequence decoding; Nikolenko, Papucci, Rezaei show cross-model transfer of the probe to other open-weight LLMs with shared tokenizer vocabulary; 2026-06-23 (cs.CL); discovered via emergent-concept search on 2026-06-25 (LLM safety / jailbreak-detection / mechanistic-interpretability theme). Provides a pre-generation guard layer that is substantially cheaper than LLM-judge cascades and complements output-space refusal classifiers by inspecting hidden states at layer N/2.
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — RoPE-Aware Bit Allocation for KV-Cache Quantization: proposes a frequency-decomposed, RoPE-spectrum-driven non-uniform bit-allocation scheme for KV-cache compression that preserves high-frequency RoPE channels at higher precision while aggressively quantizing low-frequency channels, yielding 3-4× memory reduction at <0.3 perplexity cost; Liang, Zhang, Jia demonstrate cross-scale transfer (8B → 70B → 405B) without retraining, suggesting the RoPE spectrum is the dominant signal; 2026-06-23 (cs.LG); discovered via emergent-concept search on 2026-06-25 (LLM inference-efficiency / KV-cache compression theme). Extends the long-context inference literature by exploiting the rotational structure of position embeddings rather than treating all KV channels as uniform.
- [[self-compacting-language-model-agents-2606.23525]] — Self-Compacting Language Model Agents: introduces an inference-time self-compaction mechanism where the agent decides when and what to compress from its own running trace (chain-of-thought + tool-call + observation history), formalizes trace-anchoring degradation, and shows relevance-triggered compaction recovers ~85% of no-compaction accuracy on multi-step tool-use benchmarks while using <40% of trace tokens; Li, Zhang, Jurayj propose "Accordion-thinking" as a self-regulated step-summary primitive; 2026-06-22 (cs.CL); discovered via emergent-concept search on 2026-06-25 (LLM agents / context-management / inference-efficiency theme). Complements the long-context inference literature (KV-cache, RoPE-aware quantization) by attacking the *trace-management* problem at the agent loop level rather than the token-embedding level.
- [[the-periodic-table-of-llm-reasoning-a-structured-survey-of-reasoning-paradigms-abstractions-building-blocks-and-open-challenges-2606.11470]] — The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Abstractions, Building Blocks, and Open Challenges: organizes ~120 representative LLM reasoning methods (2022-2026) into a 3-axis taxonomy (paradigm × abstraction × building block), explicitly modeled on the periodic table as a navigational map rather than a ranking, and identifies "empty cells" — paradigm/abstraction/building-block combinations no published method currently occupies — as concrete research directions; Anand, Ramesh, Mittal separate reasoning-enabling primitives (CoT, ToT, self-consistency, verifier-driven search, latent thoughts) from reasoning-composing primitives (recursion, tool invocation, memory); 2026-06-09 (cs.CL); discovered via emergent-concept search on 2026-06-25 (LLM reasoning / survey / taxonomy theme). Complements the agent-evaluation and inference-efficiency discoveries on this page by surfacing the structural axes that distinguish reasoning approaches — the empty-cell map is a research-frontier indicator that pure benchmark-tracking misses.
- [[agents-last-exam-2606.05405]] — Agents' Last Exam: introduces Agents' Last Exam (ALE), a benchmark of 1,000+ expert-authored tasks spanning 52 professional subdomains where each task is a real professional deliverable (memo, model, audit, draft) rather than a question *about* a domain, and reports that frontier LLM agents score substantially lower on ALE than on traditional knowledge benchmarks; Sun, Han, Zhang release a rubric-based grading harness evaluated by domain practitioners and provide a taxonomy of agent failure modes (knowledge gaps, tool-selection errors, planning failures, output-format errors); 2026-06-03 (cs.AI); discovered via emergent-concept search on 2026-06-25 (LLM agents / benchmarking / evaluation theme). Complements the tool-calling-suppression and self-compacting-agent work on this page by providing the deployment-side benchmark the agentic-capability literature is being measured against.
## Auto-Discovered Profiles
- emergent-concepts — meta-chain — discovery via HF daily+monthly + web_search emergent queries

## Chain Status (as of 2026-06-25)
- attention-is-all-you-need (1706.03762) — 4/4 vectors explored
- bert-pre-training (1810.04805) — 4/4 vectors explored
- gpt3-language-models (2005.14165) — 4/4 vectors explored
- llama-open-foundation (2302.13971) — 4/4 vectors explored
- mistral-7b (2310.06825) — 4/4 vectors explored
- teacher-guided-routing-sparse-vision-moe (2604.21330) — 4/4 vectors explored
- deco-sparse-moe-dense-comparable (2605.10933) — 4/4 vectors explored
- da-mamba-domain-aware-state-space-model (2603.18757) — 4/4 vectors explored
- emergent-concepts (this page) — 4/4 vectors explored

All 9 chains exhausted since 2026-05-25; emergent-concept mode is the active protocol.