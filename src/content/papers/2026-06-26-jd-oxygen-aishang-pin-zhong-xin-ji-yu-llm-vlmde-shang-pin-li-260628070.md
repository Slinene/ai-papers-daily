---
title: 'JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric
  Solution for Item Understanding, Management, and Applications'
title_zh: JD Oxygen AI商品中心：基于LLM/VLM的商品理解与管理平台
authors:
- Oxygen AIIC
- Chan Long
- Chao Liu
- Chaofan Chen
- Chaohui Dong
- Chunyuan Guo
- Danping Liu
- Debin Liu
- Deping Xiang
- Fulai Xu
affiliations:
- JD.com
arxiv_id: '2606.28070'
url: https://arxiv.org/abs/2606.28070
pdf_url: https://arxiv.org/pdf/2606.28070
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: 工业级LLM/VLM商品知识中台
tags:
- LLM
- VLM
- Item Understanding
- Ontology Engineering
- S2D
- Industrial-scale
one_liner: 用LLM/VLM构建百万级本体与S2D识别架构，实现高精度、高吞吐的商品知识生产
practical_value: '- **本体与模型解耦的 S2D 架构**：将商品属性值作为外部知识库检索，再让模型判别匹配，彻底避免本体更新时重训模型。电商属性体系频繁变动时可借鉴，快速上线新属性。

  - **计算量聚焦“差异化 SKU × 相关属性”**：通过同 SPU 相似度去重和属性相关度探测，大规模缩减无效计算，适合海量商品库的实时/近线特征生产。

  - **人机协同的本体迭代范式**：专家定义骨架，LLM 做开放抽取+融合+验证，兼顾覆盖与质量；可迁移至类目体系、标签体系等知识资产建设。

  - **统一商品隧道分层服务**：提供秒/分/天级新鲜度接口，解耦知识生产与消费，使搜索、推荐、运营等场景按需取用，避免重复建设。'
score: 10
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
电商数十亿 SKU 下，传统商品知识系统存在信息残缺、语义错配、人工维护成本高、运营追不上趋势等瓶颈。LLM/VLM 虽有强泛化能力，但直接调用成本极高且不可控，工业落地需同时解决本体动态演化、大规模高质量知识生产、多场景差异化服务三大挑战。

## 方法
- **人机协作本体工程**：专家定义分类、属性、场景标签的骨架，算法自底向上做知识发现（开放信息抽取+属性槽填充）、融合（表示学习→聚类→选择）、验证（多 LLM 投票+业务重要性评估），构建百万级本体并持续演化。
- **S2D 知识识别架构**：将本体作为外部知识库，语义搜索阶段用领域适配的双塔编码器召回 Top-10 候选属性值，判别阶段用 8B SFT 模型在候选集内判定，避免模型直接生成带来的幻觉，且本体更新无需重训。
- **计算效率优化**：SKU 层利用同 SPU 去重复用结果；属性层用相关度探测模型过滤无关属性，将“全 SKU×全属性”缩减为“差异性 SKU×相关属性”；叠加 KV-cache 复用与异步流水线，吞吐提升 3 倍以上。
- **模型自进化**：统一多任务 SFT 框架，融合知识发现、表示、判别能力，增量学习持续补齐长尾与新兴概念，知识生产精度 94.2%、召回 82.8%。

## 关键结果
覆盖 JD 数万类目、数十亿 SKU，日产数百亿商品知识资产，信息丰富度达原来的 3.35 倍。搜索流量覆盖 80.4%，商品信息质量问题下降 37%；卖家发布核心属性自动填充率超 80%；商品创意智能优化带来 9% CTR 提升。

> 最值得记住：把商品本体外挂、计算聚焦于“有差异的 SKU×真正相关的属性”，是工业级商品知识生产的核心效率杠杆。
