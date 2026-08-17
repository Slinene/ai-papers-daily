---
title: 'HERMES: a multi-agent framework for structured knowledge extraction from ultra-long
  documents in geoscience'
title_zh: HERMES：面向地球科学超长文档结构化知识抽取的多智能体框架
authors:
- Ziqi Song
- Zongyuan Xiang
- James G. Ogg
- Bruce S. Lieberman
- Gabi Ogg
- Natalia López Carranza
- Wen Du
- Yufei Ye
- Shuan Li
- Zhong Peng
affiliations:
- Zhejiang Laboratory, Hangzhou, China
- Purdue University, Indiana, USA
- University of Kansas, USA
- University of Illinois Chicago, USA
- Geologic TimeScale Foundation, Indiana, USA
arxiv_id: '2608.14055'
url: https://arxiv.org/abs/2608.14055
pdf_url: https://arxiv.org/pdf/2608.14055
published: '2026-08-14'
collected: '2026-08-17'
category: MultiAgent
direction: 多 Agent 文档知识抽取
tags:
- Multi-Agent
- Knowledge Extraction
- LLM
- Ultra-long Documents
- Evidence Tracing
- Structured Data
one_liner: 多智能体框架从超长地学文献中抽取结构化数据，在古生物专著上抽取3.2万实体、45万属性，F1约0.90
practical_value: '- 多智能体协调 + 领域约束 + 验证规则，可以借鉴来做电商商品属性/类目树的标准化知识抽取，尤其在 SPU/SKU 结构补全时，用
  validator agent 强制字段格式和枚举值，降低 LLM 幻觉。

  - 文档级统一抽取解析文本、表格、图片 caption，适合处理电商超长商品详情页、行业标准文档或广告素材库，可建立一条从多模态内容到结构化字段的 pipeline。

  - 每个字段带 evidence tracing（证据追踪），方便人工审核和纠错，这在电商知识中台里很实用：预测出的属性可以回链到原文位置，快速验证和修复。

  - 零训练跨域迁移说明该框架对不同领域知识库建设具有可复制性，冷启动类目或长尾属性补全时可以用低成本方式快速搭建抽取能力，效率提升数倍。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：地学权威知识长期困在遗留专著和历史文献中，非结构化文本、复杂版式阻碍计算访问，人工抽取成本高且不可扩展。

方法关键点：HERMES 是一个可扩展的多智能体框架，用协调 LLM 统一文档级抽取流程，整合领域约束、验证规则和证据追踪；输入同时包含解析后的正文、表格、图片和 caption，多个 agent 分工完成实体识别、属性抽取、一致性校验和证据标注。

关键结果：在 55 卷 Treatise on Invertebrate Paleontology 上抽取 32,277 个化石分类实体和 451,878 条属性，发布在线数据库；实体平均 F1 约 0.90，属性平均 F1 约 0.91；相对人工基线效率提升约 6 倍。在古地磁和地球化学领域不额外训练即可迁移，表现稳定。
