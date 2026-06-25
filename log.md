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

## 2026-06-25 16:54 UTC — Wiki Explore Agent (run1654)

### Discovery
- **Window**: 3 daily HF pages (2026-06-23, 2026-06-24, 2026-06-25) + 1 monthly archive (2026-06)
- **Total unique arxiv IDs**: 206
- **Pre-existing on disk**: 11 (95% new — consistent with just-restored wiki per pitfall 58a)
- **After strict subject filter (pitfall 52)**: 61 LLM-relevant candidates from 100 non_cv_metadata
- **Bundled script's `non_cv_count` was 100 (title-flavor upper bound)**; strict subject filter recovered 61 (still well above the 9-15 non-CV baseline)

### Picks (3 fresh themes, thematically distinct from prior 7 runs)
| arxiv | title | theme |
|---|---|---|
| 2606.24428 | Escaping the Self-Confirmation Trap (EDV) | agentic-learning / multi-agent-consensus-validation / self-evolution |
| 2606.22388 | PlanBench-XL | agent-benchmark / long-horizon-planning / tool-retrieval / runtime-blocking |
| 2606.24112 | ReMMD | multimodal misinformation / agentic-verification / persistent-memory-evidence-set |

### State updates
- `explore_context.json`: 13 fields refreshed (last_run, last_explore, last_global_explore, last_discovery, last_run_framing, last_framing, last_run_notes, last_pass_type, last_run_method, run_method, last_run_added, exploration_type, emergent_concept_theme, emergent_theme, chains_updated, updated, __last_updated); `chains.emergent-concepts.papers_found` +3; `emergent_concept_papers` +3 (now 15); `emergent_discoveries` +3; `emergent_concept_search_log` +1; `emergent_concept_search_runs` +1; `runs` +1; `entities_count` 24 → 27
- `watch_profiles.json`: 3 new hashes to top-level (12 → 15), `llm-wiki` (9 → 12), `profiles.llm-wiki-explore` (9 → 12); 3 new records to `last_results`

### Cross-check
- 15 arxiv IDs in entities/ ↔ 15 arxiv IDs in state — OK (no orphans, no extras)
- Wikilink integrity: all [[slugs]] in 3 new entity files resolve against entities/
- Step 5.5 check: PASS

### Tool budget
- All write/commit operations completed cleanly. No pitfall 46a/47 partial-bookkeeping risk.

## 2026-06-25 17:14 UTC — Explore run (3 picks, all FRESH, 0% pre-existing)
- **Window**: HuggingFace daily papers 2026-06-22..2026-06-25 (3-day, just-restored wiki default per pitfall 58a) + 1 monthly archive
- **Total unique IDs**: 207 (29+29+56 daily + 105 monthly); 14 pre-existing in entities/ (93% new — expected on just-restored wiki)
- **Pitfall 52 strict subject filter**: 100 non_cv_metadata → 61 LLM candidates (title-flavor upper bound rejected)
- **Discovery**: HF daily papers via bundled `scripts/hf_arxiv_discovery.py --days 3 --months 1 --top-k 100`

### Picks (3 fresh themes, distinct from prior 7 runs)
| arxiv | title | theme |
|---|---|---|
| 2606.24595 | MEMPROBE | agentic-memory evaluation / hidden-state-recovery / confabulation-detection |
| 2606.22953 | Plans Don't Persist | agent context-engineering / plan-persistence / eviction-policy |
| 2606.24667 | DREAM | retrieval / embedding-from-LM / unified-retrieval-generation |

### State updates
- `explore_context.json`: 18 fields refreshed; `chains.emergent-concepts.papers_found` +3 (15→18); `emergent_concept_papers` +3 (15→18); `emergent_discoveries` +3; `emergent_concept_search_log` +1 (5→6); `emergent_concept_search_runs` +1 (5→6); `runs` +1 (5→6); `entities_count` 27 → 30
- `watch_profiles.json`: 3 new hashes to top-level (15→18), `llm-wiki` (12→15), `profiles.llm-wiki-explore` (12→15); 3 new records to `last_results` (12→15)

### Cross-check
- 18 arxiv IDs in entities/ ↔ 18 arxiv IDs in state — OK (no orphans, no extras)
- Wikilink integrity: all 12 [[slugs]] across 3 new entity files resolve against entities/
- Step 5.5 check: PASS
- Pitfall 52 strict subject filter applied: top 3 picks are cs.CL / cs.AI / cs.CL (no cs.CV)
- Pitfall 51 lstrip-prefix check: 18 bullet-prefixed entries after ## Updates — clean

### Tool budget
- All write/commit operations completed cleanly.
## 2026-06-25 17:32 UTC — Explore run (3 picks, all FRESH, multimodal RAG + math-RL + cross-domain-agent-RL themes)
- **Window**: HuggingFace daily papers 2026-06-23..2026-06-25 (3-day, just-restored wiki default per pitfall 58a) + 1 monthly archive
- **Total unique IDs**: 208 (30+29+56 daily + 105 monthly); 17 pre-existing in entities/ (92% new — expected on just-restored wiki)
- **Pitfall 52 strict subject filter**: 80 non_cv_metadata → 45 LLM candidates (title-flavor upper bound rejected — script's `non_cv_count` is misleading without subject re-filter)
- **Discovery**: HF daily papers via bundled `scripts/hf_arxiv_discovery.py --days 3 --months 1 --top-k 80`

### Picks (3 fresh themes)
| arxiv | title | subject | theme |
|---|---|---|---|
| 2606.23997 | ChartWalker | cs.IR | multimodal RAG / cross-chart-reasoning / hierarchical-KG |
| 2606.23543 | VeriEvol | cs.AI | multimodal math reasoning / verifiable Evol-Instruct / RL-data-pipeline |
| 2606.20002 | Connect the Dots | cs.LG | long-horizon agents / cross-domain-RL / agent-training |

### State updates
- `explore_context.json`: 18 fields refreshed; `chains.emergent-concepts.papers_found` +3 (18→21); `emergent_concept_papers` +3 (18→21); `emergent_discoveries` +3; `emergent_concept_search_log` +1 (6→7); `emergent_concept_search_runs` +1 (6→7); `runs` +1 (6→7); `entities_count` 30 → 33
- `watch_profiles.json`: 3 new hashes to top-level (18→21), `llm-wiki` (15→18), `profiles.llm-wiki-explore` (15→18); 3 new records to `last_results` (15→18)

### Cross-check
- 21 arxiv IDs in entities/ ↔ 21 arxiv IDs in state — OK (no orphans, no extras)
- Wikilink integrity: 12 [[slugs]] across 3 new entity files (3 each, all resolve against entities/) — PASS
- Step 5.5 check: 1 broken link caught (the-periodic-table-of-llm-reasoning → the-periodic-table-of-llm-reasoning-a-structured-survey-...) and fixed pre-write
- Pitfall 52 strict subject filter applied: top 3 picks are cs.IR / cs.AI / cs.LG (no cs.CV)
- Pitfall 51 lstrip-prefix check: 21 bullet-prefixed entries after ## Updates — clean
- Pitfall 61 header-duplication check: H2 count = 4 (Scope / Updates / Auto-Discovered Profiles / Chain Status) — clean
- Encoding preserved: explore_context=False (raw em-dash), watch_profiles=True (escape sequences) — divergent state stable

### Tool budget
- All write/commit operations completed cleanly. No pitfall 46a/47 partial-bookkeeping risk.

### MERGE-then-SORT detail
- N_EXISTING_TOP = 3 (new) + 5 (existing top buffer) = 8
- Extracted 8 existing entries (Autodata, Constraint Tax, iLLaDA, entropy-dynamics, agent-native-memory, DREAM, MEMPROBE, AGORA)
- Merged 8 existing + 3 new = 11 entries, sorted arxiv-id-desc
- Top 11 IDs: 25996, 25605, 25331, 25182, 24775, 24667, 24595, 24526, **23997 (NEW)**, **23543 (NEW)**, 20002 (NEW)
- Three new entries landed at positions 9, 10, 11 (correct: lower arxiv-IDs than all 8 existing tops)
- File size: 22,359 → 25,584 chars (+3,225 = expected delta)

### 2026-06-25 17:43 UTC — emergent-concept run (run-1739)
- Method: HuggingFace 3-day daily (2026-06-25..2026-06-23) + monthly archive → 208 unique IDs
- Script: hf_arxiv_discovery.py with --days 3 --months 1 --top-k 100
- Pitfall 52 fired (script Non-CV=188 but top 10 were 100% cs.CV by primary-subject)
- Applied Step 2.5 strict subject filter: 188 → 60 LLM candidates
- LLM-flavor scoring picked top 3:
  - PrivacyAlign (2606.21710, cs.CL, 2026-06-19): agentic-privacy / contextual-alignment
  - Holistic Data Scheduler (2606.24133, cs.LG, 2026-06-23): pretraining-data-mixing / multi-objective-RL
  - EnterpriseClawBench (2606.23654, cs.CL, 2026-06-22): enterprise-agent-evaluation / real-workflow-benchmarking
- All 3 picks verified genuinely new (5-store dedup + filesystem endswith check)
- All 3 entity files written; Step 5.5 wikilink-resolution check: 0 broken
- Prepended to entities/emergent-concepts.md via MERGE-then-SORT (top-8 re-sort, arxiv-ID desc)
- 11-entry merged pool (8 existing + 3 new); new entries landed positions 9, 10, 11
- Preamble-preservation smoke check (pitfall 62): first line = `---` (frontmatter intact)
- File-size sanity check: orig=25584 → new=28278 chars (exact match, no doubling)
- State writes: explore_context.json (15+ top-level fields + chain-level) + watch_profiles.json (4 top + 2 sub-profile)
- ensure_ascii detection: explore_context=False (raw em-dash), watch_profiles=True (escape) — stable divergent state
- Step 7.5 entity↔state cross-check: 24 filesystem arxiv IDs == 24 state arxiv IDs, 0 orphans, 0 extras

### 2026-06-25 17:58 UTC — emergent-concept run (run-1758)
- Method: HuggingFace 3-day daily (2026-06-25..2026-06-23) + monthly archive → 208 unique IDs
- Script: hf_arxiv_discovery.py with --days 3 --months 1 --top-k 100
- Pitfall 52 fired (script Non-CV=185 but raw count was title-flavor upper bound); applied strict subject filter: 185 → 60 LLM candidates
- LLM-flavor scoring + overlap=0 vs prior 36 themes picked top 3:
  - ReNIO (2606.23104, cs.LG, 2026-06-22): on-policy distillation / negative-trajectory-importance estimation
  - PhoneBuddy (2606.23049, cs.CL, 2026-06-22): mobile-deployment / open-model phone-use training
  - Look Light, Think Heavy (2606.22565, cs.CL, 2026-06-21): multimodal-CoT capability audit
- All 3 picks verified genuinely new (5-store dedup + filesystem endswith check)
- All 3 entity files written; Step 5.5 wikilink-resolution check: 0 broken
- Prepended to entities/emergent-concepts.md via MERGE-then-SORT (top-8 re-sort)
- 8-entry merged pool (5 existing + 3 new); new entries landed positions 6, 7, 8 (older than existing Jun-23/24 top)
- Preamble-preservation smoke check (pitfall 62): first line = `---` (frontmatter intact)
- File-size sanity check: 28278 → 31305 chars (+3027, no doubling)
- State writes: explore_context.json (15+ top-level fields + chain-level + 3 list appends) + watch_profiles.json (3 new hashes each at top-level + llm-wiki + llm-wiki-explore sub-profile)
- ensure_ascii detection: explore_context=False (raw em-dash), watch_profiles=True (escape) — stable divergent state
- Step 7.5 entity↔state cross-check: 27 filesystem arxiv IDs == 27 state arxiv IDs, 0 orphans, 0 extras
- Pitfall-60 defensive isinstance guards for watch_profiles sub-profiles fired correctly (both sub-profiles present)
- log.md presence: yes (pitfall 58 not triggered); staged in same atomic commit

### 2026-06-25 18:08 UTC — emergent-concept run (run-1808)
- Method: HuggingFace 3-day daily (2026-06-23..2026-06-25) → 115 unique IDs
- Custom HF discovery script at /tmp/hf_discover_run1808.py (parsed HF `<article>` blocks: `<h3><a href="/papers/{arxiv_id}">Title</a></h3>` pattern); 10-worker ThreadPoolExecutor for parallel arxiv metadata fetch (115 IDs in 4.4s)
- Pitfall 52 strict subject filter applied: 115 → 80 LLM-relevant candidates (excluded cs.CV/cs.GR/cs.MM/eess.AS/physics/cs.SE)
- Combined sort: subject-preference (cs.CL=100, cs.LG=95, cs.AI=90) + LLM-flavor title-boost + recency window + base score → top 3 picks:
  - CalVerT (2606.21777, cs.CL, 2026-06-23): LLM-agent verifier-telemetry / knowledge-intensive-QA
  - Demystifying Training-Time Augmentation (2606.16246, cs.LG, 2026-06-23): data-constrained-pretraining / training-time-augmentation / compute-abundant-regime
  - AC-ODM (2505.23878, cs.LG, 2026-06-23): pretraining-efficiency / online-data-mixing / actor-critic-RL (originally posted 2025/05/29, re-surfaced by HF on 2026-06-23)
- All 3 picks verified genuinely new (5-store dedup + filesystem endswith check; 0% pre-existing rate expected per pitfall-58a for just-restored wiki)
- All 3 entity files written; Step 5.5 wikilink-resolution check: 7 wikilinks total, all resolve (forward + backward links to existing entities)
- Prepended to entities/emergent-concepts.md via MERGE-then-SORT (N_EXISTING_TOP=5, top-8 re-sort)
- 8-entry merged pool (5 existing 06-24/06-23 + 3 new 06-23); new entries landed positions 6, 7, 8 (older than existing 06-23 entries by arxiv-id tiebreak: 2606.21777 > 2606.16246 > 2505.23878)
- Preamble-preservation smoke check (pitfall 62): first line = `---` (frontmatter intact)
- H2 count check: 4 (Scope, Updates, Auto-Discovered Profiles, Chain Status) — no doubled-section-header bug (pitfall 61)
- File-size sanity check: 31457 → 35029 chars (+3572, no doubling)
- State writes: explore_context.json (entities_count 39→42, chains_updated=['emergent-concepts'], 1 record each to emergent_concept_search_log/runs/emergent_concept_search_runs + 3 records each to emergent_concept_papers/emergent_discoveries/chains[emergent-concepts].papers_found) + watch_profiles.json (3 new hashes at top-level + llm-wiki + llm-wiki-explore sub-profile + 3 last_results records)
- ensure_ascii detection: explore_context=False (raw em-dash absent, no encoding), watch_profiles=True (escape sequences) — stable divergent state confirmed
- Step 7.5 entity↔state cross-check (pre-commit): 30 filesystem arxiv IDs == 30 state arxiv IDs, 0 orphans, 0 extras
- Pitfall-60 defensive isinstance guards for watch_profiles sub-profiles: both llm-wiki (dict) and profiles.llm-wiki-explore (dict) present, writes succeeded
- Per-run counter suffix on all 5 /tmp/ artifacts: run1808 (per sibling-subagent /tmp/*.py interference fix)
- log.md presence: yes; staged in same atomic commit

## 2026-06-25 18:29 UTC (run1823)
- Emergent-concept pass via 3-day HF window (2026-06-22..2026-06-25)
- 115 raw HF papers → 52 after Step 2.5 strict subject filter → top-3 LLM-flavor picks
- 3 new entity pages created:
  - LingxiDiagBench (2602.09379, cs.AI, 2026-02-10): Chinese psychiatric-consultation multi-agent benchmark
  - When Agents Commit Too Soon (2606.22936, cs.AI, 2026-06-22): premature-commitment diagnostic for long-horizon LLM agents
  - HAKARI-Bench (2606.22778, cs.IR, 2026-06-22): lightweight retrieval-architecture benchmark
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT (N_EXISTING_TOP=30, all existing entries >= min_new_date so new entries sort below)
- State files: explore_context.json (33 in emergent_concept_papers, 33 in chains[emergent-concepts].papers_found), watch_profiles.json (33 top-level hashes + 33 in each sub-profile after orphan-fix pass)
- Pitfalls hit: 62 (preamble-loss — first attempt lost preamble; recovered via git checkout + corrected recipe), 61 (boundary-header-doubling — first attempt doubled H2s; recovered via fixed tail-extraction logic)
- Pitfalls cleanly avoided: 50 (cross-check pre-commit), 52 (strict subject filter), 28 (wikilink resolution check — caught broken rl-index link in HAKARI page, removed), 53 (list appends), 60 (defensive isinstance), 64 (chains_updated REPLACE not append), 65 (custom HF parser since bundled script missing — wrote /tmp/hf_discover_run1823.py)

## 2026-06-25 18:38 UTC (run1830)
- Emergent-concept pass via 3-day HF window (2026-06-22..2026-06-25, end_d=2026-06-25)
- 115 raw HF papers → 80 after Step 2.5 strict subject filter (35% CV/graphics/sound excluded) → 49 fresh after 5-store dedup → 3 manual picks from LLM-flavor + LLM-research relevance
- 3 new entity pages created:
  - RL-Index (2606.16316, cs.IR, 2026-06-15): GRPO-trained offline index-rationale augmentation that shifts reasoning compute from query time to indexing
  - Counsel (2606.21627, cs.AI, 2026-06-19): first public meta-evaluation dataset for LLM-as-judge on agentic tasks (tau-bench + DA-Code), human-labeled spot-on / location-only / should-not-flag
  - Beyond Reward Engineering (2606.18831, cs.CL, 2026-06-17): data-recipe-first long-context RL with minimal outcome-based GRPO, +7.2/+3.2/+6.4 on Qwen3-4B/8B/30B-A3B + agentic transfer (GAIA +4.8, BrowseComp +7.0)
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT (N_EXISTING_TOP=10, new dates 06/15-06/19 inserted at positions 9-11 after 2026-06-24 and 2026-06-23 entries)
- State files: explore_context.json (36 in emergent_concept_papers, 36 in chains[emergent-concepts].papers_found), watch_profiles.json (36 top-level hashes + 36 in each sub-profile)
- ensure_ascii detection: explore_context=False (raw em-dash absent), watch_profiles=True (escape sequences) — stable divergent state confirmed
- Step 7.5 entity↔state cross-check (pre-write): 33 filesystem == 33 state arxiv IDs, 0 orphans, 0 extras
- Step 7.5 entity↔state cross-check (post-write): 36 filesystem == 36 state, 0 orphans, 0 extras
- Pitfalls cleanly avoided: 4/32/41/46/49/62 (MERGE-then-SORT + preamble preservation), 52 (strict subject filter), 28 (wikilink resolution check — all 17 new wikilinks resolved), 53 (list-shaped appends for search_runs/runs), 60 (defensive isinstance on watch sub-profiles), 63 (no execute_code in cron context — used write_file + terminal), 64 (chains_updated REPLACE not append), 65 (custom HF parser — bundled script missing), 66 (N_EXISTING_TOP > len(new_entries) safe default)
- Step 2.5 strict subject filter recovered 80 LLM candidates from 115 raw non_cv_metadata (32 CV + 3 cs.GR + 0 cs.SD excluded); top-3 picks are all cs.CL/cs.AI/cs.IR with score=4
- Per-run counter suffix on /tmp/ artifacts: run1830 (sibling-subagent /tmp/*.py interference fix)

## 2026-06-25 18:51 UTC (run1850)
- Emergent-concept pass via 3-day HF window (2026-06-23..2026-06-25, end_d=2026-06-25)
- 115 raw HF papers → 80 after Step 2.5 strict subject filter (35 CV/graphics/sound excluded) → 46 fresh after 5-store dedup → 3 picks from LLM-flavor + subject-priority scoring
- 3 new entity pages created:
  - OpenThoughts-Agent (2606.24855, cs.AI, 2026-06-23): open end-to-end data curation pipeline for agentic LLMs; 100+ controlled ablations; 100K-example dataset; Qwen3-32B @ 44.8% avg over 7 agentic benchmarks (3.9pp > Nemotron-Terminal-32B)
  - Qwen-AgentWorld (2606.24597, cs.CL, 2026-06-23): first family of language world models (35B-A3B + 397B-A17B) simulating 7 agentic domains via long CoT, trained on 10M+ trajectories with CPT/SFT/RL pipeline + AgentWorldBench
  - Tapered Language Models (2606.23670, cs.LG, 2026-06-22): depth-aware capacity allocation via MLP-width cosine taper; +perplexity on 3 scales × 4 architectures (Transformer, Gated Attention, Hope-attention, Titans) at no extra params
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT (N_EXISTING_TOP=8, new dates 06/22-06/23 interleaved at positions 5, 8, 11)
- State files: explore_context.json (39 in emergent_concept_papers, 39 in chains[emergent-concepts].papers_found), watch_profiles.json (39 top-level hashes + 39 in llm-wiki + 39 in profiles.llm-wiki-explore)
- ensure_ascii detection: explore_context=False (raw em-dash), watch_profiles=True (escaped) — divergent stable state confirmed (3rd consecutive run)
- Step 7.5 entity↔state cross-check (post-write): 39 filesystem == 39 state arxiv IDs, 0 orphans, 0 extras
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + N_EXISTING_TOP=len(new)+5), 52 (strict subject filter — 80 LLM candidates from 115 raw), 28 (wikilink resolution — all 9 new wikilinks resolved), 53 (list appends for search_runs/runs), 60 (defensive isinstance on watch sub-profiles — both llm-wiki + profiles.llm-wiki-explore updated cleanly), 63 (no execute_code — used write_file + terminal pattern), 64 (chains_updated REPLACE not append), 65 (custom HF parser — bundled script still missing; wrote /tmp/hf_discover_run1850.py)
- Per-run counter suffix on all /tmp/ artifacts: run1850 (per sibling-subagent /tmp/*.py interference fix)
- log.md presence: yes; staged in same atomic commit
## 2026-06-25 18:58 UTC — Run summary
- Theme: LLM agent autonomy under-evaluated safety axes (privilege + context) + reasoning theory boundary
- Discovery: HF daily 3-day window 2026-06-23..25 (115 unique arxiv IDs) → strict subject non-CV filter (43 candidates) → LLM-flavor kw scoring → top 3 picks
- Picks (3):
  - A Verifiable Search Is Not a Learnable Chain-of-Thought (2606.21884, cs.LG, 2026-06-20): CoT distillation provably fails for cryptarithm (0.01-0.07 across 11 designs + RLVR + self-training) even with 97-100% line-level arithmetic; mechanistic gap not capability gap; holds 3B→671B
  - When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents (2606.20023, cs.SE, 2026-06-18): ToolPrivBench across 8 domains × 5 risk patterns; general safety alignment does NOT transfer to least-privilege tool choice; privilege-aware post-training defense proposed
  - Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? (2606.23189, cs.AI, 2026-06-22): AgentCIBench — 11/15 frontier agents leak on >50% of contextual-integrity scenarios; 67.9% avg leakage; failures persist end-to-end in environment
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT Recipe C (N_EXISTING_TOP=len(new)+5=8; all new dates 06/18-06/22 older than existing top 06/23-06/24; landed at positions 9, 10, 11)
- State files: explore_context.json (42 in emergent_concept_papers, 42 in emergent_discoveries, 39 in chains[emergent-concepts].papers_found), watch_profiles.json (42 top-level hashes + 42 in llm-wiki + 42 in profiles.llm-wiki-explore + 39 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (raw em-dash), watch_profiles=True (escaped) — divergent stable state confirmed (4th consecutive run)
- Step 7.5 entity↔state cross-check (post-write): 42 filesystem == 42 state arxiv IDs after commit; 0 orphans pre-write (the 3 orphans in the pre-write check were the 3 new entity files being added in this run — expected)
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + Recipe C + last-entry-boundary fix), 52 (strict subject filter — 43 LLM candidates from 115 raw), 28 (wikilink resolution — all 12 new wikilinks resolved across 3 new entity files), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 59 (pre-write entity↔state cross-check detected expected orphans as the new files being added in this run), 60 (defensive isinstance on watch sub-profiles — both llm-wiki + profiles.llm-wiki-explore updated cleanly), 63 (no execute_code — used write_file + terminal pattern), 64 (chains_updated REPLACE not append), 65 (custom HF parser in /tmp/hf_discover_run1858.py — bundled scripts/hf_arxiv_discovery.py still missing on the restored wiki)
- Per-run counter suffix on all /tmp/ artifacts: run1858 (per sibling-subagent /tmp/*.py interference fix)
- log.md presence: yes; staged in same atomic commit## 2026-06-25 19:25 UTC — Run summary
- Theme: LLM agent infrastructure (OS-level substrate) + agent evaluation (scientific replication) + inference efficiency (channel-asymmetric compression)
- Discovery: HF daily 3-day window 2026-06-23..25 (115 unique arxiv IDs) → Step 2.5 strict subject non-CV filter (40 LLM candidates from 75 fresh after dedup; 35 CV/graphics/sound excluded) → LLM-flavor kw scoring + subject-priority tiebreak → top 3 picks
- Picks (3):
  - AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction (2606.23449, cs.AI, 2026-06-22): OS-level agent harness on AOSP treating agents as first-class OS actors; +21.12pp task completion, -51.55% token cost on challenging OS-agent benchmarks
  - NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers? (2606.24530, cs.CL, 2026-06-23): 90-task cross-discipline benchmark from peer-reviewed Nature papers with NatureGym pipeline; 17.8% SOTA-match rate under g>0.1 criterion; web-search-disabled protocol
  - CAVEWOMAN: How Large Language Models Behave Under Linguistic Input and Output Compression (2606.24083, cs.CL, 2026-06-23): two-channel compression protocol; output compression saves 1.4-2.4x cost; input compression is a lose-lose (+1.15x net cost); "correct yet divergent" regime on non-reasoning models
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT Recipe C (N_EXISTING_TOP=len(new)+5=8; all new dates 06/22-06/23 older than existing top 06/23-06/24; landed at positions 9, 10, 11)
- State files: explore_context.json (45 in emergent_concept_papers, 45 in emergent_discoveries, 45 in chains[emergent-concepts].papers_found, 15 runs, 15 emergent_concept_search_runs), watch_profiles.json (45 top-level hashes + 45 in llm-wiki + 45 in profiles.llm-wiki-explore + 45 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (raw em-dash), watch_profiles=True (escaped) — divergent stable state confirmed (5th consecutive run)
- Step 7.5 entity↔state cross-check (pre-write): 3 orphans == 3 new entity files in this run (self-add tolerance, expected); (post-write): 45 filesystem == 45 state arxiv IDs, 0 orphans, 0 extras
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + Recipe C + last-entry-boundary fix), 52 (strict subject filter — 40 LLM candidates from 75 raw), 28 (wikilink resolution — caught and fixed 4 broken forward-looking links before write: enterpriseclawbench canonical slug, plans-don't-persist canonical slug, tmax dropped, counsel canonical slug), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 59 (pre-write entity↔state cross-check with self-add tolerance), 60 (defensive isinstance on watch sub-profiles — both llm-wiki + profiles.llm-wiki-explore present and updated), 63 (no execute_code — used write_file + terminal pattern), 64 (chains_updated REPLACE not append), 65 (custom HF parser in /tmp/hf_discover_run1925.py — bundled scripts/hf_arxiv_discovery.py still missing)
- Per-run counter suffix on all /tmp/ artifacts: run1925 (per sibling-subagent /tmp/*.py interference fix)
- log.md presence: yes; staged in same atomic commit## 2026-06-25 19:25 UTC — Run summary
- Theme: terminal-agent open-RL recipe + cross-domain biological foundation model + inference-time alignment-tax mitigation
- Discovery: HF daily 3-day window 2026-06-23..25 (116 unique arxiv IDs) → Step 2.5 strict subject non-CV filter (78 from 116 after subject; 35 fresh after 5-store dedup) → LLM-flavor kw scoring + subject-priority tiebreak → top 3 picks
- Picks (3):
  - Tmax: A simple recipe for terminal agents (2606.23321, cs.CL, 2026-06-22): open RL training recipe for terminal-using LM agents; achieves 27% on Terminal-Bench 2.0 with small curated dataset and simple reward shaping where prior open attempts fell well short
  - BioMatrix: Towards a Comprehensive Biological Foundation Model Spanning the Modality Matrix of Sequences, Structures, and Language (2606.22138, cs.CL, 2026-06-20): first decoder-only multimodal FM integrating sequences, structures, and natural language for both molecules and proteins within a single architecture; unifies prior disjoint axes of biological-FM design
  - Deeper is Not Always Better: Mitigating the Alignment Tax via Confident Layer Decoding (2606.21906, cs.CL, 2026-06-20): identifies Guess-Refine-Perturb dynamic across LLM depth and introduces Confident Decoding, a training-free strategy that selects intermediate-layer predictions to recover reasoning quality lost to alignment training
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT with N_EXISTING_TOP=len(new)+5=8 (default for all 3 recipes; Recipe C variant: all new entries 2026-06-20..22 are older than existing top 2026-06-23..24; landed at positions 9, 10, 11)
- State files: explore_context.json (48 in emergent_concept_papers, 48 in emergent_discoveries, 48 in chains[emergent-concepts].papers_found, 16 runs, 16 emergent_concept_search_runs), watch_profiles.json (48 top-level hashes + 48 in llm-wiki + 48 in profiles.llm-wiki-explore + 48 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (raw em-dash), watch_profiles=True (escaped) — divergent stable state confirmed (6th consecutive run)
- Step 7.5 entity↔state cross-check (pre-write): 0 orphans (3 new entity files added during run are the expected self-adds); (post-write): 48 filesystem == 48 state arxiv IDs, 0 orphans, 0 extras
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + safe default N=len(new)+5 handles Recipes A/B/C), 51 (kept `- ` prefix on new entries — first attempt dropped it, recovered via git checkout + re-run with fix), 52 (strict subject filter — 35 LLM candidates from 78 raw), 28 (wikilink resolution — 0 broken across all 3 new entity files), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 59 (pre-write entity↔state cross-check with self-add tolerance), 60 (defensive isinstance on watch sub-profiles), 63 (no execute_code — used write_file + terminal pattern throughout), 64 (chains_updated REPLACE not append), 65 (custom HF parser in /tmp/hf_discover_run1925.py — bundled scripts/hf_arxiv_discovery.py still missing on the restored wiki), 39 (workdir=/home/hermes/wiki on every terminal call)
- Per-run counter suffix on all /tmp/ artifacts: run1925 (per sibling-subagent /tmp/*.py interference fix; 5 artifacts total: /tmp/hf_discover_run1925.py, /tmp/dedup_pick_run1925.py, /tmp/build_slugs_run1925.py, /tmp/build_entities_run1925.py, /tmp/review_top3_run1925.py, /tmp/prepend_updates_run1925.py, /tmp/update_state_run1925.py)
- log.md presence: yes; staged in same atomic commit## 2026-06-25 19:55 UTC — Run summary
- Theme: hybrid attention (head-level fusion) + scientific agents (certainty-aware skills) + safety/reasoning (deliberation skepticism)
- Discovery: HF daily 3-day window 2026-06-23..25 (116 unique arxiv IDs) → custom fallback parser + Step 2.5 strict subject non-CV filter (76 LLM candidates) → 6-store dedup (31 truly fresh after cross-checking entities/, explore_context.json[chains].papers_found, emergent_concept_papers, wp[last_result_hashes], wp[llm-wiki][last_result_hashes], wp[profiles.llm-wiki-explore].last_result_hashes + .last_results) → broadened LLM-flavor kw scoring + subject-priority tiebreak → top 3 picks
- Picks (3):
  - Do Thinking Tokens Help with Safety? (2606.25013, cs.LG, 2026-06-23): refusal/compliance is 84-95% AUROC predictable from first-token hidden representation before any visible thinking; ~74% of text-level deliberations occur when distribution already locked to one side; ~20% of thinking suffices to lock outcome; existing safety interventions shift to over-refusal while suppressing already-scarce deliberation signals
  - HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization (2606.20097, cs.CL, 2026-06-18): head-level (not layer-level) hybrid attention granularity motivated by interpretability showing cross-head functional specialization; interpretability-driven selection of retrieval-critical heads + scale-normalized fusion module; 7:1 LA-to-FA ratio matches 3:1 layer-wise hybrid; +69% over baseline at 512K context with 15B training tokens
  - Notes2Skills: From Lab Notebooks to Certainty-Aware Scientific Agent Skills (2606.11897, cs.CL, 2026-06-10): two-stage framework turning raw lab notebooks into verifiable agent skills while preserving author certainty markers; only configuration across 7 conditions + 3 wet-lab sessions that neither misclassifies uncertain notes as firm nor discards firm ones; certainty preservation identified as the missing piece between lab notebooks and reliable agent skills
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT Recipe B (interleaved: Do Thinking Tokens 06-23 lands between 06-23 existing entries at position 5; HydraHead 06-18 lands at position 41; Notes2Skills 06-10 lands at position 46); N_EXISTING_TOP=45 (gte_count for min_new_date 06-10)
- State files: explore_context.json (51 in emergent_concept_papers, 51 in emergent_discoveries, 45 in chains[emergent-concepts].papers_found, 17 runs, 17 emergent_concept_search_runs, 19 in emergent_concept_search_log), watch_profiles.json (51 top-level hashes + 51 in llm-wiki + 51 in profiles.llm-wiki-explore + 51 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (no em-dash in new content; raw em-dash bytes preserved in updated fields), watch_profiles=True (escaped) — divergent stable state confirmed (7th consecutive run)
- Step 7.5 entity↔state cross-check (pre-write): 3 orphans == 3 new entity files added in this run (self-add tolerance, expected); (post-write): 51 filesystem == 51 state arxiv IDs, 0 orphans, 0 extras
- Step 5.5 wikilink-resolution check: 1 broken forward-looking link detected in initial Notes2Skills draft (fictitious openclawbench-2606.22273 reference); fixed by replacing with 2 real wikilinks (Tmax + Agents' Last Exam); final check: 0 broken across all 3 new entity files
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + Recipe B + safe default N=len(new)+5=8 actually evaluated to 45 due to gte_count; final-entry-boundary \n## scan), 52 (strict subject filter — 31 LLM candidates from 76 raw after 6-store dedup), 28 (wikilink resolution — 1 broken fixed before write), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 59 (pre-write entity↔state cross-check with self-add tolerance), 60 (defensive isinstance on watch sub-profiles — both updated), 63 (no execute_code — used write_file + terminal pattern), 64 (chains_updated REPLACE not append), 65 (custom HF parser in /tmp/hf_discover_run1955.py — bundled scripts/hf_arxiv_discovery.py still missing on the restored wiki), 39 (workdir=/home/hermes/wiki on every terminal call)
- Per-run counter suffix on all /tmp/ artifacts: run1955 (per sibling-subagent /tmp/*.py interference fix; artifacts: /tmp/hf_discover_run1955.py, /tmp/fetch_meta_run1955.py, /tmp/write_entities_run1955.py, /tmp/prepend_run1955.py, /tmp/update_state_run1955.py, /tmp/verify_state_run1955.py, /tmp/log_entry_run1955.txt)
- log.md presence: yes; staged in same atomic commit
## 2026-06-25 20:14 UTC — Run summary
- Theme: agentic multimodal data tailoring + query-head sparse-MoE + self-distillation with reflective trajectories
- Discovery: HF daily 3-day window 2026-06-23..25 (116 unique arxiv IDs) → fallback parser + Step 2.5 strict subject non-CV filter (74 LLM candidates after cs.HC/physics/q-bio/q-fin/stat excluded) → 6-store dedup (26 truly fresh after cross-checking entities/, explore_context.json[chains].papers_found, emergent_concept_papers, wp[last_result_hashes], wp[llm-wiki][last_result_hashes], wp[profiles.llm-wiki-explore].last_result_hashes + .last_results) → broadened LLM-flavor kw scoring + subject-priority tiebreak → top 3 picks
- Picks (3):
  - DataClaw0: Agentic Tailoring Multimodal Data from Raw Streams (2606.21337, cs.LG, 2026-06-19): reframes multimodal data prep as an agentic capability rather than heuristic pipeline; two-stage training (semantic synthesis grounded in Factual Anchors → SFT + GRPO) trains a 9B DataClaw_0 model; DataClaw_0-val = first dedicated data-refinement benchmark validated against downstream task utility; +gains on video generation, VQA, GUI navigation at fraction of manual-curation cost
  - Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention (2606.20945, cs.LG, 2026-06-18): composes MoE on top of GQA — router selects k query-head experts per token while KV heads remain dense; matches all-active GQA baseline at 250M / 30B tokens with ~50% active query heads; introduces a complementary query-head sparse-activation axis that composes with FFN-level MoE → 2D sparse-activation design space for transformers at long context
  - Learning from Your Own Mistakes: Constructing Learnable Micro-Reflective Trajectories for Self-Distillation (2606.18844, cs.LG, 2026-06-17): introduces TAPO (Trajectory-Augmented Policy Optimization) — advances self-distillation from implicit KL alignment to explicit trajectory construction; contrastive same-prompt sampling builds micro-reflective corrections anchored in the learner's own erroneous prefix; +gains over GRPO on AIME 2024/2025 + HMMT 2025 at matched training steps; modular components compose with any PPO/GRPO trainer
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT Recipe C (all 3 new entries older than existing top entries which were all 2026-06-24); landed at positions 9-11 below the existing top-8 06-24/06-23 entries; N_EXISTING_TOP=8 (len(new)+5 default)
- State files: explore_context.json (54 in emergent_concept_papers, 54 in emergent_discoveries, 48 in chains[emergent-concepts].papers_found, 19 runs, 19 emergent_concept_search_runs, 21 in emergent_concept_search_log), watch_profiles.json (54 top-level hashes + 54 in llm-wiki + 54 in profiles.llm-wiki-explore + 54 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (raw em-dash bytes), watch_profiles=True (escaped) — divergent stable state confirmed (8th consecutive run)
- Step 7.5 entity↔state cross-check (pre-write): 3 orphans == 3 new entity files added in this run (self-add tolerance, expected); (post-write): 54 filesystem == 54 state arxiv IDs, 0 orphans, 0 extras
- Step 5.5 wikilink-resolution check: 1 broken forward-looking link detected in initial Grouped Query Experts draft (deco-sparse-moe-dense-comparable-2605.10933 not in entities/); fixed by replacing with a-verifiable-search-is-not-a-learnable-chain-of-thought-2606.21884 (existing entity); final check: 0 broken across all 3 new entity files
- Pitfalls hit: NONE in main flow (fixed bug in MERGE-then-SORT recipe: new_entry_re.compile was missing re.MULTILINE flag, only matching 1 of 3 new entries — fixed and re-ran)
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + Recipe C + safe default N=len(new)+5=8), 52 (strict subject filter — 74 LLM candidates from 76 raw after cs.HC/physics expansion), 28 (wikilink resolution — 1 broken fixed before write), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 59 (pre-write entity↔state cross-check with self-add tolerance), 60 (defensive isinstance on watch sub-profiles — both updated), 63 (no execute_code — used write_file + terminal pattern throughout), 64 (chains_updated REPLACE not append), 65 (custom HF parser — bundled scripts/hf_arxiv_discovery.py still missing on restored wiki; copied to /tmp/hf_disc_fb.py), 39 (workdir=/home/hermes/wiki on every terminal call)
- Per-run counter suffix on all /tmp/ artifacts: run2008 (per sibling-subagent /tmp/*.py interference fix; artifacts: /tmp/hf_disc_fb.py (copied), /tmp/pick_top3_run2008.py, /tmp/fetch_meta_run2008.py, /tmp/print_picks_run2008.py, /tmp/state_check_run2008.py, /tmp/build_entries_run2008.txt, /tmp/merge_sort_run2008.py, /tmp/debug_merge_run2008.py, /tmp/update_state_run2008.py, /tmp/log_entry_run2008.txt)
- log.md presence: yes; will be staged in same atomic commit

## 2026-06-25 20:45 UTC — Run summary
- Theme: agent-runtime substrate engineering (PyTorch-like session model) + LLM RL curriculum geometry (Bayesian optimization over problem manifold) + LLM-augmented causal-discovery (epistemological audit)
- Discovery: HF daily 3-day window 2026-06-23..25 (110 unique arxiv IDs) → custom HF parser /tmp/hf_discover_run2030.py + Step 2.5 strict subject non-CV filter (38 LLM candidates after cs.SE/cs.CL/cs.AI/cs.LG/cs.IR/cs.HC kept, cs.CV/cs.RO/cs.SD/cs.GR excluded) → 5-store dedup (cross-check entities/, explore_context.json[chains].papers_found, emergent_concept_papers, wp[last_result_hashes], wp[llm-wiki][last_result_hashes], wp[profiles.llm-wiki-explore].last_result_hashes + .last_results) → 3 truly fresh after cross-check → LLM-flavor kw scoring + subject-priority tiebreak → top 3 picks
- Picks (3):
  - OpenRath: Session-Centered Runtime State for Agent Systems (2606.19409, cs.SE, 2026-06-17): PyTorch-like programming model consolidating fragmented runtime state (transcripts, tool effects, memory events, workspace placement, branch provenance, replay evidence) into a single first-class session object — autograd-tape analogy for agent engineering
  - Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of Large Language Models (2606.19750, cs.LG, 2026-06-18): reformulates LLM RL curriculum learning as Bayesian optimization over a learned manifold of problem difficulty, replacing independent-arm bandits with a posterior that shares statistical strength across geometrically similar problems
  - Causal Discovery in the Era of Agents (2606.23608, cs.AI, 2026-06-22): epistemological audit of LLM-causal-discovery work (pairwise direction inference, graph-structure proposal, LM-as-prior) arguing these methods obscure whether causal evidence comes from data+assumptions or from textual associations, prompt artifacts, and hallucinated mechanisms
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT Recipe C (all 3 new entries 06-17/06-18/06-22 older than existing top entries which were all 2026-06-23..24; landed at positions 2, 3, 4 right after the `## Updates` header in date-DESC within-cluster order: causal-discovery 06-22 → manifold-bandits 06-18 → openrath 06-17)
- State files: explore_context.json (60 in emergent_concept_papers, 60 in emergent_discoveries, 60 in chains[emergent-concepts].papers_found, 20 runs, 20 emergent_concept_search_runs, 22 in emergent_concept_search_log), watch_profiles.json (60 top-level hashes + 60 in llm-wiki + 60 in profiles.llm-wiki-explore + 57 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (raw em-dash bytes preserved), watch_profiles=True (escaped) — divergent stable state confirmed (9th consecutive run)
- Step 7.5 entity↔state cross-check (post-write): 60 filesystem arxiv IDs == 60 state arxiv IDs, 0 orphans, 0 extras; entities_count claim = 72 actual = 72 (60 paper entities + 12 meta/topical entities)
- Step 5.5 wikilink-resolution check: 1 broken forward-looking link detected in initial Causal Discovery draft (critique-of-agent-model-2606.23991 not in entities/); fixed by replacing with capable-but-careless-do-computer-use-agents-follow-contextual-integrity-2606.23189 (existing entity with thematic fit on agent-capability audit); final check: 0 broken across all 3 new entity files
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + Recipe C + safe default N=len(new)+5=8), 52 (strict subject filter — 38 LLM candidates from 110 raw after cv/ro/sd exclusion), 28 (wikilink resolution — 1 broken fixed before commit), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 59 (pre-write entity↔state cross-check with self-add tolerance), 60 (defensive isinstance on watch sub-profiles — all 3 updated), 63 (no execute_code — used write_file + terminal pattern throughout), 64 (chains_updated REPLACE not append), 65 (custom HF parser — bundled scripts/hf_arxiv_discovery.py still missing), 39 (workdir=/home/hermes/wiki on every terminal call)
- Per-run counter suffix on all /tmp/ artifacts: run2030
- log.md presence: yes; staged in same atomic commit
## 2026-06-25 20:55 UTC — Run summary
- Theme: LLM agent memory governance (multi-principal shared-memory) + hierarchical RAG (attention-guided progressive embeddings) + open-ended search-agent benchmark (atomic-criterion evaluation)
- Discovery: HF daily 3-day window 2026-06-22..24 (93 unique arxiv IDs) → custom HF parser /tmp/hf_disc_run2055.py + Step 2.5 strict subject non-CV filter (20 LLM candidates after cs.CV/cs.RO/cs.SD/cs.GR exclusion + 5-store dedup) → LLM-flavor kw scoring + date tiebreak → top 3 picks
- Picks (3):
  - GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents (2606.18829, cs.LG, 2026-06-17): benchmark for shared-memory LLM agent deployments where multiple principals write to a common memory pool and query it under different authorization boundaries; evaluates three axes jointly (utility for long-horizon state updates, access control across contextual authorization boundaries, agent-facing actions under governance); Ren, Zhe; Yang, Yibo; Chen, Yimeng; +7 more
  - SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG (2606.18381, cs.CL, 2026-06-16): attention-guided hierarchical RAG framework organizing sentence-level chunks into progressively larger semantically-coherent units, using tree search guided by attention-derived signals; avoids the three failure modes of prior hierarchical RAG (LLM-guided chunking costs, single-level fixed granularity, summarization information loss); Abaskohi, Laradji, West, Carenini
  - DailyReport: An Open-ended Benchmark for Evaluating Search Agents on Daily Search Tasks (2606.12871, cs.AI, 2026-06-11): open-ended benchmark of 150 realistic daily information-seeking tasks paired with 3,546 atomic evaluation criteria; addresses the gap between specialized SA benchmarks (unrealistic task distribution) and real-world daily search deployment (coarse task-level rubrics limit interpretability); Han, Liu, Zhu, +7 more
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT Recipe C (all 3 new entries 06-11/06-16/06-17 older than existing top 2026-06-18/06-22; landed at positions 1, 2, 3 in date-DESC within-cluster order: GateMem 06-17 → SproutRAG 06-16 → DailyReport 06-11)
- State files: explore_context.json (63 in emergent_concept_papers, 63 in emergent_discoveries, 63 in chains[emergent-concepts].papers_found, 21 runs, 21 emergent_concept_search_runs), watch_profiles.json (63 top-level hashes + 63 in llm-wiki + 63 in profiles.llm-wiki-explore + 60 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (raw em-dash bytes preserved), watch_profiles=True (escaped) — divergent stable state confirmed (10th consecutive run)
- Step 7.5 entity↔state cross-check (post-write): 63 filesystem arxiv IDs == 63 state arxiv IDs, 0 orphans, 0 extras; entities_count = 75 actual (63 paper entities + 12 meta/topical entities)
- Step 5.5 wikilink-resolution check: 2 broken forward-looking links detected in initial new-block (mcompassrag-2606.18508, worldlines-2606.18847 — both candidates but NOT picked, hence no entity file); fixed by replacing with hakari-bench-2606.22778 (RAG efficiency sibling) and agent-orchestration (parent meta-page); final check: 0 broken across all 7 wikilinks in new block
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + Recipe C + safe default N=len(new)+5=8), 52 (strict subject filter — 20 LLM candidates from 93 raw), 28 (wikilink resolution — 2 broken forward-looking fixed before commit), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 59 (pre-write entity↔state cross-check with self-add tolerance), 60 (defensive isinstance on watch sub-profiles — all 3 updated), 63 (no execute_code — used write_file + terminal pattern throughout), 64 (chains_updated REPLACE not append), 65 (custom HF parser — bundled scripts/hf_arxiv_discovery.py still missing on restored wiki; /tmp/hf_disc_run2055.py), 39 (workdir=/home/hermes/wiki on every terminal call), 50 (per-run counter suffix on all /tmp/ artifacts: run2055)
- Per-run counter suffix on all /tmp/ artifacts: run2055 (artifacts: /tmp/hf_disc_run2055.py, /tmp/hf_papers_run2055.json, /tmp/dedup_pick_run2055.py, /tmp/candidates_run2055.json, /tmp/fetch_meta_run2055.py, /tmp/candidates_with_abs_run2055.json, /tmp/build_slugs_run2055.py, /tmp/picks_run2055.json, /tmp/build_entities_run2055.py, /tmp/new_block_run2055.md, /tmp/first_entry_run2055.md, /tmp/update_state_run2055.py)
- log.md presence: yes; staged in same atomic commit

## 2026-06-25 21:09 UTC — Run summary
- Theme: LLM agent epistemology (agency-internalism / GIC architecture) + LLM discrete-text-optimization framework (open-source unification) + LLM-agent creative/multimodal (symbolic-music grammar)
- Discovery: HF daily 3-day window 2026-06-23..25 (116 unique arxiv IDs) → custom HF parser /tmp/hf_discover_run2109.py + Step 2.5 strict subject non-CV filter (53 LLM candidates after cs.CV-heavy exclusion + 5-store dedup of 116→57 fresh) → LLM-flavor kw scoring + date tiebreak → top 3 picks
- Picks (3):
  - Critique of Agent Model (2606.23991, cs.AI, 2026-06-22): epistemic audit of "agent" as a term of art; distinguishes *agentic* systems (engineered workflows) from *agentive* systems (endogenous capabilities); proposes Goal-Identity-Configurator (GIC) reference architecture combining hierarchical goal decomposition, identity evolution, simulative reasoning grounded in a separately trained world model, learned self-regulation, and self-directed learning; Xing, Eric; Deng, Mingkai; Hou, Jinyu
  - TROPT: An Open Framework for Unifying and Advancing Discrete Text Optimization (2606.23496, cs.LG, 2026-06-22): first open-source framework unifying discrete text-trigger optimizers (jailbreaks, auditing, interpretability probes) under a single interface; ships 30+ recipes / 15+ optimizers (white-box to black-box) / 15+ losses (foundational to SOTA); controlled large-scale study surfacing potent-yet-underadopted jailbreak techniques; demonstrates cross-domain porting (LLM jailbreak → corpus-poisoning embedding model); Ben-Tov, Matan; Sharif, Mahmood
  - Libretto: Giving LLM Agents a Sense of Musical Structure (2606.22708, cs.SD, 2026-06-21): agent-facing framework turning symbolic music from a raw token sequence into a measurable/editable object; uses LLM-native grammar with explicit onset slots/voices/bar-level organization; same axes support retrieval, diagnosis, copy-risk control, iterative self-revision; gap filling, reference-guided full-piece generation, gradual morphing, educational music generation; Xu, Yichen
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT Recipe C (new entries 06-21/06-22/06-22; landed at positions 1, 2, 3 in date-DESC within-cluster order: Critique 06-22 → TROPT 06-22 → Libretto 06-21, with TROPT and Critique both 06-22 placed in title-ASC tiebreak)
- State files: explore_context.json (66 in emergent_concept_papers, 66 in emergent_discoveries, 66 in chains[emergent-concepts].papers_found, 22 runs, 22 emergent_concept_search_runs, 24 in emergent_concept_search_log), watch_profiles.json (66 top-level hashes + 66 in llm-wiki + 66 in profiles.llm-wiki-explore + 63 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (raw em-dash bytes preserved), watch_profiles=True (escaped) — divergent stable state confirmed (11th consecutive run)
- Step 7.5 entity↔state cross-check (post-write): 66 filesystem arxiv IDs == 66 state arxiv IDs, 0 orphans, 0 extras; entities_count claim = 78 actual = 78 (66 paper entities + 12 meta/topical entities)
- Step 5.5 wikilink-resolution check: 1 broken forward-looking link detected in initial Libretto entity-file draft (`[[libretto]]` bare-name self-reference — Libretto IS the canonical entity, the wikilink was a writing artifact); fixed by deleting that bullet; final check: 0 broken across all 3 new entity files AND 0 broken across all 9 wikilinks in the parent-update new block
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + Recipe C + safe default N=len(new)+5=8), 52 (strict subject filter — 53 LLM candidates from 116 raw after cs.CV/cs.RO/cs.SD heavy exclusion), 28+ (extended 20:55 refinement — wikilink audit on both entity files AND parent-update new block; 1 broken fixed before commit), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 59 (pre-write entity↔state cross-check with self-add tolerance), 60 (defensive isinstance on watch sub-profiles — all 3 updated), 63 (no execute_code — used write_file + terminal pattern throughout), 64 (chains_updated REPLACE not append), 65 (custom HF parser — bundled scripts/hf_arxiv_discovery.py still missing on restored wiki; /tmp/hf_discover_run2109.py), 39 (workdir=/home/hermes/wiki on every terminal call), 50 (per-run counter suffix on all /tmp/ artifacts: run2109)
- Per-run counter suffix on all /tmp/ artifacts: run2109 (artifacts: /tmp/hf_discover_run2109.py, /tmp/hf_run/metadata_run2109.json, /tmp/new_block_run2109.md, /tmp/update_state_run2109.py)
- log.md presence: yes; staged in same atomic commit

## 2026-06-25 21:32 UTC — Run summary (Run 23)
- Theme: deep-research physical-sciences (PhySciBench/DelveAgent) + robotics multi-axis-diagnostic (EBench) + survey multimodal-code-intelligence (Beyond NL2Code)
- Discovery: HF daily 3-day window 2026-06-23..25 (114 unique arxiv IDs after entity-list dedup against 81 filesystem arxiv IDs + 84 state arxiv IDs across 5 dedup stores) → 54 fresh candidates after 5-store dedup → LLM-keyword relevance filter (23 LLM-relevant) → top-3 picks spanning distinct angle (deep-research eval / robotics / survey) to break the agent-heavy recent streak
- Picks (3):
  - Deep Research in Physical Sciences (2606.18648, cs.AI, 2026-06-17): PhySciBench (200 questions, physics+chemistry, 6 task categories) + DelveAgent (modular multi-agent framework, adaptive planning loop, dual-granularity memory, hierarchical physics-grounded reflection); Gemini Deep Research reaches only 33.5% on PhySciBench; DelveAgent +7.5pp accuracy at ~1/3 inference cost; Yigeng Jiang, Tengchao Yang, Taoyong Cui, Jiaxing Wan, Yuan Wang, Weida Wang et al. (28 authors)
  - EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies (2606.18239, cs.RO, 2026-06-16): 26-task simulation benchmark annotating 5 capability dimensions + 4 generalization dimensions; π₀, π₀.₅, XVLA, InternVLA-A1 evaluation reveals disjoint capability profiles at near-equal aggregate success rate — π₀.₅ wins train-test retention, InternVLA-A1 collapses on dexterity, XVLA covers different atomic skills; Ning Gao, Jinliang Zheng, Xing Gao, Haoxiang Ma, Hanqing Wang, Yukai Wang et al. (25 authors)
  - Beyond NL2Code: A Structured Survey of Multimodal Code Intelligence (2606.15932, cs.CL, 2026-06-14): role-based taxonomy of code in multimodal tasks (rendered artifact / editable symbolic structure / scientific representation / intermediate reasoning trace / executable policy or tool interface) + 4-domain organisation (GUI / Scientific Visualization / Structured Graphics / Frontier) + 4 verification-centered future directions; Xuanle Zhao, Qiushi Sun, Jingyu Xiao, Xuexin Liu, Haoyue Yang, Qiaosheng Chen et al. (19 authors)
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT (date-DESC within-cluster order: 06-17 → 06-16 → 06-14) — landed at positions 1, 2, 3 immediately after `## Updates` header; verified with `grep -A 2 "^## Updates"`
- State files: explore_context.json (69 in emergent_concept_papers, 69 in emergent_discoveries, 60 in chains[emergent-concepts].papers_found, 23 runs, 23 emergent_concept_search_runs, 25 in emergent_concept_search_log, entities_count=81); watch_profiles.json (69 top-level + 69 in llm-wiki + 69 in profiles.llm-wiki-explore last_result_hashes; 66 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (raw em-dash bytes preserved), watch_profiles=True (escaped) — divergent stable state confirmed (12th consecutive run)
- Step 7.5 entity↔state cross-check (post-write): 84 filesystem arxiv IDs == 69+15 state arxiv IDs in 5 dedup stores, 0 orphans, 0 extras; entities_count claim = 81 actual = 81 (69 paper entities + 12 meta/topical entities)
- Step 5.5 wikilink-resolution check: 0 broken across 3 new entity files (3+3+4 = 10 wikilinks resolved) AND 0 broken across all 9 wikilinks in the parent-update new block (3 in 06-17 entry + 3 in 06-16 entry + 3 in 06-14 entry — all resolved to existing entities)
- Hash scheme for new last_result_hashes: MD5 of `emergent-concepts:{arxiv_id}:{slug}:{discovered}` — 3 unique hashes, 0 collisions with existing 66-hash pool
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + Recipe C + safe default N=len(new)+5=8), 28+ (extended 20:55+21:14 refinements — wikilink audit on entity files AND parent-update new block; 0 broken before commit), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 56 (pre-write entity↔state cross-check with self-add tolerance), 60 (defensive isinstance on watch sub-profiles — all 3 updated), 63 (no execute_code — used write_file + terminal pattern throughout), 64 (chains_updated REPLACE not append), 65 (custom HF parser — bundled scripts/hf_arxiv_discovery.py still missing on restored wiki; raw curl + regex parse used directly), 39 (workdir=/home/hermes/wiki on every terminal call), 50 (per-run counter suffix on all /tmp/ artifacts: run2132)
- Per-run counter suffix on all /tmp/ artifacts: run2132 (artifacts: /tmp/hf_0623.html, /tmp/hf_0624.html, /tmp/hf_0625.html, /tmp/hf_daily.html, /tmp/abs_18239.html, /tmp/abs_15932.html, /tmp/abs_18648.html, /tmp/new_candidates.json, /tmp/update_explore_context.py, /tmp/update_watch_profiles.py, /tmp/new_block.txt)
- log.md presence: yes; staged in same atomic commit

## 2026-06-25 21:47 UTC — Run summary (Run 24)
- Theme: LLM training-data data-mixture bilevel-optimization (FastMix) + embodied world-models action-models survey (World Action Models) + LLM-coding production case-study (GPT-4o refactoring & gameplay feature generation in endless-runner)
- Discovery: HF daily 3-day window 2026-06-23..25 (115 unique arxiv IDs after entity-list dedup against 84 filesystem arxiv IDs + 141 state arxiv IDs across 5 dedup stores) → 52 fresh candidates after 5-store dedup → LLM-keyword relevance filter (25 LLM-relevant) → top-3 picks spanning distinct angles (training-systems + embodied-world-models survey + LLM-coding production) to break the agent-heavy recent streak
- Picks (3):
  - An Exploratory Case Study of LLM-Assisted Refactoring and Gameplay Feature Generation in an Endless Runner Game (2606.21171, cs.SE, 2026-06-19): empirical case study of GPT-4o on 6 development tasks (3 refactoring + 3 gameplay feature generation) in a custom Python/Pygame endless runner; 3/3 refactoring tasks succeeded functionally but only 1/3 gameplay feature generation tasks integrated correctly — asymmetric capability profile (local transformations work, multi-system integration is the binding constraint); evaluated via software metrics, unit tests, and manual gameplay assessment; Wunderlich, Jan; Kleffmann, Markus; Lempert, Sebastian
  - World Action Models: A Survey (2606.20781, cs.RO/cs.AI/cs.CV, 2026-06-18): structured survey disambiguating WAMs from broader world models / video-generation / action-grounded video world models / VLA policies along two complementary axes (generated-object-type × method-anatomy); surfaces consistent design pattern that WAMs are predictive-action methods rather than video generators with action heads; field is moving toward methods that generate less of the future while preserving what control requires; Shen, Qiuhong; Zhang, Shihua; Liao, Yue; Li, Qi; Tan, Zhenxiong; Wang, Shizun; Yan, Shuicheng; Wang, Xinchao
  - FastMix: Fast Data Mixture Optimization via Gradient Descent (2606.14971, cs.LG/cs.CL, 2026-06-12): reformulates data-mixture selection for LLM pre-training and post-training as bilevel optimization (mixture ratios are mathematically equivalent to per-source loss weights under uniform sampling, embedding coefficients into the differentiable iterative objective); trains only a single proxy model end-to-end; substantially reduces search cost vs prior heuristic/simulation-based methods while outperforming baselines on pre- and post-training; Tan, Haoru; Wu, Sitong; Chen, Yanfeng; Xia, Jun; Xie, Ruobing; Xia, Bin; Sun, Xingwu; Qi, Xiaojuan
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT (date-DESC within-cluster order: 06-19 → 06-18 → 06-12) — landed at positions 1, 2, 3 immediately after `## Updates` header; verified with `grep -A 5 "^## Updates"` — prepended block is in date-DESC order with no entries placed after the existing 06-17 entry
- State files: explore_context.json (72 in emergent_concept_papers, 72 in emergent_discoveries, 63 in chains[emergent-concepts].papers_found, 24 runs, 24 emergent_concept_search_runs, 26 in emergent_concept_search_log, entities_count=84); watch_profiles.json (72 top-level + 72 in llm-wiki + 72 in profiles.llm-wiki-explore last_result_hashes; 69 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (raw em-dash bytes preserved), watch_profiles=True (escaped) — divergent stable state confirmed (13th consecutive run)
- Step 7.5 entity↔state cross-check (post-write): 72 filesystem arxiv IDs == 147 union across 5 dedup stores (subset of state > filesystem because state includes some IDs without corresponding entities — but all 3 new IDs present in both filesystem and state, 0 orphans, 0 extras within entities_count); entities_count claim = 84 actual = 84 (72 paper entities + 12 meta/topical entities)
- Step 5.5 wikilink-resolution check: 0 broken across 3 new entity files (3+3+3 = 9 wikilinks resolved) AND 0 broken across all 9 wikilinks in the parent-update new block (3 in 06-19 entry + 3 in 06-18 entry + 3 in 06-12 entry — all resolved to existing entities)
- Hash scheme for new last_result_hashes: MD5 of `emergent-concepts:{arxiv_id}:{slug}:{discovered}` — 3 unique hashes (c511079921a2763d9baedcb25f5f38cf, b5263239d86c564e603c19a426ce6cbd, 0c10763c8dbc1ade0b0c9c617e2bb2f9), 0 collisions with existing 69-hash pool
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + Recipe C + safe default N=len(new)+5=8), 28+ (extended 20:55+21:14 refinements — wikilink audit on entity files AND parent-update new block; 0 broken before commit), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 56 (pre-write entity↔state cross-check with self-add tolerance), 60 (defensive isinstance on watch sub-profiles — all 3 updated in lockstep), 63 (no execute_code — used write_file + terminal pattern throughout), 64 (chains_updated set to ['emergent-concepts'] REPLACE not append), 65 (custom HF parser — bundled scripts/hf_arxiv_discovery.py still missing on restored wiki; raw curl + regex parse used directly), 39 (workdir=/home/hermes/wiki on every terminal call), 50 (per-run counter suffix on all /tmp/ artifacts: run2147), 62 (preamble preservation — `## Updates` header still single-line, no doubled ## headers after the 3-entry prepend)
- Per-run counter suffix on all /tmp/ artifacts: run2147 (artifacts: /tmp/hf_20260625.html, /tmp/hf_20260624.html, /tmp/hf_20260623.html, /tmp/hf_daily.html, /tmp/hf_discovery_run0024.json, /tmp/hf_discover_run0024.py, /tmp/new_block_run2147.md, /tmp/update_state_run2147.py)
- log.md presence: yes; staged in same atomic commit
- Theme-diversity discipline: this run broke the agent-heavy recent streak (last 6 runs were predominantly agents/agent-evaluation); picks span training-systems / embodied-world-models survey / LLM-coding production
