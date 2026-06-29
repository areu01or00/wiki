---
title: "PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [medical, clinical, agent, ehr, benchmark, llm, application-domain]
sources: ["https://arxiv.org/abs/2605.02240"]
---

# PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments

## Overview
First benchmark in the wiki to systematically evaluate LLM agents on **physician tasks grounded in real clinical settings within EHR environments** — distinguishing long-horizon composite clinical workflows from prior medical LLM benchmarks that focus on static knowledge recall or single-step atomic actions. Encodes tasks that span multiple actions, EHR navigation, and clinically meaningful outcomes, with verifiable execution against the environment.

## Key Facts
- **Authors**: (PhysicianBench team)
- **Year**: 2026
- **arXiv**: [2605.02240](https://arxiv.org/abs/2605.02240)
- **Online Date**: 2026-05-04
- **Domain**: medical-AI × LLM-agent-evaluation × clinical-EHR-workflow

## Key Contributions
- **Real-clinical-setting EHR workflows**: 100 long-horizon tasks adapted from real consultation cases between primary care and subspecialty physicians, with verifiable environment execution — bridges the gap between static-knowledge medical benchmarks and real clinical decision support
- **Composite-workflow evaluation axis**: tests long-horizon composite workflows (rather than single-step atomic actions or action-intent labels), capturing how physician-LLM-agents actually operate in real clinical systems
- **Verification grounding**: tasks are verifiable against the EHR environment end-to-end rather than scored by static knowledge comparison, surfacing workflow-correctness as the load-bearing primitive
- **Application-domain primitive — physician-EHR-agent-evaluation**: positions clinical LLM agents at the deployment boundary by anchoring tasks to real EHR navigation rather than abstract clinical reasoning — fully orthogonal to multi-agent peer-reviewed medical-QA and biomedical-research-question benchmarks already in the wiki
- **First physician-EHR-real-clinical-workflow benchmark in the wiki** providing a deployment-side primitive for medical-AI × LLM-agent research at the system level rather than the model level

## Related Papers
- [[let-llms-judge-each-other-multi-agent-peer-reviewed-reasoning-for-medical-question-answering-2606.15419]] — Sibling evaluation primitive on multi-agent peer review for medical QA; PhysicianBench complements by targeting EHR-grounded task execution rather than QA reasoning
- [[measuring-epistemic-resilience-of-llms-under-misleading-medical-context-2606.12291]] — Sibling on medical-context-injection robustness; PhysicianBench inverts the adversarial-axis by anchoring tasks to real EHR data
- [[openbiorq-unsolved-biomedical-research-questions-for-agents-2606.21959]] — Application-domain sibling targeting biomedical research; PhysicianBench targets clinical-physician deployment layer
- [[lingxidiagbench-a-multi-agent-framework-for-benchmarking-llms-in-chinese-psychiatric-consultation-and-diagnosis-2602.09379]] — Application-domain sibling on Chinese psychiatric diagnosis; PhysicianBench focuses on physician-EHR workflows in English clinical settings
- [[where-does-the-signal-live-a-web-data-recipe-for-medical-encoder-pretraining-2606.22079]] — Sibling on medical-encoder pretraining; PhysicianBench operates at the evaluation layer, not pretraining
