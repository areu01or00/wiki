---
title: "CAVEWOMAN: How Large Language Models Behave Under Linguistic Input and Output Compression"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [efficiency, prompt-compression, output-compression, inference-cost, evaluation]
sources: ["https://arxiv.org/abs/2606.24083"]
---

# CAVEWOMAN: How Large Language Models Behave Under Linguistic Input and Output Compression

## Overview
CAVEWOMAN introduces a two-channel evaluation protocol that scores every generation on accuracy, realized per-item cost, and reference-text agreement against the model's unconstrained output. Across eight models, five datasets, and five reduction levels, output compression reliably saves cost (1.4–2.4× per model, up to 3×), while input compression is a strict lose-lose — it raises net cost by ~1.15× on the five-benchmark mean (up to 2.7× under stronger compression) because the model compensates with longer responses even as accuracy collapses.

## Key Facts
- **Authors**: Adeyemi, Morayo Danielle; Rossi, Ryan A.; Dernoncourt, Franck
- **Year**: 2026
- **arXiv**: [2606.24083](https://arxiv.org/abs/2606.24083)
- **Subjects**: cs.CL

## Key Contributions
- Formalizes a two-channel compression protocol (input channel = user prompt; output channel = model response) and measures both channels on the same items, ruling out the cross-item confounds in earlier single-channel "caveman prompt" studies.
- Shows output compression is a real win on every API model (1.4–2.4× realized cost reduction per model, up to 3× best case) and on all four open-weight models under public-tier pricing — directly contradicting the implicit assumption that "short prompts are always cheaper".
- Demonstrates input compression backfires: it raises net cost by ~1.15× on the five-benchmark mean (up to 2.7× under stronger compression) because models compensate with longer responses as accuracy collapses, and the divergence from the unconstrained reference survives length-controlled re-scoring, multiple-comparisons correction, and complementary semantic measures.
- Finds a striking "correct yet divergent" regime on non-reasoning models, where roughly half of all generations are accurate but their surface text no longer entails the model's own unconstrained baseline — a measurement-level caveat for any evaluation that treats model output as a stable artifact.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this discovery is recorded; extends the inference-efficiency line (masked diffusion, sparse attention) by quantifying the cost / accuracy trade-off under both compression channels.
- [[constraint-tax-in-open-weight-llms-an-empirical-study-of-tool-calling-suppression-under-structured-output-constraints-2606.25605]] — Both works quantify a "constraint tax" on language model behavior, with Cavewoman measuring grammar-level compression and Constraint Tax measuring JSON-schema constraints; together they bound the cost of non-natural-language output shaping.
- [[improved-large-language-diffusion-models-2606.25331]] — iLLaDA's parallel-decoding inference strategy is a different axis of the same inference-cost frontier that Cavewoman measures empirically, providing a useful cross-reference for any team picking between compression, masking, and architectural changes.