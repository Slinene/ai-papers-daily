---
title: LLMs Encode Relevance as a Layer-Wise Cross-Lingual Signal
title_zh: LLM 的相关性信号呈逐层跨语言编码
authors:
- Pietro Bernardelle
- Samaneh Mohtadi
- Stefano Civelli
- Joel Mackenzie
- Gianluca Demartini
affiliations:
- The University of Queensland
arxiv_id: '2607.15555'
url: https://arxiv.org/abs/2607.15555
pdf_url: https://arxiv.org/pdf/2607.15555
published: '2026-07-17'
collected: '2026-07-20'
category: RecSys
direction: LLM 内部相关性表征分析
tags:
- linear probe
- relevance decoding
- cross-lingual
- LLM judgment
- retrieval evaluation
- residual stream
one_liner: 线性探针可从 LLM 残差流激活中解码查询-文档相关性，中间层最准，且常优于模型直接生成的判断
practical_value: '- **用探针替代显式 prompt 判断**：在排序或过滤阶段，直接从 LLM 中间层提取相关性信号，可能比模型生成的标签更稳定，尤其当显式输出不可靠时（如长文档、多语言场景）。

  - **层监控辅助决策**：观察中间层探针准确率，可早期判断“模型内部是否已识别出相关性”，即使最终生成错误标签，也能触发 fallback 逻辑。

  - **跨语言召回增强**：虽然跨语言迁移弱于同语言，但部分层表现出的可移植性为多语言推荐系统提供了一种低成本扩展路径——可先用英文数据训练探针，再适配目标语言。

  - **轻量级 reranker 设计**：线性探针几乎零推理开销，可部署为粗排或特征信号，结合模型生成结果提升整体排序质量。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 越来越多地被用作相关性评估和重排器，但大多数分析只关注生成的标签或分数，对模型内部如何表示相关性知之甚少。本文探究查询-文档相关性是否可线性解码、与生成判断的区别、以及跨语言迁移性。

**方法**：选用 4-9B 参数的指令微调 LLM，用 UMBRELA 风格的相关性判断提示词，从各层 Transformer 的残差流中提取最后一个 token 的激活，训练线性探针预测相关性标签。在 TREC DL20 和 MIRACL 数据集上评估，对比探针预测与模型生成判断，并测试探针伪标签能否保留系统排序。

**关键结果**：
- 相关性编码呈深度依赖性：早期层探针表现差，中后期最强，说明上下文整合后信号才线性可解码。
- 多个模型中，验证集挑选的探针在准确率和系统排序保留上匹配甚至优于模型直接生成的判断，揭示内部表征与外部表达间的分离。
- 跨语言实验显示部分可移植性，但弱于同语言解码。
