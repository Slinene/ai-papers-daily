---
title: Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement
  Learning
title_zh: 基于强化学习的视觉接地自我反思训练框架
authors:
- Liyan Tang
- Fangcong Yin
- Greg Durrett
affiliations:
- The University of Texas at Austin
- New York University
arxiv_id: '2607.02490'
url: https://arxiv.org/abs/2607.02490
pdf_url: https://arxiv.org/pdf/2607.02490
published: '2026-07-02'
collected: '2026-07-05'
category: Multimodal
direction: 视觉接地自我反思 · 强化学习
tags:
- self-reflection
- reinforcement learning
- vision-language model
- out-of-distribution
- prefix masking
- experience replay
one_liner: 通过轨迹前缀掩码与经验回放缓冲区训练视觉语言模型在分布外场景下进行视觉接地的自我反思与修正
practical_value: '- 在多模态对话推荐 Agent 中，可借鉴前缀掩码训练策略：随机遮盖 CoT 前半段，迫使模型仅从中间错误状态恢复，提升对推荐理由或商品比较链路的自我纠正鲁棒性。

  - 搜索广告系统中的多模态创意理解模块，可引入经验回放缓冲区存放历史失败案例，通过 RL 让模型反复修正不准确的视觉描述或关键词，增强对长尾商品图片的把握。

  - 利用 RL 直接优化自我反思能力，而非仅依赖 SFT 模仿正确链，可让对话推荐 Agent 在陌生领域（如新品、冷启商品）更有效地利用视觉信息进行纠正，避免单一依赖文本模式。

  - 轨迹前缀掩码思路也可用于文本 Agent 的自我修正训练：在搜索 Query 改写或回复生成中，随机删除前序推理步骤，让模型学会从半途错误中恢复，降低对初始思路的依赖。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有视觉语言模型在 CoT 推理中常忽视视觉输入，导致自我反思时无法将文本反馈转化为视觉接地的纠正，在分布外（OOD）图像上尤其严重。

**方法关键点**：提出 VRRL 强化学习框架，用两个新组件激发视觉接地的自我反思：① **轨迹前缀掩码**：训练时随机遮盖 CoT 前半部分，迫使模型从错误的中间预测（而非初始错误）中恢复，强化修正能力。② **缓冲滚动输入**：从经验回放缓冲区采样历史失败状态作为训练起始点，让模型接触多样化的错误模式并学会纠正。

**关键结果**：在表格、图表视觉接地任务及空间导航基准上，相比标准 RL 和仅面向反思的微调基线，VRRL 大幅提升 OOD 平均准确率，有效缓解了分布漂移下的性能退化。
