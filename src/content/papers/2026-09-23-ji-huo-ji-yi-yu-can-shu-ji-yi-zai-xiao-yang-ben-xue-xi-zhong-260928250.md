---
title: Complementary Roles of Activation and Parametric Memory in Few-Shot Learning
title_zh: 激活记忆与参数记忆在小样本学习中的互补作用
authors:
- Miaohe Niu
- Runsong Zhao
- Xinyu Liu
- Bo Jin
- Yucheng Qiao
- Chunliang Zhang
- Jingbo Zhu
- Tong Xiao
affiliations:
- Northeastern University, Shenyang, China
- NiuTrans Research, Shenyang, China
arxiv_id: '2609.28250'
url: https://arxiv.org/abs/2609.28250
pdf_url: https://arxiv.org/pdf/2609.28250
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM记忆机制与测试时训练
tags:
- LLM
- In-Context Learning
- Test-Time Training
- KV Cache
- Neuron Analysis
- Few-Shot Learning
one_liner: 系统比较LLM中激活记忆与参数记忆的差异，发现事实回忆靠激活记忆，复合任务需二者协同
practical_value: '- 在电商/Agent 的上下文管理中，事实性信息（如商品属性、历史订单）放进 KV cache 或 prompt 即可稳定回忆，不必为此做在线参数更新。

  - 对需要“先查事实再执行新规则”的复合任务（如促销规则叠加用户偏好），仅靠 ICL 或仅靠微调都不够，架构上应同时保留激活记忆和轻量参数更新两条路径。

  - 神经元分析表明两类记忆激活不同神经元群：模型可解释性排查时，可判断失败原因是上下文丢失还是参数适应不足，再针对性修复。

  - 整体为机制研究，业务可借鉴点有限，但可作为混合记忆设计（RAG + 测试时训练）的理论依据。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**
LLM 在测试时可通过激活记忆（即 KV cache）和参数记忆（即参数更新）编码历史信息，但二者在 few-shot learning 中的分工与协同机制不清。

**方法关键点**
通过受控实验分别评估激活记忆与参数记忆在事实回忆和新任务学习上的表现；设计 Conditional Arithmetic 复合任务，要求模型先调用事实再执行规则；进一步做神经元级分析，定位同一历史信息经两种记忆访问时激活的神经元集合。

**关键结果**
激活记忆在事实回忆上显著更强；参数记忆在任务学习上并不一致优于激活记忆；Conditional Arithmetic 必须两类记忆同时在场。神经元分析显示两类记忆激活不同神经元集，组合时模型同时召集两组神经元，仅靠单一记忆无法完成该复合任务。这提示复合任务依赖激活与参数记忆的协作。
