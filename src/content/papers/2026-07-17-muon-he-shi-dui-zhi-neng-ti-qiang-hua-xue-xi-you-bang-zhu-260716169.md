---
title: When Does Muon Help Agentic Reinforcement Learning?
title_zh: Muon 何时对智能体强化学习有帮助？
authors:
- Kai Ruan
- Jinghao Lin
- Zihe Huang
- Ziqi Zhou
- Qianshan Wei
- Xuan Wang
- Hao Sun
affiliations:
- Renmin University of China
- Institute of Computing Technology, Chinese Academy of Sciences
- Duke University
- Institute of Automation, Chinese Academy of Sciences
- Zhejiang University
arxiv_id: '2607.16169'
url: https://arxiv.org/abs/2607.16169
pdf_url: https://arxiv.org/pdf/2607.16169
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 智能体 RL 的优化器选择与联合调参
tags:
- Muon
- AgenticRL
- GRPO
- GiGPO
- optimizer
- learning rate
one_liner: 稀疏奖励智能体 RL 中，Muon 仅作用于隐藏矩阵，在低学习率下使成功率最高达 0.901，远超 AdamW
practical_value: '- 在 LLM 驱动的智能体决策任务（如多轮对话推荐、搜索 Agent）中，可尝试用 Muon 替代 AdamW 进行 RL 微调，尤其只对
  Transformer 隐藏权重矩阵应用，以避免全参数替换带来的灾难性遗忘。

  - 低学习率（如 1e-5）是 Muon 发挥优势的关键，联合调整 advantage estimator 和优化器能显著提升策略学习效率，实现在线推荐场景下更早达到可用成功率。

  - Muon 避免了元素级自适应状态，内存开销更低，适合需要在有限资源下进行实时策略更新的在线推荐系统。

  - 目前是单 seed 探索，但的提升幅度（+88%~460%）值得在业务中做多 seed 消融实验，验证其在商品搜索、内容推荐等稀疏奖励任务中的稳定性。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：Muon 在大规模预训练中能以约 52% 的 FLOPs 匹配 AdamW 的损失，但将其用于 RL 后训练的效果未知。现有报告结果不一，且存在优化器不匹配导致的遗忘问题。本研究在稀疏奖励的智能体环境 ALFWorld 中，系统评估 Muon 对策略优化的影响。

**方法**：使用 Qwen2.5-0.5B-Instruct，在 GiGPO 框架下，仅对 Transformer 的隐藏权重矩阵应用 Muon，其余参数保持 AdamW。对比了不同 advantage estimator（GRPO、GraphGPO）和学习率（3e-5, 1e-5）的组合，以最终窗口验证成功率和归一化 AUC 作为指标。

**关键结果**：AdamW 在高学习率下完全失效（成功率为 0），而 Muon 在 GiGPO 下将成功率从 0.290 提升至 0.546（+88%）。低学习率 1e-5 时，GraphGPO + Muon 达到 0.901 成功率，归一化 AUC 从 0.399 升至 0.556，并且分别提前 30 步和 60 步达到 0.5 和 0.75 成功率。效果高度依赖 advantage estimator 与学习率的协同选择。
