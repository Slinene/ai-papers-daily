---
title: 'Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual
  Reasoning'
title_zh: 感知到推理：解耦感知与推理的细粒度视觉推理框架
authors:
- Hongxing Li
- Xiufeng Huang
- Dingming Li
- Wenjing Jiang
- Zixuan Wang
- Haolei Xu
- Hanrong Zhang
- Haiwen Hong
- Longtao Huang
- Hui Xue
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2607.01191'
url: https://arxiv.org/abs/2607.01191
pdf_url: https://arxiv.org/pdf/2607.01191
published: '2026-06-30'
collected: '2026-07-02'
category: Reasoning
direction: 解耦感知与推理的细粒度视觉推理
tags:
- Fine-grained visual reasoning
- Vision-language model
- Reinforcement learning
- Decoupling
- High-resolution
- PRA-GRPO
one_liner: 提出两阶段框架显式分离视觉感知与推理，结合角色感知的交替强化学习，仅用答案监督提升细粒度推理
practical_value: '- **感知-推理解耦范式可迁移至商品图像理解**：在商品属性识别、广告素材审核等场景，可让模型先定位“文字/细节区域”作为感知阶段，再基于裁剪区域进行结构化输出，减少高分辨率下的上下文噪声。

  - **PRA-GRPO 交替强化训练适合弱监督多步推理**：电商场景中从图像到复杂描述（如违规理由判定）往往缺乏中间标注，该策略仅用最终结果反馈即可交替优化感知与推理子策略，降低标注成本。

  - **高分辨率基准的提升提示可重用视觉搜索步骤**：对于商品详情图（4K/8K），让模型显式输出“关键区域坐标”再推理，能直接嵌入搜索推荐系统的多模态链路，提高证件/标签等细粒度识别的鲁棒性。

  - **框架具有模型规模扩展性**：小模型（2B/4B）也能通过解耦显著受益，适合在资源受限的推荐侧或端侧 Agent 中部署。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视觉语言模型在处理高分辨率图像中的细微视觉线索（如小文字、精细空间关系）时，常通过反复裁剪或测试时搜索引入局部证据，但未显式区分感知与推理，导致上下文噪声大、优化困难。

**方法关键点**：提出 P2R 框架，将细粒度视觉推理分解为两步：先由 **Perceiver** 定位问题相关的局部证据（在图像上标注区域或输出裁剪坐标），再由 **Reasoner** 基于标注后的图像及裁剪区域进行回答。为匹配该解耦范式，设计 **PRA-GRPO**（感知-推理交替 GRPO）：在仅用最终答案作为奖励信号的强化学习框架中，交替冻结感知或推理模块进行策略更新，实现角色感知的协同优化，无需中间定位监督。

**关键结果**：基于 Qwen3-VL-Instruct 2B/4B/8B，P2R-4B 在 V-Star 达 93.2%，HR-Bench-4K 81.9%，HR-Bench-8K 80.5%，大幅超越基座模型；解耦带来的收益可泛化至更广泛的多模态推理任务。
