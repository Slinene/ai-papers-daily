---
title: Qwen-Image-2.0-RL Technical Report
title_zh: Qwen-Image-2.0-RL：基于 GRPO 强化学习与在线蒸馏的图像生成后训练
authors:
- Yixian Xu
- Kaiyuan Gao
- Yuxiang Chen
- Yilei Chen
- Zecheng Tang
- Zihao Liu
- Zikai Zhou
- Deqing Li
- Hao Meng
- Kuan Cao
affiliations:
- Qwen (https://qwen.ai)
arxiv_id: '2606.27608'
url: https://arxiv.org/abs/2606.27608
pdf_url: https://arxiv.org/pdf/2606.27608
published: '2026-06-24'
collected: '2026-06-29'
category: Multimodal
direction: 图像生成后训练 · RLHF 对齐
tags:
- RLHF
- GRPO
- On-Policy Distillation
- Reward Model
- Image Generation
- Diffusion Models
one_liner: 利用 GRPO 强化学习、复合奖励模型和在线蒸馏，统一提升文本到图像与图像编辑任务的视觉质量与指令遵循能力
practical_value: '- 构建任务特定的复合奖励模型（对齐、美学、一致性等维度）的思想，可迁移到多模态推荐系统的质量评估中，用于设计更全面的用户偏好奖励函数。

  - GRPO 在线强化学习结合混合 CFG 策略，在保持预训练知识的同时进行策略优化，可借鉴用于微调基于扩散模型的生成式推荐系统，避免灾难性遗忘。

  - 奖励模型的 pointwise scoring + chain-of-thought 推理，能够提升奖励信号可靠性，可应用于 Agent 的任务执行评估或用户模拟器。

  - On-policy 蒸馏通过轨迹级速度匹配合并多个专家模型，提供了一种无需额外标注即可整合多任务策略的有效方案，适合推荐场景中合并不同业务线微调模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：扩散模型在视觉质量与指令遵循方面仍有提升空间，需要可靠的奖励信号和可扩展的强化学习训练框架。

**方法关键点**：
- **复合奖励模型**：针对文本到图像与图像编辑任务，微调视觉语言模型作为逐点评分器，结合思维链推理，覆盖对齐度、美学、人脸保真度等多个维度。
- **GRPO 训练框架**：基于群体相对策略优化，引入混合 CFG 策略以保留预训练知识，通过组内奖励范围过滤自动筛选高质量 prompt，并进行类别级奖励权重校准。
- **在线蒸馏合并**：最后阶段通过轨迹级速度匹配，将文本到图像和图像编辑两个专门的强化学习策略合并为一个学生模型。

**关键结果**：在 Qwen-Image-Bench 上总分为 **57.84（+2.61）**；文本到图像竞技场 Elo 达到 **1193（+78）**；图像编辑竞技场 Elo 达到 **1349（+93）**，美学质量、prompt 贴合度与编辑准确率全面提升。
