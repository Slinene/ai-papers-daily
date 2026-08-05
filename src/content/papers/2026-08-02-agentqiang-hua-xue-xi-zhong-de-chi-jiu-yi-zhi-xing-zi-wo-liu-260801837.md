---
title: 'PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement
  Learning'
title_zh: Agent强化学习中的持久一致性自我蒸馏
authors:
- Chunji Lv
- Yangguang Wei
- Junlin Liu
- Yang Gao
- Ming Liu
- Xinming Wang
- Jinyang Wu
- Guoren Wang
- Changsheng Li
affiliations:
- Beijing Institute of Technology
- Meituan
- Institute of Automation, Chinese Academy of Sciences
- Tsinghua University
arxiv_id: '2608.01837'
url: https://arxiv.org/abs/2608.01837
pdf_url: https://arxiv.org/pdf/2608.01837
published: '2026-08-02'
collected: '2026-08-05'
category: Agent
direction: Agent强化学习·自蒸馏一致性
tags:
- Reinforcement Learning
- Self-Distillation
- Agent
- GRPO
- Token-level Weights
- Persistent Consistency
one_liner: 通过教师信号局部持久性计算token级权重，联合GRPO缓解Agent稀疏奖励问题
practical_value: '- 在电商/对话搜索Agent的RL微调中，可采用稠密token级蒸馏信号缓解稀疏奖励，利用PCSD的持久一致性权重降低教师噪声。

  - 生成式推荐中蒸馏大模型输出时，可借鉴持久一致性思想评估各token的可靠性，用于知识蒸馏中的动态权重分配。

  - 自适应窗口与指数衰减聚合捕捉局部支持趋势的做法，可迁移至用户行为序列建模或Agent轨迹中的注意力权重设计。

  - 联合GRPO与蒸馏目标的多任务训练范式，为推荐Agent提供了一种平衡探索与利用、兼顾环境反馈与教师引导的优化思路。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM Agent在多轮交互任务中，RL因稀疏奖励而训练困难。On-policy self-distillation可提供稠密token级监督，但教师模型并非处处可靠，现有方法或对噪声敏感，或忽略位置差异。

**方法**：提出PCSD，从局部教师偏好信号的持久性导出token级蒸馏权重。它利用自适应窗口与指数衰减聚合捕捉持久的教师支持，用趋势感知调制衰减下降的支持，再经sigmoid门控生成连续权重。蒸馏损失与GRPO联合优化，既保留环境稀疏反馈，又有稠密教师指导。

**结果**：在ALFWorld上，PCSD在两种backbone上均取得最优overall成绩，比GRPO高15.6/13.3点，比SDAR高6.2/5.5点；WebShop上保持竞争力；未见过的ALFWorld split上比GRPO高15.8点。
