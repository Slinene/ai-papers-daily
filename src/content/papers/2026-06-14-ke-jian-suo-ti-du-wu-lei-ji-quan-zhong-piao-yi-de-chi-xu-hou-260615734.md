---
title: 'Retrievable Gradients: Continual Post-Training Without Cumulative Weight Drift'
title_zh: 可检索梯度：无累积权重漂移的持续后训练
authors:
- Weihang Su
- Jiacheng Kang
- Jingyan Xu
- Qingyao Ai
- Jianming Long
- Hanwen Zhang
- Bangde Du
- Xinyuan Cao
- Min Zhang
- Yiqun Liu
affiliations:
- Department of Computer Science and Technology, Tsinghua University
arxiv_id: '2606.15734'
url: https://arxiv.org/abs/2606.15734
pdf_url: https://arxiv.org/pdf/2606.15734
published: '2026-06-14'
collected: '2026-06-17'
category: Training
direction: 持续后训练 · 梯度检索与临时权重适应
tags:
- continual learning
- gradient bank
- meta-learning
- retrieval-augmented
- weight drift
- post-training
one_liner: 将梯度视为可检索的知识单元，通过即插即用的临时权重调整实现持续学习，避免参数漂移与灾难性遗忘。
practical_value: '- **即插即用的知识更新**：将新领域文档（例如新品详情、政策变化）预先计算梯度并存入梯度库，推理时根据query检索相关梯度临时调整模型，实现零遗忘的在线知识注入，避免全量重训。

  - **可逆性与版本管理**：梯度库天然支持知识卸载，移除对应梯度即可擦除引入的知识，适合广告/推荐场景中需要频繁上下线的商品或活动，无需回滚模型参数。

  - **组合式适应**：多个文档的梯度可以按需组合（如多商品叠加推荐），提供类似LoRA的模块化适配能力，但更灵活且无需事前训练适配器，降低工程复杂度。

  - **元学习重塑梯度**：通过任务驱动的元目标，将文档梯度优化为更通用的适应信号，可借鉴此思路将商品描述、用户评论等转化为对推荐任务有判别力的梯度，提升下游CTR预估等性能。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：部署后LLM需持续吸收新知识，但传统持续训练（CPT）反复更新共享参数会导致权重漂移，引发灾难性遗忘。检索增强生成（RAG）虽避免参数漂移，却缺乏深层参数化知识融合。

**方法**：提出 **ReGrad**，将梯度视为可检索的知识单元。离线时，对每个文档计算语言模型梯度，存入**梯度银行**并索引；推理时，根据查询检索相关文档的梯度，临时加入模型参数进行适应，用完即丢弃，参数不变，无永久漂移。为让梯度适用于下游任务，引入**双层元学习**：内循环用文档梯度适应模型并评估任务损失，外循环通过最小化任务损失来优化文档梯度，将其重塑为通用适应信号。

**结果**：在通用与领域特定设定下，ReGrad 超越 CPT 和 RAG 基线，实现可扩展、可逆的参数化知识注入，任务性能提升的同时消除权重漂移。
