---
title: 'CREDO: Evidence-Conditioned Credit Assignment for Temporal Reasoning Agents'
title_zh: CREDO：面向时序推理智能体的证据条件化信用重分配
authors:
- Yue Leng
- Shengtao Wen
- Xiang Chen
- Xinyi Zeng
- Yu Tian
- Sheng-Jun Huang
affiliations:
- Nanjing University of Aeronautics and Astronautics
- Tsinghua University
- 360 Security Capability Center, Qihoo 360
arxiv_id: '2611.01643'
url: https://arxiv.org/abs/2611.01643
pdf_url: https://arxiv.org/pdf/2611.01643
published: '2026-11-01'
collected: '2026-11-03'
category: Training
direction: 时序知识图谱问答 · 强化学习信用分配
tags:
- TKGQA
- GRPO
- Credit Assignment
- RLHF
- LLM Agents
- Temporal Reasoning
one_liner: CREDO 用中间证据恢复局部监督，改进 GRPO 在时序知识图谱问答中的信用分配，提升 MultiTQ/TimelineKGQA 准确率
practical_value: '- 在 LLM Agent 强化学习（GRPO）中，不要只依赖最终转化/成交信号。对同一 query 的多个 rollout 互相比较，利用中间状态（如检索命中、候选覆盖、证据留存比例）构造阶段级奖励，能区分“证据找对了但后续没接住”的失败样本。

  - 全失败批次也可以训练：采用中间证据质量或答案重叠作为“机会”代理，把一部分 outcome-policy 权重分配到推理/回答阶段，避免全 0 奖励导致无梯度；这在多跳搜索推荐
  Agent、多轮对话推荐等稀疏奖励场景尤其有效。

  - 工程上可保持终端 reward 和 trajectory-level advantage 不变，仅对阶段奖励做权重再分配且保证总权重守恒，降低新增超参风险；适合用于商品知识图谱问答、带检索/过滤步骤的
  Agent 训练。

  - 若业务中有“检索到关键属性但最终没转化”的日志，可用于离线构造证据条件化奖励，指导 Agent 改写查询或重新排序。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：TKGQA 智能体的轨迹级结果信号来自 GRPO，但无法分辨中间决策质量。下游失败会惩罚有用的证据获取；全失败组内奖励相同，中间进展没有相对信号。

**方法关键点**：CREDO 通过中间证据恢复局部监督：对同一问题的多个 rollout 互相比较，给证据获取、推理、回答阶段分配正向阶段级信用；用保留答案重叠作为“机会”代理，将部分 outcome-policy 权重从终端结果向中间推理和回答倾斜。保留终端奖励与轨迹级 advantage，重分配时保持每个轨迹的 outcome-policy 总权重守恒，因此训练稳定。

**关键结果**：在 MultiTQ 上，相对最强已发布基线，Overall accuracy 从 78.0% 提高到 82.4%，Multiple accuracy 从 55.0% 提高到 65.6%；在 TimelineKGQA 上，直接迁移到 ICEWS Actor 时 cross-KG accuracy 从 30.9% 提高到 36.4%。
