---
title: "Large Language Model Reasoning Failures"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [reasoning-failure, llm-survey, embodied-reasoning, robustness, fundamental-failure, application-failure]
sources: ["https://arxiv.org/abs/2602.06176"]
---

# Large Language Model Reasoning Failures

## Overview
First comprehensive survey dedicated to reasoning failures in LLMs, introducing a novel 2-axis categorization framework that distinguishes embodied vs non-embodied reasoning and classifies failures along fundamental, application-specific, and robustness axes. Provides clear definitions, root-cause analyses, and mitigation strategies for each failure type.

## Key Facts
- **Authors**: Song, Peiyang; Han, Pengrui; Goodman, Noah
- **Year**: 2026
- **arXiv**: [2602.06176](https://arxiv.org/abs/2602.06176)
- **Category**: cs.CL, cs.AI, cs.LG
- **Date**: 2026-02-05

## Key Contributions
- Introduces a *2-axis categorization framework* distinguishing *embodied* (grounded in physical/digital action) from *non-embodied* (pure symbolic reasoning) reasoning, with the latter further subdivided into *informal* (intuitive) and *formal* (logical) — surfacing *reasoning-modality-as-taxonomy-axis primitive* as the load-bearing primitive for organizing LLM failure studies by *what kind of reasoning* is failing.
- Classifies reasoning failures along a complementary axis into three types: *fundamental failures* intrinsic to LLM architectures (broadly affecting downstream tasks), *application-specific limitations* (manifest in particular domains), and *robustness issues* (inconsistent performance across minor variations) — surfacing *failure-scope-as-orthogonal-primitive* where fundamental-vs-application-vs-robustness is independent of reasoning-type classification.
- For each reasoning failure provides *clear definition*, *analysis of existing studies*, *root causes*, and *mitigation strategies* — providing the *failure-decomposition-primitive* that allows researchers to move from observed failure to diagnosed cause to remediation pathway within a unified framework.
- Unifies fragmented research efforts under the rubric of *systemic weaknesses* — providing the *survey-as-fragmentation-unifier primitive* where the load-bearing contribution is structural organization of a previously scattered literature into a coherent taxonomy with cross-references between failure classes.
- Provides *mitigation strategies* for each failure class, with explicit mappings from failure diagnosis to remediation approach — surfacing *diagnosis-to-mitigation mapping primitive* as the load-bearing *actionable-primitive* that distinguishes survey from mere literature catalog.
- Establishes *reasoning-failure-as-load-bearing-research-line*, arguing that sustained attention to failure modes is essential to ensure future LLMs not only perform better on reasoning tasks but *fail better* (gracefully, transparently, recoverably) — surfacing *graceful-failure-as-design-goal primitive* as the load-bearing *failure-quality primitive* that complements performance metrics.

## Related Papers
- [[reasoning-models-struggle-to-control-their-chains-of-thought-2603.05706]] — Sibling Run 61 CoT-monitorability work — Reasoning-Models-Struggle-to-Control measures *CoT-vs-output controllability asymmetry* (23× for Claude Sonnet 4.5), LLM-Reasoning-Failures surveys *the broader landscape of reasoning failures* with embodied/non-embodied × fundamental/application/robustness axes — together they bracket the reasoning-failure surface between *verbalization-side controllability measurement* (Reasoning-Models-Struggle-to-Control) and *broad reasoning-failure taxonomy* (LLM-Reasoning-Failures).
- [[when-the-chain-of-thought-knows-better-failure-modes-in-multi-turn-reasoning-models-2606.10740]] — Sibling Run 60 multi-turn-reasoning-failure work — When-the-Chain-of-Thought-Knows-Better diagnoses *CoT-Output-2x2-matrix failure modes* in multi-turn reasoning models, LLM-Reasoning-Failures provides *the broad taxonomy* of reasoning failures across reasoning types — together they bracket the reasoning-failure surface between *per-turn multi-turn failure attribution* (When-the-Chain-of-Thought-Knows-Better) and *cross-domain failure taxonomy* (LLM-Reasoning-Failures).
- [[why-reasoning-fails-to-plan-a-planning-centric-analysis-of-long-horizon-decision-making-in-llm-agents-2601.22311]] — Sibling Run 60 planning-failure work — Why-Reasoning-Fails-to-Plan isolates *reasoning-vs-planning-orthogonal-axes failure mode* with FLARE future-aware-lookahead, LLM-Reasoning-Failures provides *the broader reasoning-failure taxonomy* — together they bracket the reasoning-failure surface between *planning-specific failure mechanism* (Why-Reasoning-Fails-to-Plan) and *general reasoning-failure taxonomy* (LLM-Reasoning-Failures).
- [[a-theoretical-model-for-task-routing-in-mixture-of-expert-transformers-2606.14398]] — Sibling Run 62 MoE-theoretical work — Task-Routing-Theory shows MoE *task-expert specialization as a theorem*, LLM-Reasoning-Failures provides *the failure-mode taxonomy* against which successful reasoning must be measured — together they bracket the reasoning surface between *theoretical-task-routing-guarantees* (Task-Routing-Theory) and *empirical-failure-mode-catalog* (LLM-Reasoning-Failures).
- [[reasoninglens-hierarchical-visualization-and-diagnostic-auditing-for-large-reasoning-models-2606.23404]] — Sibling Run 60 trace-auditing work — ReasoningLens provides *hierarchical-trace-strategy-vs-execution diagnostics*, LLM-Reasoning-Failures provides *the failure-mode taxonomy* that diagnostics need to identify — together they bracket the reasoning-diagnostics surface between *per-trace audit* (ReasoningLens) and *per-failure-mode classification* (LLM-Reasoning-Failures).
- [[emergent-concepts]] (parent wiki page) entries on this page by surfacing *reasoning-modality-as-taxonomy-axis* × *failure-scope-as-orthogonal-primitive* as the structurally correct primitive for LLM failure studies where the failure mode of *plausible-but-flawed reasoning* is structurally invisible to single-axis classifications but becomes tractable when reasoning type (embodied/non-embodied/informal/formal) and failure scope (fundamental/application/robustness) are independently classified — bridging fragmented research efforts into a unified framework with diagnosis-to-mitigation mappings.
