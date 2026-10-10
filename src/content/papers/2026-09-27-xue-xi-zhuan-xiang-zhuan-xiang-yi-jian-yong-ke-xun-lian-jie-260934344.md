---
title: 'Learning to Steer, Steering to See: Unveiling the Geometry of RLVR in Large
  Language Models via Trainable Vectors'
title_zh: 学习转向，转向以见：用可训练向量揭示RLVR在LLM中的几何结构
authors:
- Yuchen Cai
- Ding Cao
- Qixiang Yin
- Xin Xu
- Kai Yang
- Siye Wu
- Pengyuan Wang
- Jiaxuan Wang
- Weijie Liu
- Saiyong Yang
affiliations:
- USTC
- Tencent Hunyuan
- BUPT
arxiv_id: '2609.34344'
url: https://arxiv.org/abs/2609.34344
pdf_url: https://arxiv.org/pdf/2609.34344
published: '2026-09-27'
collected: '2026-10-10'
category: Training
direction: RLVR 激活几何与训练稳定化
tags:
- RLVR
- vector steering
- activation manifold
- training stability
- Alpha-Stabler
- LLM
one_liner: 发现RLVR有效控制方向位于激活主子空间低方差补集，并提出Alpha-Stabler稳定训练提升RL增益
practical_value: '- RLVR 微调 LLM（如电商搜索/推荐中的 Agent 策略模型）时，可监控激活的主子空间入侵程度来预警训练崩溃，提前止损，节省算力。

  - 在反向传播中移除激活梯度在主子空间的分量、保留低方差补集分量，可作为通用训练稳定化 trick，与现有 RLHF/RLVR 流程兼容，尤其适合长步训练。

  - 低维有效流形存在但不可无限压缩，提示在低秩适配（LoRA）或资源受限场景下，需平衡干预维度与输入依赖表达性；对在线持续微调有参考价值。

  - 跨任务几何对齐与能力迁移相关，可用于评估不同业务任务（查询改写、推荐策略、Agent 决策）之间的迁移潜力，指导多任务训练设计。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RL 已成为增强 LLM 推理能力的关键范式，但参数更新维度极高，训练动态难以分析，机制不透明。本文用可训练向量 steering 作为分析工具，研究 RLVR 在激活空间中与性能增益相关的低维有效流形。

**方法关键点**：
- 识别激活空间低维有效流形，发现两个几何性质：① 有效流形容量可很小但不可无限压缩，极低容量下干预维度和输入依赖表达性成为关键约束，且随注入深度变化；② 有效控制方向主要位于激活主子空间的低方差补集。
- 基于这些性质提出 Alpha-Stabler：Predictor 监控主子空间入侵以预警训练崩溃；Controller 在反向传播中移除激活梯度的主子空间分量，保留正交补分量。

**关键结果数字**：在 5 个 LLM 和 6 个可验证奖励任务上验证几何性质；Alpha-Stabler 稳定训练 2000 步，并一致提升 RL 增益。
