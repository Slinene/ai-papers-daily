---
title: Detecting Inconsistencies in Model Specifications with LLM-as-Verifier Reasoning
title_zh: 用 LLM 验证推理检测模型规范中的不一致
authors:
- Zichen Xie
- Mrigank Pawagi
- Lize Shao
- Yang Hu
- Wenxi Wang
affiliations:
- University of Virginia
- University of Pennsylvania
- The University of Texas at Austin
arxiv_id: '2610.01847'
url: https://arxiv.org/abs/2610.01847
pdf_url: https://arxiv.org/pdf/2610.01847
published: '2026-10-01'
collected: '2026-10-04'
category: LLM
direction: LLM 规范审计与一致性验证
tags:
- LLM-as-verifier
- Model specs
- Inconsistency detection
- Reasoning
- Alignment
one_liner: 提出 VeriSpec，通过保留自然语言并用 LLM 作为验证器，直接审计模型规范文本以检测规则冲突
practical_value: '- 电商/推荐系统中存在大量业务规则（合规、风控、用户体验、商业目标），这些规则可能在特定场景下冲突，可将规则文档视为规范，用
  VeriSpec 的思路自动提取结构化规则并构造 topic-guided graph 聚类相关规则，再用 LLM 逐对/逐组验证冲突。

  - 对于 Agent 或多智能体系统的策略规范，同样存在多策略冲突问题，可采用"保留自然语言 + LLM-as-verifier"的方式避免形式化损失，直接审计规范文本，提前发现策略缺陷，而不是等行为测试或线上事故。

  - 在检索/推荐评估中，如果有多个评估标准或 rubric，也可以用该方法检测标准之间的不一致，提升评估体系的可靠性。

  - 该方法成本较低（每个已验证不一致 $11.12），适合周期性对业务规则进行离线审计，作为规则上线前的检查步骤。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：模型规范定义 LLM 应如何行为，指导对齐训练、推理行为和评估。但规范本身可能存在缺陷：两个单独看来合理的规则在同一场景下可能要求不兼容的行为，导致没有响应能同时满足。检测这类不一致很难：形式化自然语言规范会丢失细微差别，行为测试又无法区分规范缺陷与模型行为差异。

**方法关键点**：VeriSpec 是首个直接审计规范文本的方法。核心洞察是保留自然语言，同时用 LLM 作为验证器。流程为：①从规范中提取结构化、上下文感知的规则；②构建 topic-guided graph，将行为相关且处于同一权威等级的规则聚类；③应用 LLM-as-verifier 推理检测成对或成组规则的不一致。该设计避免了形式化损失，并能利用 LLM 的语义推理能力发现冲突。

**关键结果**：在 OpenAI Model Spec 上应用，提取 405 条规则，人工验证 5 处不一致，均已报告给开发者，获积极回应并启动内部讨论。与五个基线相比，VeriSpec 识别出最多的已验证不一致，准确率最高达 38.5%，每个已验证不一致的成本最低仅 $11.12。结果表明直接规范审计是行为对齐评估的实用补充，能在规范影响模型之前从源头发现缺陷。
