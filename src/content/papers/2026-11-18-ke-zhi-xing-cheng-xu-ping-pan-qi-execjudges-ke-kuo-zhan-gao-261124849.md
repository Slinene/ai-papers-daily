---
title: Can Programs Replace LLM Judges? Executable Program Judges for Scalable and
  Efficient Relevance Labeling
title_zh: 可执行程序评判器 ExecJudges：可扩展高效的相关性标注
authors:
- Eugene Agichtein
- Charles L. A. Clarke
- Kaustubh Dhole
- William Stern
affiliations:
- Emory University
- University of Waterloo
- Stanford University
arxiv_id: '2611.24849'
url: https://arxiv.org/abs/2611.24849
pdf_url: https://arxiv.org/pdf/2611.24849
published: '2026-11-18'
collected: '2026-11-20'
category: Eval
direction: 检索评估 · 程序化相关性裁判
tags:
- relevance judgments
- LLM judges
- program synthesis
- TREC
- evaluation
- cost efficiency
one_liner: 用 LLM 按评估指南一次性生成可执行程序替代逐文档 LLM 裁判，成本低且与 LLM 裁判一致性相当
practical_value: '- 搜索/推荐相关性标注中，可用 LLM 按评估准则一次性生成可执行程序而非逐文档调 LLM；程序只用词法匹配、parser 和池统计，可在
  CPU 上以零推理成本跑大规模候选池。

  - 若已有少量人工标注，可仿照 ExecJudges-L 把标注样例注入程序生成流程，提升与人工标准一致度，尤其适合商品/广告匹配中规则相对明确的相关性分级场景。

  - 可执行程序可读、可 diff、可审计，适合需要可复现评估和合规解释的线上实验；单主题生成成本极低，便于多类目横向铺开。

  - 程序裁判对系统排序有足够区分力（Kendall''s tau 0.87–0.94），可作为快速离线回归评测层，降低对昂贵 LLM 裁判的依赖。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM 裁判逐条标注成本高、不透明且难复现，检索评测需要可扩展的相关性标注方法。

方法关键点：ExecJudges 用 frontier LLM 把评估指南转化为每个 topic 的可执行程序，程序仅依赖词法匹配、现成 NLP 库与 pool 统计，不逐文档调用 LLM；ExecJudges-L 变体在有人工标签示例时进一步注入少量标注提升一致性。在七个 TREC 集合上对比 NIST assessors、Claude Sonnet 5.5 LLM 裁判和 per-topic classifiers。

关键结果：在 TREC DL 2019–2021 上，ExecJudges 与 NIST 标注的一致性达到 Claude Sonnet 5.5 LLM 裁判水平；少量人工标签下，ExecJudges-L 在所有七个集合上超过 per-topic classifiers，与 LLM 裁判的 Krippendorff's alpha 或更高或差距在 0.05 内；标注结果排序 official TREC DL runs 的 Kendall's tau 达 0.87–0.94；每 topic 程序生成一次性成本 $0.17–0.49，后续标注零额外成本。
