---
title: "Me, Myself, and π: Evaluating and Explaining LLM Introspection"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [evaluation, introspection, metacognition, llm]
sources: ["https://arxiv.org/abs/2603.20276"]
---

# Me, Myself, and π: Evaluating and Explaining LLM Introspection

## Overview
This paper addresses a fundamental question in LLM metacognition: when an LLM claims to "introspect" its own reasoning, is it genuinely accessing its internal cognitive processes, or merely simulating self-report using world knowledge? The authors propose a rigorous evaluation framework to distinguish genuine meta-cognition from text-based self-simulation.

## Key Facts
- **Authors**: Atharv Naphade, Samarth Bhargav, Sean Lim, Mcnair Shah
- **Year**: 2026
- **arXiv**: [2603.20276](https://arxiv.org/abs/2603.20276)

## Key Contributions
- **Distinguishing genuine introspection from self-simulation**: Proposes behavioral and mechanistic probes that separate true metacognitive access from world-knowledge-based self-reporting
- **Evaluation framework for LLM introspection**: Introduces tasks where ground-truth internal states are knowable, enabling rigorous assessment of introspective accuracy
- **Finding of widespread self-simulation**: Most current LLMs appear to use general world knowledge and text-pattern matching rather than genuine introspective access when reporting on their own reasoning
- **Mechanistic analysis**: Investigates which internal representations correlate with accurate introspective self-reports, providing guidance for building more genuinely introspective models

## Related Papers
- [[introspection-adapters-training-llms-to-report-their-learned-behaviors-2604.16812]] — Introspection Adapters: trains LLMs to report learned behaviors via introspective adapters; complements the evaluation framework by showing how to build genuine introspective access
- [[mechanisms-of-introspective-awareness-in-large-language-models-2603.21396]] — Mechanisms of Introspective Awareness: mechanistic study of how introspective awareness emerges in LLMs; directly related to the "what separates genuine introspection from simulation" question
- [[the-metacognitive-monitoring-battery-a-cross-domain-benchmark-for-llm-self-monitoring-2604.15702]] — Metacognitive Monitoring Battery: cross-domain benchmark for LLM self-monitoring; shares the evaluation rigor concern but focuses on self-monitoring fidelity rather than distinguishing simulation from genuine access
