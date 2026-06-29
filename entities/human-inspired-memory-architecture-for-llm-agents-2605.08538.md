---
title: "Human-Inspired Memory Architecture for LLM Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent-memory-architecture, biological-cognitive-mechanism, sleep-consolidation, interference-forgetting, engram-maturation, reconsolidation, entity-kg, multi-cue-retrieval, synthetic-calibration, eval-leakage-mitigation, llm]
sources: ["https://arxiv.org/abs/2605.08538"]
---

# Human-Inspired Memory Architecture for LLM Agents

## Overview
Kerestecioglu, Robsky, Vasters, Sharma, and Kesselman introduce a biologically-grounded memory architecture for LLM agents that imports six cognitive mechanisms from human memory theory — sleep-phase consolidation, interference-based forgetting, engram maturation, reconsolidation upon retrieval, entity knowledge graphs, and hybrid multi-cue retrieval — and pair them with a synthetic calibration methodology that derives all pipeline thresholds without benchmark data exposure, eliminating a common source of evaluation leakage. Evaluated on a real VSCode issue-tracking workload (13K issues, 120K events) and LongMemEval at streaming-M-tier (475 sessions, ~540K unique turns), dedup-based consolidation achieves 97.2% retention precision with 58% store reduction, and at a 200K context budget matches raw-retrieval accuracy while exposing a tunable accuracy/store-size operating curve.

## Key Facts
- **Authors**: Kerestecioglu, Doga; Robsky, Alexei; Vasters, Clemens; Sharma, Anshul; Kesselman, Yitzhak
- **Year**: 2026
- **arXiv**: [2605.08538](https://arxiv.org/abs/2605.08538)
- **Submitted**: 2026-05-08

## Key Contributions
- **Six-mechanism biologically-grounded architecture** mapping distinct human-memory primitives to specific LLM-agent failure modes: (1) sleep-phase consolidation of episodic traces into semantic knowledge, (2) interference-based forgetting to drop redundant co-active events, (3) engram maturation so memories strengthen with downstream utility, (4) reconsolidation upon retrieval so retrieved traces are merged with current context rather than returned verbatim, (5) entity knowledge graphs that link events around named entities for multi-hop retrieval, (6) hybrid multi-cue retrieval combining lexical, temporal, semantic-graph, and surprise signals.
- **Synthetic-only calibration methodology** that derives every threshold (consolidation strength, interference decay, engram-maturation rate, retrieval fusion weights) without exposure to benchmark data, eliminating a structural source of evaluation leakage present in earlier memory systems.
- **VSCode issue-tracking workload** as a production-fidelity eval (13K issues, 120K events): dedup-based consolidation achieves 97.2% retention precision with 58% store reduction (+21.8 pp over baseline).
- **First streaming M-tier LongMemEval evaluation** (475 sessions, ~540K unique turns): at a 200K-token context budget, the pipeline matches raw retrieval accuracy (70.1% vs 71.2%, overlapping 95% CI) while exposing a tunable accuracy/store-size operating curve; at S-tier scale, dedup-based consolidation yields +13.3 pp in preference recall.
- **Tunable operating-curve primitive** that exposes a hyperparameter knob trading retention accuracy against storage cost — distinct from prior systems where the accuracy/storage trade-off is implicit in the architecture rather than explicit.

## Related Papers
- [[memory-r2-fair-credit-assignment-for-long-horizon-memory-augmented-llm-agents-2605.21768]] — Sibling memory-augmented-agent entry; human-inspired architecture complements Memory-R2's credit-assignment focus by attacking the *write-side memory evolution* problem (six-mechanism consolidation + interference forgetting) rather than the *policy-side credit assignment* problem.
- [[zenbrain-a-neuroscience-inspired-7-layer-memory-architecture-for-autonomous-ai-s-2604.23878]] — Sibling neuroscience-grounded architecture; human-inspired architecture imports cognitive science at the *mechanism level* (sleep, interference, engram), ZenBrain imports neuroscience at the *layer level* (7-layer cortical-inspired stratification).
- [[hela-mem-hebbian-learning-and-associative-memory-for-llm-agents-2604.16839]] — Sibling Hebbian-associative memory framework; human-inspired architecture centers on six mechanisms with synthetic calibration, HeLa-Mem centers on Hebbian plasticity with associative memory and is the load-bearing sibling for biological-plausibility framings.
- [[emergent-concepts]] — Meta parent page for emergent-concept chains from run-89 AGENT-MEMORY-ARCHITECTURE-PROBE.
