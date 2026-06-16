---
title: 'DreamX-World 1.0: A General-Purpose Interactive World Model'
title_zh: DreamX-World 1.0：通用交互式世界模型
authors:
- DreamX Team
- Yancheng Bai
- Rui Chen
- Xiangxiang Chu
- Rujing Dang
- Hao Dou
- Bingjie Gao
- Qiwen Gu
- Siyu Hong
- Jiachen Lei
affiliations:
- DreamX Team
arxiv_id: '2606.16993'
url: https://arxiv.org/abs/2606.16993
pdf_url: https://arxiv.org/pdf/2606.16993
published: '2026-06-14'
collected: '2026-06-16'
category: Multimodal
direction: 交互式世界模型 · 长时生成与相机控制
tags:
- World Model
- Interactive Video
- Camera Control
- Diffusion Distillation
- Long-horizon Generation
- E-PRoPE
one_liner: 一个支持相机导航、场景重访和可提示事件的通⽤交互式长时视频生成世界模型，通过蒸馏与自回归训练达到16 FPS
practical_value: '- **自生成历史缓解偏移**：用模型自身生成长序列进行训练，可借鉴到生成式推荐（如语义ID自回归生成）的长序列训练，减少曝光偏差与风格漂移。

  - **记忆条件与几何检索**：基于相机几何检索历史视图，实现场景持久化；可类比在会话推荐中按行为序列检索历史状态，保持长对话一致性。

  - **蒸馏结合RL对齐**：DMD风格蒸馏后使用RL恢复控制精度与视觉质量，对蒸馏后的生成式推荐模型可考虑类似强化微调来保持可控性。

  - **工程优化技巧**：混合精度、75%剪枝VAE解码、异步流水线并行等，可直接迁移至大规模生成式模型在线推理的加速。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：将视频生成从被动合成推向交互式模拟，需解决长时间相机控制、场景一致性保持以及事件驱动的可提示生成。现有模型在长跨度下易出现风格漂移和记忆丢失。

**方法关键**：
- **数据引擎**：结合虚幻引擎渲染（精确相机）、游戏操作录制和真实视频（恢复相机几何），覆盖写实、游戏及风格化场景。
- **E‑PRoPE**：轻量投影位置编码，在空间压缩后的 token 上应用相机感知注意力，保留 PRoPE 的投影几何。
- **训练策略**：用因果强制与 DMD 蒸馏将双向视频生成器转为几步自回归世界模型；在自生成长时上下文上训练，让模型暴露于自身生成历史，减少累积色偏与风格漂移。
- **Memory‑Conditioned Scene Persistence**：基于相机几何检索早期视图，通过残差回收降低条件路径对不完美记忆潜在变量的敏感性。
- **事件控制**：事件指令微调实现组合式事件控制，RL 对齐在蒸馏后恢复相机控制精度与视觉质量。
- **推理加速**：混合精度 DiT、残差复用、75% 剪枝 VAE 解码、异步流水线并行，8 张 RTX 5090 达到 16 FPS。

**结果**：在 5 秒基础评测中，相机控制分数 73.75，总分 84.76，均优于 HY-WorldPlay 1.5（80.79）与 LingBot-World（80.45）。
