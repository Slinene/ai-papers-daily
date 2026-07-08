---
title: 'DynaKRAG: A Unified Framework for Learnable Evidence Control in Multi-Hop
  Retrieval-Augmented Generation'
title_zh: DynaKRAG：多跳RAG中可学习证据控制的统一框架
authors:
- Yaqi Wu
- Xiaolei Guo
- Chenyu Zhou
- Jiaqi Huang
- Xianfa Zhang
- Junxu Zhang
- Zhuo Yu
- Zhubo Shi
- Jianghao Lin
- Dongdong Ge
affiliations:
- Shanghai Jiao Tong University
- Shanghai Aircraft Manufacturing Co., Ltd.
- Tongji University
arxiv_id: '2607.06507'
url: https://arxiv.org/abs/2607.06507
pdf_url: https://arxiv.org/pdf/2607.06507
published: '2026-07-07'
collected: '2026-07-08'
category: RAG
direction: 可学习证据控制 · 多跳RAG
tags:
- Multi-Hop RAG
- Learnable Control
- State-Conditioned Policy
- Evidence Operations
- Sufficiency Feedback
- Retrieval Budget
one_liner: 将多跳证据获取构建为状态条件下的原子操作控制问题，通过学习控制器动态选择操作，性能全面超越固定基线。
practical_value: '- **Agent 动作调度借鉴**：在多 Agent 搜索/推荐系统中，可引入状态条件动作空间，动态决定检索、查询改写、证据批判或停止，替代固定管道，提升多步推理任务的效率与效果。

  - **轻量控制器设计**：使用小型 LLM 学习策略控制器，根据当前证据状态选择下一步动作，适合业务中平衡推理能力与延迟，可集成到现有的 LLM-based
  Agent 架构。

  - **充分性反馈机制**：将“当前证据是否足够回答”的判断集成进工作流，避免冗余检索或对话轮次，对电商客服、商品咨询等多轮交互场景有直接降本价值。

  - **检索预算动态分配**：实验表明额外检索并非均匀有益，可根据查询难度动态分配检索次数，对广告召回、搜索排序系统的资源优化有直接指导意义。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机
多跳检索增强生成（RAG）需顺序获取证据，每篇新文档可能揭示缺失事实、桥接实体、查询缺陷或提供充分支持。现有方法将迭代检索、查询改写、证据批判、充分性判断等操作组织在特定管道或预定义拓扑中，未能学习一个共享的、状态条件化的策略来决定当前最有效的证据操作。

## 方法关键点
DynaKRAG 将多跳证据获取形式化为**状态条件控制下的原子证据操作**。每一步，有效性层根据当前状态构建可执行动作集合（如检索、改写、判断充分性、停止），然后**学习到的控制器**选择下一操作并更新证据状态，新状态可能解锁后续新操作。实验基于 Qwen2.5-7B-Instruct 实现。

## 关键结果
- 在 HotpotQA、2Wiki、MuSiQue 上分别取得 **0.5998, 0.5340, 0.3061 的 F1**，全面超越最强受控基线。
- 将学习控制器替换为均匀随机有效策略，F1 下降 **3.96～5.78 点**；去除充分性反馈在所有数据集上均损害性能。
- 控制检索容量的实验表明，额外检索带来的收益并不均匀，验证了动态控制检索预算的必要性。
