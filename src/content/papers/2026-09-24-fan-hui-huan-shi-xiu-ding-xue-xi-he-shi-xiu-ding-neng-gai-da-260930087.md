---
title: Return or Revise? Learning When Revision Helps Retrieval-Augmented QA
title_zh: 返回还是修订？学习何时修订能改善检索增强问答
authors:
- Nicholas Kashani Motlagh
- Tim Anderson
- Jeremy Gwinnup
- Grant Erdmann
affiliations:
- DCS Corp
- Air Force Research Laboratory
arxiv_id: '2609.30087'
url: https://arxiv.org/abs/2609.30087
pdf_url: https://arxiv.org/pdf/2609.30087
published: '2026-09-24'
collected: '2026-09-25'
category: RAG
direction: RAG 答案修订决策
tags:
- RAG
- Answer Revision
- Recoverability
- Decision Policy
- LLM
one_liner: 提出 recoverability 配对效果并训练 scorer，决定 RAG 中是否修订草稿答案，在 9 组设置中优于草稿置信度 scorer
practical_value: '- 在 Agent/RAG 工作流中，不要默认「检索后一定修订」。可离线构造配对数据：用同一 judge 给草稿和修订后的答案打分，训练
  recoverability scorer 来决定是否执行修订，避免过度修订带来的时延和成本。

  - 评价修订策略时，除了 accuracy，使用 accuracy–revision-rate 曲线和 oracle gap 指标；这能区分「修订有价值」和「修订只是增加调用次数」。

  - 如果系统已经有标准 RAG 答案，优先把决策建模成「草稿 vs RAG 答案」的二选一，而不是为复杂的三选一引入候选修订；实验表明增加第三个选项无显著收益，工程实现更简单。

  - 对电商客服问答、商品问答等场景，可用业务评判器标注「修订后是否解决、是否引入错误」，训练一个轻量 scorer 控制检索修订的触发，减少不必要的检索和生成开销。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：已有答案修订系统需要决定是返回现有草稿答案，还是用检索证据修订。仅靠草稿置信度无法估计具体修订的收益或损害。

方法：在离线训练和评估中，用同一正确性评判器同时给草稿和候选修订打分，使修复、损害及与 oracle 的差距可观测；将这一配对效果定义为 recoverability，并训练 scorer 在修订前预测它。

结果：在 25,870 个开放域问题上、三种修订设置下，recoverability scorer 的 accuracy–revision-rate 曲线下面积在全部 9 个 Llama 设置-种子拟合中均高于同等的草稿置信度 scorer；在开发集选择阈值下平均提升 0.23–0.68 个准确率点，但跨训练运行的差异仅在稠密检索下显著。策略优于始终修订，平均缩小超过 1/3 的 oracle 差距，但仍应用 38–46% 的有害修订。若另有 draft-free 标准 RAG 答案可选，在草稿与该答案之间选择更强（Llama 约 2 点、OLMo 约 4 点），把候选修订作为第三选项无显著增益。
