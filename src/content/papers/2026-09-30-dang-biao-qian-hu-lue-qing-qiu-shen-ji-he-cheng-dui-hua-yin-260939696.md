---
title: 'When the Label Ignores the Request: Auditing Policy-Selected Targets in Synthetic
  Conversational Music Recommendation'
title_zh: 当标签忽略请求：审计合成对话音乐推荐中的策略选择目标
authors:
- Sanjeev Suresh
affiliations:
- Independent Researcher
arxiv_id: '2609.39696'
url: https://arxiv.org/abs/2609.39696
pdf_url: https://arxiv.org/pdf/2609.39696
published: '2026-09-30'
collected: '2026-10-02'
category: Eval
direction: 对话推荐 · 标签审计与训练补充
tags:
- conversational recommendation
- synthetic benchmark
- label validity
- exact-item retrieval
- training augmentation
- nDCG@20
one_liner: 审计合成对话音乐推荐基准，发现显式点歌请求半数被官方标签违背，低权重训练补充修复且不损官方指标
practical_value: '- 在对话式推荐/智能客服中，对用户明确指定商品或歌曲的 turn，不要直接用生成式 policy 的后续 item 当训练 label，否则模型会学会忽略显式意图。可复用做法：用正则+商品目录解析构建确定性
  detector，识别精确 item/版本请求，并将其解析目标作为补充正样本，同时保留官方 label 但降低该 turn 权重（如 0.1）。

  - 评估 benchmark 或线上流量时，除全局 nDCG/转化外，应建立“请求满足切片”，专门监控用户点名 item 的满足情况。本文展示这类切片虽然占比小（1%），但行为变化巨大，全局指标完全无法反映，容易被忽略。

  - 在标签增广/去噪实验中，必须设 matched control（相同特征包括请求信号，但不使用增广 label）和 predeclared preservation
  margin，验证提升不是来自特征暴露，且不伤主指标。工程上可在推理时只在 detector 命中的 turn 上替换 reranker 分数，其他 turn
  保持 base 模型，降低风险。

  - 如果业务上有精确商品 query，优先规则覆盖（resolve 到具体 item 提升到 rank1）通常安全，但要注意 false fire 会直接成为
  top1 错误；本文选择训练 reranker 而非硬覆盖，可在检测精度不够时借鉴。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
合成对话数据已成为对话推荐系统（CRS）基准的主流来源，但其中的 label 是生成 policy 记录的下一个 track，未必是用户最新请求。在用户点名歌曲的 turn，两者可直接对比。真实音乐搜索中，命名商品是主导意图，系统不应替换；但全局 nDCG 掩盖这一行为。本文审计 RecSys Challenge 2026 TalkPlay 开发集，量化 label 与显式请求的冲突。

## 方法关键点
- 审计只使用可见 dialogue 和 catalog metadata；确定性的 regex + catalog resolver 检测 exact/version 请求：提取引用标题和命令 span，匹配 title/artist，歧义时弃权。
- 在 8000 个评估 turn 中找到 82 个显式点播，41 个官方 label 冲突，冲突集中在对话深部（turn 5–8 超过 2/3），符合 pool 耗尽的约束。
- 系统为多路召回（BM25/dense/pseudo-relevance/bi-encoder）+ XGBoost LambdaRank reranker（49 特征）。
- 训练干预：冲突 turn 保留官方 label，增加请求满足 target，整个 turn 权重调至 0.1；1.5% 训练 turn 受影响。
- 设 matched control：加 binary exact-request 特征但只训练官方 label，排除特征暴露；推理时 detector gate，只在命中 turn 用 retrained 分数。

## 关键实验
开发集 1000 sessions。冲突切片 43 例（42 exact + 1 version）。official nDCG@20 whole split 0.1908→0.1914（+0.31%，CI 不含负），请求满足 whole split +1.09%，冲突切片 nDCG@20 0.523→0.802（+53.3%），session-level +0.277 所有 bootstrap 为正。其他五个 family（硬 artist 约束、rejection/switch-away、album/year 约束、broad semantic）因 precision、目标解析或官方损失未通过证据门槛。

## 最值得记住的一句话
在合成对话推荐基准中，可验证的精确请求族能揭示 policy label 的系统性违背；用低权重补充训练可在不牺牲官方指标的前提下修复。
