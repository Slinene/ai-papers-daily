---
title: 'When Semantics Fall Short: Persona-Guided Cross-Domain Sequential Recommendation
  with Large Language Models'
title_zh: 语义不足时：用户画像引导的跨域序列推荐
authors:
- Jundong Chen
- Honglei Zhang
- Shuai An
- Enneng Yang
- Han Yu
affiliations:
- 北京交通大学
- 中山大学
- 南洋理工大学
arxiv_id: '2610.25221'
url: https://arxiv.org/abs/2610.25221
pdf_url: https://arxiv.org/pdf/2610.25221
published: '2026-10-18'
collected: '2026-10-20'
category: RecSys
direction: 跨域序列推荐 · LLM 用户画像引导
tags:
- Cross-Domain Sequential Recommendation
- LLM
- Persona
- Semantic Association
- Contrastive Learning
- Amazon
one_liner: 用 LLM 推断用户画像作为全局引导替代跨域语义桥接，结合本地语义关联提升跨域序列推荐
practical_value: '- 跨域/多场景推荐中，避免全局 item 语义对齐；用 LLM 从用户混合行为序列推断 persona（输出 why 而非 what，提示词约束不提具体
  item/brand/domain），作为跨域行为建模的全局引导信号，可作为多域用户表示的统一先验。

  - 行为与语义表示分离：跨域共享行为 embedding 随机初始化、与混合序列联合训练，避免语义域隔离；冻结的 item 语义 embedding 只用于域内局部邻域正则和域偏好分支，最后通过可学习
  gate 自适应融合。工程上可离线预计算 persona 和语义 embedding，不增加在线推理成本。

  - 辅助损失设计：Local Semantic Association 对每个 item 取 Top-K 语义邻域，回归语义相似度与行为相似度；Global Persona
  Guidance 使用 persona-aware attention 对序列隐藏态加权，做用户级对比学习。两项都是轻量插件，可加到现有 Transformer
  序列模型。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

现有 LLM 增强的跨域序列推荐（CDSR）普遍采用 item-centric 的全局语义桥接，即用 LLM 生成 item 语义表示并在域间对齐。但存在两个问题：semantic domain isolation（不同域 item 语义属性天然不同，如 Kitchen 功能性描述 vs Food 品类口味）和 semantic-behavior inconsistency（跨域行为常发生在语义无关物品之间，而语义相似性在域内才与行为一致）。因此需要转向 user-centric。

方法关键点：
- PerCDR 框架三阶段：LLM 驱动表示构建、联合行为建模、域偏好适应。
- 用 LLM 推理从用户混合域交互序列推断 persona（输出 why，不提具体 item/brand/domain），用 LLM embedding 生成 persona anchor；同时用 embedding 模型冻结 item 语义向量。
- 联合行为建模：学习可训练的行为 embedding 和共享序列编码器；Local Semantic Association（LSA）对每个 item 取 Top-K 语义邻域，回归语义相似度和行为相似度，仅增强域内；Global Persona Guidance（GPG）通过 persona-aware attention 对序列隐藏态加权，做 weighted contrastive learning 对齐同一用户 persona，推开其他用户 persona。
- 域偏好适应：单域语义分支用独立编码器得到域偏好分数，通过 gating 网络融合到联合分数，可学习系数逐步引入域偏好。所有 LLM 表示离线预计算，训练时冻结。

关键实验：三个 Amazon cross-domain 数据集 CD-Movie、Food-Kitchen、Cloth-Sport。基线包括 GRU4Rec、BERT4Rec、SASRec、CD-SASRec、C2DSR、Tri-CDR、UniSRec、CTT、LLM4CDSR、SemaCDR。PerCDR 在所有数据集上 HR@10 和 NDCG@10 均优于最强基线 SemaCDR，HR@10 提升 2.04%-8.77%，NDCG@10 提升 4.30%-15.40%。消融显示去除联合行为建模下降最大；LSA 邻域过大（K=500）会导致嵌入退回域特定簇，验证局部语义优于全局桥接。
