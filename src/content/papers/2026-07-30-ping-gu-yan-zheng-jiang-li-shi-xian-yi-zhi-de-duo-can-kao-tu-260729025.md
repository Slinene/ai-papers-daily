---
title: Evaluation-Verification Reward for Consistent Multi-Reference Image Editing
title_zh: 评估-验证奖励实现一致的多参考图像编辑
authors:
- Yingmao Miao
- Pengfei Zhang
- Xiaochen Lv
- Meng Yu
- Lei Sun
- Xiangxiang Chu
- Chao Shen
- Chenhao Lin
affiliations:
- Xi'an Jiaotong University
- Amap, Alibaba
- Shanghai Jiao Tong University
arxiv_id: '2607.29025'
url: https://arxiv.org/abs/2607.29025
pdf_url: https://arxiv.org/pdf/2607.29025
published: '2026-07-30'
collected: '2026-08-03'
category: Eval
direction: 多模态评估 · 强化学习奖励
tags:
- Multi-Reference Editing
- Reward Model
- Reinforcement Learning
- Multimodal LLM
- Visual Consistency
one_liner: 提出多维度评估-验证奖励（EVR），用 MLLM Evaluator 和 Verifier 产生可靠细粒度信号，通过 RL 微调提升多参考编辑一致性
practical_value: '- 对生成式推荐中的多条件约束（如风格、属性一致性）可借鉴评估-验证框架：让 LLM 生成多个评价假设，再通过规则或小模型验证证据，减轻单次评估的幻觉。

  - 强化学习对齐阶段，可将细粒度多维奖励替代单一全局打分，每维度独立评估并验证，提升模型对复杂指令的遵循能力。

  - 搭建自动化数据飞轮时，可复用“生成候选判断 → 证据验证 → 拒绝虚假判断”的思路，提高离线评测的可靠性，减少人工校验成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多参考图像编辑要求合成多张参考图的视觉元素并保持风格、语义和谐，但现有编辑模型在此任务上一致性差。强化学习微调是增效途径，却缺少能够刻画多图间关系的奖励模型。直接用 MLLM 作零样本评估师，长文本推理易产生幻觉，短文本判断缺乏论证力。

**方法**：提出多维评估-验证奖励（EVR）。将评估拆解为多个独立视觉标准（如色彩、纹理、物体形状），每个标准下，MLLM Evaluator 生成多条候选判断假设，随后 Verifier 模块从图像中定位具体视觉证据，逐一证实或证伪每条假设，最终保留被证实的判断并转换为细粒度奖励信号。配合可扩展的数据构造管线，该方法可对现成编辑模型进行 RL 微调，无需改动架构。

**结果**：以 Qwen-Image-Edit 为基座，经 EVR 奖励强化微调后，多参考编辑的视觉一致性与整体和谐度大幅提升，达到或超越商业模型 NanoBanana 的水平，验证了该奖励机制的有效性。
