---
title: 'Visual Para-Thinker++: A Single-Policy Multi-Agent Framework for Visual Reasoning'
title_zh: 视觉并行思维者++：单策略多智能体视觉推理框架
authors:
- Haoran Xu
- Hongyu Wang
- Yifei Gao
- Jiaze Li
- Zizhao Tong
- Xiaofeng Zhang
- Xiaosong Yuan
affiliations:
- Zhejiang University
- Hunan University
- Tianjin University
- University of Chinese Academy of Sciences
- Shanghai Jiao Tong University
arxiv_id: '2606.09290'
url: https://arxiv.org/abs/2606.09290
pdf_url: https://arxiv.org/pdf/2606.09290
published: '2026-06-07'
collected: '2026-06-12'
category: MultiAgent
direction: 多模态多智能体协作与推理优化
tags:
- Multi-Agent
- Visual Reasoning
- Role-Decoupled Optimization
- Single-Policy
- KV Cache Reuse
- Hallucination Reduction
one_liner: 提出单策略多智能体视觉推理系统，通过角色解耦优化和KV缓存复用减少幻觉，在六大基准上超越单轨迹方法。
practical_value: '- 多 Agent 单策略架构：一个大模型通过角色词元条件化为多个子 agent，共享权重，降低部署成本，适合电商推荐系统中的多任务协作（如意图识别、对话管理、商品推荐）。

  - 角色解耦优势分配：将不同角色的奖励和优势仅作用于对应词元段，避免梯度冲突。在推荐 Agent 中，可对规划、执行、总结模块分别设计奖励信号，精细优化。

  - 固定任务分配模式：定义了两种固定分配模式（分块和扫描序），避免开放式规划的不稳定性。在商品搜索与推荐任务中，可以预定义子任务划分（如属性识别、价格比较、用户评论分析）来提升并行推理可靠性。

  - KV 缓存复用推理引擎：通过共享视觉前缀并分叉生成 Worker 序列，显著降低多 Agent 推理的显存和时间开销，适合在线推理场景，可应用于多路召回或并行探索的推荐系统。'
score: 8
source: huggingface-daily
depth: full_pdf
---

视觉推理往往需要整合分布在图像不同区域、属性和关系中的证据，传统的单链思维容易过早锁定某种感知解释，延长思考链反而会加剧这种偏向，从而导致幻觉。为此，本文提出**Visual Para-Thinker++**，一个单策略多智能体框架，将同一个多模态大模型（MLLM）通过**角色词元条件化**为三种代理：**主代理**（任务分解）、**工人代理**（并行证据收集）和**总结代理**（综合回复）。

**方法设计上**：主代理采用两种固定任务分配模式——**块状分割**（将图像划分为四个独立象限，分别分派给工人代理）与**扫描序**（每个工人以不同遍历顺序观察全图）；工人代理在**上下文隔离**下独立推理，防止相互复制；总结代理可看到全部工人推理轨迹，实现**轨迹级证据调和**而非简单多数投票。训练分为两阶段：**(1) 多智能体能力注入**，通过带上下文掩码的 SFT 让共享策略学会不同角色；**(2) 角色解耦多智能体优化**，为每个工人设计局部奖励（基于多数投票），为总结代理设计结局奖励，并通过**按词元段分配优势**（工人段仅叠加自身优势）来解耦梯度，避免局部信号与全局信号的冲突。推理时配合**原生多智能体引擎**，复用视觉前缀的 KV 缓存，大幅降低多路径并行开销。

**实验结果**：在 V*（高分辨率搜索）、CountBench、Pixmo（精确计数）、MMVP（细粒度感知）、RefCOCO 系列（指称表达定位）和 HallusionBench（幻觉诊断）六个基准上，3B 模型的感知与幻觉平均分从 Qwen2.5-VL 基线的 57.7 提升至 71.2（+13.5），计数平均从 50.1 升至 60.7，其中 HallusionBench 提升 7.9。7B 模型同样全面超越单轨迹长链、自一致性、多智能体辩论等基线。消融实验证实角色解耦优势与工人奖励互补，四个工人代理达到成本-准确率最优。

**核心价值**：单策略多角色合作+解耦优势优化，为视觉推理提供了一条有效减少幻觉的新路径，其设计理念可迁移至需要并行探索与证据整合的其他多智能体系统。
