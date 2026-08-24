---
title: 'Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening
  and Provenance Ranking'
title_zh: 记忆投毒下的效用崩塌：内容筛查与溯源排序的边界
authors:
- Arulnidhi Karunanidhi
affiliations:
- Quantify Labs Ltd
arxiv_id: '2608.21230'
url: https://arxiv.org/abs/2608.21230
pdf_url: https://arxiv.org/pdf/2608.21230
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: Agent 记忆投毒与溯源检索防御
tags:
- Agent Memory
- Memory Poisoning
- Provenance Ranking
- Content Screening
- RAG Security
- Evaluation
one_liner: 1.2%记忆投毒使LongMemEval准确率从0.850降至0.300，内容筛查拦截0/360，溯源加权排序难用
practical_value: '- 在电商/广告 Agent 的持久记忆写入侧，不要仅依赖内容筛查判断断言真假；需要接入外部 grounding（如商品价格、库存、活动规则权威源）才能识别伪造但语义通顺的虚假记忆。

  - 检索侧不要使用 additive provenance penalty 或简单给可信来源加权；可在召回阶段对不同 provenance 的文档设置最大占用配额（bounded
  occupancy / quota），避免低可信源靠语义相似度淹没高可信证据，也避免高权重把低可信但真正携带答案的证据全部排除。

  - 评估 Agent 记忆安全时，必须同时构造 mixed-provenance 语料：既看投毒攻击是否成功，也看当真实答案恰好来自 untrusted 来源时系统是否仍可用，否则容易过拟合防御、误伤业务指标。

  - 内容筛查对低占比投毒（如 1.2%）不敏感，且对 trigger-laden 良性文本有误判；实际推荐系统中 UGC 或第三方商品描述不可全信，应把来源可信度作为检索约束而非后验过滤。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：持久记忆让单次请求里的虚假信息变成跨会话复用的持久攻击面；一旦错误断言写入，未来匹配的会话都会检索到它。但现有防御（写时内容筛查、溯源加权排序）的真实边界未被量化。

**方法关键点**：作者构造弱攻击——单次生成的 plain assertions，无指令、无 trigger、无 retriever 优化，仅投毒 LongMemEval 1.2% 语料；测试四阶段写时内容筛查管线（对 indirect prompt injection 的召回 0.832，且仅误标 1.5% 含 trigger 的良性文本）；再评估 provenance-weighted retrieval，包含 shipped weight 与更强权重，在 mixed-provenance 和 untrusted-evidence 两个语料上测效用与证据召回。

**结果**：投毒后准确率从 0.850 降至 0.300，且内容筛查拒绝 0/360 条投毒记忆。shipped provenance weight 与无防御统计无差异（p=0.80）；更强权重虽在 mixed-provenance 下把准确率从 0.3167 提到 0.7000，但当答案证据本身来自 untrusted 来源时，证据召回归零、准确率跌至 0.0417。在该相似度区间内 additive provenance term 没有可用设置：强到能抵抗 query-shaped 投毒，也会排除合法的 untrusted 证据。最终建议 provenance 应作为检索时的 bounded occupancy 约束，而非相加惩罚项。
