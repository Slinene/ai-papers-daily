---
title: 'Route Anything: A Study of Model and Policy Routing for General-Purpose AI
  Systems'
title_zh: 路由任意：通用AI系统模型与策略路由研究
authors:
- Pengfei Zhou
- Yixing Ma
- Hexin Wang
- Weidong Tang
- Zhenglin Wan
- Wangbo Zhao
- Yang You
affiliations:
- National University of Singapore, HPC-AI Lab
- InfRec, Cardinal AI Lab
- University of California, Berkeley
- Hong Kong University of Science and Technology
arxiv_id: '2611.05275'
url: https://arxiv.org/abs/2611.05275
pdf_url: https://arxiv.org/pdf/2611.05275
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: 模型路由 · 多模态质量成本权衡
tags:
- model routing
- multi-modal
- quality-cost trade-off
- learned router
- general-purpose AI
one_liner: 构建覆盖25个基准374k轨迹的omni-modal路由框架，证明学习路由器超最佳固定候选并提升效率8.82倍
practical_value: '- 在推荐/搜索系统中维护多个候选模型（如轻量双塔、深度交叉、LLM排序器），训练一个轻量路由器（小型MLP或XGBoost）基于用户/物品特征、上下文及模型置信度动态选择，论文证明输入信息充分时学习路由器接近oracle上限，同时平均效率提升8.82倍。

  - 搭建离线路由评估流程：对历史流量样本离线运行全部候选模型，记录质量分与延迟/成本，形成trajectory matrix，再训练路由器，可安全评估新模型加入后的整体收益，避免直接全量替换风险。

  - 将路由用于Agent工具/策略选择：在电商对话助手中，根据用户query意图、语义和上下文路由到不同工具链或生成策略，降低昂贵LLM调用次数同时保持质量。

  - 关注路由器输入特征设计：理论表明路由器可获得的信息决定可达性能，实用中可加入模型预测分布熵、历史表现等信号，而不只是原始输入特征。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
构建通用AI系统需要编排异构专家模型/策略，核心挑战是如何动态路由到最佳候选，平衡质量与成本。

**方法关键点**  
提出Route Anything框架，建立统一理论刻画质量-成本权衡下最优路由，并构建omni-modal trajectory matrix：25个基准、452个候选配置、374,401次评分运行，覆盖语言理解、图像/视频/语音生成、编码与工作代理、机器人操作。基于该矩阵训练多种路由器，系统研究全模态路由潜力、学习路由器能力及路由增效条件。

**关键结果**  
per-input oracle路由比最佳固定候选高5.4分；学习路由器在16个基准上超最佳固定候选0.3分，视频生成高2.1分，机器人操作高1.1分，同时减少24%策略时间。相比参考模型，路由平均效率提升8.82倍，编码任务25.5倍，文本问答7.1倍。
