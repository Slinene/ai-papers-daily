---
title: Towards Detecting Inconsistencies in End-to-end Generated TODs
title_zh: 面向端到端生成任务型对话的不一致性检测
authors:
- Tiziano Labruna
- Giovanni Bonetta
- Bernardo Magnini
affiliations:
- Fondazione Bruno Kessler
arxiv_id: '2607.09338'
url: https://arxiv.org/abs/2607.09338
pdf_url: https://arxiv.org/pdf/2607.09338
published: '2026-07-10'
collected: '2026-07-13'
category: Eval
direction: 约束满足问题用于对话一致性检测
tags:
- Task-Oriented Dialogue
- Constraint Satisfaction Problem
- Consistency Detection
- Hallucination
- LLM Evaluation
one_liner: 将任务型对话建模为约束满足问题，利用CSP求解器自动检测不一致并建议最小修复
practical_value: '- 在电商对话助手的商品推荐、订单查询等场景中，将商品属性（价格、库存、类别）和对话约束（用户偏好）转化为CSP变量与约束，对LLM生成的回复进行事后校验，捕捉幻觉（如推荐不存在的商品、价格矛盾）。

  - 可集成到对话系统的后处理管道中，作为一道安全网：给定知识库和对话历史，自动识别不一致的片段并建议最小修改（例如替换错误实体），提升系统可靠性和可解释性，无需额外训练。

  - CSP建模方式灵活性高，可适应不同领域的约束，例如餐厅预订的日期、人数、位置限制，或电商物流的地址、配送范围等，适合多域对话系统的质量保障。

  - 对话轨迹与有效变量赋值的对比可生成诊断信息，辅助人工审核或在线修复，降低高风险场景（如支付、预约）的业务故障率。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：端到端生成式任务型对话系统（TOD）虽然灵活，但LLM容易产生不一致，如虚构知识库中不存在的实体，导致任务失败。传统组件式系统有明确状态追踪和策略，而端到端生成缺乏可校验的内部结构，因此迫切需要自动检测不一致的方法。

**方法**：将TOD形式化为一个约束满足问题（CSP）。对话中的实体、属性等被定义为变量，对话的连贯性、知识库事实、用户约束等被编码为变量间的约束。提出两阶段流水线：首先从目标对话中识别出所有变量，然后运用CSP求解器计算满足所有约束的有效赋值。通过比较原始对话中的变量赋值与求得的有效赋值，可以定位不一致之处，并基于求解器的反馈给出最小修改建议（例如修正一个槽位值）以恢复一致性。

**结果**：在酒店预订等任务型对话数据集上，CSP方法能以高准确率检测出插入、替换、删除等不同类型的不一致；分析显示该方法精确率高，能够细粒度指出错误片段，为对话系统的可靠性保障提供了形式化、可解释的解决方案。
