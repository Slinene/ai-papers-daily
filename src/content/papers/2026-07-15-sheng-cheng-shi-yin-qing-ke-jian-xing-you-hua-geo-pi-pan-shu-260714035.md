---
title: 'Optimizing Visibility in Generative Engines: A Critical Survey of Generative
  Engine Optimization (2023-2026)'
title_zh: 生成式引擎可见性优化（GEO）批判性综述：2023-2026
authors:
- Olivier Martinez
affiliations:
- Sciences Po
arxiv_id: '2607.14035'
url: https://arxiv.org/abs/2607.14035
pdf_url: https://arxiv.org/pdf/2607.14035
published: '2026-07-15'
collected: '2026-07-17'
category: Other
direction: 生成式引擎优化方法论综述
tags:
- GEO
- RAG
- Citation Optimization
- Search Visibility
- Evidence Hierarchy
one_liner: 系统拆解生成式引擎优化全流程，揭示现有技术仅作用于已检索内容，缺乏可复现的有机发现与长期效果证据
practical_value: '- 在 RAG 驱动的推荐/回答 Agent 中，可借鉴 visibility vector 拆解“被检索 → 被引用 → 被采用”的多阶段指标，单独优化内容格式（如加粗摘要、结构化列表）往往只能提升短期引用率，对真实语料库的发现性帮助有限。

  - 采用该综述提出的重复测量、释义对照与多源干扰控制实验设计，能更可靠地评估知识库内容在 LLM 回答中的可见性，避免将随机波动误判为优化效果。

  - 电商搜索/广告文案生成场景中，若依赖生成式引擎曝光，需警惕通用启发式技巧（如关键词堆砌）跨平台迁移失效，以及竞争者文案优化可能稀释自身流量，应优先保证论域相关性而非盲目套用
  citation hack。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：生成式引擎优化（GEO）领域发展迅速，但术语、指标和证据标准混乱，多数研究仅测量“已检索固定内容池内的引用变化”，未触及有机发现性和真实流量效应。本文对 2023 年 11 月至 2026 年 7 月间的 45 项研究进行批判性综述，试图统一概念框架并检验证据强度。

**方法**：提出多阶段形式化模型，将 GEO 分解为搜索激活、爬取索引、检索、重排序、上下文分配、引用、可信度吸收等步骤；定义 visibility vector（发现性、引用、吸收、经济效果）；建立证据等级与可复现协议，强调重复测量、释义对照、人工验证与多智能体干扰控制。

**关键结果**：领域内证据普遍狭窄——已检索内容可通过改写改变引用位置或采纳概率，但无任何一个技术展现跨平台、长期、因果的有机发现性提升。可复现的有效杠杆是论域相关性和上下文排位；通用启发式技巧迁移性差；竞争会侵蚀个体收益；以引用为导向的重写甚至可能伤害检索环节。商业审计亦发现来源重叠低、运行间变异大、保真度持续不足。
