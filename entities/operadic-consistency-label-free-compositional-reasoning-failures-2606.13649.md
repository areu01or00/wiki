---
title: "Operadic Consistency: Label-Free Signal for Compositional Reasoning Failures in LLMs"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, failure-modes, compositional, label-free-detection]
sources: ["https://arxiv.org/abs/2606.13649"]
---

# Operadic Consistency: Label-Free Signal for Compositional Reasoning Failures in LLMs

## Overview
Detecting LLM reasoning failures without ground-truth labels has driven work on self-consistency, semantic entropy, and P(True). This paper applies operad theory — the mathematical formalism for systems built from structured compositional layers — to detect compositional reasoning failures. The key insight is that reasoning steps in a compositional chain have type signatures (input/output types), and violations of operadic consistency predict failures even when individual steps appear locally correct.

## Key Facts
- **Authors**: Bottman, Nathaniel; Liu, Yinhong; Richardson, Kyle
- **Year**: 2026
- **arXiv**: [2606.13649](https://arxiv.org/abs/2606.13649)

## Key Contributions
- Novel application of operad theory to LLM failure detection — first label-free, ground-truth-free signal for compositional reasoning failures
- Operadic consistency score as a single scalar that predicts multi-step reasoning collapse
- Shows that locally plausible reasoning steps can still fail compositionally; type-signature violations precede downstream errors
- **First operad-theoretic LLM failure detection paper in the wiki**

## Related Papers
- [[when-errors-become-narratives-a-longitudinal-taxonomy-of-silent-failures-in-a-production-llm-agent-runtime-2606.14589]] — Both characterize LLM reasoning failures; Operadic Consistency focuses on compositional chain collapse while Silent Failures taxonomizes runtime failures
- [[a-multi-dataset-benchmark-for-evaluating-llm-agents-in-microservice-failure-diagnosis-2606.29193]] — Both concern failure detection in deployed LLM systems; Operadic Consistency provides the signal while the benchmark measures downstream impact
- [[inducing-reasoning-primitives-from-agent-traces-2606.02994]] — Both investigate reasoning structure; RPI extracts reusable primitives while this paper detects when compositional chains fail
