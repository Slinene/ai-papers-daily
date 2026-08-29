---
title: How Language Models Organize and Structure Moral Knowledge
title_zh: 语言模型如何组织与结构道德知识
authors:
- Orion Reblitz-Richardson
arxiv_id: '2608.27402'
url: https://arxiv.org/abs/2608.27402
pdf_url: https://arxiv.org/pdf/2608.27402
published: '2026-08-27'
collected: '2026-08-29'
category: LLM
direction: LLM 表征几何与概念组织
tags:
- linear probes
- moral foundations
- representation geometry
- interpretability
- LLM
one_liner: 用六个线性探针揭示 LLM 中道德基础方向既共享正向共同成分又张成近最大独立维度，且困境方向可部分由基础方向组合
practical_value: '- 在电商意图/评论分析中，可为多个语义维度（如质量、价格、物流、品牌）分别训练线性探针，观察其方向是否既共享正向共同成分又保持独立维度，以判断模型是否具备结构化概念理解而非单点检测。

  - 论文发现概念集成结构在预训练早期就形成，早于探针精度饱和；业务上可在资源有限时直接使用预训练中间层特征构建轻量概念分类器，不必等微调或精度完全收敛。

  - 复杂场景（如“高性价比但售后差”的评论）可视为多个基础属性向量的组合，用其几何关系辅助可解释标签生成、冲突检测或 query 改写。

  - 共享成分可作为多任务学习中的正则信号，避免不同概念任务向量过度隔离或完全坍缩，提升模型对相关语义维度的联合建模能力。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：此前研究将 LLM 的道德编码视为单一二元特征（检测文本是否涉及道德），只验证了模型能发现道德内容，但未考察是否区分不同道德基础并组织其关系。本文进一步追问：模型能否区分 Moral Foundations Theory（MFT）的六类基础，并在表示空间中以几何结构组织它们。

**方法关键点**：在开源 LLM 上训练六个独立线性探针，分别对应 MFT 的 care/harm、fair/cheat、lib/oppress、loy/betray、auth/subv、sanc/degrade 方向。分析这些方向在表示空间中的几何关系，并与匹配的非道德概念探针电池对比。进一步扩展到道德困境表示，考察困境方向是否由基础道德方向组合而成。

**结果**：六个道德方向既不坍缩为单一道德检测器，也不完全正交隔离，而是张成接近最大数量的独立维度，同时共享一个正向共同成分。该共享成分的成对余弦均值为 0.26，远高于非道德概念电池的 0.013，说明其是道德特异性的集成信号。几何结构跨架构和模型规模一致，并在预训练早期即达到集成状态，早于探针精度饱和。未发现 MFT 预测的 individualizing/binding 区分，结构更多反映语料统计。在道德困境中，每个困境方向部分由对应基础方向组合，组合强度是错配基线的 2.7 倍，但大部分方差仍编码冲突特定结构，表明模型表征的是道德张力本身，而非预先解决的判断。
