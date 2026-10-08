---
title: 'Agentic AutoRAG: RAG Pipeline Optimization through Reasoning-Driven Agents'
title_zh: Agentic AutoRAG：推理驱动 Agent 优化 RAG 流水线
authors:
- Lasse B. Strand
- Robert Jakob
- Kevin O'Sullivan
- Markus Kreft
affiliations:
- ETH Zurich
arxiv_id: '2610.08452'
url: https://arxiv.org/abs/2610.08452
pdf_url: https://arxiv.org/pdf/2610.08452
published: '2026-10-06'
collected: '2026-10-08'
category: RAG
direction: Agent 驱动 RAG 超参优化
tags:
- RAG
- Hyperparameter Optimization
- LLM Agent
- Failure Attribution
- Pareto Optimization
- Cost-aware Search
one_liner: 用 LLM agent 诊断检索/生成失败并借助模型排行榜与价格先验做 RAG 超参 Pareto 优化，样本和成本效率显著提升
practical_value: '- **失败归因驱动调参**：搜索/推荐系统中召回和排序通常是两级漏斗，可以从线上 bad case 中区分“召回没召到”和“排序没排好”，把失败归因作为信号指导下一轮配置调整，比只看整体指标更能定位问题。

  - **注入先验知识库跳过劣质配置**：将模型能力排名和成本信息预先编码进搜索过程（类似模型的 leaderboard 和定价表），可以大幅减少无效试错，尤其适合成本敏感的在线服务，快速找到性价比高的配置。

  - **构建可区分性评测集**：用 probe-based selection 筛选出对不同配置敏感的评测样本，避免在大量无区分度样本上浪费评估预算；在推荐/搜索的离线评估中也可以借鉴，聚焦于能区分策略优劣的
  query 或 item 集合。

  - **输出 Pareto 前沿而非单点**：多目标优化（准确率/成本）返回 Pareto 前沿，让业务根据预算和效果要求选择配置，而不是只给一个固定最优解。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
RAG 流水线配置是一个昂贵的黑盒超参优化问题，涉及 chunking、embedding、检索深度、reranker、query expansion 和生成器等多个耦合维度。现有优化器（贪心、贝叶斯等）只把每次试验压缩为一个总分，不分析配置为何表现好或坏，浪费了检索到的 chunk 本身包含的失败证据。

## 方法关键点
- **诊断-提议循环**：每次试验后，Diagnoser 读取每个问题的失败证据，将失败归因于检索（gold span 未出现在 retrieved chunks）或生成（retrieved 但答案仍错），压缩为简短诊断；Proposer 基于该诊断选择下一配置。
- **知识库基础的成本感知**：Proposer 预先查询公开模型排行榜（Artificial Analysis、MTEB 等）和 per-token 定价（LiteLLM），在花费试验之前排除质量-成本被支配的候选，直接跳到便宜但能力足够的生成器。
- **语料库生成的冰冻考试**：Composer 从目标语料生成多跳开放问题，经 validation 和 sufficiency oracle 过滤，并用 probe-based selection 只保留能够区分不同配置的问题，冻结后作为所有试验的统一优化目标。
- **多目标 Pareto 搜索**：同时优化 answer accuracy 和 mean API cost per query，输出非支配配置集合和推荐配置。

## 关键实验与结果
- **准确性实验**（HotpotQA、MuSiQue、MultiHop-RAG）：Agentic AutoRAG 在三个基准上 LLM-judge accuracy 均高于所有 baseline（HotpotQA 0.825、MuSiQue 0.330、MultiHop-RAG 0.790）；前 10 次试验的 best config 已匹配或超过统计 baseline 全 30 次试验的 judge accuracy（如 HotpotQA 0.817 vs 0.786）。
- **Pareto 实验**（UniDoc 医疗语料）：成本感知模式下 agent 达到中位数 exam accuracy 77%，成本 $0.000741/query；最强 baseline（warm-started MO-TPE）为 71.5% @ $0.001284，agent 成本仅为其 57.7%；若匹配 71.5% 准确率，agent 只需 $0.000288，即 baseline 成本的 22.4%。
- **消融**：去掉知识库和诊断的纯 LLM optimizer 接近全 agent，但全 agent 在 held-out 指标上仍有提升，说明诊断和先验知识带来额外收益。

## 最值得记住的一句话
把失败归因（检索 vs 生成）与 LLM 先验知识结合起来，可以大幅提高 RAG 超参数搜索的样本效率和成本效率，并直接输出成本-质量 Pareto 前沿。
