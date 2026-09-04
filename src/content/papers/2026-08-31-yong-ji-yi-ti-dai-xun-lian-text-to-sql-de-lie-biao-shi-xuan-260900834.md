---
title: 'Replacing Training with Memory: Listwise Selection for Text-to-SQL'
title_zh: 用记忆替代训练：Text-to-SQL 的列表式选择
authors:
- Yeonseok Jeong
- Soyoung Yoon
- Seongjun Lee
- Seung-won Hwang
affiliations:
- IPAI, Seoul National University
- KAIST
arxiv_id: '2609.00834'
url: https://arxiv.org/abs/2609.00834
pdf_url: https://arxiv.org/pdf/2609.00834
published: '2026-08-31'
collected: '2026-09-04'
category: Other
direction: LLM 候选选择免微调 · Memory 检索
tags:
- Text-to-SQL
- Listwise Selection
- Memory
- Inference-time
- Positional Bias
- LLM
one_liner: 免微调列表式选择器，用结构化记忆作为决策标准并多排列聚合缓解位置偏差，BIRD-dev 准确率提升 2.02 且 tokens 减 2.92x
practical_value: '- 可借鉴其 **structured memory bank**：把自然语言到业务实体/操作/期望输出的映射事先蒸馏成可检索片段，作为候选排序的显式标准，避免对选择器微调；在电商
  query 改写、广告文案候选选择中可构建 query→商品属性/类目意图/文案风格的 memory，推理时检索作为评分依据。

  - 借鉴 **多排列聚合 + 执行结果/pointwise 预筛** 的推理成本优化：先用轻量打分或可执行性检查过滤多数候选，只对 top-k 做多顺序的 listwise
  比较，再聚合排名，能降低 LLM 调用 tokens 和位置偏差。

  - 位置偏差缓解可以做成推理时策略而非训练策略，兼容已有 LLM；在搜索推荐 Agent 的多个工具/候选结果重排序环节，可直接插入多排列投票逻辑，无需额外训练。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现代 Text-to-SQL 系统常用 generate-execute-select pipeline，生成多个候选 SQL 后由 selector 选择最优；listwise selector 需微调，成本高，且 listwise 输入存在 positional bias。

**方法关键点**：提出 MAP-SQL，完全免微调。构建 reusable structured memories，从训练数据蒸馏自然语言到 schema elements、SQL operations、expected outputs 的映射；给定 question 时检索相关 memory 作为显式决策标准，对候选 SQL 做 listwise 评估。为缓解顺序偏差，对多个输入排列生成排名并聚合；推理成本通过 execution results 和 pointwise scoring 优化，先利用执行结果和点式打分过滤候选，再做必要的 listwise 比较。

**关键结果**：在 BIRD-dev 上使用相同候选集，MAP-SQL 平均 execution accuracy 比之前 SOTA selector 方法 R³-SQL 高 2.02 个百分点，tokens 减少 2.92 倍；选择更稳定，不必要的比较更少。
