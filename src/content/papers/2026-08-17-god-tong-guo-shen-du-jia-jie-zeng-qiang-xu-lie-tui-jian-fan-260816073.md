---
title: 'GOD: Enhancing Generalization via Deep Grafting for Sequential Recommendation'
title_zh: GOD：通过深度嫁接增强序列推荐泛化
authors:
- WooJoo Kim
- JunYoung Kim
- JaeHyung Lim
- HwanJo Yu
affiliations:
- Pohang University of Science and Technology
arxiv_id: '2608.16073'
url: https://arxiv.org/abs/2608.16073
pdf_url: https://arxiv.org/pdf/2608.16073
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 序列推荐知识蒸馏 · 组件级嫁接
tags:
- Sequential Recommendation
- Knowledge Distillation
- Grafting
- Contrastive Learning
- Generalization
one_liner: 提出组件级知识蒸馏框架GOD，将学生组件嫁接进冻结教师构造混合源模型，强化序列推荐泛化
practical_value: '- **组件级蒸馏替代输出级蒸馏**：在电商/广告点击序列建模中，若教师-学生 KD 效果受限，可尝试将学生 embedding
  或 encoder 临时插入冻结教师路径，分别得到 Embed-Grafted Teacher 和 Encoder-Grafted Teacher。这样能分离“嵌入不可靠”和“编码器过拟合”两类误差，比仅匹配教师输出更适合稀疏行为数据。

  - **Transformer 序列模型可用 Grafted Encoding 稳定训练**：将教师侧与学生侧 token 拼接，允许互注意力（mask 为四块均
  causal），早期教师 token 提供稳定上下文，后期学生 token 细化表示。训练 attention 开销约翻倍，但收敛更快，且不影响线上推理。

  - **推理零开销，适合轻量线上模型**：混合源模型只在训练阶段使用，线上仍用原始学生模型，不增加额外耗时。对需要低延迟的推荐/广告精排模型是可落地的 KD 增强方案。

  - **自适应对比权重技巧可复用**：GCL 对六种表示对做对比学习，并用 batch 内平均相似度的 stop-gradient 计算权重，抑制冗余对、强调互补对。该思想可迁移到多视图对比学习、多任务蒸馏中的损失加权。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

序列推荐（SR）处理稀疏、噪声的交互历史时容易过拟合到观察到的共现或虚假转移，泛化不足。知识蒸馏（KD）可转移教师密集监督，但传统 KD 中教师与学生独立前向，输出或表示匹配让学生 embedding 与 encoder 的误差相互纠缠，无法给出组件级反馈。论文提出用嫁接（grafting）构造混合源模型，在学生组件置于教师计算路径时评估其质量，从而分离组件误差。

## 方法关键点

- **GOD 框架**：构造三类源模型——Non-Grafted Teacher（稳定知识锚）、Embed-Grafted Teacher（学生嵌入 + 教师编码器）、Encoder-Grafted Teacher（教师嵌入 + 学生编码器）；目标模型为 Non-Grafted Student。
- **Grafted Encoding (GE)**：针对 Transformer 推荐器，将教师侧与学生侧 embedding 拼接，允许双向互注意力，稳定混合表示生成；仅训练时使用。
- **Graft-aware Contrastive Learning (GCL)**：对四种表示（(T,T),(S,T),(T,S),(S,S)）两两配对做对比学习，用 batch 内平均相似度经 stop-gradient 得到自适应权重，降低冗余对、强调互补组件信号。
- **推理**：只使用 Non-Grafted Student，无额外推理开销。

## 关键实验

在 Amazon Beauty、Yelp、MovieLens 1M 三个数据集上，以 GRU4Rec、FMLPRec、SASRec 为 backbone，对比 RD、CD、DE、RRD、HTD、BD、AdaRec、MSKDIK、EMKD 等 KD 基线。GOD 在所有数据集、backbone、指标上最优，相对最强基线最高提升 13.92%（Yelp SASRec NDCG@10）。同容量 self-distillation 设定下 GOD 也优于自监督对比方法。泛化分析显示短序列、噪声测试、不同容量差距和教师质量下 GOD 均保持优势。训练效率上虽然单 epoch 开销高于 Student，但比 BD/EMKD 更快达到最佳验证效果。

## 一句话记忆

用嫁接构建教师条件源模型，让学生在教师计算路径中被组件级评估，比事后匹配教师信号更利于稀疏序列泛化。
