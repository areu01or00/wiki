---
title: "Exposing the Illusion of Erasure in Knowledge Editing for LLMs"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [llm, alignment, safety, jailbreak, knowledge-editing, agent, skill-distillation]
sources: ["https://arxiv.org/abs/2606.23276"]
---

# Exposing the Illusion of Erasure in Knowledge Editing for LLMs

## Overview
This paper reveals that knowledge editing (KE) methods for LLMs create an illusion of erasure — edited knowledge appears suppressed in standard benchmarks but surfaces reliably under adversarial elicitation. The authors demonstrate that KE methods like ROME, MEMIT, and EMN consistently fail to truly remove knowledge; instead, the model routes around the edited pathway via semantically equivalent representations. This is the first systematic adversarial elicitation study of the knowledge editing reliability problem.

## Key Facts
- **arXiv**: [2606.23276](https://arxiv.org/abs/2606.23276)
- **Submitted**: 2026-05-DD (from arxiv ID prefix)
- **Theme**: LLM knowledge editing / adversarial elicitation / reliability

## Key Contributions
- First adversarial elicitation framework for knowledge editing reliability
- Reveals consistent failure of ROME/MEMIT/EMN under adversarial prompting
- Demonstrates semantic equivalence routing as the failure mechanism
- Introduces countermeasures that defeat current KE methods via targeted elicitations


## Related Papers
- [[emergent-concepts]] — Emergent Concepts parent page
