---
title: "Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [alignment, tool-use, structured-output, open-weight-llm, empirical-study]
sources: ["https://arxiv.org/abs/2606.25605"]
---

# Constraint Tax in Open-Weight LLMs: An Empirical Study of Tool Calling Suppression Under Structured Output Constraints

## Overview
This paper empirically characterizes a "constraint tax" — a measurable degradation in tool-calling reliability when open-weight LLMs are forced to comply with structured-output constraints (JSON-schema / grammar-constrained decoding). The authors quantify how often and how severely structured-output enforcement suppresses correct function-call emission across multiple open-weight model families and propose mitigation strategies. The work provides a controlled evaluation framework that disentangles *schema-compliance* from *tool-selection correctness*, exposing a previously under-measured interaction between constraint decoding and the agentic capability stack.

## Key Facts
- **Authors**: Li, Fangzheng; Zhang, Aimin; Lv, Chen
- **Year**: 2026
- **arXiv**: [2606.25605](https://arxiv.org/abs/2606.25605)
- **Subjects**: cs.CL

## Key Contributions
- Introduces the "Constraint Tax" metric — the joint degradation of tool-call F1 when a structured-output grammar is layered on top of an instruction-tuned open-weight model — and shows it is non-trivially large across 6+ model families.
- Builds a controlled evaluation harness that separates *schema-format errors* (malformed JSON, wrong field types) from *tool-selection errors* (correct format, wrong function), revealing the tax is concentrated in the latter at moderate constraint strictness.
- Proposes and validates two mitigation strategies: (a) constraint-aware fine-tuning with synthetic schema violations, and (b) two-pass decoding where a "draft" call is re-parsed against the schema before commit.
- Reports empirical guidance on constraint strictness levels (JSON-schema strict mode vs. permissive grammar) that practitioners can use to trade off reliability vs. expressivity in production agent deployments.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 as a fresh 2026 contribution to LLM tool-use and structured-output alignment.
