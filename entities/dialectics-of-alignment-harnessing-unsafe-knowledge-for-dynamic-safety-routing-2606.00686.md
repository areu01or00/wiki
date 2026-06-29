---
title: "Dialectics of Alignment: Harnessing Unsafe Knowledge for Dynamic Safety Routing"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [alignment, safety, llm, routing]
sources: ["https://arxiv.org/abs/2606.00686"]
---

# Dialectics of Alignment: Harnessing Unsafe Knowledge for Dynamic Safety Routing

## Overview
Challenges the prevailing alignment paradigm that relies on erasure/filtering of unsafe knowledge. Instead, proposes dynamic safety routing that integrates unsafe knowledge in a controlled manner, enabling the model to recognize and safely navigate hazardous queries rather than pretend the knowledge doesn't exist. The routing mechanism shows zero-shot generalization to unseen safety domains.

## Key Facts
- **Authors**: Maryam Hashemzadeh et al.
- **Year**: 2026
- **arXiv**: [2606.00686](https://arxiv.org/abs/2606.00686)

## Key Contributions
- **Dialectics of alignment**: controlled integration of unsafe knowledge rather than masking/erasure
- **Dynamic safety routing**: runtime routing mechanism that classifies queries and applies appropriate handling
- **Zero-shot generalization**: routing transfers to unseen safety domains without domain-specific supervision
- **Paradigm shift claim**: true safety requires controlled integration, not hiding unsafe knowledge

## Related Papers
- [[policyalign-direct-policy-based-safety-alignment-llms-2606.25442]] — Direct policy-based safety alignment (orthogonal axis: policy-based vs routing-based)
- [[safety-alignment-as-continual-learning-mitigating-the-alignment-tax-via-orthogonal-gradient-projection-2602.07892]] — Safety alignment via orthogonal gradient projection (orthogonal axis: gradient-projection vs knowledge-routing)
