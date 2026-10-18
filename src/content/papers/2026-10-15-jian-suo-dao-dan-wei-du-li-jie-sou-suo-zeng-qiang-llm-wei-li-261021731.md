---
title: 'Retrieved but Not Read: Understanding Why Search-Augmented LLMs Fail to Use
  Available Evidence'
title_zh: 检索到但未读：理解搜索增强 LLM 未利用可用证据的原因
authors:
- Owen Walters
- Lihu Chen
- Francesca Toni
affiliations:
- Imperial College London
arxiv_id: '2610.21731'
url: https://arxiv.org/abs/2610.21731
pdf_url: https://arxiv.org/pdf/2610.21731
published: '2026-10-15'
collected: '2026-10-18'
category: RAG
direction: 搜索增强 LLM 的证据利用失败分析
tags:
- Search-Augmented LLM
- RAG
- Citation Faithfulness
- Temporal Knowledge
- Evidence Use
one_liner: 通过时序事实和分层分析，揭示搜索增强 LLM 常“检索到但未读”，即使有新证据仍输出过时答案并给出不忠实引用
practical_value: '- 在电商/Agent 场景中，价格、库存、促销、政策等事实变化频繁，别把“检索到”当“已使用”。应记录 agent 是否打开详情页/全文；若仅读
  snippet，可强制要求先展开来源页并基于全文作答，或把全文放入 context，避免 snippet 偏见。

  - 引用可信度：对购物助手/客服回答要求逐句引用已打开页面内容；用 citation faithfulness 校验（如 NLI）拦截“答 A 引 B”的回复，尤其对有时效性的事实。

  - 内部状态与最终答案不一致：即使模型隐层已表示新证据，最终仍可能偏向旧参数知识。可在 prompt 中显式对比“当前日期/最新数据”与模型先验，要求输出依据；或对关键时效属性做规则/缓存覆盖，不依赖
  LLM 自己纠偏。

  - 评测方法：构建训练截止后变更的“(实体, 属性, 旧值, 新值, 生效日期)”事实集，模拟商品改价/上下架/政策更新，用于回归测试 agent 的时效性和引用忠实性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：搜索增强 LLM 常在有相关新证据时仍输出过时答案，并可能给出不忠实引用，原因不明。

**方法**：构造训练截止后值发生变化的时序事实；评估 1 个闭源模型在真实 web 搜索下的行为，以及 6 个开源模型配置在受控检索下的表现；结合来源页打开追踪与逐层内部表征分析。

**关键结果**：模型经常只根据搜索摘要作答而不打开来源页面，这与更高的过时答案率和引用不忠实显著相关；分层分析显示，即使检索证据已经影响内部预测，模型在最终回答中仍可能偏向旧信息，说明“证据可用”与“证据有效使用”之间存在断层。
