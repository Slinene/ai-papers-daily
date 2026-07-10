---
title: Towards Mechanistically Understanding Why Memorized Knowledge Fails to Generalize
  in Large Language Model Finetuning
title_zh: 理解LLM微调中记忆知识为何难以泛化的机制
authors:
- Lu Dai
- Ziyang Rao
- Yili Wang
- Hanqing Wang
- Hao Liu
- Hui Xiong
affiliations:
- HKUST(GZ)
- HKUST
arxiv_id: '2607.08393'
url: https://arxiv.org/abs/2607.08393
pdf_url: https://arxiv.org/pdf/2607.08393
published: '2026-07-09'
collected: '2026-07-10'
category: Training
direction: LLM微调 · 知识泛化与电路错位
tags:
- Knowing-Using Gap
- self-patching
- memorization
- generalization
- knowledge-circuit misalignment
- fine-tuning
one_liner: 揭示“知用鸿沟”：记忆的表示存在但未路由到有效计算层，提出自修补干预可恢复58-75%的泛化失败
practical_value: '- **微调注入新知识后推理失败的诊断**：在电商/Agent场景中，若微调后模型能记忆商品属性但无法正确回答组合推理（如“哪个去年发布的手机拍照最好”），可通过自修补（self-patching）分析内部激活定位，找出哪些层的表示未参与推理，指导后续模型优化。

  - **无需重新训练即可部分修复推理**：采用简单的启发式规则（如将某些层的记忆表示转移到关键计算层），可快速恢复泛化能力，适合在线知识更新后紧急修复推理表现，成本低。

  - **微调策略的启示**：设计训练损失时，应考虑让与推理相关的深层也参与记忆表示的学习，或加入辅助任务迫使知识表示向有效计算层对齐，避免“知用鸿沟”。

  - **模型调试工具**：自修补方法可作为内部调试工具，用于持续集成测试中自动检测新知识注入后的推理衰退，降低线上事故风险。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM微调注入新知识时常出现“能记住但不会用”的现象，即模型可以正确输出记忆的事实（如悉尼在[X]），但无法在需要推理的问题（如悉尼所在国家的首都是？）中使用该知识。作者将这一问题形式化为“知用鸿沟”（Knowing-Using Gap），表现为记忆准确率和推理准确率间的差距及时间滞后。

**方法**：通过微调引入未见知识，并利用一种新颖的干预技术“自修补”（self-patching）来监测知识在模型内部的扩散动态。自修补识别出那些将激活表示重新定位后能显著改善失败推理案例的位置。

**关键结果**：实验发现知识存在但未被路由到计算有效的层，即“知识电路错位”假设。基于该诊断，设计了一个简单的启发式策略，能够恢复泛化失败中58-75%的oracle改进空间，且跨领域实验验证了结论的鲁棒性。
