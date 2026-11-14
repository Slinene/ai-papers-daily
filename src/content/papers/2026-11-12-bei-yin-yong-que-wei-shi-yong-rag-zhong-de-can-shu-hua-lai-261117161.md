---
title: 'Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation'
title_zh: 被引用却未使用：RAG 中的参数化来源研究
authors:
- Tanzeel Abbas
- Tehseen Zia
- David Windridge
affiliations:
- COMSATS University Islamabad
- Middlesex University London
arxiv_id: '2611.17161'
url: https://arxiv.org/abs/2611.17161
pdf_url: https://arxiv.org/pdf/2611.17161
published: '2026-11-12'
collected: '2026-11-14'
category: RAG
direction: RAG 引用溯源与参数记忆检测
tags:
- RAG
- provenance
- citation verification
- parametric memory
- NLI
- attribution
one_liner: 用反事实替换测量 RAG 引用来源，发现 1.2%–15.7% 可引用声明来自参数记忆而非检索上下文
practical_value: '- 在电商 RAG 问答、商品推荐解释或客服回答中，引用来源不一定代表模型真正用了检索内容；不要只靠 NLI 支持性验证，因为模型倾向事后选择与输出一致的引用，会构造性通过验证。

  - 可用反事实替换做离线评估：将检索事实替换为假变体再查询，若模型仍输出原事实，则说明来自参数记忆，适合作为内部审计信号，但基础率较低，不宜直接做线上拦截。

  - 对比有/无上下文时模型输出分布差异是相对最好的溯源信号，可用于日志诊断或归因分析，但需注意它衡量的是“模型知道什么”而非“模型用了什么”。

  - 流程上建议避免事后贴引用；可尝试先引用后生成或并行生成引用，降低后合理化导致的引用来源失真。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：RAG 系统给生成声明附上引用，但引用经常错误声明来源，而标准的支持性验证无法发现这种来源失真。

方法：作者采用反事实值替换来测量来源真实性——将检索段落中的某个事实替换为假变体后重新查询模型，若模型仍输出原事实，则说明该答案来自参数记忆而非检索上下文。实验覆盖一个模型家族的五个尺寸及另一个对照家族。

关键结果：1.2%–15.7% 的可引用声明来自参数记忆而非检索上下文；在最保守替换距离下，两个测试模型分别为 4.6% 和 8.5%，且同家族内随模型规模增大而上升。标准 NLI 验证结果接近随机，即使限定到引用段落也无效。原因是结构性的：从记忆回答的模型会选择与输出一致的引用。比较 10 种归因方法后，有/无上下文时模型分布差异最能分离来源，但据此行动无法在这些基础率下提升来源诚实度。检测器仍不够准确，只能测量模型知道什么而非使用了什么，区分二者仍是开放问题。
