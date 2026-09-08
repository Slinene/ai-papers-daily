---
title: What Else Needs Fixing? Exploring Cost-Effective Test-Time Compute for Revision
  Propagation in Artifacts Generated Through Conversation
title_zh: 对话生成制品修订传播的低成本测试时计算探索
authors:
- Daisuke Kikuta
affiliations:
- NTT, Inc.
arxiv_id: '2609.03254'
url: https://arxiv.org/abs/2609.03254
pdf_url: https://arxiv.org/pdf/2609.03254
published: '2026-09-02'
collected: '2026-09-08'
category: Eval
direction: LLM 评估 · 修订传播与测试时计算
tags:
- LLM
- Revision Propagation
- Test-Time Compute
- Benchmark
- Parallel Sampling
- Conversational Artifacts
one_liner: 提出对话生成制品的修订传播基准，评估九种测试时计算方法，三路并行采样+选择最具性价比
practical_value: '- 在对话式商品推荐或营销文案生成中，用户只给出局部修改请求（如更换目标人群）时，容易造成预算、卖点、行程等字段不一致；可以把该工作的方法迁移进来：在修订
  prompt 中显式让模型列出所有受影响字段或依赖关系，并做一次自检，确保局部改动被传播到所有相关部分。

  - 测试时多采样+选择是低成本的准确率提升手段：生成 3 个候选修订，用 LLM-as-judge 或 medoid 选择最优，比单次生成或长链反思更划算，适合线上低延迟、低预算的
  LLM 修订任务。

  - 可以建立小规模“修订传播”评测集，模拟用户局部修改请求，检查模型是否同步更新关联字段，作为对话式推荐助手或内容生成引擎的离线回归评估。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 在对话中迭代生成与修改文档、代码、计划等制品时，用户常只给出局部修改请求；模型需自行识别依赖并传播修订到所有受影响部分，否则会造成不一致。该能力在对话生成场景下缺乏专门基准，且测试时计算成本效益不明确。

**方法关键点**：构建新的对话生成制品修订传播基准；评估 9 种修订方法，包括顺序反思与并行采样变体；使用 gpt-oss-20b/120b、gpt-5.4-mini、qwen3.5-9b/27b/122b；并行采样后采用 LLM 打分或 medoid 选择。

**关键结果数字**：基线准确率 68.3%–93%；从三个并行样本中选择（LLM-based 或 medoid）是最高性价比方案，准确率提升 2.2–9.7%。
