---
title: 'Model Carving: Training Transformers That Optimize Their Own Topology'
title_zh: 模型雕刻：训练优化自身拓扑的Transformer
authors:
- Kaden Zheng
- Pratyusha Sharma
affiliations:
- Harvard University
- New York University
arxiv_id: '2611.27962'
url: https://arxiv.org/abs/2611.27962
pdf_url: https://arxiv.org/pdf/2611.27962
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 训练中拓扑学习 · 模型压缩
tags:
- Model Carving
- Structured Sparsity
- Architecture Learning
- Transformer Training
- Model Compression
- Efficiency
one_liner: 通过可学习门控在训练中移除冗余子层，直接雕刻出更小更快更强的异质 Transformer
practical_value: '- 在训练推荐/搜索中的 Transformer 序列编码器、生成式推荐模型时，对每个子层引入可学习标量门控（例如乘以 sigmoid(gate)）并施加稀疏正则（如
  L1/L0），让优化器自动移除冗余 attention/MLP 模块，直接产出可在线上低延迟部署的稀疏子网，省去事后剪枝流程。

  - 该方法的收益随模型规模增大而扩大，且优于蒸馏和剪枝获得的同尺寸模型。对于需要压缩 LLM 作为特征提取器或 ranker 的场景，可考虑从预训练阶段就执行结构雕刻，而不是先训大模型再压缩。

  - 被移除子层不再执行，推理 FLOPs 可降低最多 34%，解码加速 1.6 倍。在实时排序、召回或生成式推荐等服务中，可直接使用 carved 后的模型提升吞吐，无需额外推理优化。

  - 方法同样适用于 looped Transformer（权重共享层），若业务采用 ALBERT 式共享参数减少显存，可结合门控雕刻进一步降低计算。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：
传统机器学习将架构选择和训练分开，Transformer 固定每层的 attention 和 MLP 子层结构与顺序，这更多是惯例而非最优设计。理想训练过程应同时塑造模型拓扑。

方法关键点：
Model Carving 在训练 Transformer 时给每个子层引入可学习标量门控，训练损失在优化权重的同时可以推动门控关闭，从而移除冗余子层，最终从大而均匀的网络中雕刻出更小的异质网络。该方法可应用于标准 Transformer 和 looped Transformer（层间共享权重），无需预先指定架构或后处理剪枝。

关键结果：
在 140M 至 2.7B 参数标准 Transformer 和 140M-1.3B looped Transformer 上预训练，在相同训练计算预算下，carved models 的验证损失低于使用最多 1.7 倍计算训练的稠密模型；且优于剪枝和蒸馏得到的同等规模模型。移除的子层在推理时不执行，每 token FLOPs 最多降低 34%，解码速度提高 1.6 倍且质量不下降。优势随模型规模增大而增长，并迁移到 few-shot 评估和生成任务。

结论：架构应像权重一样通过训练学习，而非预先固定。
