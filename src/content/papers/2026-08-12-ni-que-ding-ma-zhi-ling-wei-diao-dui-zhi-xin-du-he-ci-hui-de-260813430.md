---
title: Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence
  and Lexical Diversity
title_zh: 你确定吗？指令微调对置信度和词汇多样性的影响
authors:
- Irina Proskurina
- Mayank Kumar
- Oyindolapo O. Komolafe
affiliations:
- Cohere Labs Community
- Laboratoire Hubert Curien, UMR CNRS 5516, Saint-Étienne, France
- School of Computer Science Engineering and Technology (SCSET), Bennett University,
  Greater Noida, India
- School of Physical Therapy, Faculty of Health Sciences, Western University, London,
  Canada
arxiv_id: '2608.13430'
url: https://arxiv.org/abs/2608.13430
pdf_url: https://arxiv.org/pdf/2608.13430
published: '2026-08-12'
collected: '2026-08-15'
category: Eval
direction: 指令微调改变置信度与 rationale 多样性
tags:
- instruction tuning
- confidence calibration
- lexical diversity
- question answering
- LLM evaluation
one_liner: 在问答基准上评估匹配基座与指令微调模型，发现指令微调一致改变置信度但非均匀改变 rationale 词汇多样性
practical_value: '- 在电商/推荐场景用 LLM 生成推荐理由或解释时，指令微调后的模型 verbalized confidence 可能系统性偏高，与真实准确率脱钩；上线前需要额外做
  confidence calibration，不要直接采信模型自述置信度。

  - 若用 LLM 批量生成商品卖点、用户 push 文案，需监控跨样本 rationale 多样性：指令微调可能使生成内容趋于同质化，建议引入多样性约束或后处理去重。

  - 将 surface-level 词汇多样性（如 Unique-2）作为生成多样性监控指标时，注意它可能与语义多样性（cross-rationale diversity）不同向变化；最好同时监控两类指标，避免误判。

  - 在 Agent 链路中让 LLM 输出思考过程或理由时，指令微调带来的置信度变化可能影响下游决策；可在 prompt 中要求模型更客观地报告不确定性，或使用
  logit-based 校准替代 verbalized confidence。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：指令微调后的 LLM 在问答中表现更强，但已有研究显示其 verbalized overconfidence 增加。本文研究指令微调是否同时改变了生成 rationale 的词汇多样性，以及置信度变化是否与多样性变化相关联。

**方法关键点**：选取三组匹配的 base 与 instruction-tuned 模型，在多个问答基准（如 ARC-Easy 等）上评估。分别测量 answer confidence（如生成答案的 entropy 或 uncertainty）、likelihood-based calibration、跨 rationale 的 diversity 和表面级词汇多样性（如 Unique-2）；并通过控制答案选择和 rationale 长度来分离效应。

**关键结果**：指令微调一致改变模型表达的置信度，即便预测准确率变化不大，且 likelihood-based calibration 反而下降；跨 rationale 多样性一致降低，但表面级词汇多样性在不同模型和数据集上方向和幅度都不一致；在控制答案选择与 rationale 长度后上述差异仍然存在，说明置信度和 rationale 多样性捕捉的是指令微调的不同影响维度。
