---
title: 'Blind Men and the Elephant: Probing the Epistemic Myopia of LLMs under Long-Tail
  Divergent Knowledge'
title_zh: 盲人摸象：探测大模型在长尾分歧知识上的认知短视
authors:
- Zhuoshi Pan
- Junru Lu
- Yan Qian
- H. Vicky Zhao
- Di Yin
- Xing Sun
affiliations:
- Tsinghua University
- Tencent Youtu Lab
- University of Warwick
arxiv_id: '2608.28478'
url: https://arxiv.org/abs/2608.28478
pdf_url: https://arxiv.org/pdf/2608.28478
published: '2026-08-27'
collected: '2026-08-31'
category: Eval
direction: 长尾分歧知识的LLM记忆完整性评估
tags:
- LLM
- Knowledge Probing
- Long-Tail
- Benchmark
- Divergent Knowledge
- Evaluation
one_liner: 构建ElephantBench知识探针，发现最强模型也仅能完整回忆52.4%的长尾分歧答案
practical_value: '- 在商品知识问答或客服 Agent 中，针对长尾商品属性、小众品类，仅依赖 LLM 参数记忆容易遗漏 minority 版本答案，应结合
  RAG 或知识图谱做多源校验。

  - 评估知识型 Agent 时，不应只看单一答案的 Exact Match，需引入多答案召回指标，以识别模型只记住主流答案而忽略分歧答案的不足。

  - 可借鉴 graph-based pipeline 从低曝光语料自动挖掘分歧点，用于构建长尾场景测试集，诊断模型在业务垂直领域（如二手商品、非标品）的知识覆盖盲区。

  - 训练或微调时注意 exposure imbalance：提高 minority 侧样本的曝光频率与多样性，有助于提升模型对长尾知识的完整回忆。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：传统事实问答假设每个问题只有一个标准答案，掩盖了 LLM 是否完整保留长尾事实中存在的分歧性描述。为填补这一评估空白，论文构建了专门的知识探针。

方法：提出 ElephantBench，包含 1094 个 closed-book 问答对，通过可审计的图驱动 pipeline 从低曝光网络语料中检索相关文档，自动识别自然发生的分歧观点，并转化为多答案 QA 记录。每个答案都经过原始文档和权威公开来源的双重验证，再由人工审核。

结果：在 32 个模型上测试，即使最强的模型也仅能在 52.4% 的问题上同时回忆出两个分歧答案；在几乎所有剩余问题上，模型都能回忆出一个答案但遗漏另一个。增大模型规模和推理时思考能提升召回，但不能完全消除这种不完整性。语料分析进一步表明，曝光不平衡有利于主流答案，而 minority 侧曝光越多，模型完整回忆的概率越高。

结论：ElephantBench 为诊断参数记忆中的认知短视提供了可复现的基准，其 pipeline 可高效地将长尾语料转化为来源可追溯的知识探针。
