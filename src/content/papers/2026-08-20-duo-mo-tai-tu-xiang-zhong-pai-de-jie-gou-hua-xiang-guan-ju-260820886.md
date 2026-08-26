---
title: 'EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking'
title_zh: 多模态图像重排的结构化相关证据方法
authors:
- Enjun Du
- Siyi Liu
- Zirong Chen
- Xinyu Zuo
- Jinwen Luo
- Ruiwen Tao
- Lisheng Duan
- Haijin Liang
- Jin Ma
- Junfu Pu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tencent Yuanbao
- The University of Hong Kong
arxiv_id: '2608.20886'
url: https://arxiv.org/abs/2608.20886
pdf_url: https://arxiv.org/pdf/2608.20886
published: '2026-08-20'
collected: '2026-08-26'
category: Multimodal
direction: 多模态搜索重排 · 结构化证据
tags:
- Multimodal
- Image Re-ranking
- Composed Image Retrieval
- Structured Evidence
- Listwise Verification
- Distillation
one_liner: 将多模态图像重排建模为语义约束满足，解析查询为结构化证据包并做证据条件验证，SOTA 且可蒸馏
practical_value: '- 将用户查询解析为 typed semantic slots（required/forbidden/ignorable）的结构化证据，比不透明
  embedding 或自由 CoT 更能捕获电商搜索中的复合约束（如“同款但粉色”“保留版型、忽略背景”），减少细粒度条件遗漏或幻觉。

  - 采用 deterministic rubric scoring + evidence-grounded listwise comparison 的无训练重排流程，可直接接入已有召回/粗排链路，无需微调、上线快，适合电商场景数据分布频繁变化、快速迭代的需求。

  - 显式证据可蒸馏轻量学生模型，保留 90%+ 效果且成本大幅降低，适合线上高 QPS 的排序阶段；可将证据包作为结构化监督信号迁移到商品/广告排序模型。

  - 六个语义槽（entities, attributes, relations 等）与 required/forbidden/ignorable 的标注方式，可复用到商品属性约束理解模块，提升对用户意图（保留什么、改什么、忽略什么）的结构化建模能力。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：真实图像搜索查询通常是多模态组合的，例如「找这件衬衫的粉色版」同时包含实体保留、属性修改和背景忽略。现有重排器要么将多面相关性压缩成不透明 embedding，要么依赖自由 CoT 容易遗漏或幻觉细粒度约束。

方法关键点：受 NLP 中 rubric/checklist 评估启发，将多模态图像重排形式化为语义约束满足问题。EviRank 将任意查询（纯文本、纯图像、组合）解析为统一证据包：六个语义槽（实体、属性、关系等）的类型化标准，每个标注 required/forbidden/ignorable。重排退化为证据条件验证：结合确定性 rubric 打分和证据支撑的 listwise 比较，全程无需训练。显式证据还可作为结构化监督蒸馏轻量学生。

关键结果：在五个基准（text-to-image, image-to-image, composed image retrieval）上取得 SOTA；蒸馏学生以显著更低成本保留超过 90% 教师能力。
