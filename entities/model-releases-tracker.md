# Model Releases Tracker

Comprehensive log of AI/LLM model releases, API launches, weight drops, and major benchmark/paper announcements. Updated every 30 minutes by the Model Release Tracker cron job.

## Scope
- **Major labs:** OpenAI, Anthropic, Google DeepMind, xAI, Meta AI, Mistral, Microsoft, Amazon (Nova)
- **Chinese/open:** DeepSeek, Alibaba (Qwen), Zhipu (GLM/ChatGLM), Moonshot (Kimi), Baidu (ERNIE), Tencent (Hunyuan), 01.AI (Yi)
- **Aggregators:** lmmarketcap.com, llm-stats.com, pricepertoken.com, dentro.de
- **HuggingFace trending:** daily papers + model releases
- **arXiv cs.CL:** new submissions

## Categories
- 🚨 WEIGHTS DROP — actual model weights uploaded (HF, GitHub, blog)
- 🚨 API LAUNCH — model available via API (new endpoint, GA, preview)
- 📄 BENCHMARK/PAPER — new paper claiming SOTA, arXiv submission
- 📣 OFFICIAL ANNOUNCEMENT — major blog post, product launch
- 🔓 OPEN SOURCE — fully open weights + training code

## Updates

- **2026-07-01** | [DeepSeek V4 Launches in Mid-July with Peak-Valley Pricing](https://www.kucoin.com/news/flash/deepseek-v4-launches-in-mid-july-with-peak-valley-pricing) | kw: deepseek-releases | score: 6
- **2026-07-01** | [DeepSeek to launch V4 in mid-July with new peak-time API pricing](https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/) | kw: deepseek-releases | score: 6
- **2026-07-01** | [DeepSeek V4 Official Release: Peak Pricing Guide](https://explainx.ai/blog/deepseek-v4-official-release-peak-pricing-mid-july-2026) | kw: deepseek-releases | score: 6
- **2026-07-01** | [DeepSeek V4 Official Launch + Peak/Off-Peak Pricing](https://www.reddit.com/r/DeepSeek/comments/1uio6yf/deepseek_v4_official_launch_peakoffpeak_pricing/) | kw: deepseek-releases | score: 6
- **2026-07-01** | [Is Google Delaying Gemini 3.5 Pro Launch to July for Further Testing?](https://www.androidpolice.com/google-gemini-3-5-pro-launch-delay-july-2026/) | kw: google-deepmind-releases | score: 6
- **2026-07-01** | [Google delays Gemini 3.5 Pro launch to July 2026](https://9to5google.com/2026/06/29/google-gemini-35-pro-launch-delay/) | kw: google-deepmind-releases | score: 6
- **2026-07-01** | [Kog Laneformer 2B: The Latency-First Model Behind Kog Inference Engine](https://blog.kog.ai/kog-laneformer-2b-the-latency-first-model-behind-kog-inference-engine/) | kw: kog-ai | score: 8
- **2026-07-01** | [Kog Labs](https://blog.kog.ai/) | kw: kog-ai | score: 8

## Auto-Discovered Profiles
*Profiles auto-added by discovery layer each cycle. Tracked from this cycle onwards.*

- **sakana-releases** — cycle 3 — Sakana AI Fugu model release Japanese lab
- **swiss-ai-apertus** — cycle 3 — swiss-ai/apertus Hugging Face open weights multilingual (c73 reword: HF slug anchor per c72 L1 + variant 17)
- **krea** — cycle 4 — Krea AI Krea 2 image generation model open weights
- **MiniMax** — cycle 9 — MiniMax AI MiniMax-M3 release new model multimodal MoE
- **inclusion-ai** — cycle 52 — inclusionAI Ring-1T Ling billion parameter Ant Group (c89 reword: specific model name anchors, c86 backlog applied 3 cycles late; replaces prior c83 "inclusionAI foundation model open weights")
- **deepreinforce-ai** — cycle 56 — DeepReinforce AI Ornith model release coding agent weights
- **liquid-ai** — cycle 59 — Liquid AI LFM2.5 family edge LLM open weights model release
- **kog-ai** — cycle 68 — kogai laneformer-2b-it model card release (c89 reword: HF model-name anchor, c86 backlog applied 3 cycles late; replaces prior c73 "kogai Laneformer huggingface open weights latency-first")
- **yuvion-llm** — cycle 99 — Yuvion LLM adversarial content safety model arXiv cs.CL Jun 2026 (auto-discovered via arXiv cs.CL new submission, new org not in known blocklist)
- **meituan-longcat** — cycle 106 — Meituan LongCat-2.0 open-weight MoE model announced Jun 30 2026 via x_search: 1.6T params, 1M context, trained on Huawei Ascend chips, open weights on HuggingFace
- **huawei** — cycle 107 — Huawei OpenPangu-2.0-Flash open weights MoE model released Jun 30 2026 via x_search: 92B total / 6B active, 512K context, Apache/Ascend stack, weights on HF
- **internscience** — cycle 109 — InternScience Agents-A1 35B MoE agentic model released Jun 30 2026 via x_search: arXiv:2606.30616, weights+code on HF/GitHub, trillion-parameter performance via horizon scaling
