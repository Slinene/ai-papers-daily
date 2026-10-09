---
title: 'Project Greenhouse: Progress Toward Fully Open and Sovereign Agentic Search'
title_zh: Project Greenhouse：构建完全开放与主权的智能体搜索重排模型
authors:
- Jimmy Lin
- Sahel Sharifymoghaddam
- Lingwei Gu
- Nour Jedidi
affiliations:
- University of Waterloo
arxiv_id: '2610.11922'
url: https://arxiv.org/abs/2610.11922
pdf_url: https://arxiv.org/pdf/2610.11922
published: '2026-10-08'
collected: '2026-10-09'
category: RecSys
direction: 开放主权 agentic search 重排
tags:
- reranker
- pointwise ranking
- decoder-only
- open-source
- sovereign AI
- agentic search
one_liner: 用从零预训练+SFT 的 3B 点式重排模型，以少量 GPU 实现不依赖第三方权重的开放主权检索重排
practical_value: '- **可复用训练配方**：3B decoder-only 模型从通用语料（ClimbMix）从零预训练，再用公开相关性标注（RLHN-250K）做
  LCE 点式微调，即可逼近/超过同量级 fine-tuned listwise/pointwise 重排器；电商/广告团队可照搬到商品/广告候选重排，避免依赖
  Qwen/Gemma 等第三方权重带来的 license 与合规风险。

  - **工程集成简单**：点式重排把 query-doc 对映射为标量分数，候选独立打分、排序；相比 listwise 更适合局部候选集（如召回 top100）和线上并行，3B
  可单 GPU 部署，适合 agent 搜索循环中对抓取/召回结果做优先级筛选。

  - **模型 soup 提升稳定性**：同一 SFT recipe 多次训练后平均权重作为最终 checkpoint，降低单次波动；在业务迭代中可用少量多次微调再平均来提升线上指标稳定性。

  - **重排器可当 relevance judge/奖励信号**：其标定后的分数可作为 RAG/agent 搜索中的相关性校验、强化学习 reward 或 rollout
  verifier，与 LLM 生成/重排组件解耦。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：开放权重模型虽好用，但 pre-training corpus 与 recipe 不透明，带来合规、版权、数据偏见和供应链风险。Project Greenhouse 探索仅用少量 GPU 与公开数据，从零训练完全开放、自主可控的 agentic search 模型。首个里程碑选点式重排器，作为后续 query 改写、listwise rerank、搜索轨迹控制等能力的基础。

**方法关键点**：
- 训练链路建模为有向属性超图，顶点=数据/权重，超边=训练/微调 recipe；完全开放主权定义为所有上游顶点与超边公开且无专有依赖。
- 两步训练：在 ClimbMix 语料上从零 pre-train 3B decoder-only 因果语言模型；再用 RLHN-250K 公开相关性标注做 SFT，采用 localized contrastive estimation（LCE）进行点式重排。
- 最终 Gaggle base reranker 由同 recipe 四次微调结果做 model soup 平均得到；文档/query 分别截断 512/128 tokens，BM25 top100 作为候选。

**关键结果数字**：
在 TREC DL19–23 上 Gaggle 3B 平均 nDCG@10=0.641，超过所有 fine-tuned pointwise/listwise 对照（RankZephyr 0.621、Qwen3-Reranker 8B 0.605、MonoT5 0.604），仅低于 GPT-6.1 Sol 0.653；BEIR 平均 0.547，与 Gemma-4 0.548 相当。所有 SFT 可在单个 GPU 完成，pre-train 仅用单机 8×H100。

**最值得记住**：不依赖第三方 open-weight backbone，用公开语料从零预训练 + 公开标注微调，就能训练出与同量级开源重排模型竞争的点式重排器，证明自主可控路线可行。
