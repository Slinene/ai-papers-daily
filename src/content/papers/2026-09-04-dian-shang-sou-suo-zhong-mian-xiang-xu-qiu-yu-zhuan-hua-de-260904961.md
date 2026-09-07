---
title: 'SAM-D2Q: Aligning Multimodal Doc2Query with Search Demand and Conversion for
  E-commerce'
title_zh: 电商搜索中面向需求与转化的多模态 Doc2Query 对齐
authors:
- Hui Zhou
- Jian Hui Ji
- Lei Ma
- Rong Xiao
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2609.04961'
url: https://arxiv.org/abs/2609.04961
pdf_url: https://arxiv.org/pdf/2609.04961
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 电商搜索 · 多模态文档扩展与 RL 对齐
tags:
- Doc2Query
- Multimodal
- GRPO
- E-commerce Search
- Sparse Retrieval
- Preference Alignment
one_liner: 三阶段课程学习将多模态 Doc2Query 对齐到召回增益和商业转化，线上 GMV +3.38%
practical_value: '- 布尔召回下，文档扩展不要做 TF 加权，只生成不在 title 中的新词；训练时用信息增益过滤（V_Q ⊈ V_T）防止模型退化复制标题。

  - 用 CPV 视觉属性码表做反事实掩码：把 title 中的颜色/材质/款式等词遮掉，保留图片，构造多模态样本，逼模型从图里补属性，改善长尾/短标题商品召回。

  - 奖励设计可直接复用：安全 gate 先滤掉低相关或无新词生成，再叠加语义评分 + 商业词价值（PV×CVR 贝叶斯平滑，冷启动词用全局分平滑）+ 视觉属性
  bonus；优化用 GRPO 省 value net。

  - 工程上离线对选品批量生成 Top-K 查询填充倒排索引，线上无模型推理，索引 +35% 但 P99 延迟只 +0.2%，增量可回滚，适合大规模电商搜索。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
电商搜索依赖布尔倒排检索，但商品标题短、图片属性多，用户查询与标题常存在词汇不匹配。传统 Doc2Query 仅基于文本、只优化语义相关性，容易生成低商业价值或冗余词，且忽略图片中的颜色、款式、材质等关键属性。

## 方法关键点
SAM-D2Q 采用三阶段课程学习：
- **Stage 1 信息增益约束 SFT**：只用 query 未被 title 完全覆盖的日志样本训练，避免模型退化为简单复制标题中的词。
- **Stage 2 反事实视觉增强**：对 query 被 title 覆盖但含 CPV 视觉属性的样本，遮罩 title 中这些视觉词，保留图片，迫使模型从图像恢复属性；混合过滤后的人工标注数据，强化视觉接地。
- **Stage 3 GRPO 偏好对齐**：设计复合奖励 = 安全 gate + 语义一致性 + 商业价值 + 视觉属性 bonus。商业价值用 term 级 PV×CVR 的贝叶斯平滑估计，冷启动词用全局分平滑；优化采用 GRPO 去掉 value network。
- **部署**：离线生成 Top-100 候选查询，经过滤后插入倒排索引，在线无模型推理。

## 关键结果
- 离线 8.8M 商品索引、30k 查询：Top-3000 相关商品数从 454.5 提升到 594.1（+30.7%），Total Qual 从 5,366M 提升到 7,139M（+33.0%）。
- 生成质量：相关性从文本 baseline 的 43.11% 提升到 74.96%，Query-Value 达到 0.981。
- 线上 A/B（4% 流量，21 天）：GMV +3.38%，Pay Count +2.27%，CTR +0.25%，CVR +0.53%，零结果 PV 占比从 2.07% 降至 1.72%。
- 索引增大 35%，P99 召回延迟仅增加 0.2%。

## 值得记住
在布尔检索里，Doc2Query 的价值只来自“引入 title 里没有的新词”；用信息增益过滤 + 反事实视觉遮罩 + 商业复合奖励，可以把生成式扩展直接对齐到 GMV。
