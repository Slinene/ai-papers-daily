---
title: 'ProRetrieval: Learning to Orchestrate Hybrid Search via Executable Program
  Synthesis'
title_zh: ProRetrieval：通过可执行程序合成学习编排混合检索
authors:
- Chengsong You
- Zhen Sun
- Yunhai Hu
- Junwei Zhou
- Xiaoyu Cao
- Binyu Li
- Ziyan Zhao
- Weiyao Wang
- Liren Lu
- Zhijie Ye
affiliations:
- East China Normal University
- New York University
- Matter Innovation Inc.
- ThinRedLine
- Shandong University of Science and Technology
arxiv_id: '2608.27017'
url: https://arxiv.org/abs/2608.27017
pdf_url: https://arxiv.org/pdf/2608.27017
published: '2026-08-27'
collected: '2026-08-28'
category: QueryRec
direction: LLM检索编排 · 可执行程序合成
tags:
- Retrieval Orchestration
- DSL
- RL
- Hybrid Search
- SQL
- GRPO-DAPO
one_liner: 将LLM训练为检索编排器，生成SQL+向量原语的DSL程序，4B模型在电商/邮件Hit@1超越GPT-5.5
practical_value: '- **用 SQL 作为混合检索的融合骨架**：让模型输出 `sql` + `retrieval_list`，向量检索 top-K
  候选集通过 `id IN <text_0>/<image_0>` 占位符注入 SQL，天然支持 AND/OR/NOT 和嵌套。电商搜索/广告召回里，可以用同一套
  DSL 统一编排品牌、价格、类目等结构化过滤与文本/图片向量召回，替代硬编码 RRF 或只支持 AND 的 self-query retriever。

  - **小模型 + RL 比 few-shot 大模型更划算**：Qwen3-4B 经 SFT + GRPO/DAPO 训练后在 DSL 检索编排上超过 GPT-5.5，执行成功
  >99%，单 query 推理约 50ms。适合需要低延迟、低成本但复杂查询解析的线上检索服务，4B 部署在单张 RTX 4090 即可。

  - **复杂动作空间下 SFT 存在多任务干扰，RL 是解锁多模态的关键**：全 DSL SFT 反而不如只保留 SQL+text 的受限 DSL，但 RL 能让图片检索
  Hit@1 从 0.323 提升到 0.716。如果业务只做结构化+文本检索，先上受限 DSL 的 SFT 即可；要加入图片召回，建议走 SFT→RL 路径。

  - **分层奖励与 DAPO 稳定性值得复用**：format→execution→result→length 的奖励设计天然形成隐式优先级，可以让小模型快速学会可执行程序格式；DAPO
  非对称裁剪比 GRPO 更稳定，生产部署优先选 DAPO。工程上注意 SQL 转义问题（如品牌名含撇号）并加执行失败 fallback。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
真实检索查询同时包含结构化过滤、文本/图片语义意图和任意布尔逻辑（AND/OR/NOT、嵌套）。现有方案两边不讨好：RRF 等融合管道只支持加权析取，self-querying retriever 只支持简单 key-value 合取，Search-R1、DeepRetrieval 等 RL 检索器只能对单一后端生成 query，无法编排异构检索路径。因此需要把 LLM 的角色从 query generator 升级为 retrieval orchestrator，动作空间是可执行程序。

## 方法关键点
- **Hybrid DSL**：程序为 JSON，含 `sql` 和 `retrieval_list`。`sql` 是标准 SQL，`retrieval_list` 是文本/图片向量检索原语；每个原语返回 top-K=20 候选集，通过 `id IN <text_k>/<image_k>` 占位符注入 SQL，最终由 SQL 引擎完成布尔融合。该设计将向量检索与关系融合解耦，可独立优化。
- **自动构建基准**：基于 Amazon ESCI+Reviews 与 Enron 邮件，按复杂度 L1–L3 采样 1–5 个叶子条件，生成结构化、文本、图片条件及正/负叶，编译为 gold DSL 并执行得到 ground-truth，再用 GPT-4o 将 DSL 改写为自然语言查询。每个域 20k 训练 / 3k 测试。
- **两阶段训练**：先在 gold DSL 上 SFT 预热，再用 GRPO/DAPO 做 RL。奖励为四层：格式、执行、结果 Hit@1、长度；分层依赖提供隐式优先级。DAPO 采用非对称裁剪，对长 DSL 输出更稳定。

## 关键结果
- 电商：4B GRPO Hit@1 0.809，DAPO 0.808，超过 GPT-5.5 的 0.693、RankGPT 0.768、BGE-Reranker 0.618、DeepRetrieval 0.625；邮件：DAPO 0.909，超过 GPT-5.5 0.855。
- 动作空间消融：SFT 全 DSL 0.680 低于 SQL+text 0.752，但 RL 全 DSL 0.809 超过所有受限变体；图片查询 SFT 0.323 → RL 0.716，提升 +39.3pp。
- OOD 人工查询 IID-to-OOD 差距≤3pp，执行成功>99%，说明不是过拟合。

最值得记住的一句话：把 LLM 的动作空间从“生成 query”扩成“生成 SQL+向量原语的检索程序”，用 SQL 的逻辑完备性统一异构召回，小模型也能超过大模型。
