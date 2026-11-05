---
title: 'Turns Matter: Advancing Streaming Video RL via Turn-Level Credit'
title_zh: 轮次很重要：通过回合级信用推进流式视频强化学习
authors:
- Shuai Dong
- Kanghui Tian
- Linghan Chen
- Wenqi Shao
- Hongrui Wu
- Haowen Hou
- Yongfu Zhu
- Xuehui Wang
- Ziyue Wang
- Wenpu Liu
affiliations:
- Fudan University
- Shanghai Innovation Institute
- JD.com
- Stanford University
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2611.06728'
url: https://arxiv.org/abs/2611.06728
pdf_url: https://arxiv.org/pdf/2611.06728
published: '2026-11-03'
collected: '2026-11-05'
category: Training
direction: 流式视频理解 · 回合级强化学习
tags:
- Streaming Video
- GRPO
- Credit Assignment
- RLHF
- Multi-turn Decision
- Video Understanding
one_liner: 提出 TurnWise 回合级 GRPO 框架，用回合级信用分配和回合均值策略优化提升流式视频理解
practical_value: '- **可迁移到对话式推荐 / 实时交互决策**：在用户 session 中模型每一步需要决定继续收集信息还是给出推荐，使用回合级
  credit assignment 替代整条 trajectory 共享 advantage，能减少重复回复、鼓励失败后的有效跟进，适合流式推荐与实时广告决策。

  - **Turn-mean 策略优化解决长短动作权重失衡**：先对每个 turn 内 token loss 平均，再跨 turns 平均，使“等待/观察”与“生成回答”等不同长度的决策获得相等权重；在对话推荐中可避免长推荐文案主导梯度。

  - **工程实现成本低**：无需 learned critic 或额外 rollouts，可直接嵌入已有 GRPO 训练流程；适合在已使用 GRPO 的 LLM
  多轮交互系统里快速验证。

  - **前缀补全打分的剩余回报思路**：借鉴 silence-completed prefix scoring，可在电商场景中为未完成的用户会话构建价值估计，用于早期终止或动态推送决策。'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
流式视频理解要求模型在观测到达过程中反复决定是继续等待还是立即回答。现有 GRPO 方法虽改进了奖励设计，但始终在整条 trajectory 上共享同一个 advantage，导致早期成功后容易强化冗余回复，早期失败后又会抑制后续有价值的跟进回答。核心问题是轨迹级反馈与回合级交互不匹配。

## 方法关键点
TurnWise 提出两个互补设计：
- **Turn-level credit assignment**：使用 silence-completed prefix scoring 为每个决策构造剩余回报，再用组相对 advantage 分离各决策的学习信号，避免与之前奖励耦合。
- **Turn-mean policy optimization**：先在每个 turn 内对 token loss 取平均，再跨 turns 取平均，使响应与等待决策无论输出长度都获得等权重。

这些设计不依赖 learned critic，也不需要额外 rollouts，可直接融入 GRPO。

## 关键结果
在流式视频理解基准上，TurnWise 优于现有 RL 方法，具体提升了信息量并减少了冗余回复，验证了回合级信用分配与均值优化的有效性。
