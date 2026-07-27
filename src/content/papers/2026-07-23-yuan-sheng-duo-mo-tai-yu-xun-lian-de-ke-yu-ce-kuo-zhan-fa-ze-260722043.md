---
title: Scaling Native Multimodal Pre-Training From Scratch
title_zh: 原生多模态预训练的可预测扩展法则
authors:
- Haoyuan Wu
- Aoqi Wu
- Hai Wang
- Jiajia Wu
- Jinxiang Ou
- Bei Yu
affiliations:
- The Chinese University of Hong Kong
- Tencent
arxiv_id: '2607.22043'
url: https://arxiv.org/abs/2607.22043
pdf_url: https://arxiv.org/pdf/2607.22043
published: '2026-07-23'
collected: '2026-07-27'
category: Multimodal
direction: 多模态缩放法则与训练效率前沿
tags:
- multimodal pre-training
- scaling laws
- compute-optimal
- cross-modal transfer
- vision-language model
one_liner: 发现原生多模态预训练的损失、模型大小与数据量遵循幂律，数据配比影响计算最优分配，且存在跨模态正向迁移
practical_value: '- **多模态训练预算分配**：固定计算资源下，模型参数量与训练token数存在幂律最优关系，可参考其拟合公式，在训练电商多模态模型（如图文商品理解）时合理分配扩大模型或增加数据的投入。

  - **数据混合策略**：文本占比高的多模态混合数据在模型规模较小时不划算，只有大模型才能高效利用，提示在设计电商多模态预训练数据（如商品标题+图片）时，若算力有限可适当提高图片/视觉token比例以获得更快收敛。

  - **跨模态能力迁移**：多模态预训练能提升纯文本空间推理，可用于电商场景中需要空间理解的推荐（如家具摆放、服装搭配），无需额外标注即可增强模型的几何关系推理。

  - **少样本多模态上下文学习**：原生多模态预训练使模型具备稳健的多模态上下文学习能力，可借鉴到少样本商品属性提取、图文匹配验证等任务中，减少对大量标注的依赖。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有大规模多模态模型多从文本预训练LLM后期扩展视觉模块，存在视觉-语言优化不对称；而从零开始的原生多模态预训练虽能深度跨模态融合，但其缩放特性（如模型大小、数据量、数据配比与计算预算的关系）尚未被系统研究。

**方法**：在固定计算预算下，训练不同规模的Transformer视觉-语言模型，探索损失、最优模型参数量、最优训练token数与计算量之间的幂律关系（compute law 与 allocation law）。特别考察纯语言目标与多模态目标的缩放行为差异，以及数据中图文混合比例对最优配置的影响。

**关键结果**：
- 损失与计算量遵循可预测的幂律缩放，最优模型大小和token数亦随计算量幂律增长。
- 语言目标的缩放行为对数据配比不敏感，而多模态目标的缩放高度敏感：文本占比高的混合数据仅在大模型下才计算高效，迫使最优资源向更大模型倾斜。
- 通过建模数据配比对缩放指数的影响，推导出效率前沿，可精确配置模型大小、token数与数据混合。
- 下游评估发现，原生多模态预训练带来正向跨模态迁移：纯文本空间推理能力提升，且能进行稳健的多模态上下文学习。
