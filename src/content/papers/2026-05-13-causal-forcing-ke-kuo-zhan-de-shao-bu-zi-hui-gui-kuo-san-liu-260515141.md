---
title: 'Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation
  for Real-Time Interactive Video Generation'
title_zh: Causal Forcing++：可扩展的少步自回归扩散蒸馏用于实时交互视频生成
authors:
- Min Zhao
- Hongzhou Zhu
- Kaiwen Zheng
- Zihan Zhou
- Bokai Yan
- Xinyuan Li
- Xiao Yang
- Chongxuan Li
- Jun Zhu
affiliations:
- Tsinghua University
- ShengShu
- Renmin University of China
arxiv_id: '2605.15141'
url: https://arxiv.org/abs/2605.15141
pdf_url: https://arxiv.org/pdf/2605.15141
published: '2026-05-13'
collected: '2026-05-18'
category: Multimodal
direction: 视频生成 · 扩散蒸馏加速
tags:
- Diffusion Distillation
- Autoregressive Generation
- Causal Forcing
- Few-Step Sampling
- Interactive Video
one_liner: 通过因果一致性蒸馏高效初始化少步自回归学生模型，在帧级2步采样下性能超越4步块级SOTA，延迟减半
practical_value: '- **自回归生成初始化策略**：在生成式推荐（如序列化行为/内容生成）中，可将因果一致性蒸馏思想用于AR组件的初始化，用在线教师单步指导替代昂贵轨迹预计算，降低训练成本。

  - **少步采样训练技巧**：针对1-2步极端蒸馏场景，所提因果关系对齐损失可直接迁移到推荐流水线的扩散模型加速，如商品序列生成、用户行为预测。

  - **分阶段扩展范式**：先因果初始化再上下文扩展的流程，可复用于多轮对话Agent或多模态交互系统，平衡训练效率与长程一致性。

  - **延迟与质量权衡**：帧级细粒度控制首次响应延迟的实践，对电商直播、实时推荐等需要流式交互的场景有参考价值。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：实时交互视频生成要求低延迟、流式输出与可控性。现有自回归扩散蒸馏方法在块级（chunk-wise）4步采样下效果良好，但响应粒度粗、延迟仍高。本文探索更激进的帧级（frame-wise）1-2步采样，发现少步自回归学生的初始化是核心瓶颈：现有策略要么目标错位，要么无法少步生成，要么扩展成本高。

**方法**：提出Causal Forcing++，核心是因果一致性蒸馏（causal CD）进行初始化。causal CD学习与因果ODE蒸馏相同的AR条件流映射，但监督来自相邻时间步间的单步在线教师ODE，无需预计算完整PF-ODE轨迹，使初始化高效且易优化。初始模型再经上下文扩展与微调，得到最终2步帧级自回归生成器。

**结果**：在帧级2步设定下，Causal Forcing++超过先前最优4步块级Causal Forcing：VBench总分+0.1，质量分+0.3，VisionReward+0.335；首帧延迟降低50%，第二阶段训练成本降至约1/4。方法还成功扩展到动作条件世界模型生成。
