---
title: 'HASTE: Hierarchical and Attribute-aware Supervision for Generative Recommendation'
title_zh: HASTE：面向生成式推荐的层级与属性感知监督
authors:
- Tripti Shukla
- Shwetha Somasundaram
- Akshat Gupta
- Rohit Garg
- Paul Duff
- Ian Anderson
affiliations:
- Glance
arxiv_id: '2610.17368'
url: https://arxiv.org/abs/2610.17368
pdf_url: https://arxiv.org/pdf/2610.17368
published: '2026-10-12'
collected: '2026-10-14'
category: GenRec
direction: 生成式推荐 · Semantic ID 层级/属性监督
tags:
- Generative Recommendation
- Semantic IDs
- Hierarchical Loss
- Attribute-aware
- Long-tail
- Training Efficiency
one_liner: 提出层级损失与属性辅助损失，在 Semantic ID 生成式推荐中实现约 2 倍训练提速与长尾显著提升
practical_value: '- 对基于 RQ-VAE Semantic ID 的生成式推荐，可直接把 flat causal CE 换成层级损失：粗粒度 SID
  code 给更大静态权重（如 4:3:2:1），再用 detached 置信度 gate 控制下游 level 的 loss 权重，并让权重从静态逐步退火到条件权重；同时用
  scheduled sampling 扰动上游粗 code。这样不改变推理结构，却可拿到约 2× 收敛提速。

  - 如果业务有商品属性（颜色、材质、版型等），可以在精细 SID 位置（如 L2 hidden state）接一个 64 维 MLP 回归头做辅助监督，目标由
  SID tuple 查 catalog 聚合得到，不需要 query 中显式出现属性；用 Huber loss 且对低频 item 做频率加权 clamp((f_med/f_i)^0.5,
  1, 5)，长尾 Recall@10 可提升 18%–24%。

  - 属性辅助 head 不修改 SID 词表、logits 或生成分布，方便单独保存/上线回滚；但要先确认属性标注覆盖率，缺少 structured attribute
  的数据集无法直接复用。

  - 结果提示：标准 CE 微调会侵蚀预训练阶段形成的层级结构，使相邻 SID level 的 cosine coupling 下降、embedding drift
  增大；因此在迁移 LLM 做生成式推荐时，值得监控 SID embedding 的结构保持程度，而不是只看 Hit/NDCG。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式推荐用 Semantic ID 自回归生成 item，但现有方法用 flat causal CE 监督 SID 预测，忽略了 RQ-VAE 天然编码的 coarse-to-fine 层级：粗 level 错会重定向后续所有细粒度预测，细 level 错只影响局部细化。实验显示，flat CE 微调会让相邻 SID level 的 cosine coupling 从 0.55 降到 0.36，并造成更大 embedding drift。同时，tail item 交互监督不足，颜色、材质等属性信号又分散在 SID 多级中，未被生成目标显式利用。

## 方法关键点
- **Hierarchical Loss**：按 SID 层级分配静态权重 4:3:2:1，粗粒度 code 获得更大惩罚；用 detached confidence gate 对下游 level 做条件加权，只有上游粗 code 置信度高才强化下游监督；训练中从纯静态权重逐步退火到完全置信度门控。
- **Scheduled sampling**：以线性增大的概率用模型采样替换 ground-truth L1 token，缩小 teacher forcing 与推理时的 exposure gap。
- **Attribute-Specific Losses**：在 L2 SID 预测位置的 hidden state 上接轻量 MLP 回归头，预测 CIELAB 颜色或 15 维 material composition；目标由 SID tuple 查 catalog 聚合得到，不依赖 query 是否显式提到属性；对低频 item 做频率感知加权。

## 关键结果
在 Amazon Beauty/Sports/Toys、Fashion-140k 和 internal-fashion 上与 SASRec、BERT4Rec、TIGER、HSTU、IDGenRec、OneRec-Think 等对比：
- Hierarchy Loss 在 Beauty/Sports/Toys 的 Recall@10 分别较最强 baseline 提升 4.0%、12.4%、15.5%。
- 训练效率上，Hierarchical Loss 达 CE 同等验证 loss 所需步数平均减少约一半，speedup 1.99×。
- HL+Color 在 Fashion-140k tail Recall@10 相对 HL 提升 24.2%，internal-fashion tail 提升 17.8%；长尾整体提升显著大于头部。
- 消融显示 static weighting + confidence gating + scheduled sampling 组合在 Toys 上 Recall@10 较 CE 提升 44.3%、NDCG@10 提升 50.0%。

最值得记住的一句话：层级结构不应让模型从 flat CE 中重新发现，而要在 loss 中显式编码；这样既保结构，又换训练效率，并把属性监督精准补到长尾。
