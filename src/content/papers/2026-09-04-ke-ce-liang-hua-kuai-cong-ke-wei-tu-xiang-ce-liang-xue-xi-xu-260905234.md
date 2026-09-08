---
title: 'Measured Sliders: Learning Continuous Controls from Differentiable Image Measurements'
title_zh: 可测量滑块：从可微图像测量学习连续控制
authors:
- Yijia Chen
- Boyu Wei
- Xuanhua Yin
affiliations:
- School of Computer Science, The University of Sydney
arxiv_id: '2609.05234'
url: https://arxiv.org/abs/2609.05234
pdf_url: https://arxiv.org/pdf/2609.05234
published: '2026-09-04'
collected: '2026-09-08'
category: Other
direction: 扩散模型可控生成 · 可微测量
tags:
- Diffusion Models
- Controllable Generation
- Differentiable Measurement
- LoRA
- Disentanglement
one_liner: 提出Measured Sliders框架，用可微图像测量定义并学习连续图像属性控制，实现有序、选择性和可组合
practical_value: '- 可微图像测量作为监督信号，替代文本或学习表示来定义控制轴，让生成结果的属性变化与量化指标直接对齐。在电商商品图生成或广告创意生成中，可将亮度、饱和度、色温、构图等属性定义为可微函数，训练可控LoRA。

  - 可观测性测试在训练前筛选可学习属性，避免对不可控维度浪费训练资源。推荐系统或生成式推荐中可借鉴：先验证目标属性在隐空间/特征空间能否被可靠观测和优化，再投入训练。

  - 多个LoRA分支存储同一checkpoint，推理时免训练组合，不依赖联合激活。可复用到多属性可控生成场景，减少多任务训练成本，且组合时保持各方向独立性，类似推荐中的多目标解耦。

  - 训练后校准到实际图像变化单位，使不同控制强度可比，便于产品侧设定语义化滑块范围（如亮度+10%），提升用户体验和可控性。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：扩散模型连续滑块通常从文本或学习表示推导控制轴，其尺度与实际图像属性变化脱节，导致无法预知哪些属性可学习、难以比较控制强度、组合时产生干扰。需要一种以可观测图像属性为基准的统一控制框架。

**方法关键点**：
- 定义闭式可微图像测量（如亮度、饱和度、光照方向）作为统一空间，贯穿学习、诊断、校准、组合全流程。
- 训练前用可观测性测试判断某属性是否可作为有效监督，剔除不可学习候选。
- 训练时采用测量引导目标：学习目标属性移动的同时抑制非目标属性变化，提升选择性。
- 训练后解码校准，将控制系数映射到实际图像变化单位，使控制强度可比。
- 多个LoRA分支存于单一checkpoint，推理时无需在联合激活上训练即可组合。

**关键结果**：在SDXL和FLUX.1-dev上验证，553个prompt下光照方向控制相关系数ρ=0.995，98.9%扫描单调；五属性checkpoint平均选择性2.59，远超最强基线1.50；双属性组合96.7%、三属性组合86.1%保持每个请求方向；可观测性测试成功区分所有后续成功测量与失败候选。
