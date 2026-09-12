---
title: 'Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and
  Evaluation'
title_zh: 基准雷达：AI 基准与评估的活数据库和搜索引擎
authors:
- Koutian Wu
- Junjie Zhou
- Ergan Shang
- Jiayu Wang
- Pengqian Han
- Junkai Wang
- Wanghan Xu
affiliations:
- Earth-Space-AI
- Tacite AI
- Hangzhou Dianzi University
- Carnegie Mellon University
- Xi’an Jiaotong University
arxiv_id: '2609.11115'
url: https://arxiv.org/abs/2609.11115
pdf_url: https://arxiv.org/pdf/2609.11115
published: '2026-09-10'
collected: '2026-09-12'
category: Eval
direction: AI 评测基准检索与发现系统
tags:
- AI benchmarks
- LLM evaluation
- search engine
- benchmark database
- evidence tracking
one_liner: 构建持续更新的 AI 评测基准数据库与搜索引擎，支持基准发现、证据溯源和分数历史检索
practical_value: '- 借鉴其“living catalog + daily feeds”模式，建立内部评测基准库，自动追踪业界新 benchmark
  和 SOTA 分数，避免手动搜集，尤其适合跟踪 LLM-based 推荐/Agent 工具评测。

  - 在内部模型对比时，不只盯 leaderboard 总分；参照其保留 source identity 和 score history 的做法，溯源每个分数的模型版本、prompt、数据集版本，避免评估不可比或作弊。

  - 用 Pareto frontier 和 adoption 趋势做选型：在采用新评测基准前，查看其被引用/使用频率与分数分布，避开 saturated 或低采纳的
  benchmark，减少无效评估。

  - 如果搭建 Agent 评测体系，可参考其多源发现（paper、repo、dataset、release）的设计，将评测集、代码和论文绑定管理，提高可复现性。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：LLM/AI 评测基准碎片化，研究者难以快速定位相关评估、数据集、代码及分数背景。现有 catalogs 静态、分散，缺乏持续更新与证据溯源。

方法关键点：构建持续更新的数据库与搜索引擎 Benchmark Radar，覆盖 LLM 评估、Agent/工具使用、编码、推理、安全等领域。每日从 37 个来源发现论文、仓库、数据集和发布：13 个 direct connectors + 24 个第一方研究/工程 feeds。系统保留 source identities 和 citations，提供 model cards/technical reports 中的 mention 和 score histories，支持按基准查询、查看评估证据。提供 leaderboard、Pareto frontier（分数 vs 采用量）、saturation 与趋势视图、CLI 和可复现分析。

关键结果：catalog 含 1,283 条 source records，来自 4 个 benchmark catalogs；在 790 条记录上有 12,916 个数值观测。论文对全 catalog 进行审计，分析基准饱和、采用趋势和分数比较的局限，并给出完整 prior-art 搜索示例。
