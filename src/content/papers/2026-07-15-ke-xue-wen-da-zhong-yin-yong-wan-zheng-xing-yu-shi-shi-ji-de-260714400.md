---
title: 'DS@GT ARC at LongEval: Citation Integrity and Factual Grounding in Scientific
  QA'
title_zh: 科学问答中引用完整性与事实基础的校正管道
authors:
- Brandon Michaels
- Brendon Johnson
affiliations:
- Georgia Institute of Technology
arxiv_id: '2607.14400'
url: https://arxiv.org/abs/2607.14400
pdf_url: https://arxiv.org/pdf/2607.14400
published: '2026-07-15'
collected: '2026-07-17'
category: Eval
direction: RAG 可信评估与校正
tags:
- RAG
- Citation Integrity
- Factual Grounding
- LLM-as-judge
- Scientific QA
- Trustworthy AI
one_liner: 前沿模型即使不使用检索文档也能高相关性回答，校正管道小幅提升引用忠实度，强调评估需奖励严格答案根基
practical_value: '- 构建电商RAG问答/推荐解释时，传统相关性和流畅性指标会掩盖模型是否真正引用检索文档，需增加引用忠实度或答案根基性指标。

  - 可采用预生成前CRAG过滤不相关块+后生成CiteFix强制对齐的校正管道，提升生成文本的引用完整性，适用于电商客服、搜索解释等场景。

  - LLM-as-judge诊断可检测模型虽识别相关文档却未使用其内容，用于验证RAG系统是否真正依赖检索信息，对可解释推荐和对话式agent至关重要。

  - 设计Agent的RAG生成模块时，加入后验步骤强制每个声明有出处，能提高可信度，尤其适合电商中需要验证的推荐理由或产品问答。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统NLG评估指标与RAG QA系统所需的引用完整性存在分歧。在科学问答中，答案必须严格基于检索文献，但现有指标往往奖励答案的表面相关性与流畅性，忽略是否真正使用检索上下文。

**方法**：在CLEF 2026 LongEval任务上，对比无校正的基准模型与前沿模型，并引入校正管道：预生成前用CRAG过滤不相关文档块，后生成时用CiteFix强制生成声明与所引用材料的蕴含关系，利用RAGAs的LLM-as-judge诊断答案忠实度及文档使用情况。

**关键结果**：前沿模型（如GPT-4）在答案相关性和流畅性上得分最高，但诊断显示它们能正确识别相关文档却未将其内容用于答案生成，实质上忽略了检索到的证据。校正管道在引用忠实度和答案根基性上带来轻微但一致的改善，表明仅靠模型能力提升无法自动确保引用完整性，需要专门的校正机制。

**结论**：评估可信RAG QA必须引入奖励严格答案根基的指标，而非仅依赖传统NLG分数。
