---
title: "The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [llm-safety, mechanistic-interpretability, refusal-mechanism, linear-feature, contrastive-logit-steering, alignment-robustness, jailbreak]
sources: ["https://arxiv.org/abs/2606.22686"]
---

# The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs

## Overview
Investigates whether safety compliance in aligned LLMs is a deep semantic decision or a manipulable linear feature — and introduces Contrastive Logit Steering (CLS), a zero-optimization framework that isolates the "refusal direction" by contrasting hidden states derived from safe and unrestricted system prompts, then operates directly on the output distribution rather than internal activations, serving as a diagnostic probe for alignment fragility. When coupled with prefix injection to bypass initial refusal reflexes, CLS induces a *phase transition* where guardrails collapse — across 7 model families, safety implementation is shown to be architecturally deterministic (Llama-3.1 exhibits a "Late Decision" topology easily bypassed in ~1s reaching 95% ASR, while Qwen-2.5 demonstrates "Early Divergence" by integrating safety mid-computation), with substantially higher attack success rates than established activation-level steering on Llama 2 (73% vs 22.6%) and Qwen 7B (91% vs 79.2%). Critically, the linearity enables *bidirectional control*: inverting the steering vector *hardens* models against jailbreaks without retraining, reframing the safety axis as both critical vulnerability and precise primitive for defense.

## Key Facts
- **Authors**: Ratnakar, Shivam; Vats, Kartikeya
- **Year**: 2026
- **Date**: 2026-06-21
- **arXiv**: [2606.22686](https://arxiv.org/abs/2606.22686)
- **Categories**: cs.CR

## Key Contributions
- **Contrastive Logit Steering (CLS)**: A zero-optimization logit-level intervention framework that isolates the refusal direction via system-prompt contrast, operating on the output distribution (rather than internal activations) and exposing alignment vulnerabilities that hidden-state methods systematically underestimate.
- **Architectural phase-transition diagnostic**: Identifies *Late Decision* vs *Early Divergence* topologies as model-family-level safety implementation choices — Llama-3.1 (Late Decision) reaches 95% ASR in ~1s via prefix injection, Qwen-2.5 (Early Divergence) integrates safety mid-computation and resists the same attack pattern — surfacing safety architecture as a measurable, family-specific structural property.
- **Logit-level intervention outperforms activation-level steering by 3-50×**: 73% ASR vs 22.6% on Llama 2, 91% vs 79.2% on Qwen 7B — demonstrates that the canonical representation-engineering intervention surface (hidden states) systematically under-probes alignment fragility, and that output-distribution interventions expose a deeper vulnerability layer.
- **Bidirectional control via steering-vector inversion**: The same linearity that makes refusal bypassable also makes it *hardenable* — inverting the steering vector defends against jailbreaks without retraining, reframing the safety direction as a structurally exploitable primitive for both attack and defense rather than a fixed internal property.
- **Surfaces *safety-as-linear-feature* as a load-bearing primitive for mechanistic interpretability**: The geometric structure of refusal is not deep semantic but linear and steerable, with architectural phase transitions that determine exploitability — the safety axis is both the vulnerability and the defense primitive.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this discovery was logged
- [[comparing-linear-probes-mahalanobis-cosine-similarity-2606.19603]] — Sibling linear-probe interpretability: Comparing Linear Probes audits *which* linear probe best recovers learned representations, Geometry of Refusal shows that *refusal itself* is such a linearly decodable feature — together they bracket the linear-feature interpretability surface between *probe design* (Comparing Linear Probes) and *refusal-direction geometry* (Geometry of Refusal)
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Sibling jailbreak detection from internal entropy: Detecting-Jailbreaks-from-Entropy audits *intermediate-layer entropy* as a jailbreak signal, Geometry of Refusal audits *logit-level contrastive directions* as a jailbreak surface — together they bracket the safety-internals surface between *detection via entropy dynamics* (Detection paper) and *attack via linear feature geometry* (Geometry of Refusal)
- [[deeper-is-not-always-better-mitigating-the-alignment-tax-via-confident-layer-decoding-2606.21906]] — Sibling alignment robustness: Confident-Layer-Decoding mitigates alignment tax via decoding-time intervention, Geometry of Refusal shows that logit-level steering (a different intervention surface) exposes and exploits the underlying alignment geometry — together they bracket the alignment-robustness surface between *decoding-time mitigation* (Confident-Layer-Decoding) and *logit-time exploitation / inversion* (Geometry of Refusal)
- [[do-thinking-tokens-help-with-safety-2606.25013]] — Sibling safety reasoning mechanism: Thinking-Tokens audits whether chain-of-thought reasoning helps safety, Geometry of Refusal audits whether safety is a manipulable linear feature — together they bracket the safety-mechanism surface between *reasoning-time safety* (Thinking-Tokens) and *steerability-time safety* (Geometry of Refusal)
- [[privacyalign-contextual-privacy-alignment-for-llm-agents-2606.21710]] — Sibling contextual alignment: PrivacyAlign aligns LLMs for contextual privacy compliance, Geometry of Refusal surfaces a more general principle — alignment is geometrically linear and thus steerable in both attack and defense directions, of which privacy is one specific axis — together they bracket the alignment-discipline surface between *application-specific alignment* (PrivacyAlign) and *general-mechanism alignment geometry* (Geometry of Refusal)