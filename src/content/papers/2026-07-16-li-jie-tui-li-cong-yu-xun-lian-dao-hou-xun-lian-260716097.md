---
title: Understanding Reasoning from Pretraining to Post-Training
title_zh: 理解推理：从预训练到后训练
authors:
- Jingyan Shen
- Ang Li
- Salman Rahman
- Yifan Sun
- Micah Goldblum
- Matus Telgarsky
- Pavel Izmailov
affiliations:
- New York University
- Modal Labs
- University of California, Los Angeles
- University of Illinois Urbana-Champaign
- Columbia University
arxiv_id: '2607.16097'
url: https://arxiv.org/abs/2607.16097
pdf_url: https://arxiv.org/pdf/2607.16097
published: '2026-07-16'
collected: '2026-07-20'
category: Reasoning
direction: LLM推理的预训练-RL缩放与行为分析
tags:
- RLHF
- pretraining
- scaling law
- reasoning
- chess
- math
one_liner: 以国际象棋为受控实验，揭示预训练损失可预测RL后性能，RL在困难任务中涌现新推理能力
practical_value: '- 预训练损失是RL后性能的强预测指标：在推荐或Agent任务中，可先通过预训练损失筛选有潜力的模型/数据配置，降低RL实验成本。

  - RL并非仅锐化SFT策略：在困难样本上能涌现SFT未覆盖的正确行为，提示在生成式推荐或Agent决策中，RL可能探索出更优的item/动作空间。

  - RL提升斜率与预训练数据量近似线性关系，预训练投入对下游RL收益有直接放大效应，为「先大力预训练，再轻量RL」的工程路径提供依据。

  - 使用棋类等可控环境作为测试平台，思路可复用于推荐系统离线模拟：设计规则明确、奖励可验证的推荐游戏，研究LLM推理行为。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：RL后训练极大提升LLM推理能力，但预训练阶段（模型大小、数据量）如何影响RL收益缺乏定量理解。由于真实LLM预训练语料不可控、实验成本过高，难以隔离变量，因此需要一个可控实验环境。

**方法**：以国际象棋为推理测试平台，模拟标准LLM训练流程：用人类棋局文本预训练5M～1B参数的Transformer，再用合成推理轨迹做SFT，最后在可验证奖励的战术谜题上进行RL（PPO）。通过系统性地变化预训练计算量、模型大小和数据量，观察RL后的性能变化和策略行为。

**关键结果**：
1. **缩放定律**：给定RL计算预算，最终性能可由预训练损失准确预测；RL奖励曲线斜率随预训练token数近似线性提升。
2. **RL行为模式**：在简单谜题上，RL主要放大SFT已偏好的正确走法；在困难谜题上，RL能“浮现”出SFT几乎未出现的正确走法，即RL并非单纯锐化先验，而是具有发现新推理路径的能力。
3. **跨领域验证**：在数学文本上复现类似现象，更长预训练的checkpoint在RL后达到更高性能且提升更快。

以上发现为预训练与RL的协同提供了定量解释，并建立了可复用的实验范式。
