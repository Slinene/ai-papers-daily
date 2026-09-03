---
title: Discriminative World Models for Web Agents
title_zh: 面向 Web Agent 的判别式世界模型
authors:
- Kelvin Li
- Dhruv Pendharkar
- Anish Pahilajani
- Chuyi Shang
- Leon Oks
- Leonid Karlinsky
- Rogerio Feris
- Trevor Darrell
- Roei Herzig
affiliations:
- University of California, Berkeley
- MIT-IBM Watson AI Lab
- Cal Poly San Luis Obispo
- Xero
arxiv_id: '2609.02885'
url: https://arxiv.org/abs/2609.02885
pdf_url: https://arxiv.org/pdf/2609.02885
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: Web Agent 世界模型判别式训练
tags:
- Web Agents
- World Models
- Predicted-State Matching
- PRM
- Action Ranking
one_liner: 用预测状态匹配训练世界模型，使预测表示能区分不同动作结果，提升 PRM 动作排序与端到端任务成功率
practical_value: '- 训练状态模拟器时对齐下游排序目标：不要只做 next-state 重建，应加入判别式目标，使预测状态可区分不同动作的后果。在电商/搜索的
  agent 场景中，若用世界模型模拟用户点击或意图变化，可改用 contrastive 或 ranking loss 训练，以辅助后续动作打分。

  - 构建分支式决策数据集：从真实交互轨迹中记录每个决策点的候选动作及各自后续状态，用于训练判别式世界模型。可借鉴到搜索推荐 agent，通过离线用户日志构造“动作-结果”对比样本，避免昂贵在线探索。

  - PRM/ranker 增强：将世界模型预测的状态表示拼接到 PRM 输入，能比仅用动作特征提升动作排名。在做推荐 agent 的多步决策时，可设计类似的 process
  reward 模型，用预测用户状态辅助评估候选推荐或 query。

  - 测试时采用“候选生成 + 预测状态 + 打分”的 pipeline，可提高端到端成功率。在电商 agent 中可对候选商品或 query 做模拟排序，减少试错。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有 Web 智能体在测试时用世界模型采样候选动作、预测结果网页状态，再交给 ranker 或 Process Reward Model (PRM) 打分排序。但这些世界模型通常通过监督下一状态预测训练，目标是生成忠实快照（如 HTML、AXTree），并不关心预测状态对下游打分是否具有区分性，导致世界模型与 ranker 目标错位。

**方法关键点**：引入 predicted-state matching 训练目标，让预测的表征不仅能还原真实结果状态，还能区分真实结果与替代动作产生的状态。训练数据来自 WebArena Go-Browse 轨迹构造的 branching 数据集，每个决策点包含多个候选动作及其实际结果状态。

**关键结果**：在 held-out 的 predicted-state matching 基准上，该判别式训练目标优于监督下一状态预测；在 WebPRMBench 上，相比仅动作输入的 PRM 和用监督世界模型增强的 PRM，预测状态匹配增强的 PRM 动作排名更准确；在 WebArena-Lite 上，测试时用该世界模型进行动作选择带来端到端任务成功率的提升。
