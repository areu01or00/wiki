---
title: "Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [multi-agent, survey, failure-attribution, self-evolution, llm]
sources: ["https://arxiv.org/abs/2605.14892"]
---

# Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems

## Overview
Existing surveys cover individual agent capabilities, multi-agent collaboration, or agent self-evolution separately, leaving the causal dependencies among them unexamined. This paper provides the first unified survey of collaboration, failure attribution, and self-evolution in LLM-based multi-agent systems — examining how these three dimensions interact causally rather than independently. The authors identify structural gaps in each area and provide a systematic framework for understanding how failures in one dimension propagate to others.

## Key Facts
- **Authors**: Shihao Qi and 16 co-authors
- **Year**: 2026
- **arXiv**: [2605.14892](https://arxiv.org/abs/2605.14892)
- **Submitted**: 2026-05-14

## Key Contributions
- First unified survey examining **causal dependencies** among collaboration, failure attribution, and self-evolution in LLM multi-agent systems — prior surveys treat each in isolation
- Systematically taxonomizes failure attribution methods: outcome-based (did the agent succeed?), process-based (where in the reasoning chain did it fail?), and counterfactual-based (what would have changed the outcome?)
- Identifies that self-evolution mechanisms are currently underspecified for multi-agent settings — most self-evolution research focuses on single agents, leaving multi-agent credit assignment unresolved
- Maps the causal graph connecting collaboration failures → attribution failures → evolution failures, showing how each dimension's limitations compound in multi-agent settings
- **First unified multi-agent survey covering failure attribution in the wiki** — orthogonal to Rule 92's adversarial-attack focus (ShareLock, Memory Poisoning, Adaptive PI Defense) and Rule 91's benchmark design focus (SidConArena, Decoupling-Reconnaissance, Safe-Generalizable)

## Related Papers
- [[sidconarena-open-ended-positive-sum-bargaining-benchmark-2606.27397]] — sibling benchmark paper; SidConArena focuses on positive-sum bargaining as an agentic evaluation environment, while this survey maps the broader theoretical landscape including failure attribution and self-evolution across all multi-agent paradigms — together they bracket agentic benchmark design from environment-specific evaluation (SidConArena) to systematic survey taxonomy (this paper)
- [[decoupling-reconnaissance-exploitation-capability-boundaries-llm-pentest-2606.25332]] — sibling capability boundary paper; Decoupling-Reconnaissance isolates phase-specific capability assessment in pentesting, while this survey provides the overarching causal framework for how collaboration and failure attribution interact across multi-agent settings — together they bracket the measurement-methodology space between phase-isolated capability assessment (Decoupling-Reconnaissance) and causal dependency mapping (this survey)
