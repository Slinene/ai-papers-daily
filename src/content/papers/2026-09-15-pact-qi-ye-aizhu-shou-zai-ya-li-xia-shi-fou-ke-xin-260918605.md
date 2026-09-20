---
title: 'PACT: Can Enterprise AI Assistants Be Trusted Under Pressure?'
title_zh: PACT：企业AI助手在压力下是否可信
authors:
- Mika Okamoto
- Ansel Kaplan Erol
affiliations:
- Georgia Institute of Technology
- Decagon AI
- Baseten
arxiv_id: '2609.18605'
url: https://arxiv.org/abs/2609.18605
pdf_url: https://arxiv.org/pdf/2609.18605
published: '2026-09-15'
collected: '2026-09-20'
category: Eval
direction: 企业LLM合规压力测试基准
tags:
- LLM
- Agent
- Compliance
- Evaluation
- Benchmark
- Enterprise AI
one_liner: PACT基准首次系统测量企业LLM助手在持久用户施压下的合规表现
practical_value: '- 在电商/客服Agent上线前，可借鉴PACT的「规则+违规捷径+压力注入」结构，构造针对售后、优惠、价格合规等场景的对抗式合规测试集，发现高违规风险模型。

  - 多轮对话中持续合规监控机制值得落地：不要只测单轮，要模拟用户反复施压、管理者催促等真实交互，并计算类似PACTScore的可靠性加权违规率作为模型选型硬指标。

  - 用LLM-as-judge审计样本构建测试集的方法可直接迁移：确保样本无歧义、不可通过识别评估意图取巧、且足够真实，避免模型评估时表现出「表演合规」。

  - 结果提示即使最强LLM也有6-10%规则误用率，且普通用户压力下违规率平均上升65%，因此电商Agent不能仅依赖模型自身对齐，必须外挂规则引擎或护栏（如政策校验、敏感操作二次确认）。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
企业LLM Agent正进入招聘、医疗、金融等受监管场景，规则遵守是首要法律风险。但现有评估框架没有系统测量模型在用户持续施压、管理者催促或违规看起来更方便时的合规表现，导致模型选型与护栏设计缺乏依据。

**方法关键点**
PACT覆盖12个受监管企业领域、48个多轮对话场景，每个样本将一条常设规则与一个违规捷径配对，并施加多种压力（不同措辞、系统提示模式）。构建过程采用LLM-as-judge严格审计，确保样本无歧义、不可取巧且足够真实。基于6个互补指标（多轮稳健性、透明度、规则适用判别等）生成PACTScore，即可靠性加权的合规率。

**关键结果数字**
在22个主流LLM上评估显示，模型间合规差异显著：最强助手在6-10%的样本上也错误应用规则；普通用户压力使平均违规率提高65%。PACT可作为企业LLM合规压力测试的基准，直接支撑模型选型与guardrail设计。
