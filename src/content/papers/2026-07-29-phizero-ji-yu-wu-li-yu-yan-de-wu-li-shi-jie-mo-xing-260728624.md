---
title: 'PhiZero: A World Model Built Around Physical Language'
title_zh: PhiZero：基于物理语言的物理世界模型
authors:
- Shuyao Shang
- Yuqi Wang
- Ruopeng Gao
- Xu Chen
- Tieniu Tan
- Lue Fan
- Zhaoxiang Zhang
affiliations:
- NLPR, Institute of Automation, Chinese Academy of Sciences (CASIA)
arxiv_id: '2607.28624'
url: https://arxiv.org/abs/2607.28624
pdf_url: https://arxiv.org/pdf/2607.28624
published: '2026-07-29'
collected: '2026-08-02'
category: Multimodal
direction: 物理世界建模 · 离散视觉表示
tags:
- Physical World Model
- Discrete Representation
- Self-Supervised Learning
- Video Generation
- Zero-Shot Transfer
- World Model
one_liner: 从野生视频自监督学习紧凑离散物理语言，先推理后渲染实现物理一致生成与零样本动作迁移
practical_value: '- 将连续动态抽象为离散 token 序列的思路可迁移至用户行为建模：用 vector quantized 方式学习行为语义 ID，在紧凑空间内捕捉状态转移规律，降低下游序列预测的复杂度。

  - 自监督学习“物理语言”的方法对无标注交互数据的表征学习有启发：从原始点击/购买序列中挖掘隐含因果结构，无需昂贵标注即可获得可推理的隐状态表示。

  - “推理-渲染”分离的架构可拆解推荐系统：先由 Planner 生成抽象行为序列，再交由 Renderer 生成具体推荐内容，提升可解释性并支持可控生成。

  - 主要贡献在物理世界建模，直接迁移至电商推荐场景的工程化价值有限，更多是概念层面的借鉴。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有物理世界模型直接在像素空间预测未来，将物理动态隐式混入高维视觉预测器，缺乏显式推理。人类能从视觉经验中抽象出结构化知识并用自然语言组织，因此本文探索从野生视频自监督学习一种“物理语言”——紧凑离散的世界状态转移表示，并用它显式推理世界演化。

**方法关键点**：
- 提出 Physical Language（物理语言），一种离散 token 序列，捕获底层物理状态的转变。
- 采用“先推理后渲染”范式：Reasoner 根据当前图像和可选动作预测未来物理语言序列；Generator 将该序列解码为未来视频。
- 整个系统包含三个组件：Physical Language Tokenizer 通过 VQ-VAE 将视觉帧映射到离散码本；Reasoner 用 Transformer 对物理语言序列进行自回归建模；Generator 从推理出的语言序列重建视频。
- 训练分两阶段：先训练 Tokenizer 和 Generator 的视觉重建，再固定 Tokenizer 训练 Reasoner 预测未来的语言 Token。

**关键结果**：
- 在多种视频生成和理解基准上，PhiZero 生成的视频在物理一致性指标上显著优于基线（如 VideoGPT、TECO）。
- 支持细粒度动作条件模拟，给定单个动作指令就能控制物体运动。
- 展现零样本动作迁移能力，将人体动作迁移到机器人或灵巧手，无需样本训练。
- 可交互地探索世界演化，如从单张图像出发生成多样且物理合理的未来轨迹。
