---
title: 'TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon
  Agent Training'
title_zh: TurnOPD：让在策略蒸馏感知轮次以实现高效长时智能体训练
authors:
- Yuhang Zhou
- Kai Zheng
- Haoling Li
- Dengyun Peng
- Can Xu
- Jingjing Chen
affiliations:
- 复旦大学
- 腾讯混元
arxiv_id: '2607.05804'
url: https://arxiv.org/abs/2607.05804
pdf_url: https://arxiv.org/pdf/2607.05804
published: '2026-07-06'
collected: '2026-07-09'
category: Agent
direction: 在策略蒸馏的轮次感知预算优化
tags:
- on-policy distillation
- long-horizon agent
- turn-aware budgeting
- adaptive rollout
- KL supervision
- training efficiency
one_liner: 通过轮次级预算策略解决长时智能体训练中全轮次 rollout 浪费与令牌级损失偏向浅层的问题
practical_value: '- **自适应 rollout 深度**：可借鉴到电商对话 Agent 训练，当模型在多轮交互中已产生足够确定性决策时提前终止
  rollout，节省推理时间，适合在线学习场景。

  - **渐进式轮次归一化损失**：解决序列开头 token 损失占比过高的问题，让训练更关注中后段的关键决策点，适用于需要多步工具调用或搜索推理的推荐/购物助手
  Agent。

  - **探针统计指导预算分配**：通过简单探测动作分布决定是否继续 rollout，这一思路可复用到流式训练资源调度中，动态决定分配给不同样本的计算量。

  - **基于壁钟时间的公平比较**：该评估方式对业务系统有启示，实际部署更关心训练时间而非采样数，优化壁钟效率比仅看样本效率更有工程价值。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：在长时智能体任务中，标准的在策略蒸馏（OPD）存在两个低效问题：(1) 全轮次 rollout 会消耗大量壁钟时间在尾部轮次上，这些轮次往往提供弱且嘈杂的 KL 监督；(2) 轨迹级 KL 目标将大部分损失集中在初始的浅层令牌，导致深层决策轮次训练不足，模型只在早期行为对齐后就停止优化。

**方法**：提出 TurnOPD，一种轮次级预算策略，包含两个控制器：(1) 自适应 rollout 深度预算，利用基于探针的轮次统计（如动作分布的熵）来决定何时提前终止 rollout，避免无价值的尾部采样；(2) 渐进式轮次归一化损失预算，在训练过程中逐步将 KL 权重从令牌级平滑过渡到轮次均衡，从而平衡不同深度的监督信号，强制模型关注多轮决策中的关键步骤。

**结果**：在 ALFWorld、WebShop 和 Multi-Hop Search 三个长时智能体基准上，TurnOPD 在使用相同壁钟训练预算的条件下获得了更优的验证准确率，并将准确率-时间前沿推至 vanilla OPD 之上。消融实验验证了两个预算控制器的独立贡献。
