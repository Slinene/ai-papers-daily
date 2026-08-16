---
title: A corpus-specific clinical RAG system matches or outperforms newer frontier
  LLMs on HealthBench
title_zh: 语料特定的临床 RAG 系统在 HealthBench 上匹敌或超越新前沿 LLM
authors:
- Praveen Reddy
- Charuta Mandke
- Suvrankar Datta
- Sarah Khan
- Siddharth Reddy Anthireddy
- Shitij Arora
- Vishal Singh
arxiv_id: '2608.12138'
url: https://arxiv.org/abs/2608.12138
pdf_url: https://arxiv.org/pdf/2608.12138
published: '2026-08-12'
collected: '2026-08-16'
category: RAG
direction: 领域特定 RAG 系统评估
tags:
- RAG
- domain-specific
- clinical LLM
- benchmark evaluation
- LLM judge
one_liner: 领域特定 RAG 通过定制语料在开放基准上与最新前沿 LLM 打平或领先，验证语料特异性对 grounding 的作用
practical_value: '- 电商/客服领域 RAG 可借鉴「语料特异性」：把平台规则、商品政策、本地化约束、用户历史上下文等做成强约束检索源，能提升事实
  grounding，不一定需要最大模型；具体做法是让检索 top-k 覆盖业务规则和场景化文档，并在 prompt 中显式要求优先依据检索证据回答。

  - 评估模型和 judge 最好不共享家族/血缘，否则分数会系统性高估；可以用中立开源模型（如不同厂商模型）做第二评判，看结论是否稳健，尤其关注「准确性」「完整性」和「沟通分数」的分维度变化，避免只看总分。

  - 当业务知识库足够垂直时，专用 RAG + 中等生成模型可对标甚至压过通用大模型，但会牺牲表达流畅度；产品上可以用 RAG 保证准确，再用后处理或改写模型补偿沟通体验。

  - 消融「语料范围」是个高价值实验：把知识库从通用语料换成店铺/行业/活动强相关语料，观察同一 LLM 的准确率变化，即可量化语料特异性收益。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：近期研究称通用 LLM 在临床基准上已经匹敌甚至超过专门临床 AI，但这些对比使用的工具范围较窄，基准也大多来自高收入医疗环境。VITA 是一个专为印度等中低收入地区设计的 RAG 系统，需要验证领域特定语料是否仍能带来 grounding 优势。

**方法**：VITA 从疾病指南、印度本地区抗生素耐药数据、国家处方集约束和资源受限护理方案中检索；架构和语料未公开，但基准、医生标注 rubrics 和完整评分结果公开。在 HealthBench 英文子集 4,023 题（占基准 80.5%）上，以 GPT-4.1 作为 judge，对比 GPT-5.4、o4-mini、Gemini 3.1 Pro、Claude Sonnet 4.6。另取 500 题子集，换用中立开源 judge DeepSeek-V4-Pro，对比 GPT-5.5、Claude Opus 4.8、Gemini 3.5 Pro、Grok 4.3，测试对模型和 judge 血缘的鲁棒性。

**结果**：首轮 VITA 获得 51.9% 可能评分点，排名第一，超过 GPT-5.4（46.1%）、o4-mini（44.3%）、Gemini 3.1 Pro（42.6%）、Claude Sonnet 4.6（37.3%），并在 45.4% 题目上得分最高。第二轮差距缩小至统计持平：VITA 与 GPT-5.5 在平均每题得分上无显著差异，但 VITA 在分权重得分和赢题数上仍领先；其准确性和完整性优势保持，但沟通评分较低。

结论：语料特异性是有效设计变量，能提升 grounding，代价是表达 polished 程度下降。
