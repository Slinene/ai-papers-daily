---
title: 'SearchHorizonBench: A Benchmark for Search Value in AI Agents'
title_zh: SearchHorizonBench：AI Agent 搜索价值评估基准
authors:
- Jingjie Ning
- Xueqi Li
- Yibo Kong
affiliations:
- Carnegie Mellon University
arxiv_id: '2610.34714'
url: https://arxiv.org/abs/2610.34714
pdf_url: https://arxiv.org/pdf/2610.34714
published: '2026-10-25'
collected: '2026-10-29'
category: Eval
direction: Agent 搜索价值评估基准
tags:
- search agents
- benchmark
- decision utility
- search gain
- calibration
- LLM agents
one_liner: 通过配对延续与重复执行构建搜索价值评估基准，分离搜索增益与生成噪声
practical_value: '- 将搜索/工具调用决策显式建模为成本-收益问题，用历史执行数据校准“搜索增益”，可迁移到电商导购 Agent 的检索决策：何时检索商品库、用户画像、知识库，何时直接生成回答。

  - 配对延续（paired continuations）与重复执行能分离期望增益与生成噪声，可用于离线评测或线上 AB 实验，更干净地评估 RAG、工具调用、召回策略的增量价值。

  - 关键结论：只预测成功率不够，必须直接预测增益。搜索增益方差达 21.4 个百分点，而历史估计器只能解释不到 2%，说明在推荐/搜索系统中评估“召回/重排/生成”环节时，应直接建模增量收益，而非绝对成功率。

  - 开源冻结 split 与评分工具可作为训练 value-aware agent 策略的基础，例如在多轮购物助手中决定是否调用价格查询、库存查询、评论总结等工具，优化用户效用与
  token 成本。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：AI Agent 需要判断何时搜索值得成本；仅预测答题成功率不足以支撑搜索决策，必须估计搜索带来的额外收益。

方法：构建 SearchHorizonBench，通过配对延续（paired continuations）与重复执行分离期望搜索增益与生成噪声，从执行经验中学习搜索价值，并将预测质量与决策效用连接。资源包含 45,632 次执行、3,168 个问题，划分冻结 split、提供强基线与评分工具。

关键结果：在 1,632 个留出问题上，历史校准将 Brier 误差降低 16.2%，改进集中在成功级信息；搜索增益标准差为 21.4 个百分点，但测试的历史估计器只能解释点估计方差不到 2%；在参考 token 价格下，自由选择观测相较最优恒定动作带来 2.49 点效用机会，主要来自增益信息。
