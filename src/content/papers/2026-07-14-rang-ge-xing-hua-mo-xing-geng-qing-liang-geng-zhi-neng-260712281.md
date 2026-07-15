---
title: 'SlimPer: Make Personalization Model Slim and Smart'
title_zh: 让个性化模型更轻量更智能
authors:
- Siqi Wang
- Xianjie Chen
- Shaofeng Deng
- Albert Chen
- Romil Shah
- Jiawei Huang
- Zhaoqin Wang
- Zhang Zhang
- Yiqun Liu
- Meilei Jiang
arxiv_id: '2607.12281'
url: https://arxiv.org/abs/2607.12281
pdf_url: https://arxiv.org/pdf/2607.12281
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 个性化排序模型轻量化与深度缩放
tags:
- personalization
- transformer
- scalability
- user modeling
- Instagram
- recommendation
one_liner: 将个性化排序重构为紧凑知识库的迭代精炼，实现 O(N) 每层成本，解耦深度与用户历史长度
practical_value: '- **紧凑中间表示解耦深度与序列长度**：借鉴 SlimPer 固定大小的知识库表示，在电商推荐中可串联更深网络而不显着增加计算与内存，便于扩展更细粒度的用户行为建模。

  - **请求级优化共享用户特征**：对同一请求中多个候选商品，只维护一份用户侧 token，大幅减少显存占用，适合高并发在线广告/推荐服务。

  - **显式多模态匹配打分**：在注意力中直接计算用户与商品 token 的匹配分数，可迁移到搜索广告中，在粗排或精排阶段提供可解释的相关性信号。

  - **统一稀疏稠密序列特征**：将账户画像、实时行为与长期序列统一 backone 处理，简化特征工程与模型部署，适合大促场景下多类型特征快速融合。'
score: 10
source: arxiv-cs.IR
depth: abstract
---

**动机**：Transformer 应用于推荐，生成式假设导致中间张量随序列长度二次增长，但推荐仅需输出单个相关性分数，无需 token 级自回归监督。现有模型深度与用户历史长度强耦合，限制了更深网络和大规模历史的使用。

**方法**：提出 SlimPer，将个性化排序视为迭代精炼一个紧凑的 <用户, 物品> 知识库。每层：① 从用户侧原始多模态 token 中显式计算与当前知识库的匹配分数，选择性关注；② 用匹配结果更新知识库；③ 知识库维度固定，每层复杂度 O(N)（N 为用户 token 数）。深度由此与历史长度解耦。推理时共享一份用户 token 的单副本给所有候选物品，内存随用户数而非物品数增长。

**结果**：部署于 Instagram Reels 与 Feed，用户参与度明显提升，同时系统简化，能有效建模超过 1 万条细粒度用户历史事件，实现更深理解而不成比例增加算力。
