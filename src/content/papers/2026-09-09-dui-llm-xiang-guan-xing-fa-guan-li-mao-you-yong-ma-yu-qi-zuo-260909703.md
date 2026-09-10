---
title: Should I Be Polite to My LLM Relevance Judge? Tone as a Severity Operating-Point
  Shift
title_zh: 对 LLM 相关性法官礼貌有用吗？语气作为严重度操作点偏移
authors:
- Tian Zhang
- Meng Li
affiliations:
- Independent Researcher
arxiv_id: '2609.09703'
url: https://arxiv.org/abs/2609.09703
pdf_url: https://arxiv.org/pdf/2609.09703
published: '2026-09-09'
collected: '2026-09-10'
category: Eval
direction: LLM-as-judge 语气鲁棒性
tags:
- LLM-as-a-judge
- prompt tone
- relevance assessment
- calibration
- TREC DL
- NDCG
one_liner: 在 TREC DL19/DL20 上发现 prompt 语气主要改变 LLM 相关性法官的严重度操作点而非判断质量，影响校准类一致率大于排序
practical_value: '- 若用 LLM 作为离线相关性/质量 judge，不要把礼貌等级当可调超参；固定 prompt tone 和模板（含 paraphrase）以降低
  severity shift，上线前做 prompt 变体稳健性测试。

  - 更应校准 LLM judge 的宽严程度，而不是追求更高 agreement：对绝对 graded label，用 human 标注数据估计 severity
  偏移并做阈值/概率校准，或对 prompt 做温度与 threshold 适配。

  - 排序指标（NDCG@10）对 tone 不敏感（最大平均变化 0.011），若只用于召回/粗排排序对比，风险较低；但需要关注 Kendall τ 下降导致的精排重排。

  - Query-disjoint 验证法值得借鉴：把 query 切分，用未参与 prompt 选择的 queries 评估 prompt 变化，避免过拟合 prompt
  到特定 query 集合。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM 越来越多做相关性法官，但 prompt 表面形式会漂移标签。本文专门研究语气（politeness）是否影响判断质量。

方法关键点：在 TREC DL19/DL20 的 3,498 query-passage 对上，用 8 个 judge 模型、5 个分类器校准的礼貌等级、每级 3 个改写，比较一致率、NDCG@10/Kendall τ；按 query-disjoint cross-fit 检验语气与 human strictness 偏差的关联。

关键结果：效果高度依赖模型，只有 1 个模型呈 U 型，多数变化小；语气改变的主要是 judge severity operating point（整体宽严），一致率升降取决于该偏移接近/远离人类标注者的 strictness。query-disjoint 预期关联 Spearman ρ=-0.683，model-block permutation p=0.019。32 个 model-tone contrast 中，NDCG@10 最大绝对平均变化仅 0.011，但 Kendall's τ 低至 0.743，说明排序扰动减少但非零。结论：语气是绝对相关性标签的 validity threat。
