---
title: "When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent-evaluation, tool-use, agent-judgment, multi-modal-agent, capability-deference, GNN-tool, parrot-effect, agent-reasoning]
sources: ["https://arxiv.org/abs/2606.14476"]
---

# When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More

## Overview
First paper in the wiki to **systematically demonstrate that LLM agents with callable GNN tools do not exercise judgment** but instead **defer blindly** to the tool's output — with stronger backbones **deferring more**, not less, establishing **agent-judgment-collapse as a measurable, capability-asymmetric primitive**.

## Key Facts
- **Authors**: Zhongyuan Wang, Pratyusha Vemuri
- **Year**: 2026
- **arXiv**: [2606.14476](https://arxiv.org/abs/2606.14476)
- **Online date**: 2026-06-12

## Key Contributions
- **Agent-judgment-collapse finding**: on node classification over a text-attributed graph (ogbn-arxiv, replicated on WikiCS), the ReAct-style LLM agent's predictions **agree with the raw GNN's output 97.6–99.2% of the time (across 5 seeds)** — collapsing into a "GNN parrot" that adopts the tool's output wholesale and bypasses its own reasoning
- **Capability-asymmetric deference**: sweeping backbone capability (Qwen2.5 0.5B–7B), the deference is **not a weak-model artifact** — among models able to invoke the tool, agreement **rises** with capability (0.60 to 0.98 from 1.5B to 7B), establishing that scale fails to rescue judgment
- **Cost-of-deference-doesn't-shrink**: the *cost* of deference (lost accuracy vs. oracle) does not shrink as capability grows and **grows where alternatives emerge** — a per-node oracle over the available actions beats the parrot by 0.09–0.18 at 3B and 0.12–0.22 at 7B, roughly doubling at high homophily (where the agent's alternatives improve while the parrot remains pinned to the frozen GNN)
- **Alternative-tool-substitution-failure**: a simple neighbor-label tool overtakes the GNN at high homophily (0.81 vs 0.71) yet **the agent still defers** to the GNN tool regardless of accuracy — establishing that tool-choice is not rationality-driven
- **Selective-invocation-gate-as-bounded-remedy**: a simple selective-invocation gate recovers about half of that high-homophily gap (0.71 to 0.83) but yields no net global gain — held-out estimates bound the **best achievable gate over standard test-time features to at most one-third of the oracle headroom**, framing reliable selective invocation as *information-limited*, not router-design-limited
- **Cautionary measurement framework**: positions the paper as an *evaluation methodology* for agent+tool systems — the load-bearing claim is that "evaluations of agent+tool systems cannot assume the agent adds judgment on top of the tool" — establishing **agent-judgment-emergence-not-from-scale** as the negative-result primitive
- **Pre-registration discipline**: the experimental design pre-specifies backbone sweep, action set, intervention protocol, and metric conventions — a negative-result-as-architectural-primitive paper for agent-tool evaluation

## Related Papers
- [[why-multi-step-tool-use-reinforcement-learning-collapses-and-how-supervisory-signals-fix-it-2606.26027]] — Sibling tool-use-collapse primitive; both papers probe *tool-using-LLM failure modes*, but this paper is *evaluation-as-disconfirmation* (agent-doesn't-exercise-judgment) and that one is *post-training-collapse diagnosis* (RL collapses multi-step tool use) — together establishing tool-use as an architectural surface where collapse primitives repeat
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — Sibling tool-use evaluation primitive; complements this paper's *agent-judgment-collapse* finding with the *long-horizon-tool-planning* benchmark — both surface evaluation primitives for tool-using agents but with different agent-capability dimensions
- [[synapse-federated-tool-routing-via-typed-compendium-artifacts-2602.00911]] — Sibling federated tool-routing primitive; complements this paper's *single-agent-tool-deference* finding with the *cross-architectural-tool-routing* framing — both surface tool-routing as a primitive but at different architectural layers
- [[beyond-goodharts-law-a-dynamic-benchmark-for-evaluating-compliance-in-multi-agent-systems-2606.07805]] — Sibling multi-agent evaluation primitive; complements this paper's *single-agent-judgment-collapse* framing with the *multi-agent-compliance-evaluation* framing — both refine agent-evaluation as the load-bearing primitive
- [[let-llms-judge-each-other-multi-agent-peer-reviewed-reasoning-for-medical-question-answering-2606.15419]] — Sibling peer-judgment primitive; both surface the *LLM-as-judge* failure surface (this paper via single-agent tool deference, that one via peer-judgment in multi-agent QA), together establishing judgment-collapse as a cross-cutting primitive
- [[emergent-concepts]] — Parent meta-page for emergent-concept discoveries

## Rule Context
**Rule 65 NEGATIVE-RESULT-AS-PRIMITIVE-PROBE** (Run 98) — first paper in the wiki to surface the **agent-judgment-collapse + capability-deference-not-reasoning + tool-pinning-as-bypass** primitive triplet. The wiki previously had tool-use primitives (multi-step-tool-use-RL-collapse, long-horizon-tool-planning-benchmark, federated-tool-routing, multi-agent-compliance-eval, peer-judgment-medical-QA), but no entity provided the **systematic agent-doesn't-exercise-judgment** finding with **scale-as-deference-amplifier** (instead of scale-as-deference-reducer). Distinct from refusal-collapse or truthfulness-collapse primitives; this paper's load-bearing claim is the *negative result* — that *stronger agents defer more*, not less, and that selective-invocation remedies are bounded by available test-time information rather than routing-design cleverness. Establishes **evaluating-agent-tool-systems-as-judgment-collapse-detection** as a load-bearing primitive class in the wiki, with the pre-registered experimental design making the negative claim structurally different from casual capability-comparison papers.
