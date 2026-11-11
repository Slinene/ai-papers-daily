---
title: 'CLADE: Category-Level Answering from Deficient Evidence in Retrieval-Augmented
  Language Models'
title_zh: CLADE：检索增强中类别级作答与证据不足问题
authors:
- S M Rayeed
- Charles V. Stewart
- Yao Ma
affiliations:
- Rensselaer Polytechnic Institute
arxiv_id: '2611.14355'
url: https://arxiv.org/abs/2611.14355
pdf_url: https://arxiv.org/pdf/2611.14355
published: '2026-11-10'
collected: '2026-11-11'
category: RAG
direction: RAG 证据粒度与本体查询
tags:
- RAG
- Abstention
- Ontology
- LLM
- Biomedical QA
- Calibration
one_liner: LLM 面对粗粒度类别证据时倾向猜测而非弃答或查询本体，且简单校准无法解决
practical_value: '- 在电商导购/客服 RAG 中，可借鉴「resolvable insufficiency」分类：当检索结果只给到类目或品牌而不含具体型号/规格时，不是简单判为不足，而应触发澄清、二级检索或本体查询，避免模型直接给错答案。

  - 可设计规则：若检索片段只出现上位词（如“缓解过敏”），且下游答案需要下位词（如具体药品名），先做实体链接到商品知识图谱，得到候选列表再让 LLM 重排，降低幻觉。

  - 论文显示 confidence filtering、更大的模型、显式要求弃答都没用，因此业务中不能只靠 prompt 或阈值；需要架构上引入外部结构化校验（本体/知识图谱）作为刚性约束。

  - 端到端恢复率低主因是 family/类目名在文本中匹配难，说明工程上应预先对文档做实体标注或构建别名映射，而不是运行时字符串匹配。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

## 动机

RAG 系统检索到的段落可能准确且相关，但答案粒度比问题粗。例如问题问具体疾病“家族性高脂血症”，检索文本只提到“高脂血症”。之前工作把这类上下文直接视为不足，作者认为这是可解析不足（resolvable insufficiency）：文本无法确定细粒度答案，但提到的上位类别可通过领域本体映射到候选列表。

## 方法关键点

- 定义 Clade 现象：LLM 阅读仅含类别/家族名的段落时，倾向直接回答而不是弃答或进一步检索。
- 在 PrimeKG 生物医学问答和 GloBI 生态物种交互数据上测试模型对 family-only 段落的行为，并进行反事实实验。
- 尝试 confidence filtering、模型规模扩大、显式要求弃答等简单修复。
- 最后测试用本体将粗粒度类别转为精确答案：给定正确 family，本体候选命中率 98.5%；但页面字符串匹配只有 19.8%，让模型选择 family 提升到 30.0%，端到端恢复从 10.0% 到 26.8%。

## 关键结果

- family-only 段落相比无信息段落，使弃答率下降 13.8 个百分点，但猜测错误约一半。
- 反事实实验：将精确疾病名替换为上位家族名，弃答率降低 17.4 个百分点。
- 简单修复均无法解决 Clade。
- 本体辅助受限于实体链接和 family 识别步骤，整体恢复率仍低。
