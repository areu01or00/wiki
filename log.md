# Wiki Explorer — Run Log

## 2026-06-25 16:14 UTC — Emergent-concept search (3 fresh themes)

**Mode**: emergent-concept-search (all 9 named chains at 4/4 since 2026-05-25)
**Method**: web_search title-quoted topic queries (LLM reasoning / MoE / long-context / agents) + arxiv abs-page meta extraction via curl
**Candidates surveyed**: 12 fresh June-2026 arxiv IDs (all cs.CL / cs.AI / cs.IR, all deduped clean against existing entities)
**Papers added**: 3

### Papers
1. **Self-Compacting Language Model Agents** (2606.23525) — Li, Zhang, Jurayj (cs.CL, 2026-06-22). Theme: LLM agents / context-management / inference-efficiency. Introduces inference-time self-compaction; quantifies trace-anchoring degradation; Accordion-thinking primitive.
2. **The Periodic Table of LLM Reasoning: A Structured Survey** (2606.11470) — Anand, Ramesh, Mittal (cs.CL, 2026-06-09). Theme: LLM reasoning / survey / taxonomy. 3-axis taxonomy of ~120 methods (2022-2026); empty-cell research-frontier map.
3. **Agents' Last Exam** (2606.05405) — Sun, Han, Zhang (cs.AI, 2026-06-03). Theme: LLM agents / benchmarking / evaluation. 1,000+ expert-authored tasks across 52 professional subdomains; rubric-based grading harness.

### Parent updates
- `entities/emergent-concepts.md` ## Updates — MERGE-then-SORT prepend (existing top entries 06-24, 06-23, 06-23; new entries interleaved below: 06-22, 06-09, 06-03).

### Coordination note (pitfall 50)
A parallel wiki-explore-agent run fired at 16:15 UTC during this session and committed 6 entity files (the 3 new + 3 from a prior session already in HEAD). This run brought the state files (`explore_context.json`, `watch_profiles.json`) in sync with the entity files that were already in HEAD, completing the bookkeeping for the 3 papers (2606.23525, 2606.11470, 2606.05405) that were added as entity files by the parallel run but not yet reflected in the state-file mirror lists.

### Dedup
- `endswith(f'-{arxiv_id}.md')` suffix check: 0 collisions (12 of 12 candidates were fresh)
- `watch_profiles.json[last_result_hashes]`: 3 new MD5 hashes appended (top-level only — `llm-wiki` and `profiles.llm-wiki-explore` sub-profiles do not exist in this restored wiki's watch_profiles.json)
- `explore_context.json[chains][*][papers_found]`: 3 new entries appended to `emergent-concepts` chain

## 2026-06-25 16:25 UTC — Emergent-concept search (3 fresh themes: non-autoregressive diffusion + agentic-data + agent-memory)

**Mode**: emergent-concept-search (all 9 named chains at 4/4 since 2026-05-25)
**Method**: HuggingFace daily papers (3-day window: 2026-06-23..25) + arxiv abs-page meta extraction (10 parallel workers) + strict subject filter cs.CL/cs.LG/cs.AI/cs.IR
**Candidates surveyed**: 108 fresh arxiv IDs from HF daily pages, 58 passed LLM-relevant subject filter, 3 picked
**Papers added**: 3

### Papers
1. **Improved Large Language Diffusion Models** (2606.25331) — Nie, Shen, Min, Qiyang, Xu, Shaoxuan (cs.CL, 2026-06-24). Theme: LLM architecture frontier / non-autoregressive diffusion. iLLaDA — 8B masked diffusion LM trained from scratch that matches autoregressive baselines at matched compute; curriculum-style noising schedule; parallel-decoding inference.
2. **Autodata: An agentic data scientist to create high quality synthetic data** (2606.25996) — Kulikov, Whitehouse, Wu (cs.AI, 2026-06-24). Theme: LLM training-data / agentic-data-pipeline / synthetic-data. AI agents as data scientists via meta-optimization; agentic iterative loop over schema/gen/filter/verify; matches human-curated dataset quality.
3. **Are We Ready For An Agent-Native Memory System?** (2606.24775) — Zhou, Zhou, Han (cs.CL, 2026-06-23). Theme: LLM agent infrastructure / memory-systems / data-management. Argues agent memory is a first-class data-management system; surveys current generation; design recommendations from DB / KG / OS memory hierarchies.

### Parent updates
- `entities/emergent-concepts.md` ## Updates — MERGE-then-SORT prepend: 3 new entries sorted into the (date desc, arxiv_id desc) top block. Final order: constraint-tax (06-24) / autodata (06-24) / iLLaDA (06-24) / intermediate-layers (06-23) / rope-bit-allocation (06-23) / agent-native-memory (06-23) / self-compacting (06-22) / periodic-table (06-09) / agents-last-exam (06-03). All 9 entries properly bullet-prefixed (pitfall 51 lstrip smoke-test: 0/0 lines start with `[[` in first 20 lines after Updates header).

### Step 5.5 wikilink-resolution check
- All 3 new entity files have a single `[[emergent-concepts]]` parent link; the parent file exists. 0 broken forward-looking links.

### Dedup
- `endswith(f'-{arxiv_id}.md')` suffix check: 0 collisions (108/108 candidates were fresh; just-restored state)
- `watch_profiles.json[last_result_hashes]`: 3 new MD5 hashes appended (top-level = 9 total; llm-wiki = 6 total; profiles.llm-wiki-explore = 6 total)
- `explore_context.json[chains][*][papers_found]`: 3 new entries appended to `emergent-concepts` chain (now 9 papers total in this chain)

### Tool budget
- All write/commit operations completed cleanly. No pitfall 46a/47 partial-bookkeeping risk.

## 2026-06-25 16:42 UTC — Emergent-concept search (3 fresh themes: LLM embeddings / agent document-reasoning / flow-matching planning)

**Mode**: emergent-concept-search (all 9 named chains at 4/4 since 2026-05-25)
**Method**: HuggingFace daily papers 3-day window (2026-06-23..25) + arxiv abs-page meta extraction (10 parallel workers) + strict subject filter (pitfall 52 recovery) + LLM-flavor title scoring + 5-store dedup
**Candidates surveyed**: 197 raw HF IDs → 61 after strict subject-filter (cs.CV/image/graphics/sound excluded) → 3 picks by score (8/6/6)
**Papers added**: 3

### Papers
1. **EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory** (2606.21649) — Nie, Fu, Feng, Shan (cs.CL, 2026-06-19). Theme: LLM embeddings / long-context retrieval / agentic-memory. Embedding model that produces *evolvable* representations via a continuously-updated latent memory — the same query retrieves different targets depending on prior context. EvoTrain-180K + memory queue + segment-batching (3.8× speedup). Outperforms Qwen3-Embedding-8B and KaLM-Embedding-Gemma3-12B on long-context retrieval; naive RAG with EvoEmbedding surpasses dedicated agentic-memory systems.
2. **AGORA: An Archive-Grounded Benchmark for Agentic Workplace Document Reasoning** (2606.24526) — Guo, Zhang, Zhang, Li, Zheng et al. (cs.CL, 2026-06-23). Theme: LLM agent benchmarking / document-reasoning / long-context exploration. 362 questions × 9,664 authentic workplace docs × 372M tokens × 8 domains. Agentic pipeline for benchmark construction (cross-document task synthesis + leakage-preventing obfuscation + difficulty filtering). Even strongest model reaches only 59.4%.
3. **FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning** (2606.24231) — Li, Liu, Ye, Han, Pan, Han, Zhao (cs.AI, 2026-06-23). Theme: LLM robotics / generative planning / flow-matching. Unifies scoring-based (dense reward supervision, fixed vocabulary) and anchor-based (dynamic proposals, sparse supervision) planning by reframing rewards as *generative conditions* of a flow-matching decoder. SOTA on NAVSIM v1/v2.

### Parent updates
- `entities/emergent-concepts.md` ## Updates — MERGE-then-SORT prepend: 3 new entries sorted into the (date desc, arxiv_id desc) top block. Final order: autodata/constraint-tax/iLLaDA (06-24) / intermediate-layers/agent-native-memory/AGORA/FlowR2A/rope-bit-allocation (06-23, arxiv_id desc) / self-compacting (06-22) / EvoEmbedding (06-19) / periodic-table (06-09) / agents-last-exam (06-03). All 12 entries properly bullet-prefixed (pitfall 51 corrected smoking-gun check: 0/20 lines start with `[[` after Updates header).

### Step 5.5 wikilink-resolution check
- All 3 new entity files have a single `[[emergent-concepts]]` parent link; the parent file exists. 0 broken forward-looking links.

### Dedup
- `endswith(f'-{arxiv_id}.md')` suffix check: 0 collisions (3/3 candidates were fresh)
- 5-store hash check: top-level `watch_profiles[last_result_hashes]` 9→12 (+3); `watch_profiles[llm-wiki].last_result_hashes` 6→9 (+3); `watch_profiles[profiles].llm-wiki-explore.last_result_hashes` 6→9 (+3); `watch_profiles[profiles].llm-wiki-explore.last_results` 6→9 (+3); `explore_context.chains[emergent-concepts].papers_found` 9→12 (+3).
- `explore_context.emergent_concept_papers`: 9→12; `emergent_discoveries`: 9→12; `emergent_concept_search_log` +1; `emergent_concept_search_runs` +1; `runs` +1.

### Pitfalls encountered
- **Pitfall 52 confirmed**: HF `non_cv_count` (197) is a title-flavor upper bound, NOT a subject-filtered count. Top 10 picks were 100% cs.CV by actual `<span class="primary-subject">` subject. Recovery: strict subject filter (`not any(kw in subj for kw in ['computer vision and pattern', 'image and video', 'graphics', 'sound'])`) recovered 61 LLM candidates from 100 non_cv_metadata.
- **Pitfall 58a confirmed**: 0% pre-existing dedup rate (3/3 picks fresh) is EXPECTED on just-restored wiki with 21 entities (post-pitfall-56 state).
- **Different `ensure_ascii` settings per file detected and preserved**: `explore_context.json` = False (raw em-dashes); `watch_profiles.json` = True (escape sequences). Wrote each with its own setting.

### Tool budget
- All write/commit operations completed cleanly. No pitfall 46a/47 partial-bookkeeping risk.
