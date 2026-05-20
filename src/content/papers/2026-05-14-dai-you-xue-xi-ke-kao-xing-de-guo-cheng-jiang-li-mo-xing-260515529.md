---
title: Process Rewards with Learned Reliability
title_zh: 带有学习可靠性的过程奖励模型
authors:
- Jinyuan Li
- Langlin Huang
- Chengsong Huang
- Shaoyang Xu
- Donghong Cai
- Yuyi Yang
- Wenxuan Zhang
- Jiaxin Huang
affiliations:
- Washington University in St. Louis
- Singapore University of Technology and Design
arxiv_id: '2605.15529'
url: https://arxiv.org/abs/2605.15529
pdf_url: https://arxiv.org/pdf/2605.15529
published: '2026-05-14'
collected: '2026-05-20'
category: Training
direction: 过程奖励可靠性建模与自适应推理
tags:
- PRM
- Reasoning
- Uncertainty
- Best-of-N
- Token Reduction
- Beta-Binomial
one_liner: BetaPRM 预测步骤正确概率和该预测的可靠性，并利用可靠性信号实现自适应计算分配，减少推理 token 消耗
practical_value: '- 在 Agent 多步决策中，使用 Beta 分布建模每步奖励的可靠性，避免单点奖励误导决策，增强动作选择的可信度。

  - 对于生成式推荐候选集选择的 Best-of-N 推理，可借鉴自适应计算分配（ACA）：根据可靠性提前终止高置信候选，将计算资源集中到不确定的候选上，显著减少
  LLM 调用成本。

  - 训练 PRM 时，不再回归有限样本成功率，而是采用 Beta-Binomial 似然直接学习 Beta 信念，输出不确定性，这对排名、过滤等下游任务更友好。

  - 在需要对中间结果（如 query 重写、解释生成）打分的系统中，可引入可靠性阈值控制，避免过早丢弃潜在正确但暂时评分偏低的步骤。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有过程奖励模型（PRM）仅输出步骤正确性的单点估计，缺乏对奖励可靠性的指示，导致下游任务（如 Best-of-N 选择）盲目信任不完美的分数，造成决策偏差或计算浪费。

**方法**：提出 BetaPRM，一种分布式 PRM。它预测步骤成功概率的同时输出该预测的可靠性，具体通过 Beta-Binomial 似然从蒙特卡洛连续采样监督中学习 Beta 信念分布，而非直接回归有限样本成功率。该可靠性信号使下游应用能区分可信与不确定的奖励。基于此信号，进一步提出自适应计算分配（ACA）用于 PRM 引导的 Best-of-N 推理：当高奖励解足够可靠时提前终止，对不确定候选前缀投入更多计算，从而动态平衡准确率和代价。

**结果**：在四个骨干模型和四个推理基准上，BetaPRM 不仅提升了 PRM 引导的 Best-of-N 选择效果，还保持了标准的步骤级错误检测能力。ACA 相较于固定预算 Best-of-16，在提升最终答案准确率的同时，Token 用量最多减少 33.57%，显著改善了准确率-Token 权衡。
