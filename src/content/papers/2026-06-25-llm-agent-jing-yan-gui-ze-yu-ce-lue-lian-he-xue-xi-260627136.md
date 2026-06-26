---
title: Joint Learning of Experiential Rules and Policies for Large Language Model
  Agents
title_zh: LLM Agent 经验规则与策略联合学习
authors:
- Shicheng Ye
- Chao Yu
affiliations:
- Sun Yat-sen University
arxiv_id: '2606.27136'
url: https://arxiv.org/abs/2606.27136
pdf_url: https://arxiv.org/pdf/2606.27136
published: '2026-06-25'
collected: '2026-06-26'
category: Agent
direction: LLM Agent 经验复用 · 规则增强强化学习
tags:
- LLM Agent
- Reinforcement Learning
- Experiential Rules
- GRPO
- LoRA
- Interactive Decision Making
one_liner: JERP联合更新经验规则池和策略参数，在多步交互任务上超越纯RL基线
practical_value: '- 多步交互Agent（如对话导购）可维护规则池（如“先确认场景再推荐”），与模型RL训练同步更新，避免规则过时。

  - 规则更新采用对比反思式生成：提供成功/失败轨迹给LLM，自动产出规则编辑操作（ADD/EDIT/UPVOTE/DOWNVOTE/MERGE），工程上可用固定模板解析，实现自动化规则管理。

  - 规则效用评分机制与容量限制剪枝，确保规则池在在线学习中规模可控、质量可维护。

  - 同批轨迹两次利用（策略更新、规则更新）提高数据效率；可与LoRA等参数高效微调结合，降低训练资源开销。'
score: 10
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
LLM Agent在多步交互任务中需要利用历史经验提高决策能力。现有方法要么将经验外化为自然语言规则（如Reflexion、ExpeL），但规则随策略变化可能过时；要么仅用RL更新参数（如GRPO），但在稀疏奖励下局部错误难以及时纠正。JERP旨在融合两种经验使用方式，在同一训练循环中更新规则池和策略参数。

**方法**  
- 为每个任务维护长期经验规则池，每条规则由自然语言内容和效用分数组成。每回合选分数最高的top-k规则作为工作规则注入prompt。  
- 阶段一（策略更新）：对采样轨迹组计算组相对优势，使用GRPO目标更新LoRA参数。  
- 阶段二（规则更新）：基于当前轨迹组、参考成功轨迹和现有规则池，调用冻结LLM生成结构化编辑操作（ADD/EDIT/UPVOTE/DOWNVOTE/MERGE），更新规则文本与分数，低分规则被裁剪。  
- 更新后的规则池用于后续episode，实现与策略共同演进。

**关键结果**  
在AlfWorld（6类家务任务）和WebShop（在线购物）上使用LoRA微调，对比Vanilla LLM、ReAct、Reflexion、RLOO、GRPO。JERP在AlfWorld整体成功率61.5%（GRPO 57.8%），在Clean/Heat/Cool/Pick2等约束密集任务上提升更明显；WebShop平均分79.0，成功率64.1%，均优于GRPO和RLOO。消融实验表明冻结规则池会导致后期训练收益停滞。
