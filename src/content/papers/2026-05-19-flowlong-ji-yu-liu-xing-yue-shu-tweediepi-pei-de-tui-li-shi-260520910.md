---
title: 'FlowLong: Inference-time Long Video Generation via Manifold-constrained Tweedie
  Matching'
title_zh: FlowLong：基于流形约束Tweedie匹配的推理时长视频生成
authors:
- Jangho Park
- Geon Yeong Park
- Gihyun Kwon
- Jong Chul Ye
affiliations:
- KAIST
- Amazon
arxiv_id: '2605.20910'
url: https://arxiv.org/abs/2605.20910
pdf_url: https://arxiv.org/pdf/2605.20910
published: '2026-05-19'
collected: '2026-05-23'
category: Multimodal
direction: 长视频生成 · 推断时优化
tags:
- Video Generation
- Diffusion Models
- Tweedie Matching
- Inference-time
- Temporal Consistency
- Manifold Constraint
one_liner: 在推理时通过滑动窗口重叠的Tweedie匹配与随机早期采样实现无训练、架构无关的长视频生成
practical_value: '- **长序列生成的一致性控制**：对于电商场景中需要生成长商品描述、营销故事或多模态内容时，可借鉴滑动窗口重叠与Tweedie匹配机制，在序列拼接处保持语义和风格连贯，避免内容漂移。

  - **无需重新训练的低成本扩展**：该推理时方法无需额外微调模型，可直接应用于已部署的视频/文本生成模型，快速赋予其生成长内容的能力，适合业务快速迭代。

  - **随机早期采样抑制重复模式**：在生成过程的早期阶段注入噪声，能有效避免自回归生成中的重复和单调问题，这一思路可迁移至对话式推荐或交互式叙事生成，提升内容多样性。

  - **架构无关的插件化设计**：方法不依赖特定模型结构，对Transformer或扩散模型均适用，为已有生成系统提供统一的长序列生成插件，降低集成成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频扩散模型受限于训练长度，现有训练免费方法中，双向扩展受架构约束且长时质量下降，自回归方法因曝光偏差累积漂移并产生重复运动。

**方法关键点**：
- 采用滑动窗口重叠生成视频段，相邻窗口的预测干净样本在重叠区域通过Tweedie匹配进行混合，既施加了流形约束又保证了时间一致性。
- 引入随机早期采样：在高噪声阶段，每次Tweedie匹配修正后注入新鲜噪声，同步各窗口轨迹以防止偏差累积；随后转为确定性ODE采样，保留精细视觉保真度。
- 整体流程无需训练，架构无关，仅需推理时适配。

**关键结果**：
- 在多种视频生成模型上，生成长度比原生窗口长数倍的视频，时间一致性和视觉质量均优于现有训练自由和自回归基线。
- 方法可无缝扩展至音视频联合生成和文本到3D高斯泼溅，无需任何微调。
