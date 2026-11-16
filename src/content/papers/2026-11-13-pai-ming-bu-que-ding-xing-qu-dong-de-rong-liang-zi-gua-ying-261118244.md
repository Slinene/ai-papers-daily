---
title: 'RACE: Ranking-Uncertainty Aware Capacity-Adaptive Customization for Efficient
  Sequential Recommendation'
title_zh: 排名不确定性驱动的容量自适应高效序列推荐框架 RACE
authors:
- Tianqi Liu
- Kaipu Sun
- Kairui Fu
- Wenkai Wang
- Sihao Liu
- Hui Zang
- Ran Chen
- Tao Wang
- Shengyu Zhang
affiliations:
- Zhejiang University
- Huawei Technologies Co., Ltd.
arxiv_id: '2611.18244'
url: https://arxiv.org/abs/2611.18244
pdf_url: https://arxiv.org/pdf/2611.18244
published: '2026-11-13'
collected: '2026-11-16'
category: RecSys
direction: 高效序列推荐 · 不确定性驱动自适应推理
tags:
- Sequential Recommendation
- Adaptive Inference
- Uncertainty Quantification
- Model Compression
- On-device Recommendation
- Ranking Uncertainty
one_liner: 用 list-wise 排名不确定性预测实例复杂度，动态裁剪模型结构和输入序列，实现端侧高效推荐
practical_value: '- 端侧 / 实时 rerank 场景不要再用统一压缩比。可以用 VBLL 作为预测头，单次 forward 同时得到预测均值与方差，计算
  list-wise ranking uncertainty 作为 query/用户难度信号；它比 MC Dropout、Ensemble 更省算力，且比 point-wise
  variance/entropy 更贴近排序目标。

  - 结构动态裁剪可复用 backbone 中间层 last hidden state 作为 user embedding，接轻量 hypernetwork-style
  sensitivity extractor 生成 channel importance，再按 quantile mask；训练用 straight-through
  estimator，推理直接 mask。辅助 FLOPs 很低，适合在已有序列模型上增量加。

  - 历史行为序列裁剪不要固定 budget，可基于 head-averaged attention 的累积重要性，并加 position-aware factor
  更关注近期 query，逐 block 保留核心 items；训练时 soft mask 保持梯度，推理时 hard drop 才能真实降低 FLOPs。

  - 若做 LLM/Agent 推理效率，可迁移“早层特征预测难度 → 提前分配资源”的思路：例如预测 query 难度决定 KV cache 保留长度、推理步数或
  MoE 专家数；self-supervised pseudo label 无需人工标注，适合在线学习。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
端侧高效序列推荐通常采用模型压缩，但现有方法大多施加统一压缩率，忽略用户意图复杂度差异，造成简单实例浪费算力、复杂实例容量不足的 Capacity-Complexity Mismatch。需要一种能按实例难度动态分配计算资源、并在结构和输入两个维度做个性化裁剪的推理机制。

**方法关键点**  
- 采用 variational Bayesian last layer 作为预测头，单次 forward 得到预测均值与方差；在此基础上定义 list-wise ranking uncertainty：对 top-K 内所有 pairwise 排序事件计算负对数似然，得到排序结构稳定性信号。该信号与推荐性能呈负相关，可作为实例复杂度 proxy。  
- 训练轻量 threshold predictor，从 early-layer features 提前预测理想裁剪率；用当前 batch 归一化的 uncertainty 生成 self-supervised pseudo label，无需额外标注。  
- 结构裁剪：复用 backbone 中间层 last valid token 作为动态 user embedding，经 hypernetwork-style sensitivity extractor 生成 channel sensitivity，按预测比例的 quantile 动态 mask FFN channels，训练用 straight-through estimator。  
- 序列裁剪：基于 head-averaged attention 的累积重要性，并加 position-aware factor，逐 block 保留 TopK items；训练 soft mask，推理 hard drop。  
- 训练目标联合推荐 loss、平均稀疏性约束与 threshold 预测 loss。

**关键实验**  
在 MovieLens-100k、Douban、Amazon-CD、Amazon-Game 四个数据集，以 SASRec 和 BSARec 为 backbone，对比 Normal、Finetune、SNIP、GEM、APG、DIET、ATP-LLAVA、PerSRec、CAUSE 等 baseline。RACE 在 SASRec 上平均 NDCG +40.87%、Hit +35.12%，FLOPs 降 2.37x；在 BSARec 上 NDCG +47.73%、Hit +41.77%，FLOPs 降 2.49x。RACE backbone FLOPs 为 0.7549，auxiliary overhead 仅 0.0490，比 DIET 低 62x，CPU 延迟 5.78ms 比 Finetune 低 40.6%。在更严格推理预算下，NDCG 仅下降 0.8%/0.3%，并额外节省 21%/11% FLOPs。

**最值得记住的一句话**  
把模型自身预测的 list-wise ranking uncertainty 从后验性能指标变成 proactive 资源分配信号，联合结构与序列双维动态裁剪，实现无 backprop 的容量自适应端侧推理。
