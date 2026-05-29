---
title: 'Same Evidence, Different Answers: Canonical-Context On-Policy Distillation
  for Multi-Turn Language Models'
title_zh: 相同证据，不同答案：面向多轮语言模型的规范上下文在线策略蒸馏
authors:
- Zizhuo Lin
- Quanling Liu
- Jinsheng Quan
- Chao Zhang
- Yifan Zhu
- Xing Shi
- Jingtao Xu
- Zhihui Li
- Yawei Luo
affiliations:
- Zhejiang University
- University of Science and Technology of China
arxiv_id: '2605.30251'
url: https://arxiv.org/abs/2605.30251
pdf_url: https://arxiv.org/pdf/2605.30251
published: '2026-05-28'
collected: '2026-05-29'
category: Training
direction: 多轮对话一致性 · 在线策略自蒸馏
tags:
- Self-anchored drift
- Canonical-context consistency
- On-policy distillation
- Reverse KL
- Multi-turn dialogue
- LoRA
one_liner: 提出 CCOPD 自蒸馏方法，通过冻结的完整上下文教师来矫正多轮分片输入下的答案，消除自我锚定漂移，仅用数学训练即可泛化至多种任务。
practical_value: '- 多轮交互下的答案一致性提升：在客服、推荐问卷、Agent 任务等逐渐收集用户需求的场景中，早期不完整回答容易引入错误先验。借鉴
  CCOPD，可以用完整上下文的模型输出作为监督信号，对齐最终回复分布，缓解模型被自身历史“带偏”。

  - 低成本训练策略：教师和学生使用同一基础模型，无需额外大模型或人工标注，仅需构造任务等价的分片-完整对，并通过 on-policy reverse KL 优化。训练数据仅用了数学题，却能零样本迁移到代码、SQL、摘要等任务，说明学到的是通用的证据锚定能力，适合资源有限的业务快速部署。

  - 注意力和诊断工具可复用：文中提出的 SAAR（自锚注意力比）和 neutral-placeholder 替换实验，可用来探测业务多轮对话模型是否过度依赖自身历史回复，从而针对性地优化提示或训练数据。

  - 训练范式优于推理时修复：与推理时反思或重置策略相比，CCOPD 将一致性内化到模型权重中，不增加推理延迟，适合对延迟敏感的在线应用。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
大型语言模型在多轮对话中面临“自我锚定漂移”问题：当用户需求通过多个轮次逐步给出时，模型在前几轮由于信息不足，容易产生猜测性回答，这些早期回复会成为后续推理的强锚点，即使最终轮用户已提供完整信息，模型仍可能偏离正确答案，与一次性给出全部信息时的结果不一致。现有解决方案多在推理时借助反思或重置等外部控制循环，增加系统复杂度和延迟。本文提出将多轮下的一致性内化为模型核心能力，通过训练消除自我锚定漂移。

**方法关键点**
- **规范上下文在线策略蒸馏（CCOPD）**：对每个任务构造一对数据——干净的完整提示（FULL）与逐步揭示的原始分片历史（RAW-SHARDED）。教师模型（冻结的基础模型）以 FULL 为条件，学生模型（可训练）以 RAW-SHARDED 历史为条件。
- **同模型自蒸馏与回答掩码**：教师与学生共享同一 backbone，仅在最终答案位置上计算 reverse KL 损失，避免对中间不确定轮次施加过度约束。教师只在学生生成的答案前缀上给出概率评分，不输出完整文本。
- **在线采样与训练**：学生从自己的交互轨迹中采样答案前缀，教师对相同前缀评分的分布对齐，形成跨呈现方式的监督信号。训练仅使用 GSM8K 数学题对应的分片对话，通过 LoRA 适配器进行。

**关键实验与结果**
在 Qwen3-8B 上，CCOPD 将数学 RAW-SHARDED 准确率从 66.0% 提升至 82.5%（+16.5），同时对 FULL 准确率无影响（90.3%）。更关键的是，该数学训练信号零样本迁移至五个非数学任务（代码、函数调用、text-to-SQL、表格到文本、长摘要），非数学 RAW-SHARDED 平均得分从 36.8 提高到 49.7（+12.9），全任务平均相对提升 32%。对比 SFT 和 GRPO 等基线，CCOPD 在 RAW-SHARDED 上增益更显著且不损害 FULL 性能。消融实验表明：reverse KL 优于 forward KL；使用同 backbone 教师效果优于引入更大或更小的外部教师。SAAR 和中性占位符诊断证实，CCOPD 增强了模型对完整用户证据的注意力，降低了模型对自身前序输出中噪声的敏感度。

**一句话总结**：CCOPD 通过在模型内部对比完整与分片两种输入，强制最终答案对齐完整证据分布，实现了轻量、可迁移的多轮一致性提升。
