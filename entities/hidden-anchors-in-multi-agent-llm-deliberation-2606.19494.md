---
title: "Hidden Anchors in Multi-Agent LLM Deliberation"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [multi-agent, deliberation, belief-revision, opinion-dynamics, social-reasoning]
sources: ["https://arxiv.org/abs/2606.19494"]
---

# Hidden Anchors in Multi-Agent LLM Deliberation

## Overview
Multi-agent LLM deliberation — where agents exchange and revise answers over several rounds — is increasingly used to improve reasoning and accuracy, yet how and why it works is rarely modelled. This paper shows that hidden anchors can drive consensus beyond initial beliefs. The deliberation mirrors how humans reach decisions: pulled both by the group (herd effect captured by DeGroot and Friedkin-Johnsen opinion dynamics) and by internal belief (which those models do not capture). The paper models multi-agent deliberation as a context repair mechanism where anchors stabilize belief revision.

## Key Facts
- **Authors**: Apurba Pokharel, Ram Dantu
- **Year**: 2026
- **arXiv**: [2606.19494](https://arxiv.org/abs/2606.19494)

## Key Contributions
- **Hidden anchor mechanism**: Identifies a specific cognitive mechanism (hidden anchors in internal belief) that drives multi-agent belief revision beyond group conformity
- **Opinion dynamics model**: Extends DeGroot/Friedkin-Johnsen models to capture both social influence and private belief persistence
- **Context repair as deliberation function**: Frames multi-agent deliberation as a context maintenance mechanism that repairs drifted or corrupted belief states
- **Experimental validation**: Shows that agents with stronger hidden anchors are more resistant to social pressure and contribute more unique information to group consensus

## Related Papers
- [[persuasivetom-benchmark-evaluating-machine-theory-mind-in-persuasive-dialogues-2502.21017]] — ToM for persuasion and belief tracking in dialogue
- [[decompose-tom-enhancing-theory-mind-reasoning-through-simulation-and-task-decomposition-2501.09056]] — Simulation theory ToM with recursive perspective taking
- [[hidden-in-memory-sleeper-memory-poisoning-in-llm-agents-2605.15338]] — Hidden memory poisoning attacks in LLM agents
- [[probing-lack-of-stable-internal-beliefs-llms-2603.25187]] — Probing for stable internal beliefs in LLMs
