---
title: 'ScholarSum: Student-Teacher Abstractive Summarization via Knowledge Graph
  Reasoning and Reflective Refinement'
title_zh: ScholarSum：基于知识图谱推理与反思精炼的学生-教师摘要生成框架
authors:
- Bohou Zhang
- Xiaoyu Tao
- Mingyue Cheng
- Huijie Liu
- Qi Liu
affiliations:
- State Key Laboratory of Cognitive Intelligence, University of Science and Technology
  of China
arxiv_id: '2606.18850'
url: https://arxiv.org/abs/2606.18850
pdf_url: https://arxiv.org/pdf/2606.18850
published: '2026-06-17'
collected: '2026-06-19'
category: Other
direction: LLM 摘要生成 · 事实一致性优化
tags:
- Abstractive Summarization
- Knowledge Graph
- Reflective Refinement
- Factual Consistency
- Student-Teacher
- LLM
one_liner: 通过分层知识图谱引导的学生-教师迭代框架，同时提升科学文献摘要的流畅性和忠实性
practical_value: '- **商品文案生成的可信度增强**：在生成商品描述或广告文案时，可借鉴分层知识图谱捕捉商品属性与卖点间的全局关系，再通过学生-教师迭代核对，确保文案不出现与商品实际信息不符的“幻觉”。

  - **用户评论摘要的事实校验**：为海量用户评价生成总结时，可以引入类似教师模型的检查步骤，识别无证据支持的概括，并触发重新检索原始评论进行改写，提升摘要的忠实度。

  - **检索增强生成（RAG）中的迭代精炼**：在电商知识问答或搜索导购场景，可将 ScholarSum 的反思机制嵌入 RAG 流程——先生成答案草案，再由独立评估器检查每个陈述是否有检索片段支撑，发现无依据内容后定向重查与重写，显著提高答案可信度。

  - **Agent 系统的事实验证模块**：在多智能体协作架构中，可以专门设计一个“事实核查 Agent”，像教师模型一样审视其他 Agent 生成的文本，通过检索源头证据进行反驳和修正，提升整体输出的可靠性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：科学文献摘要需要同时具备语言流畅性和事实一致性，但现有提取式方法破坏逻辑连贯，LLM 生成式方法则常出现事实偏差。为此，提出 ScholarSum，模拟学生-教师写作过程，以同时优化两者。

**方法关键点**：
1. **分层知识图谱构建**：将文档分割成语义连贯的片段，并构建分层知识图谱，通过多层社区结构自动捕捉文档的全局逻辑和宏观主题。
2. **学生生成草案**：在图结构引导下，学生模型（基于 LLM）生成初始摘要草案，确保主题覆盖完整。
3. **细粒度证据检索与反思精炼**：教师审阅者（另一个 LLM）迭代检查草案中的每一陈述，识别缺乏原文依据的内容，并触发针对性重新检索和局部重写，直到所有陈述都能被原文支持。

**关键结果**：在多个科学摘要基准测试中，ScholarSum 在摘要的完整性（ROUGE 等）和事实一致性（FactCC 等）指标上均大幅超越之前的基线方法，验证了知识图谱全局建模与反思精炼机制的有效性。
