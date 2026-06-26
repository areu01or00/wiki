---
title: "Routing-Free Mixture-of-Experts"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [mixture-of-experts, moe, architecture, transformer, llm, routing]
sources: ["https://arxiv.org/abs/2604.00801"]
---

# Routing-Free Mixture-of-Experts

## Overview
Eliminates the centralized routing mechanisms (external routers, Softmax, Top-K, load balancing) that standard Mixture-of-Experts models rely on. Each expert in Routing-Free MoE encapsulates its own activation functionality and decides autonomously via continuous gradient flow whether to fire, with a unified adaptive load-balancing framework that simultaneously optimizes expert-balancing and token-balancing. The result: better scalability and robustness than routed-MoE baselines, with no rigid inductive bias from the routing mechanism.

## Key Facts
- **Authors**: Liu, Yilun; Han, Jinru; Yan, Sikuan (and collaborators)
- **Year**: 2026
- **arXiv**: [2604.00801](https://arxiv.org/abs/2604.00801)
- **Online date**: 2026-04-01

## Key Contributions
- **No centralized router** — every expert decides its own activation entirely from continuous gradient flow. This removes the rigid inductive bias of Softmax+Top-K routing (which forces a sparse, discrete choice structure that may not match expert specialization) and lets experts develop more nuanced co-activation patterns.
- **Unified adaptive load-balancing framework** — a configurable interpolation between expert-balancing and token-balancing objectives, allowing flexible resource allocation. This decouples the *load* constraint from the *router* mechanism: load balancing was historically conflated with routing, but Routing-Free MoE shows they can be orthogonal primitives.
- **Better scalability and robustness** — extensive experiments show consistent outperformance over routed-MoE baselines. The architectural simplification (no router) yields better scaling behavior, suggesting the router itself was a bottleneck rather than an enabler.

## Why this matters for the wiki
**First routing-primitive-removed MoE in the wiki.** Complements Run 62's [task-routing theoretical primitive](#) (which proved *why* routing works under discrete-language formalism) by instead asking *what if we remove routing entirely?* The two papers bracket MoE theory: Run 62's paper gives a theorem for *why* routing localizes knowledge circuits, this paper gives an empirical demonstration that routing isn't strictly necessary. Together they form a complete MoE-routing theory primitive pair.

## Related Papers
- [[a-theoretical-model-for-task-routing-in-mixture-of-expert-transformers-2606.14398]] — Task-routing theoretical primitive under discrete-language formalism; complementary theoretical paper proving *why* routing localizes knowledge circuits. Routing-Free MoE shows routing isn't strictly necessary — the two bracket MoE-routing theory.
- [[secret-mixtures-of-experts-inside-your-llm-2512.18452]] — Empirical discovery of hidden MoE structure inside dense LLMs; sibling MoE-architecture primitive from Run 55
- [[grouped-query-experts-mixture-of-experts-on-gqa-self-attention-2606.20945]] — MoE on GQA self-attention; sibling MoE-architecture primitive showing a different way to specialize experts (on grouped-query self-attention rather than FFN)