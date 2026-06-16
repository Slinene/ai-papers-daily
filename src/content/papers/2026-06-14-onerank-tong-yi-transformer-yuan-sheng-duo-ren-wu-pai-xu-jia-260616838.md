---
title: 'OneRank: Unified Transformer-Native Ranking Architecture for Multi-Task Recommendation'
title_zh: OneRank：统一 Transformer 原生多任务排序架构
authors:
- Jiakai Tang
- Sunhao Dai
- Kun Wang
- Zhiluohan Guo
- Yu Zhao
- Cong Fu
- Kangle Wu
- Yabo Ni
- Anxiang Zeng
- Xu Chen
affiliations:
- Renmin University of China
- Shopee
- Nanyang Technological University
- Beijing Key Laboratory of Research on Large Models and Intelligent Governance
arxiv_id: '2606.16838'
url: https://arxiv.org/abs/2606.16838
pdf_url: https://arxiv.org/pdf/2606.16838
published: '2026-06-14'
collected: '2026-06-16'
category: RecSys
direction: 多任务排序 · Transformer 原生架构
tags:
- Multi-Task Learning
- Transformer
- Ranking
- Gradient Detachment
- Candidate-Aware
- Dynamic Scoring
one_liner: 通过任务专用 token、梯度分离与候选感知情境描述符，将多任务推理内建于 Transformer 栈，消除编码器‑预测器分裂。
practical_value: '- **任务专用 token 与梯度隔离**：为每个任务引入可学习 token，配合注意力掩码实现早期特征分离；反向传播时对跨任务注意力进行梯度
  detach，仅保留前向知识迁移，有效缓解跷跷板效应，可直接复用到电商 CTR/CVR/加购等多目标场景。

  - **候选感知情境描述符**：使用可学习的 cross‑attention 聚合整个候选集的分布信息，为每个任务生成全局表示，桥接训练‑服务差异；电商排序中可将其设计为包含
  session 时间、搜索词、用户画像等业务信号的模块，提升列表级排序质量。

  - **动态匹配评分取代静态 MLP 头**：任务全局表示与候选任务表示内积打分，替代多层 MLP，实现 session 级自适应排序；对广告、搜索推荐中需要实时适应上下文（如大促、时段）的业务尤其有价值，且可与现有
  KV‑cache 配合降低在线推理成本。

  - **灵活跨任务信息流配置**：通过注意力掩码实现 parallel、cascade、null、hybrid 等多种跨任务交互模式，工业界可直接根据漏斗关系（click→cart→order）设定单向级联，或让同类任务双向共享，省去复杂的手工建模或搜索。'
score: 10
source: huggingface-daily
depth: full_pdf
---

**动机**
现有 Transformer‑based 多任务推荐仍沿用“编码器→任务无关表示→MLP 预测头”的范式，导致三个结构缺陷：1) 共享表示形成信息瓶颈，迫使下游预测器在容量受限阶段解耦任务差异；2) 共享参数的梯度冲突引发跷跷板现象；3) 注意力驱动的上下文编码与静态前馈预测器的信息读写范式失配，破坏端到端推理。因此，需要一种原生在 Transformer 内部完成多任务推理的统一架构。

**方法关键点**
- **结构化 token 化**：将用户行为序列、检索到的偏好锚序列、候选物品及每任务专属 token 组织为统一序列，并通过互不可见的注意力掩码让各任务 token 仅能 attend 用户上下文和自身候选，实现**早期任务专业化**。
- **候选感知情境描述符（SD）**：引入可学习的 session 级上下文描述符，通过任务专属的多头交叉注意力聚合整个候选集信息，生成每任务的全局表示，弥补训练与在线服务之间的分布鸿沟。
- **跨任务注意力 + 战略梯度 detach**：在前向传播中，通过可配置的注意力掩码（并行、级联、空、混合等）允许任务间信息流动；反向传播时，对非对角线梯度进行 detach，使跨任务注意力退化为**只读知识存储器**，有效消除梯度干扰。
- **动态匹配评分**：用任务全局表示与候选任务表示的内积代替静态 MLP 预测头，使同一用户‑物品对在不同 session 下获得自适应分数；同时采用 InfoNCE 对比损失 + BCE 损失的联合训练。

**实验与结果**
在 Shopee 生产数据集（30 天，33M 用户，26.6B 曝光，涵盖点击/加购/下单）上，OneRank 显著优于 DNN+MMoE/PLE/ResFlow 及 Transformer 基线（MTGR、OneTrans）。与 OneTrans+ResFlow 相比，下单 GAUC 提升约 0.63%，加购 AUC 提升 0.91%，模型参数量仅 4.9M，计算量 1.0G FLOPs，性价比突出。7 天在线 A/B 测试中，GMV/UU 提升 +1.01%，广告收入 +0.81%，坏查询率下降 2.29%。消融实验证实：移除任务专用 token 导致加购 AUC 下降 0.39%，移除候选感知描述符使点击 AUC 降至 0.7872（全量 0.7910），梯度 detach 对稳定性贡献明显。

**最值得记住的一句话**
“OneRank 将多任务推理的‘记忆’与‘优化’解耦：前向让任务读到彼此表示以实现知识迁移，反向通过梯度截断阻止干扰，从而在统一的 Transformer 栈内实现稳且强的多目标排序。”
