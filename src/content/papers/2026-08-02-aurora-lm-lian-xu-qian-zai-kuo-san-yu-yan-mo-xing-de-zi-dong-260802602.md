---
title: 'AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion
  Language Modeling'
title_zh: AURORA-LM：连续潜在扩散语言模型的自动编码统一表示
authors:
- Jiajun Liang
- Yucheng Liao
- Yukang Cao
- Jiazhe Wei
- Ken Li
- Wende Tan
- Jiankun Zhang
- ZY Cui
- Jingkang Yang
- Liucheng Guo
affiliations:
- PRLab, Nanjing University
- S-Lab, Nanyang Technological University
- Imperial College London
arxiv_id: '2608.02602'
url: https://arxiv.org/abs/2608.02602
pdf_url: https://arxiv.org/pdf/2608.02602
published: '2026-08-02'
collected: '2026-08-06'
category: LLM
direction: 连续潜在扩散语言模型
tags:
- Continuous Diffusion
- Flow Matching
- Latent Language Model
- Block-Causal
- Text Generation
- Representation Learning
one_liner: 解耦表示与生成，用高容量可解码连续潜在空间实现高质量文本扩散
practical_value: '- **解耦表示与生成**：在电商推荐/搜索中可训练一个连续潜在编码器（如物品描述、查询意图），冻结后单独优化扩散生成模型，降低耦合，灵活调优。

  - **高容量潜在保留信息**：使用高维连续潜在向量表示商品或查询，利用低秩噪声输入瓶颈（如 \(D_b=128\)）减少扩散模型计算，同时保留全宽解码质量，适合平衡效果与效率。

  - **噪声分配校准**：根据潜在维度调整训练时的噪声水平分布，对高维潜在侧重高噪声样本，改善生成多样性，可用于推荐文本生成或搜索词推荐中控制多样性-质量权衡。

  - **自轨迹一致性**：在扩散推理时通过相邻步预测一致性正则化，显著提升少步（如 16 步）生成质量，降低线上推理延迟，利于实时生成场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**

文本生成仍依赖离散 token，与图像、视频等连续生成范式形成不对称。现有连续语言模型要么继承非解码优化的嵌入空间，要么压缩潜在以降低生成难度却损失细节。本文主张保留高容量、可解码的文本潜在表示，并专门设计扩散模型去学习其分布，而非牺牲表示来迁就生成。

**方法关键点**
- **连续文本潜在构建**：用 Query-based Encoder-Decoder 构造因果有序的连续潜在序列。编码器利用可学习查询聚合变长 token 序列，解码器仅基于潜在前缀恢复 token，保证解码保真度。
- **块因果扩散 Transformer**：将潜在序列分块，从左到右生成块，块内通过流匹配并行去噪，平衡自回归条件与扩散并行性。
- **全宽潜在分布学习**：冻结编码器后，扩散模型直接预测全宽清洁潜在。仅对噪声输入路径施加低秩瓶颈（\(D_b=128\)），保留全宽解码接口；采用 Clean-endpoint 预测与 x0 空间损失。
- **噪声分配宽校准**：使用 tan-d 调度，将更多训练样本分配到高噪声区间（如 \(\Pr(\sigma>0.7)\) 高），适配宽潜在表示。
- **自轨迹一致性**：对齐相邻去噪步骤的清洁预测，减少少步采样时的累积误差，提升生成质量。

**关键结果**
- 在 OpenWebText 无条件和 XSum 条件摘要上，AURORA-LM (130M) 在 MAUVE、ROUGE 等指标上超越现有连续/扩散语言模型。
- 潜在宽度 \(D=1024\)、瓶颈 \(D_b=128\)、高噪声分配（\(d=7\)）以及自轨迹一致性均带来显著增益。
- 扩展到 1B 参数，超越更大规模的公开潜在扩散语言模型，验证可扩展性。

**核心洞见**：高容量、因果有序的连续潜在表示可成为连续生成与离散解码间的有效桥梁，无需为生成简化而牺牲解码能力。
