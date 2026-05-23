---
title: Unsupervised Process Reward Models
title_zh: 无监督过程奖励模型
authors:
- Artyom Gadetsky
- Maxim Kodryan
- Siba Smarak Panigrahi
- Hang Guo
- Maria Brbic
affiliations:
- Swiss Federal Institute of Technology (EPFL)
arxiv_id: '2605.10158'
url: https://arxiv.org/abs/2605.10158
pdf_url: https://arxiv.org/pdf/2605.10158
published: '2026-05-10'
collected: '2026-05-23'
category: Training
direction: PRM训练 · 无监督学习
tags:
- PRM
- unsupervised learning
- reasoning
- step-level reward
- LLM
- reinforcement learning
one_liner: 提出无需人工标注的无监督PRM，通过LLM next-token概率联合定位第一步错误步骤
practical_value: '- **无监督奖励塑形**：借鉴基于LLM自身token概率的评分函数，在Agent多步交互或推荐多轮对话中，无需人工标注即可识别错误步骤，用于重试或矫正策略。

  - **批次内对比定位**：利用同一批次多个轨迹的相似性联合评估第一步错误位置，可迁移到电商搜索多意图理解或生成式推荐的HIT预估，通过对比候选序列一致性定位偏差。

  - **强化学习稳健训练**：uPRM作为reward信号比有监督PRM更稳健，适合推荐策略在线优化时，避免过拟合人工偏好，直接利用模型自身不确定性进行探索。

  - **测试时验证器**：uPRM作为验证器可提升多数投票基线（+6.9%），在推理链较长的生成式推荐（如Semantic ID生成）中可用于beam search重新排序。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：过程奖励模型（PRM）通过步骤级监督精细控制LLM推理，但需要昂贵的人工步骤标注，难以规模化。现有无监督方法仍依赖最终答案真值验证。本工作旨在完全去除人类监督，仅利用LLM自身概率信息训练PRM。

方法：核心思想是定义一个基于LLM next-token概率的评分函数，对一批推理轨迹联合评估第一步错误位置。具体地，对batch内每条轨迹的每一步，通过语言模型计算该步前后token概率的变化，并利用整个batch的统计特征（如众数一致性）识别异常步骤，无需任何标注即可定位错误。据此可构建二分类训练信号，训练一个轻量级uPRM。

结果：在ProcessBench数据集上，uPRM识别第一步错误的准确率比LLM-as-a-Judge绝对提升15%；作为测试时验证器，性能与有监督PRM相当，且比多数投票基线提升6.9%；在强化学习中作为奖励信号，uPRM训练的模型比使用真实标签训练的PRM更鲁棒。
