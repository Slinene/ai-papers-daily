---
title: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
title_zh: 带采样示例的在线策略自蒸馏降低输出多样性
authors:
- Andrei Liviu Nicolicioiu
- Mohammad Pezeshki
- Aaron Courville
arxiv_id: '2606.26091'
url: https://arxiv.org/abs/2606.26091
pdf_url: https://arxiv.org/pdf/2606.26091
published: '2026-06-24'
collected: '2026-06-25'
category: Training
direction: LLM 训练 · 自蒸馏与多样性偏差
tags:
- Self-Distillation
- On-Policy
- Diversity
- LLM
- Reinforcement Learning
- Mode Collapse
one_liner: 揭示在线自蒸馏因条件于采样示例而放大模型偏差，导致输出多样性锐减和 pass@k 性能饱和
practical_value: '- **监控 pass@k 与多样性指标**：在电商文案生成、搜索查询扩展等实际 LLM 应用中，若使用在线自蒸馏（如 SDPO、SDFT），必须同时监控
  distinct-n、pass@k 等指标，避免模型陷入单一高置信模式，失去从多样生成中获益的可能。

  - **引入多样性正则化或温度调节**：可在自蒸馏损失中加入基于熵的正则项，或适当调高采样温度，以保持策略的概率质量不过度集中，有助于在推荐理由生成、对话式推荐等场景保留多样性。

  - **Agent 规划中慎用纯自蒸馏微调**：在需要多种推理路径或工具调用策略的 Agent 系统中，单纯依赖在线自蒸馏可能导致策略趋同，降低对分布外场景的适应力；可结合
  RL 或增加策略蒸馏的多样性约束。

  - **用互信息视角诊断模式坍塌**：论文给出的理论工具——条件互信息倾斜——可用于分析其他蒸馏范式下的多样性损失，为设计新的训练算法提供方向。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
在线自蒸馏（如 SDPO、SDFT、OPSD）让模型同时扮演教师与学生，教师通过条件于一条正确解法来评估学生生成，提供密集 token 级反馈，在多项 QA 任务上取得强 pass@1 性能。但作者发现，这种范式会显著降低输出的功能多样性与语义多样性，导致 pass@k 曲线平坦——生成更多候选也无法提升准确率，揭示了隐藏在强平均性能下的模式坍塌风险。

**方法关键点**  
1. **偏差溯源**：教师模型在评分时预置一条采样的正确 rollout，其反馈将模型自身的概率偏好传导给学生，放大了已有模式之间的概率差距。  
2. **理论分析**：推导出最优自蒸馏策略等价于用学生输出与正确上下文间的逐点条件互信息对基分布进行倾斜，而理想在线 RL 则能保序地保留等正确输出的概率比。自蒸馏因此会将概率质量集中在已经占优的模式上。

**关键结果**  
- 在图路径寻找与科学问答数据集上，自蒸馏模型 pass@1 匹配或超过 RL，但功能多样性（如不同路径数）和语义多样性（如答案簇数）大幅降低。  
- 在需要多样化策略的分布外测试中，自蒸馏模型显著弱于 RL 基线，证明多样性缺失直接损害泛化能力。
