---
title: 'ACARE: Agent-Context-Aware Reranker for Iterative Search'
title_zh: ACARE：面向迭代搜索的智能体上下文感知重排器
authors:
- Sahel Sharifymoghaddam
- Yauhen Babakhin
- Reza Esfandiarpoor
- Oliver Holworthy
- Jimmy Lin
- Bo Liu
affiliations:
- University of Waterloo
- NVIDIA
arxiv_id: '2610.35840'
url: https://arxiv.org/abs/2610.35840
pdf_url: https://arxiv.org/pdf/2610.35840
published: '2026-10-26'
collected: '2026-10-27'
category: Agent
direction: Agent 搜索 · 上下文感知重排
tags:
- Agentic Search
- Context-Aware Reranker
- LLM Reranker
- Iterative Retrieval
- Search Efficiency
one_liner: 用原始问题与推理轨迹解释子查询的 4B 点式 LLM 重排器，提升 agentic search 检索质量并减少搜索次数
practical_value: '- **会话/Agent 搜索中的子查询不能孤立评分**：电商搜索、对话式推荐里用户当前 query 往往省略背景，reranker
  应把会话级原始意图和已有推理轨迹作为上下文一起输入，而不是只对当前 query 打分。ACARe 的 M0–M3 模式设计可直接复用到客服机器人、多轮搜索、Agent
  选品等场景。

  - **单 checkpoint 兼容多 context 模式，工程落地友好**：通过独立 context dropout（原问题与推理轨迹各以 0.5 概率丢弃）训练，同一个
  reranker 支持有/无推理轨迹、有/无原始问题的部署。这对 proprietary agent 不暴露 CoT、或线上隐私限制的场景很有价值，不需要为不同上下文可用性维护多个模型。

  - **点式评分避免 listwise 滑窗，适合长候选列表**：用 LLM 对 query–doc 对独立输出 yes/no logit difference，推理时
  sigmoid 保序，无需 sequential sliding window，可并行处理大量候选。在电商搜索/推荐精排阶段，若候选量大且需低延迟，可以把类似轻量
  4B reranker 作为并行精排器。

  - **小 agent + 强 reranker 可以显著缩小与大模型的效果差距**：论文中小模型搭配 ACARe 后，分别缩小 51–74% 的 nDCG@10
  差距，远高于 base reranker 的 26–46%。这提醒业务上可以用低成本小 agent 加上高质量检索工具，用更低 API 成本逼近大模型效果。

  - **训练数据构造可借鉴**：用 oracle reranker 基于原问题+gold answer 对 agent 子查询的候选文档排序，取 top 正样本、bottom
  负样本，再以 final answer 是否与 gold answer 一致过滤轨迹。这种利用 agent trajectory 自动挖掘弱监督样本的方式可迁移到电商搜索的
  query 改写/召回/精排监督数据扩产。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
Agentic search 中，agent 生成的子查询（sub-query）常常是关键词式、省略了原始任务背景。传统 reranker 只对子查询评分，会导致文档虽然匹配当前子查询，却无助于回答用户原始问题。已有 context-aware 一阶段检索需要本地访问全量语料，而 reranker 只处理候选文档，更适合 API 搜索和黑盒检索场景。

## 方法关键点
- **模型与上下文**：ACARe 是一个 4B decoder-only LLM，从 Qwen3-Reranker-4B 微调而来。输入包含子查询、可选原始问题 Q、可选当前推理轨迹 τ，定义四种模式：M0（仅子查询）、M1（子查询+τ）、M2（子查询+Q）、M3（子查询+τ+Q）。
- **单 checkpoint 多模式**：训练时对 Q 和 τ 独立做 0.5 概率 dropout，使同一个模型兼容无推理/无原问题的部署场景，包括 proprietary agent 不暴露 CoT 的情况。
- **点式评分与训练**：对 query–document 对计算 yes/no 下一 token logit difference，sigmoid 得到相关性分数，支持独立并行评分长候选列表，无需 listwise 滑窗。训练采用 localized contrastive estimation（LCE），每组 1 正 + 7 负，temperature 0.5，序列 cap 5120 tokens。
- **训练数据扩展**：在 DR-Synth 基础上保留 Q 和 τ，用 Nemotron-3-Embed-8B 重新挖掘候选并新增 rollout；最终得到 16,601 个标注实例、54,838 个 distinct passages。

## 关键结果
- **One-shot retrieval**：在 BCP、BRIGHT、TRQA 及四个 first-stage retrievers 上，ACARe 数据集平均 nDCG@10 比无 reranking 提升 9.8–12.8 pp，比 Qwen3-Reranker-4B 提升 1.7–4.5 pp（M0）。
- **Agentic retrieval**：跨五个 agent families，ACARe 平均 nDCG@10/Recall@10 比 base reranker 提升 0.9–2.0 pp，同时搜索次数减少 0.3–1.0 次/查询（2.0–10.0%）；在 TRQA 上，base reranker 对 4/5 agent 降低了 context-aware retriever 的 nDCG@10，而 ACARe 对全部 5 个 agent 均提升。
- **端到端 answer generation**：在 Piika + BrowseComp-Plus CM 上，ACARe 使 accuracy 提升 8.2–9.1 pp，且减少搜索次数；BCP context control 显示，仅给未微调的 base reranker 加入 M2/M3 上下文，accuracy 从 48.2% 升至 54.8%/55.9%，ACARe M3 达 57.6%，说明上下文公式贡献主要增益。
- **小 agent 受益更大**：搭配 ACARe 后，GPT-5.6 Luna、Gemini 3.5 Flash-Lite、Claude Haiku 4.5 分别缩小与大 agent 的 nDCG@10 差距达 73%、74%、51%，远高于 base reranker 的 46%、46%、26%。

最值得记住的一句话：**agent 搜索中，当前子查询往往丢失全局意图，把原始问题和已有推理轨迹作为上下文交给轻量 reranker，能以极低成本同时提升检索质量和搜索效率。**
