---
title: 'Predicting What Answer Engines Cite: Open Decision Models, Rerankers and a
  Distilled 4B Student on Ten Engines under Controlled Retrieval'
title_zh: 预测答案引擎引用：开源决策模型与蒸馏4B重排学生模型
authors:
- Elisha Bajemon
- Andre-Louis Rochet
affiliations:
- TW3 Partners (Citead)
arxiv_id: '2610.38090'
url: https://arxiv.org/abs/2610.38090
pdf_url: https://arxiv.org/pdf/2610.38090
published: '2026-10-28'
collected: '2026-10-31'
category: RecSys
direction: 生成式引擎优化 · 引用预测重排蒸馏
tags:
- GEO
- citation prediction
- reranker distillation
- LoRA
- LLM judge
- benchmark
one_liner: 用LoRA微调Qwen3-Reranker-4B蒸馏27B决策模型，预测答案引擎引用份额，性能与教师差异不显著
practical_value: '- 可直接复用其蒸馏思路：用大模型/决策模型（如Jev或开源27B）为候选内容打分作为教师标签，再用 LoRA 微调小参数量重排器（Qwen3-Reranker-4B），大幅降低线上打分成本且性能接近教师，适合电商/广告中预测
  LLM 会引用哪些商品卖点、评论或内容。

  - 教师打分方式影响学生上限：论文发现让教师逐条 passage 独立打分（而非 group 打分）能消除位置/上下文偏差，建议在构建蒸馏数据时同样采用 pointwise
  标注，避免 listwise 评分中的锚定效应。

  - 多引擎投票一致性可作为弱监督信号：十个引擎对同一候选源的引用具有组内 Spearman 0.704 的相关性，可用多个 LLM 裁判或引擎输出的一致票数生成伪标签，减少人工标注成本，实用性强。

  - 开源了模型、基准、所有 scorer 预测和代码，可直接用于生成式搜索优化、内容营销预测，也可迁移到电商场景预测答案引擎会引用哪些产品描述或用户问答。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机
生成式引擎优化（GEO）需要一个打分器，预测候选页面在答案引擎中获得的引用份额。直接查询引擎昂贵、慢且不稳定，因此用模型预测引用得分成为关键。

## 方法
在 GEO-Bench 查询集上，控制相同候选源提供给十个答案引擎，测量预训练重排器、托管类型决策模型 Jev、八个开源决策模型以及用 LoRA 微调的 Qwen3-Reranker-4B 学生模型。采用教师标签蒸馏，比较不同教师（Jev、开源27B、观测引擎引用）及单/多教师设置，并在多个随机种子上评估。

## 关键结果
- 多个引擎回答同一查询时，组内 Spearman 相关系数为 0.704，说明引擎间有一定一致性。
- 无训练情况下，Jev 和两个开源 27B 决策模型最强，达到 0.575–0.578。
- 蒸馏4B学生模型（GEO Citation Ranker 4B）性能 0.542–0.549，在 229 个查询上与 27B 模型和 Jev 的差异不显著。
- 当 Jev 逐条 passage 打分时，学生与 Jev 的剩余差距大部分消失；0.6B 参数量下，仅用 Jev 标签即可达到双教师目标水平。
- 全部模型、基准、预测和代码开源。
