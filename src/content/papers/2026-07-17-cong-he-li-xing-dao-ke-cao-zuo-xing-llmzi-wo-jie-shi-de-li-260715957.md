---
title: 'From Plausible to Actionable: A Position on LLM Self-Explanations'
title_zh: 从合理性到可操作性：LLM自我解释的立场观点
authors:
- Elize Herrewijnen
- Benedetta Muscato
- Gizem Gezici
- Fosca Giannotti
affiliations:
- University of Utrecht
- National Police Lab AI, Netherlands Police
- Scuola Normale Superiore
- University of Pisa
arxiv_id: '2607.15957'
url: https://arxiv.org/abs/2607.15957
pdf_url: https://arxiv.org/pdf/2607.15957
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: LLM 自我解释的可信度与可操作性
tags:
- LLM
- Self-explanation
- Explainability
- Faithfulness
- Plausibility
- Actionability
one_liner: 区分自我解释的合理性、忠实度与可操作性，提出兼顾三者的评估框架
practical_value: '- 在推荐/搜索场景中，用 LLM 生成推荐理由或查询解释时，不能仅满足于表面合理（plausible），需要额外设计忠实度（faithfulness）检测机制，例如核对解释中的关键事实是否与模型内部注意力或决策路径一致。

  - 将解释的评估从「人对合理性的主观判断」拓展到「下游任务可操作性」：比如将解释作为 Agent 下一步动作的依据（如触发退款、调整排序），通过解释能否准确引导后续决策来反向验证。

  - 工程实现上，可构建「解释-动作闭环」：记录解释中的关键声明，用规则或小模型自动校验其与系统实际决策逻辑的匹配度，对不一致的做标记或抑制。

  - 对于电商搜索的查询推荐（QueryRec），LLM 给出的推荐理由（如「为您推荐‘蓝牙耳机’因为近期浏览过」）需确保忠实反映用户行为序列，避免生成虚构理由，可将用户日志与解释对比做线上校验。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 能生成自然语言形式的自我解释（self-explanations），这种解释在人看来往往合理（plausible），但其是否忠实反映模型内部真实的推理过程（faithfulness）存疑。传统 XAI 评估多关注合理性而忽视忠实度与下游可操作性，导致解释可能误导用户或决策者。

**方法关键点**：本文是一篇立场观点文，系统梳理了自我解释的三个核心维度——合理性（plausibility）、忠实度（faithfulness）和可操作性（actionability）。作者指出标准评估协议在衡量忠实度上的局限（如仅靠人工打分不可靠），提出需结合模型内部状态（注意力、激活）与外部行为一致性来综合判断。并强调可操作性应成为评估的必要部分：解释是否帮助不同利益方做出合适决策、采取正确行动。

**关键结论**：自我解释可以是“高合理性、可疑忠实度、但高可操作性”的。评价体系应转向以可操作性为导向，例如在医疗、司法等高风险场景，解释能否引导人类正确采纳或拒绝模型建议，其价值远超表面是否通顺。文章呼吁 XAI 社区重新定义评估标准，将解释的效用纳入闭环。
