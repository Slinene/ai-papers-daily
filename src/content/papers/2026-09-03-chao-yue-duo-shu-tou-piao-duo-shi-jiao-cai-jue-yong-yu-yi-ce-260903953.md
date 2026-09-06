---
title: 'Beyond Majority Vote: Multi-Perspective Adjudication for Medical Hallucination
  Detection'
title_zh: 超越多数投票：多视角裁决用于医疗幻觉检测
authors:
- Joe Cecil
- Marjorie Freedman
affiliations:
- Information Sciences Institute, University of Southern California
arxiv_id: '2609.03953'
url: https://arxiv.org/abs/2609.03953
pdf_url: https://arxiv.org/pdf/2609.03953
published: '2026-09-03'
collected: '2026-09-06'
category: Eval
direction: LLM 幻觉检测与标注基准
tags:
- hallucination detection
- LLM-as-a-Judge
- annotation
- factuality
- medical LLM
- benchmark
one_liner: 多视角标注与裁决流程揭示单遍幻觉基准会低估事实错误，LaJ 可辅助发现但无法替代专家判断
practical_value: '- 在商品文案、广告生成或购物助手回复的幻觉评估中，不要只做单遍人工标注；先用 LLM-as-a-Judge 批量召回可疑事实错误，再人工/证据核查，能提升错误覆盖。

  - LaJ 不能作为唯一裁判：它漏掉人类能抓到的错误。把 LaJ 输出当候选生成器，与人类标注合并去重后进入裁决，可以在成本和覆盖率间平衡。

  - 对产品参数、价格、活动规则等高风险内容，建议引入结构化证据库做事实核查（类似论文中 evidence-based adjudication），而不只依赖模型判断。

  - 做 LLM 评估 benchmark 时，单遍标注可能系统性低估事实错误；上线前可增加一轮多视角裁决，尤其是长文本中隐蔽错误。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 生成内容的事实错误检测常被当作单遍、单标注员的任务，但长文本中的事实错误隐蔽且嵌在正确文本中，容易被漏标，导致幻觉基准低估错误率，并影响检测系统的可靠性评估。

**方法关键点**：论文构建多视角标注流程，结合首轮人工标注、LLM-as-a-Judge 候选发现，以及两类裁决——医学专家裁决和基于证据的事实核查。流程允许多个候选来源进入最终裁定，而非简单多数投票。

**关键结果**：首轮标注员经常漏掉后来被裁决确认的事实错误；LaJ 能提升候选发现，但单独使用不够，会漏掉人类标注员能发现的错误。裁决者之间也存在分歧，说明多来源裁决能提升基准完整性，但仍不能替代判断与专业知识。将同一方法应用于现有基准，也发现类似漏标模式。结论是：在考察场景中，单遍幻觉基准以漏计事实错误为代价换取规模；多遍裁决能改善覆盖，但基准推断仍依赖裁决所用判断、专业知识和证据。
