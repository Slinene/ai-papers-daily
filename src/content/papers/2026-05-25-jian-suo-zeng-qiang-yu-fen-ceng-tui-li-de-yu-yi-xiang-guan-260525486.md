---
title: 'RAG-Match: Retrieval-Augmented Knowledge Injection and Hierarchical Reasoning
  for Calibrated Semantic Relevance'
title_zh: 检索增强与分层推理的语义相关性校准框架
authors:
- Hengjun Jiang
- Liansheng Sun
- Yan Jiang
- Xiaojie Ke
- Yongjin Wang
- Xiangkun Liu
- Cunxin Gu
- Jian Xu
- Guanjun Jiang
affiliations:
- Alibaba Qwen Applications Business Group
arxiv_id: '2605.25486'
url: https://arxiv.org/abs/2605.25486
pdf_url: https://arxiv.org/pdf/2605.25486
published: '2026-05-25'
collected: '2026-05-27'
category: RecSys
direction: 检索增强的语义相关性判断
tags:
- RAG
- RelevanceJudgment
- HierarchicalReasoning
- PreferenceOptimization
- LLM
- Search
one_liner: 通过知识注入、分层推理对齐和偏好校准三阶段提升搜索相关性判断
practical_value: '- 用**检索生成伪文档**做知识注入预训练：对无标注查询，先检索 top-k 证据并合成回答文档，再用 query-to-synthesized-document
  生成任务做继续预训练。电商搜索中可直接复用，将商品描述、属性、用户评论作为知识库，让模型学习 query 到最相关商品知识的映射，改善冷启动和长尾查询。

  - 分层推理模板设计：将相关性判断拆成 **Knowledge-Infused Grounding + Holistic Multi-Dimensional Alignment**
  两个阶段。电商场景中可类比：先让模型基于查询和检索知识总结用户意图、关键属性约束，再从意图一致性、实体匹配、属性完备性等维度评判候选商品，提升可解释性和准确性。

  - 用 **相邻等级偏好优化** 修正系统性高估：发现 LLM 微调后容易打高相关性分数，可针对人类标注数据构造 adjacent-label 偏好对，使用 DPO
  训练让模型倾向于正确标签。电商搜索中常见的“Good vs Fair”容易混淆，可借鉴此方法在少量标注上做边界校准，降低误判率。

  - 不依赖在线 RAG 推理：知识注入仅在训练阶段通过伪文档完成，推理时无需拼接检索结果，减少延迟和上下文窗口消耗。对时延敏感的生产排序系统很实用。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
搜索相关性判断在知识密集型场景中面临挑战：查询意图隐含、需要背景知识、细粒度区分（如 3 级相关度）。现有模型多依赖直接标签监督或浅层语义相似，导致长尾查询、事实等价和边界情况表现不佳。LLM 直接用于相关性容易产生推理不稳定、高估关键词重叠的文档。

**方法关键点**
- **三阶段框架**：检索增强预训练 (Phase I)、分层推理对齐 (Phase II)、差异引导偏好优化 (Phase III)。
- Phase I：利用 1000 万查询，每个查询取检索 top-k 证据并合成一个回答文档，训练模型从 query 生成该合成文档，注入查询相关背景知识，获得更强的语义先验。
- Phase II：用 GPT-5.2 作为教师，分两步生成推理轨迹：先基于 query 和合成文档做知识注入基础（KIG），输出意图、预期答案类型、对象范围、关键约束等结构化表示；再基于候选文档进行多维度对齐（意图一致性、实体保真度、逻辑完备性、信息密度），最后得标签。训练学生模型生成完整推理链和标签。
- Phase III：用 3000 条人工标注样本，构造相邻等级错误偏好对，让模型生成偏好轨迹，用 DPO 结合标签预测损失微调，修正 Phase II 模型系统性高估倾向。

**关键实验**
- 测试集：1728 条人工标注 query-doc 对，含头部和中长尾查询。
- Baseline：DeepSeek-R1、GLM-4、MiniMax-SynLogic、Qwen3-Reranker（8B），均用标签 SFT。
- RAG-Match（8B）在 NDCG@1 达 0.902，远超最强基线 0.846；nPNR 0.833，提升显著。消融显示 Phase I→II→III 逐步增益，Phase III 将过估率从 0.502 降至 0.336，均值偏置从 0.560 降至 0.238。

**核心 insight**
相关性模型不应直接拟合标签，而应通过知识注入重塑语义空间，再分层推理并校准边界，三个设计互补且可解耦部署。
