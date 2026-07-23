---
title: 'TSGR: Taobao Search Generative Retrieval'
title_zh: TSGR：将业务价值感知引入淘宝搜索生成式检索的统一框架
authors:
- Tianyu Zhan
- Gui Ling
- Tong Xiong
- Kunhai Lin
- Yang Wang
- Kaixuan Zhang
- Zhihong Chen
- Yuliang Yan
- Dan Ou
- Shengyu Zhang
affiliations:
- 浙江大学
- 淘宝天猫集团
arxiv_id: '2607.18796'
url: https://arxiv.org/abs/2607.18796
pdf_url: https://arxiv.org/pdf/2607.18796
published: '2026-07-21'
collected: '2026-07-23'
category: GenRec
direction: 生成式检索 · 价值感知排序
tags:
- Generative Retrieval
- Semantic ID
- Business Value
- Query-aware SID
- Value-aware Ranking
- E-commerce Search
one_liner: 查询感知并行Semantic ID与价值感知排序模块让单一模型兼具召回与粗排，离线HR@1000提升9.16%，线上GMV+1.64%
practical_value: '- **查询感知并行SID**：利用query-item点击统计构建多路并行排序码本，同一物品在不同查询下获得不同token索引，可迁移到需要意图感知的生成式推荐/搜索中，提升长尾查询的召回精准度。

  - **召回粗排一体化**：VRM 从生成式骨干的隐藏态提取用户表示，通过交叉注意力融合 item side-info 直接输出价值分数，避免了独立粗排模型带来的目标错位和额外延迟，适合对延迟敏感的在线系统。

  - **分级训练策略**：Pre-SFT 多任务预训练（编码、检索、推荐、协同）激活各项能力，再使用加权多正样本 SFT（pay > click > pv）对齐业务目标，能够稳定训练并降低数据需求，可直接应用于其他业务场景的生成式模型训练。

  - **工程化部署**：通过前缀树约束前两层 SID 解码，动态 beam search 与 VRM 即时计算价值分，将推理延迟控制在 65ms 以内，为工业级生成式检索的在线部署提供了可行的架构参考。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
工业电商搜索中，生成式检索（GR）虽能端到端生成语义 ID，但对物品的商业价值（点击、转化、GMV）不敏感。现有 SID 构建缺乏价值信号，候选排序仅依赖生成概率，导致高价值物品在召回阶段即被漏排，严重影响下游商业效果。淘宝搜索的业务目标驱动设计亟需将价值感知嵌入 GR 框架，同时弥合召回与粗排的目标割裂。

**方法关键点**  
- **查询感知并行 SID (QP-SID)**：在物品语义码本（类别+聚类先验）之上，构建多路并行效率码本。每个簇内按默认点击量排序，并基于 query-term-cluster 统计生成 3 个查询条件排序，高价值且查询相关的物品被分配更靠前的 token 索引；训练时根据 query 自动选择最匹配的排序路径，实现动态、价值感知的 SID 表示。  
- **价值感知排序模块 (VRM)**：复用生成式骨干的隐藏态提取用户表示，通过交叉注意力融合候选物品的 side-info（行为统计、类别、卖家、query-item 共现）、物品 embedding 和 SID embedding，同时输出 PV、CTR、CVR 分数，并以 PV×CTR 作为最终排序分；VRM 与生成损失联合优化，使单一模型同时完成召回和粗排，消除独立粗排阶段的错位问题。  
- **渐进式训练**：Pre-SFT 阶段设置编码、个性化检索、推荐、协同等 5 类任务激活基础能力；SFT 阶段采用加权多正样本损失（pay>click>pv）对齐行为价值，VRM 融入联合训练；RL（GRPO+DPO 增强+动态熵正则）作为辅助探索，但主要采用 VRM 方案。

**关键结果**  
在淘宝搜索 2 亿交互数据上，以 FORGE 为基线，QP-SID + Pre-SFT + VRM 的 TSGR 取得 HR@1000 = 0.8651（较 FORGE 提升 9.16%）。在线 A/B 测试(1% 流量，38 天) 显示：IPV +0.43%，交易笔数 +1.12%，GMV +1.64%，并已在全量生产环境部署。
