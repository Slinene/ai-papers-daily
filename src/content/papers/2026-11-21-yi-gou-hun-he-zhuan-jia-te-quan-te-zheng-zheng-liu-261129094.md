---
title: 'HME-PFD: Heterogeneous Mixture-of-Experts Privileged Feature Distillation'
title_zh: 异构混合专家特权特征蒸馏
authors:
- Wen Xu
- Xiaomin Zhang
- Yucheng Yang
- Danny Liu
- Xunlong Gui
- Fei Huang
- Sha Meng
affiliations:
- Meta
- University of Toronto
arxiv_id: '2611.29094'
url: https://arxiv.org/abs/2611.29094
pdf_url: https://arxiv.org/pdf/2611.29094
published: '2026-11-21'
collected: '2026-11-24'
category: RecSys
direction: 广告推荐 · 特权特征蒸馏 · MoE 路由
tags:
- Knowledge Distillation
- Privileged Features
- Mixture-of-Experts
- CVR Prediction
- Ads Recommendation
- Routing
one_liner: 将特权特征引入 student 侧 MoE 路由，应对训练期特权特征稀疏异质，提升广告 CVR 学生模型
practical_value: '- 在电商/广告排序模型的 PFD 或蒸馏任务中，如果存在训练期特权特征（如 post-click 行为、落地页停留时长）且覆盖不均，可以在
  student 的辅助蒸馏任务中加一个 MoE，用特权特征的 availability 或数值做路由，区分高/低信号样本；主任务不接触特权特征，线上推理无额外成本。

  - 路由模块不必复杂：线性 gating 在大多数情况下接近 MLP/Attention 的效果，且计算开销低；硬编码按“特权特征是否缺失”做二路分流是强 baseline，适合冷启动或快速验证。

  - 专家数量 2-3 个通常足够，4 个专家容易退化；expert MLP 容量与 backbone embedding 维度匹配（如 512->[512,1]）效果最好；每个样本选
  top-2 experts 比 top-1 略好，但强制所有专家参与会引入噪声。

  - 避免在推荐场景使用 expert choice routing：论文中它导致 NE 显著上升（+1.8% 以上），说明强制负载均衡的专家选择不适合单 embedding
  向量输入，应采用 soft MoE 或 top-k。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
在广告推荐的知识蒸馏中，Privileged Feature Distillation（PFD）让 teacher 使用训练期才有的特权特征（如点击后停留时长、落地页快速离开等信号）蒸馏 student，以提升线上模型。但现实数据里特权特征覆盖低且分布异质：不同样本拥有的特权特征子集不同，甚至完全缺失。这导致 teacher 蒸馏监督质量参差不齐，传统 PFD 对所有样本一视同仁，学生可能过拟合低质量软标签或浪费高质量信号。

## 方法关键点
论文提出 HME-PFD，在 student 模型里引入辅助蒸馏任务，用 MoE 架构消费特权特征做路由，而主任务只使用 regular features，因此线上推理不依赖特权特征，不增加 serving 成本。

- 结构：student 共享 backbone 输出 embedding，主任务 head 预测 CVR；辅助蒸馏任务将 embedding 输入 MoE，由特权特征驱动路由。
- 路由设计：支持硬编码规则（如按特权特征缺失与否分流）和可学习路由（linear gating、MLP、ResNet、multi-head attention）。
- 训练目标：主任务 ground-truth loss + 辅助蒸馏 loss，MoE 内部各专家 loss 聚合为单一辅助 loss，避免额外多任务加权。
- 理论直觉：场景条件路由的 oracle gain 等于 E[(μ_G(Z)-μ(Z))²]，当特权特征的可用模式/取值改变 teacher 目标条件均值时，路由能带来严格提升。

## 关键实验
在 CVR_Large 和 CVR_Small 两个工业级 post-click 转化预测数据集上评估，指标为 Normalized Entropy（NE，越低越好），对比 Plain（无蒸馏）和不同路由模块。

- CVR_Large：linear/ResNet 路由相对 Plain 下降 0.09% NE，hard-coded 下降 0.07%。
- CVR_Small：MLP 路由下降 0.42% NE，效果最好；linear 也有 0.27% 下降。
- 消融：2-3 个专家最优，4 个专家退化；专家 MLP 维度 [512,1] 最优；p=10 时 e=3、top-2 选中效果最好；soft MoE 在 e=4 时仍保持正向，而 expert choice 路由在所有配置下 NE 上升 1.8% 以上，不适合该场景。

## 最值得记住的一句话
特权特征的 availability 和数值本身就是有效的样本分流信号，在 student 侧用 MoE 路由消费特权特征，可以在不增加在线成本的前提下提升蒸馏效果。
