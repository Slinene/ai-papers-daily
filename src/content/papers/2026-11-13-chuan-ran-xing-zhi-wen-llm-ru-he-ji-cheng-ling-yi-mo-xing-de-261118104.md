---
title: 'Contagious Fingerprints: When LLMs Inherit Another Model''s Identity'
title_zh: 传染性指纹：LLM 如何继承另一模型的身份
authors:
- Zailong Tian
affiliations:
- Nanyang Technological University
arxiv_id: '2611.18104'
url: https://arxiv.org/abs/2611.18104
pdf_url: https://arxiv.org/pdf/2611.18104
published: '2026-11-13'
collected: '2026-11-16'
category: Eval
direction: LLM 指纹审计与多轮对话身份一致性
tags:
- LLM fingerprint
- API audit
- Multi-turn conversation
- Style imitation
- Statistical test
one_liner: LLM 指纹在多轮对话中会传染，破坏了基于静态参考的 API 审计，提出了上下文条件排名检验方法
practical_value: '- 多模型路由/级联场景（如贵模型首响、便宜模型承接多轮）需警惕指纹传染：监控或审计时应基于同一对话历史采样参考，不能用静态参考直接比对，否则误报率极高。

  - 电商/广告对话式 Agent 若在会话中途切换模型，用户感知差异可能被上下文风格掩盖；引入 LINEUP 类测试可无阈值地检测替换，且不需要访问模型 log-probabilities。

  - 评估模型一致性或上线 A/B 时，长对话上下文会驱动模型偏离自身静态特征；应使用同 prompt 历史下的对照样本，而非单独 baseline 对比。

  - 若业务依赖第三方 LLM 服务商，可借鉴预注册 + 交换性控制的检验框架，对 API 质量进行持续审计，防止以次充好。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 指纹通常被视为模型固定属性，是 API 审计的基础。本文发现指纹会传染：当模型继续另一个模型开启的对话时，它继承前一个模型的指纹。这破坏了 API 中继审计——服务商可以用客户付费的模型开始对话，后续悄然切换为更便宜的模型。

**方法关键点**：多轮对话中模型对历史风格的模仿导致指纹偏移。现有分类器在 fresh contexts 校准，把 history-dependent 回复与 history-free 参考比较，产生大量假阳性。为此提出 LINEUP：从声称模型在相同对话历史下采样参考，测试被审计回复在参考中的排名，通过 exchangeability 控制假阳性，无需拟合阈值或 log-probabilities。

**关键结果**：文本分类器检测替代品的准确率从 0.97 降至 0.72（DeepSeek 替换 Claude Sonnet），同厂商降级 Haiku 从 0.87 降至 0.54；在长上下文上诚实模型被误标率高达 1.00；LINEUP 在封闭模型上误报率 0.056（预注册边界 0.10），六对模型四轮审计后检测替代会话 0.81。
