---
title: 'UniPath: Adaptive Coordination of Understanding and Generation for Unified
  Multimodal Reasoning'
title_zh: UniPath：统一多模态推理的自适应协调路径框架
authors:
- Hayes Bai
- Yinyi Luo
- Wenwen Wang
- Qingsong Wen
- Jindong Wang
arxiv_id: '2605.11400'
url: https://arxiv.org/abs/2605.11400
pdf_url: https://arxiv.org/pdf/2605.11400
published: '2026-05-12'
collected: '2026-05-17'
category: Multimodal
direction: 统一多模态推理下的自适应路径协调
tags:
- Multimodal
- Reasoning
- Adaptive Coordination
- Path Diversity
- Unified Models
one_liner: 提出自适应利用协调路径多样性，动态选择理解与生成路径，提升统一多模态推理效果
practical_value: '- **自适应路径选择思路可迁移到推荐系统多策略路由**：电商推荐中，不同用户和场景适合不同推荐策略（如协同过滤、内容推荐、热门兜底），可借鉴
  UniPath 的轻量 planner 机制，根据输入特征动态选择执行路径，避免单一固定策略的局限。

  - **多智能体协调可参考路径多样性建模**：在 Agent 协同场景，任务可由不同子 Agent 按顺序或并行完成，路径多样性有助于提高解决复杂问题的成功率。可通过构造路径条件化的执行角色和输入感知的调度器，类似
  UniPath 的 planner，实现自适应 Agent 编排。

  - **生成式推荐中的多模态内容生成可利用协调路径**：商品文案生成可能结合视觉理解（图片特征）和文本推理，UniPath 的路径选择与执行分离架构可帮助平衡视觉与语言模态的贡献，避免固定融合方式导致信息丢失。

  - **可解释性与中间行为监控**：UniPath 产生的可解释中间行为（如视觉思考、假设探索）对业务有参考价值，可在推荐理由生成或智能客服回复中暴露推理步骤，提升用户信任度。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：统一多模态模型（UMMs）需要协调理解与生成能力以完成推理任务，但现有方法要么仅在训练时耦合，要么对全部输入使用固定协调模式，忽略了不同输入所需推理路径的多样性，导致性能受限。

**方法**：提出 UniPath 框架，将任务求解建模为一条从直接回答、文本推理、视觉思考到假设探索的协调路径。首先构建角色对齐的路径轨迹，训练路径条件化的执行器（path-conditioned executor），使其能按指定路径生成答案。然后引入轻量级 planner，根据输入特征动态选择最优路径。planner 与 executor 分离，可在推理时自适应切换路径，无需重训。

**结果**：在多个多模态推理基准上，UniPath 比固定协调策略取得更好表现，同时产生了可解释的中间推理步骤，证明了利用路径多样性的有效性。
