---
title: 'Seeing Before Reasoning: Decoupling Perception and Reasoning for Shortcut-Resilient
  Multimodal On-Policy Self-Distillation'
title_zh: 先观察后推理：解耦感知与推理的抗捷径多模态在线自蒸馏
authors:
- Sihan Wang
- Xiyao Liu
- Lianqing Liu
- Zhi Han
affiliations:
- State Key Laboratory of Robotics and Intelligent Systems, Shenyang Institute of
  Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2606.19120'
url: https://arxiv.org/abs/2606.19120
pdf_url: https://arxiv.org/pdf/2606.19120
published: '2026-06-16'
collected: '2026-06-20'
category: Multimodal
direction: 解耦感知与推理防止文本捷径
tags:
- on-policy self-distillation
- multimodal LLM
- visual grounding
- shortcut mitigation
- perception-reasoning decoupling
one_liner: 提出 ViGOS，通过先视觉描述后推理并解耦感知与推理教师，防止多模态自蒸馏中基于文本的捷径，提升视觉 grounding。
practical_value: '- **多模态模型训练防捷径**：在电商商品理解任务中（如从图文预测属性），可借鉴先描述后推理的生成格式，并用纯图像教师监督描述部分，迫使模型依赖视觉而非文本偏差，提升跨模态对齐。

  - **在线自蒸馏的应用**：在推荐或多模态 agent 的循环训练里，可引入冻结副本提供稠密 token 级监督，替代稀疏奖励，以缓解学生模型生成与训练分布偏差。

  - **错误恢复机制**：对无效 rollout 使用参考教师恢复格式，可迁移到 agent 的自我校正或序列生成任务中，保证输出结构规整。

  - **视觉推理任务增强**：若业务涉及空间 grounding 或图文推理（如图片 QA、导航 agent），可将视觉描述前置，并结合专用感知教师，提升对图像的忠实度。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：On-policy self-distillation (OPSD) 在 LLM 推理中有效，但直接用于多模态大模型时会出现文本捷径——教师模型可能只基于文本参考目标指导 token 生成，而忽略图像。这削弱了多模态模型的视觉 grounding 能力。

**方法**：提出 ViGOS，将生成链改为“先视觉描述，后推理”。训练时，冻结的学生副本作为教师集合：
- **Image-only 感知教师**：仅凭图像监督视觉描述部分（去除文本捷径可能）；
- **Privileged 推理教师**：在相同学生前缀下，基于参考答案监督推理和最终答案；
- **参考教师**：仅用于无效 rollout 以恢复输出格式。
通过这种解耦，ViGOS 在保持 OPSD 稠密监督优点的同时，强制模型关注图像。

**结果**：在通用视觉-语言、专家推理、视觉数学、空间 grounding 等基准上，ViGOS 不但保留了 OPSD 的收益，还在易产生捷径的场景下显著提升了图像依赖于行为，验证了解耦感知与推理的有效性。
