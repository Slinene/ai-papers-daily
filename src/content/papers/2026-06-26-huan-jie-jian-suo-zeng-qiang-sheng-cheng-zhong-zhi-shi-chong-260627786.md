---
title: 'SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict Mitigation
  in Retrieval-Augmented Generation'
title_zh: 缓解检索增强生成中知识冲突的门控调制激活引导方法
authors:
- Ruochang Li
- Pengcheng Huang
- Zhenghao Liu
- Yukun Yan
- Huiyuan Xie
- Yu Gu
- Ge Yu
- Maosong Sun
affiliations:
- Northeastern University
- Tsinghua University
arxiv_id: '2606.27786'
url: https://arxiv.org/abs/2606.27786
pdf_url: https://arxiv.org/pdf/2606.27786
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: 门控机制自适应调节激活以解决知识冲突
tags:
- RAG
- Knowledge Conflict
- Gate Modulation
- Activation Steering
- LLM
- Parameter-Efficient
one_liner: 提出 SHIFT，用可学习门控模块替代神经元编辑，自适应调节激活，以低于 0.01% 参数解决 RAG 知识冲突
practical_value: '- 可借鉴轻量门控模块（训练参数 <0.01%）插件式插入 LLM，冻结骨干，在不损害通用能力的前提下提升 RAG 冲突场景下的上下文遵循度，适合低资源快速适配。

  - 门控调制激活的方式比神经元定位和层固定规则更灵活，可在电商搜索推荐中的商品知识增强、客服问答等 RAG 场景使用，避免因知识冲突产生错误推荐。

  - 该方法属于参数高效微调，可与现有 PEFT 方案（如 LoRA）叠加，工程实现成本低，可直接嵌入到已有 RAG 管线。

  - 论文在多个数据集上验证，开源代码可直接复用，适合业务团队快速验证门控激活引导在自身场景的效果。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RAG 系统引入检索上下文时，常发生上下文与 LLM 内部参数知识冲突，导致模型忽略上下文或产生幻觉。现有方案通过定位并编辑知识相关神经元来缓解冲突，但神经元粒度的修改会引发级联效应，损害模型通用能力。

**方法**：提出 SHIFT，将神经元级修改重构为可学习的门控调制。在冻结的 LLM 中插入轻量门控模块（训练参数量 <0.01%），门控模块根据输入自适应调节隐藏状态激活值，使模型在参数知识和检索上下文间动态平衡。训练时仅优化门控参数，不修改原模型。

**关键结果**：在 6 个涵盖不同知识冲突类型的数据集上，SHIFT 在上下文一致性、答案准确率等指标上均超越神经元编辑、层固定规则等基线方法，同时显著减少对通用能力的负面影响。该框架兼具参数高效和即插即用特性，为 RAG 知识冲突解决提供了新范式。
