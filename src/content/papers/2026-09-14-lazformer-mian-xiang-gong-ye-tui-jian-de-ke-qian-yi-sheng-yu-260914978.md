---
title: 'LazFormer: Scaling Transformers for Industrial Recommendation via Transferable
  Generative Pre-training'
title_zh: LazFormer：面向工业推荐的可迁移生成式预训练 Transformer 扩展
authors:
- Xiaodong Li
- Alin Fan
- Mingyang Li
- Yan Xiao
- Shichao Nie
- Junfeng Zhang
- Shaochuan Lin
- Zhanming Ou
- Tao Luo
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2609.14978'
url: https://arxiv.org/abs/2609.14978
pdf_url: https://arxiv.org/pdf/2609.14978
published: '2026-09-14'
collected: '2026-09-16'
category: RecSys
direction: 生成式预训练 + 排序 Transformer
tags:
- Transformers
- Generative Pre-training
- CTR Prediction
- Sparse-Dense Transfer
- Long-sequence Modeling
- Scaling Laws
one_liner: 用生成式预训练 + 残差适配器 + 非对称多 epoch 训练，实现工业推荐 Transformer 的参数与数据双扩展
practical_value: '- 预训练与排序特征空间不一致时，用零初始化的残差适配器（类似 LoRA）注入排序特定特征，比直接拼接或额外投影更稳定，能避免稠密参数负迁移

  - 长序列建模可保留最近 1k 细粒度 token + 更早历史按组求和池化；混合稀疏注意力中最近 128 个 token 设为全局 token，其余用滑动窗口，目标
  item 只与历史交互且目标之间隔离，再逐层剪枝历史 token，可达到 92%+ 稀疏度和 5x 注意力加速，AUC 损失仅 0.1pt

  - 多 epoch 训练时，每 epoch 把稀疏 embedding 重置回预训练状态、稠密参数持续累积，能避免稀疏过拟合，使数据规模扩展持续带来收益

  - 同请求多个候选 item 共享一次用户历史序列编码，消除重复数据传输和编码开销，在线吞吐下降仅 12.1%，工程收益显著'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
工业推荐 Transformer 通常用单一排序模型从头联合训练稀疏 embedding 和稠密网络，计算资源消耗大、收敛慢。生成式预训练可同时初始化两类参数，但存在两个问题：预训练与排序的输入特征不一致，直接加载稠密参数会导致负迁移；排序多 epoch 训练又会让十亿级稀疏参数过拟合，而冻结稀疏参数则限制了对排序目标的适配。

## 方法关键点
- **生成式预训练**：对用户历史交互序列做自回归 next-item prediction，联合学习稀疏 item embedding 和稠密 Transformer 参数，用于初始化排序模型。
- **可迁移残差适配器**：借鉴 LoRA，用 `W_up·GELU(W_down·s)` 生成排序特定特征的残差，并初始化 `W_up=0`，让排序从预训练特征空间出发，逐渐注入额外行为信号（如加购、下单、行为间隔），避免直接融合带来的负迁移。
- **请求感知排序**：保留最近 1024 个 token 作为细粒度短期偏好，更早历史按组大小 8 做求和池化压缩；混合稀疏注意力结合滑动窗口和 128 个全局历史 token，目标 item 只与历史交互且目标之间完全隔离；逐层将历史 token 数从压缩后长度线性剪枝到 128；同时以请求为单位组织训练样本，多个目标 item 共享一次历史序列编码。
- **非对称多 epoch 训练**：每 epoch 开始把稀疏参数重置回预训练状态，稠密参数从上一 epoch 继承，实现数据规模扩展而不导致稀疏过拟合。

## 关键结果
在阿里国际电商工业数据集（预训练 16M 用户 / 11B tokens，排序 11M 用户 / 370M impressions）上，LazFormer 比 HSTU、OneTrans、SORT 等 baseline 的 CTR AUC 提升 +0.74pt、GAUC +1.28pt，CVR AUC +0.55pt、GAUC +0.62pt；多 epoch 版本 LazFormer† 进一步达到 CTR AUC 0.7761 / GAUC 0.6891。混合稀疏注意力在 92.63% 稀疏度下实现 5.1x 注意力加速，AUC 仅损 0.10pt。在线 A/B 两周，IPV +5.21%、订单 +3.38%、买家 +3.70%、GMV +9.85%，A10 GPU 单机吞吐仅降 12.1%。
