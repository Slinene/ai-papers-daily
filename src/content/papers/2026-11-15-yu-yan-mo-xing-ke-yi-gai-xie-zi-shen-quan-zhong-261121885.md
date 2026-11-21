---
title: Language Models Can Rewrite Their Own Weights
title_zh: 语言模型可以改写自身权重
authors:
- Jiajun Fan
- Neil He
- Changyi Yang
- Andy Mao
- Xi Zhu
- Chaoran Cheng
- Kaiqu Liang
- Shuaike Shen
- Zetian Li
- Ruihan Guo
affiliations:
- UIUC
- CMU
- Rutgers
- Princeton
- Stanford
arxiv_id: '2611.21885'
url: https://arxiv.org/abs/2611.21885
pdf_url: https://arxiv.org/pdf/2611.21885
published: '2026-11-15'
collected: '2026-11-21'
category: LLM
direction: LLM自改写权重 · 无梯度自我优化
tags:
- self-rewriting
- weight editing
- self-improvement
- model repair
- emergent ability
one_liner: 27B模型通过自我诊断并编辑自身权重，无需训练实现持续自改进
practical_value: '- 借鉴“自诊断 + 定向权重编辑”代替全量微调：业务中的LLM4Rec/Agent策略模型线上出现bad case后，可让模型读取自身权重与失败样本，定位并修改少数关键权重方向，无需训练基础设施，部署成本低。

  - 迭代自编辑 + 小样本验证：模型只在留出的practice problems上验证edit有效后才提交，每次edit替换上一个；推荐系统线上策略可借鉴这种“自测再上线”闭环，避免坏更新。

  - 前向传播only，可在推理服上更新权重；改进写入权重，线上推理零额外开销；适用于需要快速修复的生成式推荐模型，如商品标题生成、query改写、广告文案模型。

  - 规模是前提：小模型自编辑会破坏模型，只有足够大的模型才能稳定自我改进；业务上若用小型LLM做推荐/Agent，不要直接套用self-rewriting，先评估模型规模与自我诊断能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM训练后冻结，改进需再训练或推理时增强，但训练成本高、推理时增强效果不持久。本文探索模型能否仅靠自身推理、无梯度无训练地改写自己的权重，实现永久提升。

**方法关键点**：给定自身权重、带评分的答案和运行自己的能力，27B模型诊断失败原因并编辑背后的权重；迭代多轮，只有自测通过才提交编辑，每次编辑替换上一个；利用hidden states对比成功与失败样本，削弱导致失败的hidden state方向；整个过程只需前向传播，无需反向传播，在单个GPU上数小时完成。

**关键结果**：首次编辑在未见过的490道数学题上提升6.6个百分点；连续8个编辑会话准确率持续上升；修复损坏副本：在未见的6个图像基准上从7%提升到70%，达到完整模型83%的能力；能力随规模出现，2B模型不做编辑，4B/9B模型自我破坏，只有27B模型能稳定改进并修复自己。
