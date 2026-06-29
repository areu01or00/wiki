# Run 117 Lessons — 2026-06-29

## Run Summary
- **Run**: 117
- **Date**: 2026-06-29
- **Theme**: MULTIMODAL-SAFETY + CASCADED-SERVING + PROGRESSIVE-MULTIMODAL-AGENT
- **Discovery**: HF daily (2026-06-29/30) + arxiv HTML extraction
- **Pitfall-83**: HF pool thin on LLM-keyword (38 papers, 10 fresh_llm after 5-store dedup)
- **3-store lockstep**: 342 → 345

## 3 Picks
1. **SingGuard** (2606.22873) — Policy-adaptive multimodal VLM guardrail with fast-slow reasoning spectrum and decoupled RL; 56,340-example SingGuard-Bench across 80+ risk types
2. **Cluster Route Escalate** (2606.27457) — Two-stage cascaded serving: query clustering + quality-estimation cascade; 97-99% accuracy at reduced TPOT
3. **ProMSA** (2606.27974) — Progressive multimodal search agent for KB-VQA with TN-GSPO sequence-level RL; iterative image/text search under tool-call budgets

## Orthogonality Check
- Recent runs (113-116): test-time-compute, verifiable-prm, prm-taxonomy, causal-reasoning, mechanistic-circuit-KE, process-harness, latent-reasoning, test-time-gradient, epistemic-UQ, counterfactual-faithfulness, pragmatic-reasoning
- Run 117 themes: policy-adaptive guardrail, cascaded serving, progressive multimodal agent — NONE overlap with recent runs

## Key Observations
- HF daily v2 returned 38 papers across 2 dates (2026-06-29/30), 10 fresh LLM-keyword candidates
- 2606.27378 (Formalizing Latent Thoughts) was already on disk from prior run
- 6 fresh LLM-keyword candidates identified, all 3 selected for diversity
- Pitfall-137 entities_count: was 357, actual 360 (3 new files written)
- wikilink audit: all cross-references resolve correctly (verified via `ls entities/` check)
