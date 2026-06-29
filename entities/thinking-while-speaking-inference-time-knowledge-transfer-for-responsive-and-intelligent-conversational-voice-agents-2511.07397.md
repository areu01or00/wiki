---
title: "Thinking While Speaking: Inference-Time Knowledge Transfer for Responsive and Intelligent Conversational Voice Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [voice, conversational, inference-time, knowledge-transfer, latency, llm]
sources: ["https://arxiv.org/abs/2511.07397"]
---

# Thinking While Speaking: Inference-Time Knowledge Transfer for Responsive and Intelligent Conversational Voice Agents

## Overview
This paper addresses the fundamental responsiveness-vs-capability tension in voice agents by introducing *conversational infill*: a small talker model that both immediately generates contextually grounded responses to hide the latency of an external reasoner model and fluently integrates streamed reasoner knowledge into its responses during inference. The authors curate a 290,571-example synthetic dataset spanning six domains, demonstrate that conversational infill is learnable across seven widely used small language models (135M–1.7B parameters), and show that their system sustains millisecond-level time-to-first-response while closing the accuracy gap to within 6.3% of the corresponding frontier reasoner performance.

## Key Facts
- **Authors**: Srinivas, Vidya; Englhardt, Zachary; Patel, Shwetak; Iyer, Vikram
- **Year**: 2025 (online 2026-06-23)
- **arXiv**: [2511.07397](https://arxiv.org/abs/2511.07397)

## Key Contributions
- **Conversational infill primitive**: a new architecture pattern in which a small talker model both generates immediate contextually grounded responses AND fluently integrates streamed reasoner knowledge into its responses during inference — moving beyond the standard talker-OR-reasoner dichotomy.
- **290,571-example synthetic dataset across six domains**: a learnable dataset for conversational infill that supports training small models (135M–1.7B parameters) to perform the dual-talker-and-infill role.
- **Latency-capability Pareto frontier advance**: the system sustains millisecond-level time-to-first-response while closing the accuracy gap to within 6.3% of the corresponding frontier reasoner performance — a new point on the latency-capability Pareto frontier for voice agents.
- **Live user study (n=18) on Apple M2 SoC**: participants rank the system on par with frontier models overall, prefer it for retrieval-heavy tasks, and rate it significantly more responsive — providing deployment-validated evidence for the conversational infill approach.
- **Cross-model generalization across 7 small language models**: conversational infill is shown to be learnable across a diverse range of small language models, suggesting the primitive is broadly portable rather than model-specific.

## Related Papers
- [[distilling-examples-into-task-instructions-enhanced-in-context-2606.15641]] — Sibling work distilling examples into task instructions for enhanced in-context learning; complements Thinking While Speaking by distilling capabilities into compact in-context representations, sharing the goal of bringing frontier-model capabilities into compact inference-time footprints.
- [[the-african-language-tax-quantifying-the-cost-latency-and-context-penalty-of-tokenizing-2606.24460]] — Sibling work quantifying the cost, latency, and context penalty of tokenizing; complements Thinking While Speaking by characterizing the cost-side of the same latency-vs-capability frontier that conversational infill targets.
- [[an-empirical-study-of-many-shot-in-context-learning-for-machine-translation-of-low-resource-languages-2604.02596]] — Sibling work systematically characterizing many-shot in-context learning scaling behavior; complements Thinking While Speaking by exposing the dual budget of context-length cost and per-example informativeness that governs the small-talker-large-reasoner split.
- [[emergent-concepts]] — Parent meta-page listing all emergent-concept entities in the wiki.
