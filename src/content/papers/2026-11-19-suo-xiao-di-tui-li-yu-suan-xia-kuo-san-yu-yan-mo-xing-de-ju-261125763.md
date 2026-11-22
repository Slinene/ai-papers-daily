---
title: Closing Performance Gap for Diffusion Language Models under Low Inference Budgets
title_zh: 缩小低推理预算下扩散语言模型的性能差距
authors:
- Hao Wu
- Sipeng Chen
- Jingwen Fu
- Yuwang Wang
affiliations:
- University of Wisconsin–Madison
- Northwestern University
- Zhongguancun Academy
- Zhongguancun Institute of Artificial Intelligence
- Tsinghua University
arxiv_id: '2611.25763'
url: https://arxiv.org/abs/2611.25763
pdf_url: https://arxiv.org/pdf/2611.25763
published: '2026-11-19'
collected: '2026-11-22'
category: LLM
direction: 扩散语言模型低预算推理优化
tags:
- diffusion language models
- low-budget inference
- training-free
- token remasking
- code generation
- math reasoning
one_liner: CaRR 训练免费框架通过重掩码与轨迹恢复提升扩散 LM 低预算生成质量，1/8 预算下平均精度 +7.44pp
practical_value: '- 低延迟生成场景（如搜索 query 推荐、商品卖点文案）可借鉴“不增加前向步数，通过重掩码/refill 利用已更新上下文”的思路：把有限解码预算集中在信息量高的
  token 上，而不是均匀减少步数。

  - 输出前增加“提交检查”和“轨迹恢复”：维护中间候选，当最终输出不满足业务约束（如长度、关键词、类目、格式）时，回退到历史可接受候选，避免重新生成，工程实现简单且几乎零成本。

  - 对于需要严格任务约束的生成，可在现有 decode 调度内集成轻量校验器（规则或小模型），只在最终不满足时从轨迹中选取候选，适合线上低延迟服务。

  - 如果团队在探索扩散/并行解码 LLM，CaRR 的 TCR（选择 native pure replacements 重新 mask）和 SCR（从精修轨迹恢复候选）可以直接复用，代码生成和数学推理上的提升说明该策略在不同任务上具有通用性。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：扩散语言模型（DLM）通过并行更新多个 token 减少顺序解码步数，在低推理预算下有望比自回归解码更快。但实际低预算时生成质量下降严重，可编辑扩散模型虽然通过 post-draft refinement 改善质量，却可能丢失有用的中间结果，导致最终提交的响应不是最优。

**方法关键点**：CaRR 是训练免费框架，在不增加额外 backbone forward 的前提下，从固定可编辑 checkpoint 提升提交质量。包含两个模块：
1. **Token Commitment Remasking (TCR)**：重新掩码被选中的“原生纯替换”token，并在下一个 scheduled edit forward 中利用更新后的上下文进行 refill，从而更有效地利用有限的前向步数。
2. **Submission Commitment Recovery (SCR)**：利用精修轨迹，在最终响应不满足任务特定输出要求时，恢复历史中受支持的候选结果，避免直接接受较差输出。

两个模块都运行在原生的 mask/edit schedule 内，不增加 backbone 前向次数。

**关键结果**：在代码生成和数学推理任务上，CaRR 在四个推理预算下均一致提升平均准确率，预算越紧提升越大。在 1/8 全调度前向预算下，CaRR 将六指标平均准确率提升 7.44 pp，其中 MBPP 和 MBPP+ 分别提升 11.37 和 10.05 pp，证明该方法在低预算场景下能显著缩小与高预算生成的质量差距。
