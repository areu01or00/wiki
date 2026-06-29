---
title: "GlobalDentBench: A Multinational Benchmark for Evaluating LLM Clinical Reasoning in Dentistry with Expert Calibration"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [medical, dental, clinical-reasoning, benchmark, llm, multinational, application-domain]
sources: ["https://arxiv.org/abs/2605.24636"]
---

# GlobalDentBench: A Multinational Benchmark for Evaluating LLM Clinical Reasoning in Dentistry with Expert Calibration

## Overview
First benchmark in the wiki to systematically evaluate LLM clinical reasoning in **dentistry** across **88 countries and regions spanning six continents** with **expert calibration** — filling a structural gap in clinical-reasoning evaluation by addressing a non-medicine vertical specialty (dental medicine) where reasoning robustness and safety in real-world scenarios remain underexplored.

## Key Facts
- **Authors**: (GlobalDentBench team)
- **Year**: 2026
- **arXiv**: [2605.24636](https://arxiv.org/abs/2605.24636)
- **Online Date**: 2026-05-26
- **Domain**: medical-AI × dental-specialty × LLM-clinical-reasoning × expert-calibration

## Key Contributions
- **Multinational-dental-specialty clinical benchmark**: 8,978 expert-validated questions across 14 dental specialties × 88 countries × six continents × three progressive reasoning levels (knowledge recall, applied reasoning, case-based reasoning) — first systematic multinational dental-LLM benchmark with expert calibration
- **Three-format question design**: multiple-choice + short-answer + case-based questions targeting different clinical-reasoning depth layers, with expert-validated ground truth at every layer
- **Reasoning robustness diagnosis at dental-specialty frontier**: surfaces dentistry as a less-explored clinical-reasoning vertical where current LLMs' reasoning robustness is structurally undertested compared to general-medicine benchmarks
- **Expert-calibration primitive**: rather than labeling via model agreement or static knowledge-base lookup, every question is expert-validated by dental specialists across multiple countries, providing the missing calibration layer that commodity medical benchmarks often lack
- **First multinational-dental-specialty LLM benchmark with expert calibration in the wiki**, verified via `ls entities/ | grep -iE "(globaldentbench|dentistry.*llm|dental.*benchmark)"` returning empty

## Related Papers
- [[physicianbench-evaluating-llm-agents-in-real-world-ehr-environments-2605.02240]] — Sibling Run-75 medical-domain application-domain benchmark on physician-EHR workflows; GlobalDentBench targets the dental-specialty vertical rather than generalist clinical-physician tasks
- [[let-llms-judge-each-other-multi-agent-peer-reviewed-reasoning-for-medical-question-answering-2606.15419]] — Sibling on multi-agent peer-reviewed medical QA; complements GlobalDentBench's expert-calibration-vs-peer-review primitive for medical benchmark design
- [[openbiorq-unsolved-biomedical-research-questions-for-agents-2606.21959]] — Application-domain sibling on biomedical research questions; GlobalDentBench targets specialty clinical reasoning, not biomedical research
- [[measuring-epistemic-resilience-of-llms-under-misleading-medical-context-2606.12291]] — Sibling on medical-context-injection robustness; GlobalDentBench is robustness-tested at the specialty × multinational layer
- [[lingxidiagbench-a-multi-agent-framework-for-benchmarking-llms-in-chinese-psychiatric-consultation-and-diagnosis-2602.09379]] — Application-domain sibling on psychiatric consultation; GlobalDentBench targets dental specialty, complementing cross-specialty coverage
