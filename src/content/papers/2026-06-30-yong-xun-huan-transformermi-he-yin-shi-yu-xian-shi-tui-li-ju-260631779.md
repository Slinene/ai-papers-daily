---
title: Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers
title_zh: 用循环Transformer弥合隐式与显式推理差距
authors:
- Ying Fan
- Anej Svete
- Kangwook Lee
affiliations:
- UW-Madison
- Microsoft Research
- ETH Zürich
- KRAFTON
- Ludo Robotics
arxiv_id: '2606.31779'
url: https://arxiv.org/abs/2606.31779
pdf_url: https://arxiv.org/pdf/2606.31779
published: '2026-06-30'
collected: '2026-07-01'
category: Reasoning
direction: 隐式CoT推理加速 · 循环Transformer
tags:
- latent reasoning
- looped transformers
- chain-of-thought
- inference efficiency
- supervision on latents
one_liner: 首次在3B规模用循环Transformer+并行监督弥合隐式与显式思维链性能差距，并降低推理延迟2.5-6.9倍
practical_value: '- 在电商搜索推荐Agent中，可用隐式循环推理替代显式CoT，将多步决策压缩为并行隐状态迭代，显著降低线上延迟；需为每个推理步设计中间监督信号（如意图、子查询），可用已有行为数据或蒸馏构造。

  - 循环权重共享在不增加参数的前提下加深推理深度，适合线上部署的资源受限环境，可直接应用于Agent的轻量级推理模块。

  - 可解释性验证技巧（将隐状态投影至词表）可用于监控Agent推理过程，确保推荐/搜索决策的合理性与可解释性。

  - 若业务存在用户决策路径数据（如浏览-加购-购买），可仿照中间步骤监督，训练隐式推理模型以加速商品推荐理由生成或解释生成。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机：** 显式思维链（CoT）推理需逐token解码，延迟高；隐式CoT在隐藏状态推理效率高，但在1B以上模型性能显著劣于显式CoT，且差距随模型规模增大。循环Transformer（权重共享、增加深度的同时不增参数）天然适合隐式推理，但此前尚未被系统探索。

**方法关键点：** 提出LOTUS（Looped Transformers with parallel supervision on latents）：一个循环填充Transformer，将K个隐式块并行处理R次迭代，并在每个隐式位置上用交叉熵损失监督对应的黄金CoT步骤token，实现并行监督。推理时，模型在隐藏空间完成多步思考，无需逐一解码中间token，最后一次性输出答案。

**关键结果：** 在3B参数量级上，LOTUS首次达到与显式CoT相当的准确率，弥合了性能差距；同时将思考阶段延迟降低2.5-6.9倍（从紧凑数学表达式到自然语言）。将循环后的隐变量通过基础LM头投影，可恢复黄金推理步骤甚至出现替代有效中间步骤，表明隐空间可解释且与CoT对齐。消融证实循环骨干和并行监督均不可或缺。
