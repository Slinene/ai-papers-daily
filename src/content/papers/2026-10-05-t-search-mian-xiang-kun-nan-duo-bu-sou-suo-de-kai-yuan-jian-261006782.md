---
title: 'T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search'
title_zh: T-Search：面向困难多步搜索的开源 Agentic 检索器与实验平台
authors:
- Olga Tsymboi
- Ramil Latypov
- Aleksandr Medvedev
- Danil Taranets
- Dmitrii Stoianov
- Nikita Gulyakov
- Gleb Alektorov
- Anatolii Potapov
affiliations:
- T-Tech
arxiv_id: '2610.06782'
url: https://arxiv.org/abs/2610.06782
pdf_url: https://arxiv.org/pdf/2610.06782
published: '2026-10-05'
collected: '2026-10-06'
category: RAG
direction: Agentic 多步搜索与检索器训练
tags:
- Agentic Retriever
- Multi-step Search
- Recall@10
- GSPO
- Synthetic Data
- Open-weight
one_liner: 开源权重 Agentic 检索器，以多轮短上下文搜索返回证据块，平均 Recall@10 达 56.0 并超越更大模型
practical_value: '- 检索与生成解耦：把 agentic retriever 独立成服务，只返回证据块而非最终答案，下游生成器可替换；在电商搜索/推荐中，可拆分为召回证据
  Agent + 答案/推荐生成模型，便于独立迭代与后端切换。

  - 短上下文轮次 + 显式记忆：每轮 32k token 上限，丢弃前一完整 transcript，只保留 saved chunks、round summary、coverage、next
  goal，避免 context rot 影响判断；适用于电商多轮会话/Agent 工具调用，防止长工具输出堆积。

  - 合成任务对抗过滤 + recall 奖励：训练数据通过整问检索、闭卷可解、支撑必要性等 shortcut 测试过滤，仅保留难任务；RL 以 chunk identifier
  的 Recall 作为奖励，无需 LLM judge，适合商品/内容证据召回目标，奖励直接对齐最终 Recall。

  - 后端可插拔与多 rollout 融合：模型只通过 search_corpus 工具访问文档，支持 dense/BM25/rerank 同 checkpoint
  切换；3 个 rollout 用 RRF 融合可提升召回（55.96→61.33），适合广告候选生成等高召回场景，代价是 3 倍推理。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
RAG 假设直接查询问题即可找到答案，但多跳问题常需发现未在问题中出现的实体；deep-research agents 以长轨迹、大模型、最终答案评判，慢且贵且把检索与生成混在一起。T-Search 将检索阶段独立出来，只返回证据块，下游生成可替换。

**方法关键点**
- 模型基于 Qwen3.6-35B-A3B，在 harness 中训练：三工具 search_corpus、save_and_advance、finalize_ranking；最多 5 轮，每轮 32k 上下文，75% 锁定；跨轮只携带显式保存的 chunks + summaries + coverage + next goal，丢弃完整 transcript。
- 合成数据工厂：在本地语料上按 taxonomy 生成多跳问题，用 NER/共现预选子图、事实改写避免词法泄漏；对抗验证含整问检索、闭卷可解、支撑必要性、agentic 难度，67k 候选保留约 40k。
- 训练两阶段：round-sliced SFT 从 GLM-5.1 teacher 轨迹选 11k rounds/语言，覆盖 retriever robustness；RL 用 GSPO，奖励为最终排序中 gold chunk 的 Recall，无 judge，无逐轮 shaping。英俄分别训练后用 DARE/SLERP 合并为双语模型。

**关键实验**
- 在 BrowseComp-Plus、SealQA-Seal-Hard、TRuST、SynthComp 等七个固定索引 benchmark 上，T-Search 单 rollout 平均 Recall@10 55.96，比 base 41.54 高 14.42；三 rollout RRF 融合达 61.33，在全部 benchmark 上最高，超过 GLM-5.1（53.96）、Kimi-K2.6（51.07）等更大模型。
- Latency 曲线：1 轮 T-Search 可达到 Qwen3.5-397B 5 轮类似召回，延迟仅 40%；3 轮接近 GLM-5.1 5 轮，延迟不足 1/3。
- Retriever robustness：默认 Qwen3-Embedding-8B 55.96，加 LLM reranker 达 62.87；BM25 在 TRuST/SynthComp 最佳但在 BrowseComp-Plus 最差。

**最值得记住的一句话**
把证据收集做成可替换后端的组件，用短上下文、显式记忆和 Recall 奖励训练 Agentic Retriever。
