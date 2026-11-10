---
title: 'Hierarchical Residuals: A Minimalist Decoupling of Residual Width from Compute
  Width'
title_zh: 层级残差：极简解耦残差宽度与计算宽度
authors:
- Ziteng Wang
- Jianqiao Lu
- Xinyu Ma
- Jintao Zhang
- Jun Zhu
- Yiyuan Ma
- Jianfei Chen
affiliations:
- Tsinghua University
- ByteDance Seed
arxiv_id: '2610.41711'
url: https://arxiv.org/abs/2610.41711
pdf_url: https://arxiv.org/pdf/2610.41711
published: '2026-10-30'
collected: '2026-11-10'
category: Training
direction: 高效 Transformer 架构 · 残差宽度扩展
tags:
- HiRes
- Residual Networks
- Transformer Architecture
- Scaling Laws
- Pretraining Efficiency
- Model Architecture
one_liner: HiRes 用块间宽残差+块内窄计算，在不增加单层 FLOPS 下提升 Transformer 容量与训练效率
practical_value: '- 在训练 LLM 作为排序/召回/生成式推荐基座时，可将 HiRes 的块间宽残差作为独立容量维度，在不增加每层 attention/FFN
  计算宽度的情况下提升模型表达，适合在现有推理预算下榨取更多性能。

  - 只使用 dense projection 和 normalization，不依赖自定义 kernel，便于在现有 PyTorch/训练框架中快速实现和验证，适合业务团队做架构
  A/B。

  - 激活内存与 I/O 成本低于 VWN、mHC、AttnRes 等残差扩展方法，对于广告/推荐场景中长序列、大 batch 训练更友好。

  - 该解耦思路可迁移到多任务/多模态推荐模型：将共享的主干网络保持窄计算宽度，通过宽残差通道传递任务间或模态间的全局信息。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
标准 PreNorm Transformer 中，残差状态宽度与每层计算宽度绑定，限制表征容量且无法独立扩展。

## 方法关键点
HiRes 将层分组为块：块内保持原 d 维 PreNorm Transformer 层，仅做常规计算；块间引入更宽的 D 维 PostNorm 外残差，通过可学习的 read/write 投影在两层空间之间桥接。单层结构完全不变，只增加块边界的 dense 投影与归一化。

## 关键结果
- 在多种模型规模和深度下，HiRes 一致优于 vanilla 残差，拟合 scaling laws 显示 FLOPs 效率提升 1.30 倍。
- OLMoE-1B-7B 预训练 500B tokens：训练 loss 降低 0.0208，下游准确率提升 1.14 点。
- 相比 VWN、mHC、AttnRes 等残差扩展方法，激活内存和 I/O 成本更低。
- 仅依赖 dense 投影和归一化，无需专门 kernel 或基础设施优化。
