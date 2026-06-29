---
title: "IV Co-Scientist: Multi-Agent LLM Framework for Causal Instrumental Variable Discovery"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [identifiability, instrumental-variable, causal-inference, multi-agent, llm]
sources: ["https://arxiv.org/abs/2602.07943"]
---

# IV Co-Scientist: Multi-Agent LLM Framework for Causal Instrumental Variable Discovery

## Overview
First systematic framework for treating LLM agents as instruments for **instrumental-variable (IV) discovery** from observational data in the presence of unobserved confounding. The paper introduces a two-stage evaluation (recovery of established IVs + rejection of discredited ones) and a multi-agent proposer–critic–refiner architecture that surfaces valid IVs from a large observational database, paired with a consistency test for the no-ground-truth regime.

## Key Facts
- **Authors**: Ivaxi Sheth, Zhijing Jin, Bryan Wilder, Dominik Janzing, Mario Fritz
- **Year**: 2026
- **arXiv**: [2602.07943](https://arxiv.org/abs/2602.07943) (online 2026-04-06, submitted 2026-02-08)

## Key Contributions
- **First IV-discovery-as-LLM-agent-architecture primitive in the wiki**: reduces the problem of *isolating the causal effect of an endogenous variable on an outcome under unobserved confounding* to a multi-agent proposer / critic / refiner loop on observational data.
- **Two-stage evaluation framework**: (a) recovery of well-established instruments from literature — measuring whether LLMs replicate standard reasoning; (b) identification-and-rejection of empirically/theoretically discredited IVs — measuring whether LLMs can avoid known failure modes.
- **Statistical consistency test for no-ground-truth regime**: a novel test that contextualizes IV consistency when there is no ground truth, addressing the practical deployment problem that IVs are typically assessed against external validity judgments.
- **Multi-agent proposer / critic / refiner architecture (IV Co-Scientist)**: agents propose candidate IVs for a given treatment–outcome pair, critique one another's reasoning, and refine — operationalizing the *creativity + interdisciplinary knowledge* requirements of IV discovery as a structured LLM workflow.
- **Demonstrates potential of LLMs to discover valid IVs from a large observational database** — moving IV discovery from a domain-expert bottleneck to an LLM-assisted exploratory process.

## Related Papers
- [[causal-methods-for-llm-development-and-evaluation-2605.25998]] — Sibling discovery from prior run: surveys causal methods (intervention, counterfactual, mediation) for LLM development/eval — IV Co-Scientist is the *identifiability under unobserved-confounding* primitive that the survey frames as one of four causal primitives.
- [[causal-discovery-in-the-era-of-agents-2606.23608]] — Sibling causal-discovery primitive focused on autonomous causal structure discovery from observational data; IV Co-Scientist targets the harder *instrument discovery* sub-step within that pipeline.
- [[towards-a-universal-causal-reasoner-unico-2605.24873]] — Sibling universal-causal-reasoner primitive; IV Co-Scientist narrows the scope to *identifiability under unobserved confounding* via IVs rather than universal reasoning over all causal structures.
- [[does-reasoning-emerge-examining-the-probabilities-of-causation-in-large-language-models-2408.08210]] — Sibling null-model-comparison primitive (Rule 66) introducing probability-of-causation framework; IV Co-Scientist is the *identifiability-side* counterpart that asks "can the causal effect be isolated from observational data at all?".
- [[emergent-concepts]] — Parent meta-page tracking emergent-concept search discoveries.