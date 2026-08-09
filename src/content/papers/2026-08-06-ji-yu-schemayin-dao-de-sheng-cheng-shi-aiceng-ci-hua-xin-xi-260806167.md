---
title: Schema-Guided Hierarchical Information Extraction and Semantic Evaluation Using
  Generative AI
title_zh: 基于Schema引导的生成式AI层次化信息抽取与语义评估
authors:
- Modhurita Mitra
- Jan-Willem Versteeg
- Maarten D. Schermer
- Shiva Nadi Najafabadi
- Marie L. De Bruin
- Lourens T. Bloem
affiliations:
- Utrecht University
- Utrecht Institute for Pharmaceutical Sciences
arxiv_id: '2608.06167'
url: https://arxiv.org/abs/2608.06167
pdf_url: https://arxiv.org/pdf/2608.06167
published: '2026-08-06'
collected: '2026-08-09'
category: LLM
direction: LLM 结构化信息抽取与评估
tags:
- Schema-based
- Information Extraction
- Semantic Matching
- Zero-shot
- LLM Evaluation
- Nested Attributes
one_liner: 用单一生成式模型零样本抽取嵌套属性，并通过路径语义匹配与分级评估实现自动化高精度信息提取
practical_value: '- 在电商商品描述、搜索增强等场景中，可借鉴Schema定义信息模型，用单次LLM调用直接从非结构化文本（如商品详情页、用户评论）提取层次化属性（如规格、适用人群），实现零样本结构化，替代传统多模型流水线。

  - 提出的路径语义匹配算法能处理提取结果中嵌套、重复、变长属性与金标准的对齐，适用于自动校验LLM输出的结构化数据，例如在商品知识图谱自动构建中，比对提取的属性值与已有库。

  - 引入的“精确/语义/有用/不匹配”多级评估量表，为业务场景提供了灵活的质量判断准则，例如在商品信息补全或用户生成内容挖掘中，可允许语义相近的匹配视为有用，提高覆盖率。

  - 框架跨模型、跨领域、跨语言的可迁移性验证，表明在电商多语言环境（如不同站点）下，可能无需为每种语言单独设计抽取器，降低维护成本。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：健康技术评估（HTA）依赖从大量非结构化报告中手动提取结构化信息，效率低且易不一致。需要一种能处理层次嵌套、多值属性的自动化抽取方案，并能准确评估抽取质量。

**方法**：
- 设计Schema（信息模型）编码领域知识，定义属性、嵌套结构及基数约束。每个文档通过单次调用生成式模型（如Claude Opus 3）在零样本下按Schema抽取为JSON。
- 提出路径语义匹配算法：将抽取结果与金标准按属性路径对齐，处理变长列表和缺失属性。
- 将属性值成对输入LLM进行语义比较，设计四级匹配量表（精确匹配、语义匹配、有用匹配、不匹配），根据领域需求设定容错阈值。

**关键结果**：
- 在NICE的HTA文档上，14个属性中的12个F1>90%，抽取速度比人工快约30倍。
- 框架对GPT-4o、Llama-3.1等模型均适用，在不同HTA机构（加拿大、德国）和语言（德语）上表现稳健。
