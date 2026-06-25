---
title: "When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agent-safety, tool-use, llm-agents, privilege-escalation, alignment, evaluation]
sources: ["https://arxiv.org/abs/2606.20023"]
---

# When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents

## Overview
As LLM agents select tools autonomously, their choices among tools with different privilege levels become safety-relevant — yet prior tool-selection studies focus on safety-agnostic metadata preferences, leaving privilege-sensitive choices underexplored. This paper introduces ToolPrivBench, a benchmark that measures whether agents choose higher-privilege tools despite sufficient lower-privilege alternatives, both at initial selection and via escalation after transient tool failures. Across eight domains and five recurring risk patterns, the authors find over-privileged tool selection is common among mainstream LLM agents and is further amplified by transient failures; general safety alignment does not transfer reliably to least-privilege tool choice, and prompt-level controls provide only limited mitigation. They propose a privilege-aware post-training defense that substantially reduces unnecessary high-privilege tool use while preserving general capabilities.

## Key Facts
- **Authors**: Kaiyue Yang, Yuyan Bu, Jingwei Yi, Yuchi Wang, Biyu Zhou, Juntao Dai, Songlin Hu, Yaodong Yang
- **Year**: 2026
- **arXiv**: [2606.20023](https://arxiv.org/abs/2606.20023) ([pdf](https://arxiv.org/pdf/2606.20023))
- **Date published**: 2026-06-18
- **Subjects**: cs.SE
- **Methodology**: ToolPrivBench benchmark across 8 domains and 5 recurring risk patterns; evaluation of initial tool selection and escalation after transient failures; privilege-aware post-training defense vs prompt-level baselines.

## Key Contributions
- **ToolPrivBench**: a benchmark for least-privilege tool selection that distinguishes initial-selection failure modes from escalation-after-transient-failure modes, both of which the paper finds prevalent.
- **Empirical finding**: over-privileged tool selection is common among mainstream LLM agents and amplified by transient failures — agents escalate to high-privilege tools when a lower-privilege alternative would have sufficed.
- **Alignment-transfer failure**: general-purpose safety alignment does not reliably transfer to least-privilege tool choice, indicating the privilege dimension is a distinct alignment axis that current alignment recipes leave untouched.
- **Privilege-aware post-training defense**: a fine-tuning approach that teaches agents to prefer sufficient lower-privilege tools and escalate only when necessary, substantially reducing unnecessary high-privilege use while preserving general capabilities.
- **Prompt-only mitigation is insufficient**: prompt-level controls provide limited mitigation under transient failures, motivating the post-training approach.

## Related Papers
- [[capable-but-careless-do-computer-use-agents-follow-contextual-integrity-2606.23189]] — sibling paper on LLM-agent contextual-integrity failures (information leakage across application contexts); the two papers jointly establish that agent autonomy has *at least two* under-evaluated safety dimensions: privilege and context.
- [[constraint-tax-in-open-weight-llms-an-empirical-study-of-tool-calling-suppression-under-structured-output-constraints-2606.25605]] — isolates the constraint-decoding layer's contribution to tool-call failures; complements this paper's privilege-axis finding by isolating the *selection* failure from the *call-format* failure.
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — a pre-generation guard layer for jailbreaks; orthogonal to this paper's tool-selection mitigation but together they cover pre-call and at-call safety primitives.
- [[emergent-concepts]] — parent meta-page that catalogued this paper as part of the LLM agent-safety / tool-use-alignment theme.