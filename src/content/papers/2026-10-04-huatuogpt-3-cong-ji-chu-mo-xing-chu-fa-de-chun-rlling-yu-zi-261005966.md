---
title: 'HuatuoGPT-3: RL-Only Domain Adaptation from Base Models'
title_zh: HuatuoGPT-3：从基础模型出发的纯RL领域自适应
authors:
- Junying Chen
- Xinyuan Xie
- Ziniu Li
- Wenyuan Gu
- Jianquan Li
- Xiang Wan
- Guangjun Yu
- Ruoyu Sun
- Haizhou Li
- Benyou Wang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Shenzhen Research Institute of Big Data
- Shenzhen Loop Area Institute
- National Health Data Institute, Shenzhen
arxiv_id: '2610.05966'
url: https://arxiv.org/abs/2610.05966
pdf_url: https://arxiv.org/pdf/2610.05966
published: '2026-10-04'
collected: '2026-10-07'
category: Training
direction: RL-only 大模型领域自适应训练
tags:
- RL-only
- Domain Adaptation
- Policy Optimization
- Teacher Retirement
- LLM Training
one_liner: 提出OnePO，以自适应目标演化和教师退休实现RL-only领域自适应，在医学上用20K样本超越SFT+RL和纯RL
practical_value: '- 借鉴 Teacher Retirement 机制：在 RLHF/LLM 微调时，若策略模型在验证集上的奖励或质量指标已稳定超过教师/参考模型，可自动切换为纯
  on-policy 采样，避免陈旧教师分布限制探索，适合推荐文案、搜索 query 扩写等生成任务。

  - Adaptive Objective Evolution 中强化低概率但有信息量的 token（如商品卖点、数字、属性词），可迁移到电商文案生成或搜索增强，让模型更准确覆盖关键低频
  token。

  - 仅用 RL 从 base model 开始领域适应，可减少 SFT 对生成多样性的压缩，对推荐理由、对话式推荐等需要多样性的场景有参考；但工程上需要解决冷启动，可采用教师输出作为快速启动的辅助数据。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：领域适应通常采用 SFT+RL 流程，但 SFT 会降低探索多样性并引入多阶段优化复杂度。纯 RL 存在冷启动问题，混合策略 RL 则面临两个失败模式：Gradient Starvation（教师输出中有信息量的低概率 token 学习过慢）和 Teacher-Distribution Anchoring（陈旧教师输出在后期限制策略提升）。

方法关键点：One-stage Policy Optimization（OnePO）将教师输出视为策略改进的过渡性指导。两个核心组件：Adaptive Objective Evolution 强化对教师输出中低概率但有信息量 token 的学习，缓解梯度饥饿；Teacher Retirement 在当前策略性能超过教师输出时自动丢弃教师数据，切换到纯 on-policy RL，解除教师分布锚定。

关键结果：在医学领域适应中，OnePO 仅用 20K 训练样本在 HealthBench (Total) 达到 67.2 分，相比 SFT+RL 和纯 RL 分别提高 2.7 和 7.4 分。扩展为 HuatuoGPT-3 系列，27B 模型在 HealthBench (Total) 达到 70.1，在 HealthBench Professional 达到 71.4，超过 GPT-6 Astra 等前沿模型。代码与模型已开源。
