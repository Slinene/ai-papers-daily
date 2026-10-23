---
title: Training Small Language Models for Transferable Tool Selection
title_zh: 训练小语言模型实现可迁移的工具选择
authors:
- Zhaoyi Zhou
- Akshayaa Magesh
- Jeongyeol Kwon
- Artem Kuriksha
- Daniel Jiang
- Andrea Zanette
- Ayush Jain
affiliations:
- Meta
- Carnegie Mellon University
arxiv_id: '2610.31483'
url: https://arxiv.org/abs/2610.31483
pdf_url: https://arxiv.org/pdf/2610.31483
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent工具选择与跨域迁移
tags:
- Tool Selection
- RL
- Small LLM
- Cross-domain Transfer
- GRPO
- Retriever-agnostic
one_liner: 用SFT+RL训练Qwen3小模型，在Plan-Retrieve-Select流程中超过Llama-4-Maverick并零样本迁移工具域
practical_value: '- 多意图查询先 Plan 再按子意图 Retrieve：将用户请求拆成独立 substep 后分别召回，可缓解电商搜索中“订酒店+订机票”类多意图相互干扰；Select
  只从 top-K 候选中选一个，上下文可控，适合小模型部署。

  - 训练小模型做 selection policy 时，可复用「SFT 冷启动 + GRPO 强化」：用大模型生成 teacher trajectories；Plan
  reward 用 retriever 命中 gold 的 precision/recall/F1，Select reward 用 exact match，无需额外人工标注。生产上可训练
  1-8B 模型替代大模型 API 做工具/物料筛选。

  - 把 retriever 抽象成接口：训练用 BM25，推理可换 COLT 等 dense retriever，无需重训；模型继承更强召回。电商/Agent
  系统里可把召回层与精排/选择策略解耦，便于替换底层索引。

  - 注意 gold label 噪声过滤：只保留仅凭 query 就能识别出工具/商品的样本，否则会教模型选无关项；同时跨域多步任务 Plan 可能失效，必要时退回扁平
  Search-R1 式推理。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
LLM agent 面对超大规模工具库，每次把所有 tool descriptions 放进 context 不可行；单一 retriever 只做相关性排序，不懂多步指令真正需要哪些工具。已有方案依赖 Claude/ChatGPT 等闭源大模型驱动 retriever。本文探索用小模型通过 RL 训练完成 Plan-Retrieve-Select 工具选择，并跨工具域和 retriever 迁移。

## 方法关键点
- 工作流：Plan 把用户指令拆成独立 substeps；每个 substep 用 retriever (BM25, τ=3, top-K=15) 召回候选；Select 从候选集中选一个工具。同一小模型 Qwen3 负责 Plan 和 Select，每次调用状态有限，上下文受限。
- 训练：先用 Llama-4-Maverick 生成 SFT 数据，包括 gold tool 过滤、plan 分解、reasoning 生成；再用 GRPO 做 RL，Plan reward 基于子步骤经 retriever 命中 gold 的 precision/recall/F1，Select reward 为 exact match；Plan 和 Select 解耦训练。
- 迁移设计：训练只用 BM25，推理可替换 COLT dense retriever；模型学的是指令分解和描述匹配，不绑定语料。

## 关键结果
- ToolBench G3 上，Qwen3-8B SFT+RL 达 41.5%，超过 Llama-4-Maverick 最优 prompt 流程 Search-R1 的 30.6%；1.7B/4B 分别 37.6%/40.3%。
- 零样本跨域：G2 25.8% vs Llama Search-R1 20.8%；Gorilla 29.9% vs 15.9%；CRAFT 69.0% vs 41.0%。TaskBench 上 Search-R1 80.6% 超过本文 72.8%，说明多步跨域 Plan 仍是弱点。
- 换 COLT retriever 后各尺度成功率进一步提升，无需重训。
- 消融：K=15 为默认候选集；SFT 冷启动对 RL 很重要（仅 RL 35.7% vs SFT+RL 41.5%）。

## 最值得记住的一句话
用便宜的 BM25 + 小模型 RL 训练的 selection policy，可以迁移到更强 retriever 和不同 tool domains；但 Plan 能力跨域有限。
