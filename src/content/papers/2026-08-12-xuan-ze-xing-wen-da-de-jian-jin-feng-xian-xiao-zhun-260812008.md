---
title: Asymptotic Risk Calibration for Selective Question Answering
title_zh: 选择性问答的渐近风险校准
authors:
- Shufan Lin
- Sijin Dong
affiliations:
- Zhangjiang University
- Ibaraki University
arxiv_id: '2608.12008'
url: https://arxiv.org/abs/2608.12008
pdf_url: https://arxiv.org/pdf/2608.12008
published: '2026-08-12'
collected: '2026-08-13'
category: Eval
direction: LLM 不确定性校准与选择性拒答
tags:
- selective question answering
- uncertainty calibration
- conformal risk control
- LLM
- abstention
- risk control
one_liner: 模型无关的事后校准框架，为LLM选择性问答提供渐近错误率控制，无需训练即可搭配任意不确定性估计器
practical_value: '- 在电商客服、商品问答、搜索摘要等场景，当LLM输出需要保障准确率时，可借鉴A-CRC-QA的事后校准思路，在验证集上对不确定性分数进行单调化校准，获得满足目标错误率的动态拒答阈值，而不是拍脑袋固定阈值。

  - 方法模型无关、无需训练，可与多种不确定性估计（如语义一致性、perplexity、self-consistency）结合，非常适合快速集成到现有LLM服务中，以最小成本提高输出可靠性。

  - 对于推荐/搜索中的Agent决策（如自动生成推荐解释、选品理由），可应用类似风险控制，对Agent最终输出进行选择性过滤，降低向用户展示错误信息的概率，并量化控制风险。

  - 注意方法针对渐近控制，工程上需积累足够校准集并定期更新阈值，以应对数据分布漂移。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
LLM在问答中可能生成流畅但错误答案，需要不确定性量化来保障可靠性。但启发式不确定性分数无法完美区分对错，固定阈值缺乏统计控制，导致无法保证接受答案的错误率。

## 方法关键点
A-CRC-QA 将选择条件下的错误控制重构为线性期望约束，采用单调化经验风险校准过程（受 conformal risk control 启发）。由于实例损失对接受阈值一般非单调，框架目标为渐近而非有限样本风险控制。方法模型无关、无需训练，可与不同不确定性估计器结合。

## 关键结果
在 CoQA（开放式）和 MedMCQA（封闭式）数据集上验证，与未校准和基于置信边界的基线相比，A-CRC-QA 在答案可靠性与答案保留率之间取得更优权衡，能在统计控制下降低接受答案的错误率，同时保留更多回答。
