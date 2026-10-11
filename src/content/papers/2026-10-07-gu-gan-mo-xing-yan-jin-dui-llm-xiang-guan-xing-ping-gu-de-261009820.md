---
title: The Impact of Backbone Evolution on LLM-Based Relevance Assessments
title_zh: 骨干模型演进对 LLM 相关性评估的影响
authors:
- Chuting Yu
- Guido Zuccon
- Teerapong Leelanupab
affiliations:
- The University of Queensland
arxiv_id: '2610.09820'
url: https://arxiv.org/abs/2610.09820
pdf_url: https://arxiv.org/pdf/2610.09820
published: '2026-10-07'
collected: '2026-10-11'
category: Eval
direction: LLM Judge 骨干版本演进与稳定性
tags:
- LLM Judge
- Relevance Assessment
- Backbone Evolution
- Prompt Robustness
- IR Evaluation
one_liner: 固定 prompt 下，模型升级不必然提升 LLM 相关性判断与人类一致性，且聚合性能不变不等于判断稳定
practical_value: '- 把“prompt + backbone version”当作一个固定评测单元，模型升级不等于自动更好；不要仅因模型能力提升或版本更新就更换线上
  judge，必须做等效性验证。

  - 维护 golden set：对搜索/推荐相关性、广告质量、Agent 输出等人工标注样本，在升级 backbone 时跑旧/新版本 diff，统计“正确标签翻转率”和分
  query/类目的稳定性，而不要只看总体 kappa/accuracy。

  - LLM judge 产出若用于生成训练数据（如相关性弱监督、蒸馏排序模型），label drift 会传导到下游模型；建议冻结 judge 版本并留存 prompt+model
  快照，必要时用旧版本回放或双版本并行过渡。

  - 对 rubric 类 prompt（如多维度打分）也需要重新标定阈值/评分映射，不能假设同 prompt 在不同 backbone 上分数可比；可在评分后做单调校准或
  ordinal calibration。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 被越来越多地用于自动相关性判断，典型假设是模型升级、能力增强后，同一 prompt 会带来更高的与人类判断一致性。本文验证该假设是否成立。

**方法关键点**：固定 prompt 不变，选取代表性单 prompt 方法 UMBRELA 和 rubric 类 prompt 方法 EXAM，在商业模型 Gemini、GPT 以及开源模型 Qwen、Llama 的连续版本上系统评估相关性判断表现；除聚合一致性指标外，重点分析跨版本的判断稳定性，如早期版本已判对的样本是否在后续版本中被改错。

**关键结果**：没有一致证据表明新版本能成为更好的相关性 judge；聚合性能相似或略有提升，也不代表判断稳定——早期 backbone 做出的正确判断不一定被后一版本保持。提示同一家族的模型更新后，针对旧版本设计并验证的 judge prompt 不保证等价或更好；不同模型家族和 prompt 类型均存在回归风险。
