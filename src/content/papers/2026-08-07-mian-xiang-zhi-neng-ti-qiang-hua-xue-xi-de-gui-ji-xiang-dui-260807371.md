---
title: Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning
title_zh: 面向智能体强化学习的轨迹相对事后蒸馏框架
authors:
- Haoyu Zheng
- Yun Zhu
- Qing Wang
- Wenqiao Zhang
affiliations:
- Zhejiang University
- Shanghai AI Laboratory
- Tencent
arxiv_id: '2608.07371'
url: https://arxiv.org/abs/2608.07371
pdf_url: https://arxiv.org/pdf/2608.07371
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agentic RL · 轨迹相对事后蒸馏
tags:
- Agentic RL
- Hindsight Distillation
- GRPO
- Multi-turn Agent
- Credit Assignment
- Self-Distillation
one_liner: 提出TRIAL，通过轨迹相对事后蒸馏将密集监督按轮次合理分配，显著提升多轮Agent的RL训练效率
practical_value: '- 多轮对话/推荐Agent训练中，可用轨迹相对事后视图提供密集token级信用分配，突破GRPO仅靠结局奖励的局限

  - 事后视图构造方法可迁移：将用户后续反馈（如点击、购买）作为条件化上下文，重评分已生成的推荐回复，获得符号化修正信号

  - 轮次归一化权重（token加权均值=1）确保不改变整体更新强度，仅重新分配监督焦点，易于与现有RL框架（如PPO）集成

  - 训练时引入事后信息，推理阶段无需任何额外模块或开销，适合在线服务部署'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
多轮智能体任务中，GRPO等强化学习方法仅依据最终稀疏奖励分配信用，忽略了各决策轮次的不同贡献。现有事后蒸馏方法虽利用已完成的交互进行回顾，但缺乏跨轮次的校准分配机制，导致密集监督信号未能有效集中在关键决策上。

**方法关键点**
- **轮次对齐事后视图**：对每一决策轮次，抽取该轮次导致的局部结果作为事后证据，构建训练专用的条件化上下文，保持回答token序列不变。
- **双视图评分**：用冻结的快照策略分别在普通上下文和事后增强上下文下计算同一回答的对数概率，其差值给出token级修正方向与强度。
- **轨迹相对轮次分配**：将每轮内绝对对数概率差的均值作为轮次得分，以轨迹中全部合格token数为基准对得分进行归一化，得到轮次权重，且权重满足合格token加权均值为1。权重>1表示该轮次的事后修正幅度高于其token占比。
- **联合优化**：将轮次权重与符号化token差距相乘构建密集事后目标，与GRPO的结局优势损失相加，并通过幅值钳位保持稳定。训练结束后丢弃所有事后组件，推理仅用普通策略。

**关键实验结果**
在WebShop和ALFWorld两个交互环境上，使用Qwen2.5-3B和Qwen3-1.7B，TRIAL在所有8种（模型×环境×指标）组合上均优于GRPO。WebShop成功率从56.4%提升至75.2%（+18.8），任务得分从78.7%提升至85.7%。ALFWorld的Seen和Unseen平均成功率分别领先最强基线3.6和6.0个百分点。控制实验显示，单纯使用均匀权重的事后蒸馏提升有限，而TRIAL的源轮次对齐分配带来额外显著增益。从训练动态可见，随着训练进行，绝对事后差距均值下降，但轮次间权重分布的标准差上升，表明方法自动将监督焦点收缩到变化最大的关键轮次。

**核心洞察**
“TRIAL用轨迹内归一化的轮次权重重新分配事后修正信号，让多轮智能体在训练中自动聚焦于那些被事后证据改变最大的决策，而无需额外奖励塑形。”
