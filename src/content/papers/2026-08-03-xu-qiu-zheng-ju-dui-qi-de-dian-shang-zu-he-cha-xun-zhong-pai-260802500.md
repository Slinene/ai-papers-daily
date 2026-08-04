---
title: Requirement--Evidence Alignment for Compositional E-Commerce Queries
title_zh: 需求-证据对齐的电商组合查询重排序框架
authors:
- Weihao Shen
- Wei Chen
- Fuwei Zhang
- Meng Yuan
- Yuqin Lan
- Guojun Liu
- Qingsong Hua
- Wei Lin
- Fuzhen Zhuang
affiliations:
- Beihang University
- Meituan
arxiv_id: '2608.02500'
url: https://arxiv.org/abs/2608.02500
pdf_url: https://arxiv.org/pdf/2608.02500
published: '2026-08-03'
collected: '2026-08-04'
category: RecSys
direction: 需求感知的重排序优化
tags:
- Compositional Query
- Requirement Alignment
- Evidence Grounding
- R-GRPO
- E-Commerce Reranking
- Near Miss
one_liner: 将查询需求与商品证据显式对齐，通过需求感知分组策略优化，大幅减少组合查询中的近线失误
practical_value: '- 查询结构化：可将用户查询拆解为类型化的需求原子（类型、操作符、值、强度、证据要求），作为排序模型的显式输入特征

  - 证据对齐可作为排序信号：用确定性验证器对比需求与商品属性，给出满足/违反/未支持的三态标记，并将其压缩为紧凑向量，输入重排模型，提供可解释的排序依据

  - 优化目标设计：在列表效用中集成需求满足度、证据覆盖率、违规惩罚，利用 R‑GRPO 直接针对组合查询中的约束满足进行策略优化，可迁移到电商推荐排序的强化学习框架

  - 软硬需求区分：区分硬约束与软偏好，仅对违反硬需求进行惩罚，而对缺失证据的商品不直接降级，这种设计避免误杀，适合处理商品信息不全的场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商查询常包含多个约束（预算、属性、排除项等），传统重排序仅依据主题相关性，导致“近线失误”（near miss）——语义相似但不符合硬约束的商品占优，真正可用的商品却被排在后面。这种相关性-需求错配源于聚合式相关性监督无法区分满足与违反具体需求。

**方法关键点**：
- 需求-证据表示：将查询解析为类型化需求原子 `(type, op, value, strength, evidence_flag)`，利用商品可见属性通过确定性验证器判断每条需求是满足、违反还是未支持，并压缩为商品级状态向量。
- 需求针对性对比：为每个候选构建训练信号 `(relevance, satisfaction, evidence, violation, role)`，角色包括正例、预算超支、证据缺失、违规等，形成需求导向的难负样本。
- 需求感知列表效用：奖励由四部分构成——源相关性、需求满足度、证据覆盖率、违规惩罚，并加入格式有效性惩罚。
- R‑GRPO 优化：在分组相对策略优化框架内，用需求感知奖励替代单纯的相关性奖励，使模型直接学习区分可行商品与近线失误。

**关键实验**：在 Shop‑Need 和 KS‑Need 两个固定池重排序基准上，R‑GRPO 相比 relevance‑only GRPO 在 NDCG@10 上分别提升 11.4pp 和 1.24pp，Violation@5 降低 3.1% 和 1.54%；消融实验证实需求图、证据卡及各奖励通道的互补作用；在复杂查询上收益最大，兼容性类查询 NDCG@10 提升达 20.3pp。
