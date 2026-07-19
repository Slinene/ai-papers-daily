---
title: 'MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators'
title_zh: MeanFlowNFT：面向平均速度生成器的前向强化学习
authors:
- Yushi Huang
- Xiangxin Zhou
- Jun Zhang
- Liefeng Bo
- Tianyu Pang
affiliations:
- Tencent Hunyuan
- The Hong Kong University of Science and Technology
arxiv_id: '2607.15273'
url: https://arxiv.org/abs/2607.15273
pdf_url: https://arxiv.org/pdf/2607.15273
published: '2026-07-15'
collected: '2026-07-19'
category: Other
direction: 平均速度生成器的RL对齐
tags:
- MeanFlow
- Reinforcement Learning
- Diffusion Models
- Flow Matching
- Few-Step Generation
- Forward-Process RL
one_liner: 构建诱导瞬时速度预测器，使MeanFlow能用前向RL优化奖励，实现快速少步生成且性能超越多步模型
practical_value: '- 若业务采用基于流匹配的生成式检索（如生成Semantic ID），可利用诱导预测器技巧将前向RL直接用于平均速度模型，避免反向轨迹计算，实现快速对齐。

  - 少步生成（如一步或四步）能大幅降低推理延迟，适合在线推荐系统，同时RL微调可显著提升生成质量。

  - 恒等式桥接平均与瞬时速度的思路可推广至其他需要粗粒度预测但细粒度优化的场景，例如多步推理与一步决策的对齐。

  - 严格策略改进保证为在线学习提供了安全部署的理论基础，可借鉴用于推荐模型的持续优化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：MeanFlow生成器通过预测平均速度实现快速少步采样，但现有前向过程强化学习（DiffusionNFT）仅优化瞬时速度模型，无法直接应用于MeanFlow。为赋予MeanFlow奖励对齐能力，需要解决平均速度与瞬时速度之间的目标不一致问题。

**方法关键点**：利用MeanFlow恒等式（连接平均速度与瞬时速度的数学关系），从原始平均速度预测器构造一个诱导瞬时速度预测器。将DiffusionNFT的前向RL目标直接用于该诱导预测器，使奖励优化在MeanFlow上有定义，而采样仍使用原始平均速度预测器，从而保留快速少步生成的优势。同时证明了该方法继承DiffusionNFT的严格策略改进保证。

**关键结果**：在图像和视频生成实验上，MeanFlowNFT一致提升基线模型。在SD3.5-M上，8项指标中的6项超越之前最先进的RL微调少步生成器；仅用4步即可超过多步RL微调的扩散模型（如Wan 2.1上VBench得分84.33，对比50步LongCat-Video RL的82.57）。少步生成效率与高质量对齐得到统一。
