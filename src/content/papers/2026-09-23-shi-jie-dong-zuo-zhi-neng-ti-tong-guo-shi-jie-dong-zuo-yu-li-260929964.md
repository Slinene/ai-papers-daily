---
title: 'World Action Agent: Harnessing VLMs for Robot Manipulation via World Action
  Rehearsal'
title_zh: 世界动作智能体：通过世界动作预演利用 VLM 进行机器人操作
authors:
- Yehang Zhang
- Haojian Huang
- Yifan Chang
- Jianchong Su
- Bohan Zhou
- Yingjie Xu
- Wosong Chen
- Tianhao Zhou
- Chenxu Wang
- Tianyi Zhang
affiliations:
- HKUST(GZ)
- CUHK
- Knowin AI
arxiv_id: '2609.29964'
url: https://arxiv.org/abs/2609.29964
pdf_url: https://arxiv.org/pdf/2609.29964
published: '2026-09-23'
collected: '2026-09-25'
category: MultiAgent
direction: 多智能体机器人操控与技能演化
tags:
- Multi-Agent
- VLM
- Robot Manipulation
- Action Rehearsal
- Skill Evolution
- Fine-tuning
one_liner: 多智能体视觉动作工作空间让 VLM 通过动作预演、视图内修正和技能演化实现机器人操作 SOTA
practical_value: '- 可编辑动作提案与预演机制：在推荐/广告 Agent 中，可让 LLM 先产出候选策略或推荐列表，由 Reviewer/Imagination
  Agent 在低成本模拟中预演，结合离线评估器反馈修订，再决定是否真实上线，降低高风险操作成本。

  - 多智能体分工：把主决策、预演评估、技能检索拆成不同 Agent，例如电商推荐中主 Agent 负责当前会话决策，Skill Agent 检索历史有效策略（选品、话术、促销），避免单一
  Agent 上下文过载。

  - 用交互轨迹蒸馏轻量模型：论文中 harness 轨迹微调将域外成功率从 1.7% 提升到 43.3%，这启示我们可以收集线上 Agent 高质量决策轨迹，蒸馏一个轻量策略模型用于高频、低时延场景，兼顾泛化与成本。

  - 选择性上下文呈现：从场景几何自动挑选与当前交互相关的视图，类似在商品推荐中可以根据用户当前浏览/购物车动态裁剪商品属性、图片切片或用户行为段，减少无关信息对
  VLM 决策的干扰。'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机

通用 VLM 具备广泛知识与空间推理能力，但在机器人操作中，已有系统要么将其作为间接规划器预测约束或生成程序，要么只给 VLM 提供场景视图，缺少一个可行动的世界环境，导致决策与执行脱节、泛化受限。

## 方法关键点

- 构建视觉动作工作空间：自动从场景几何选择 **contact views**，仅呈现当前交互周边区域。
- **动作预演**：将每个动作转化为可编辑提案，由主 Agent 或 Imagination Agent 结合规划反馈预览、修订，再执行。
- **视图内修正**：在观察—预演—底层执行间形成闭环，使 Agent 能在观察到残差偏移的同一视图中修正。
- **技能获取**：从专家视频与人类教学中通过循证审查演化多模态技能，并由 Skill Agent 调用；交互轨迹用于微调较小 VLM。

## 关键结果

在 LIBERO-Pro 上，仅使用 LIBERO-90 演化出的技能，WAA 平均成功率达 **75.6%**，超过端到端 VLA、code-as-policy 方法及同 backbone 的视觉 harness 基线；相同技能无需额外学习即可在 robosuite 上保持有效。用 harness 轨迹微调 Qwen3.5-9B，域外成功率从 **1.7%** 提升至 **43.3%**。
