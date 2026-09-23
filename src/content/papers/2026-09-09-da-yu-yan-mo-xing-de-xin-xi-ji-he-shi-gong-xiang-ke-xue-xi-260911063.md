---
title: The information geometry of large language models is shared, learned, and controllable
title_zh: 大语言模型的信息几何是共享、可学习且可控的
authors:
- Dario Picozzi
affiliations:
- Department of Physics and Astronomy, University College London (UCL)
- London Centre for Nanotechnology
arxiv_id: '2609.11063'
url: https://arxiv.org/abs/2609.11063
pdf_url: https://arxiv.org/pdf/2609.11063
published: '2026-09-09'
collected: '2026-09-23'
category: LLM
direction: LLM 信息几何与控制
tags:
- Fisher-Rao geometry
- LLM
- model steering
- interpretability
- natural gradient
- output geometry
one_liner: 用 Fisher-Rao 输出几何揭示 LLM 共享结构并给出最小扰动局部控制方法
practical_value: '- 做 LLM 推荐/搜索时，若要对模型进行编辑/steering/微调，用输出概率的 Fisher-Rao 几何做正则或自然梯度，能比
  Euclidean 激活距离更少扰动无关行为，适合在多任务推荐/广告文案模型中做局部行为调整。

  - 该几何下学到的控制更新可在 donor prompt 上学、迁移到 unseen prompts，类似可复用 prompt steering；可用于电商 query
  改写、营销文案风格控制，同时保持参考 prompt 行为稳定。

  - 共享的输出几何支持语义类别迁移，跨 Transformer/SSM/RNN 架构一致，说明可以基于输出分布对齐做跨模型蒸馏或跨域迁移，而不是强求激活空间对齐。

  - 预训练语料统计可预测 held-out fact acquisition，提示在训练推荐/广告大模型时，可监控语料侧统计指标提前判断知识/事实掌握，减少昂贵评估。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM 行为相似但共享结构不清，且改变单一行为容易干扰其他行为；激活空间坐标不唯一，常用 Euclidean 距离/内积在重参数化下不稳定。

方法关键点：改用 next-token 概率的 Fisher-Rao 几何，行为在输出保持对称下唯一决定几何。跨 Transformer、状态空间和循环模型比较输出几何与激活几何；用模型逐 token 概率和 read-out 几何预测谱与有效维度；做受控语言分配、随机证据深度实验；基于该几何推导最小扰动局部干预，并在 donor prompt 上学习控制更新迁移到 unseen prompt。

关键结果：输出几何一致性显著高于激活几何；共享几何支撑语义类别迁移；与人类选词一致性随预测准确度、规模、训练提升，模型校正后进一步提升；预训练语料统计可无重校准预测 held-out 事实习得；更深证据在所有架构和证据构造中显著推迟习得；几何干预预测相对成本，迁移控制比 Euclidean 控制更好保持参考行为，并改善 steering、editing、attribution、dictionary learning、fine-tuning。
