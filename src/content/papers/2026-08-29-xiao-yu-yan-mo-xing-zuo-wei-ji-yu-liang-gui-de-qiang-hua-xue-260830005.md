---
title: Small Language Models as Judges for Rubric-Based Reinforcement Learning
title_zh: 小语言模型作为基于量规的强化学习评判器
authors:
- Fengyu Xie
- Yilun Zhao
- Bingsen Chen
- Arman Cohan
- Chen Zhao
affiliations:
- New York University
- Yale University
arxiv_id: '2608.30005'
url: https://arxiv.org/abs/2608.30005
pdf_url: https://arxiv.org/pdf/2608.30005
published: '2026-08-29'
collected: '2026-09-04'
category: Training
direction: 高效奖励模型与 RL 训练
tags:
- Rubric-based RL
- GRPO
- Probe judge
- Small language models
- Reward model
- Efficient RL
one_liner: 1.7B Probe 评委替代大模型生成式评委做逐条量规打分，RL 训练效果更优且奖励判断快 10.7 倍
practical_value: '- 在需要逐条 rubric 打分的 RL 训练中，用冻结小模型 backbone + 线性 probe 头输出每条标准满足概率，替代生成式
  LLM judge，可将奖励计算延迟降低一个数量级，适合需要高吞吐在线奖励信号的 Agent 训练与推荐文案优化。

  - 对电商多维度评价（如相关性、覆盖度、转化意图）可分别训练多个 probe 头，共享同一小模型编码器，把 instance-specific criteria
  转化为隐藏状态上的线性分类问题，避免逐 token 生成，工程实现简单且稳定。

  - 当奖励标准明确且 itemwise 标签可标注时，小模型 probe 评委能保留标准级奖励结构，跨任务/领域迁移良好，可用于搜索推荐系统的多属性质量控制，无需为每个新场景重新训练大模型评委。

  - 若当前使用 7B+ 生成式奖励模型，可尝试用 1-2B 小模型 probe 替代，在效果不降甚至更优的情况下大幅降低 API 成本与训练时间。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：基于量规的 RL 能用于长文本生成、Agent 等没有精确答案的任务，但奖励计算需反复调用大模型 judge 或 API，成本高、延迟大，限制训练规模。

**方法**：构建 PointRubric 和 RaR-Science-Static 两个逐条量规评测集，每条标准有 itemwise 满足标签。比较三种从小模型提取标准级判断的方法：生成式回答、Yes/No logprob 边缘、Probe judge（在隐藏状态上加线性头预测每条标准满足概率）。以 Qwen3-1.7B 为 backbone，并将 Probe judge 作为 GRPO 奖励模型训练策略。

**结果**：Qwen3-1.7B Probe judge 在两个数据集上标准级一致性最强，超过生成式和 Logprob 评委；在 RaR-Science 上，用 Probe judge 作奖励模型，策略分数从 0.232 提升到 0.643，对比 8B 生成式 judge 的 0.594，且奖励判断时间减少 10.7 倍。任务和领域迁移实验显示 Probe judge 能保留标准级奖励结构。
