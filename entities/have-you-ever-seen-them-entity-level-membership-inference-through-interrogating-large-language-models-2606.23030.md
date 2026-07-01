---
title: "Have You Ever Seen Them? Entity-level Membership Inference through Interrogating Large Language Models"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [privacy, membership-inference, security, llm]
sources: ["https://arxiv.org/abs/2606.23030"]
---

# Have You Ever Seen Them? Entity-level Membership Inference through Interrogating Large Language Models

## Overview
Existing membership inference attacks (MIAs) focus on whether specific text snippets or training examples were used to train an LLM. This paper identifies a gap: entity-level membership — whether a named entity (person, organization, location) appeared in the training data — is a distinct and underexplored attack surface. The paper shows that LLMs encode entity-level memory traces that can be extracted via careful prompting strategies, revealing whether the model has "seen" specific entities during training. This has significant implications for privacy compliance (e.g., GDPR right-to-be-forgotten requests involving entities) and copyright analysis.

## Key Facts
- **Authors**: N/A (arxiv 2606.23030)
- **Year**: 2026
- **arXiv**: [2606.23030](https://arxiv.org/abs/2606.23030)

## Key Contributions
- First entity-level membership inference attack framework for LLMs (beyond sample-level MIA)
- Demonstrates extraction of entity-memory traces via carefully designed prompting strategies
- Proposes entity-level forgetting mechanisms as a compliance tool for privacy regulations
- Shows entity-level memory is robust across model scales and persists even when text-level memory is erased
- First privacy/membership-inference paper in the wiki focused on entity-level rather than text-level attacks

## Related Papers
- [[cache-resident-llm-inference-gb-scale-last-level-caches-2606.25353]] — Privacy-adjacent: inference system design (cache residency implications)
- [[beyond-flops-benchmarking-real-inference-acceleration-of-llm-pruning-under-a-gemmcentric-taxonomy-2606.09080]] — Privacy-adjacent: inference efficiency taxonomy
