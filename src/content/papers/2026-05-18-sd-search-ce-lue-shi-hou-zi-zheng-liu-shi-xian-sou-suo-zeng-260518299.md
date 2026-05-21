---
title: 'SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning'
title_zh: SD-Search：策略事后自蒸馏实现搜索增强推理的步骤级监督
authors:
- Yufei Ma
- Zihan Liang
- Ben Chen
- Zhipeng Qian
- Huangyu Dai
- Lingtao Mao
- Xuxin Zhang
- Chenyi Lei
- Wenwu Ou
affiliations:
- Kuaishou Technology
arxiv_id: '2605.18299'
url: https://arxiv.org/abs/2605.18299
pdf_url: https://arxiv.org/pdf/2605.18299
published: '2026-05-18'
collected: '2026-05-21'
category: Agent
direction: 搜索增强推理 · 事后自蒸馏
tags:
- Self-Distillation
- Hindsight
- Agent Training
- GRPO
- Token-Level Loss
- Search-Augmented
one_liner: 提出事后自蒸馏框架，从策略自身获取搜索步骤的细粒度监督，无需外部教师或额外标注
practical_value: '- **从策略自身挖掘步骤级信号**：同一模型在训练时分别以“学生”（仅推理时上下文）和“教师”（额外看见同组滚动的事后摘要）两种视角运行，用分布匹配提取各搜索决策的细粒度反馈，无需外部教师或昂贵标注。可在推荐
  Agent 的多步交互中复用，对关键决策步骤（如召回、重排）施加 token 级自蒸馏。

  - **事后信息块的精巧设计**：通过屏蔽答案和思考内容、保留查询与二元结果标签（CORRECT/INCORRECT）构建对比，迫使教师隐含地评价哪些查询值得执行。在对话或推荐
  Agent 中，可用历史动作和成功/失败标签构建类似的事后上下文，强化正向动作模式。

  - **Jensen-Shannon 散度替代 KL 或 MSE**：对称、有界的 JSD 比 forward KL（强迫覆盖所有模式）或 reverse KL（过早坍塌到单一模式）更稳定，且对
  top-k 截断不敏感，适合 token 级分布对齐。可用于任何需要软目标匹配的生成任务，如生成式推荐中的语义 ID 蒸馏。

  - **无额外推理开销的 RL 融合**：自蒸馏仅增加一次辅助前向和损失项，不修改奖励或优势计算，训练耗时仅增 15.5%，推理完全不变。低成本地提升了多跳问答的查询质量，而不增加搜索次数，对线上
  Agent 服务的效率优化有启发。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
搜索增强推理 Agent 在 RL 训练中仅获得轨迹级结果奖励，无法区分每次搜索查询的质量，导致次优的检索行为。现有过程监督方法依赖外部大模型（如 72B 教师或 GPT-4o）提供步骤级信号，成本高且通用性受限。本文提出，策略自身在事后条件下（知晓各滚动结果）能更好地判断查询好坏，由此可自产步骤级监督。

**方法关键点**  
- **学生-教师架构**：同一策略模型充当两种角色：学生仅见当前轨迹前缀，教师额外看到“事后信息块”（同组内所有滚动的搜索查询与对应的正确/错误标签），两者共享参数。  
- **事后信息块设计**：屏蔽轨迹中的思考、文档和答案，仅保留查询序列和二元结果，形成对比；去除答案和文档避免信息泄露，保留跨滚动的成败对比增强信号。  
- **Token 级分发对齐**：在搜索查询令牌位置，用 Jensen-Shannon 散度（JSD）拉近学生与教师的分布，JSD 对称且有界，训练更稳定。  
- **与 GRPO 无缝结合**：自蒸馏损失直接加到 GRPO 目标，不修改优势估计器；仅需额外一次教师前向与 JSD 计算，无外部推理开销。

**关键实验**  
在 7 个 QA 基准（单跳+多跳）上用 Qwen2.5-3B/7B 评测：  
- SD-Search (3B) 平均 EM 0.428，超越所有纯结果奖励基线（如 AutoRefine 0.405），并媲美使用 72B 教师的 Thinker（0.430），无需外部教师。  
- SD-Search (7B) 平均 EM 0.476，比最强结果奖励基线 MR-Search 高 1.6 点，比 Thinker 高 2.4 点。  
- 消融证实：屏蔽未来信息、使用结果标签、保留多滚动对比、JSD 均对性能至关重要；训练开销仅增 15.5%，且搜索次数不变，性能来自查询质量提升。

**核心结论**  
步骤级监督不必来自外部模型，通过事后条件化从策略自身提取即可，为搜索增强推理提供了一种廉价且有效的过程监督替代方案。
