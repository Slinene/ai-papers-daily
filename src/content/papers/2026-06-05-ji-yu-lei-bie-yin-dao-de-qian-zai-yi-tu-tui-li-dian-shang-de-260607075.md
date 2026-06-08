---
title: 'Beyond Matching: Category-Guided Latent Intent Reasoning for Generative Retrieval
  in E-Commerce'
title_zh: 基于类别引导的潜在意图推理：电商生成式检索的桥接语义鸿沟
authors:
- Fuwei Zhang
- Xiaoyu Liu
- Jiajie Jin
- Jiale Mao
- Wei Chen
- Dongbo Xi
- Yifan Yang
- Peng Yan
- Zichao Hao
- Zhao Zhang
affiliations:
- Beihang University
- Meituan
- Renmin University of China
- Beijing Information Science and Technology University
arxiv_id: '2606.07075'
url: https://arxiv.org/abs/2606.07075
pdf_url: https://arxiv.org/pdf/2606.07075
published: '2026-06-05'
collected: '2026-06-08'
category: GenRec
direction: 生成式推荐 · 潜在推理 · 类别层级
tags:
- Generative Retrieval
- Latent Reasoning
- E-Commerce Search
- Semantic ID
- Category Hierarchy
- Constrained Decoding
one_liner: CaLIR 利用产品类别层级在连续空间进行潜在意图推理，避免显式 CoT 的延迟，高效桥接查询与语义 ID 的鸿沟。
practical_value: '- **用产品类别层级做生成式检索的隐式推理脚手架**：在电商场景中，可直接复用现有的多级类目体系，将解码器隐藏状态逐层对齐到类目，替代显式思维链，大幅降低线上延迟。

  - **多正例对比学习处理多意图查询**：电商查询常对应多个有效类目，使用 Multi-Positive InfoNCE 损失，让查询的潜在状态同时靠近所有相关类目原型，提升意图覆盖与鲁棒性。

  - **动态装配类别级前缀树约束解码**：线下按类目预建语义 ID 前缀 Trie，线上根据推理出的 Top-K 类目动态合并，缩小搜索空间，提高解码准确率且几乎不增加在线开销。

  - **粗到细的潜在推理无需显式解码步**：插入固定数量的连续隐状态滑动推理（L 步），不产生额外 token，只在 beam search 前一次性计算，批量处理后与编码器状态拼接用于后续解码，适用于低延迟电商搜索。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商搜索中，查询短、噪声多、属性密集，现有生成式检索（GR）模型需要将自然语言查询直接映射为抽象的语义 ID（SID），存在严重的表征鸿沟。显式 Chain-of-Thought 推理虽然可桥接语义，但增加的 token 解码延迟难以满足线上低延迟要求。

**方法关键点**：
- **索引阶段**：用 RQ-VAE 将商品语义嵌入量化为层级 SID。
- **训练阶段**：
  1. **层级语义推理（HSR）**：在解码器首先生成 L 步连续隐状态（潜在推理路径），每步隐状态经投影后预测对应层级的商品类别，用掩码交叉熵强制粗到细的对齐。
  2. **查询级推理增强（QRE）**：针对一个查询对应多个有效类目的情况，采用多正例 InfoNCE 损失，拉近查询潜在状态与所有相关类目原型的距离，增强意图多样性与鲁棒性。
  3. 最终隐状态用于自回归生成 SID，与上述辅助目标联合优化。
- **推理阶段**：
  - **推理感知约束解码（RCD）**：用最后一步推理隐状态预测 Top-K 类目，动态装配预建的类别级前缀 Trie 作为束搜索约束，将解码限制在与意图相符的 SID 子空间内。
  - 潜在推理状态一次性计算，拼接到编码器输出，被束搜索所有 beam 共享，计算开销固定。

**关键结果**：在 Amazon ESCI 多语言数据集（us/es/jp）上对比三类基线（稀疏检索 BM25、稠密检索 DPR/Sentence-T5/MPNet/BGE-M3、生成式检索 DSI/TIGER/Hi-Gen/LTRGR/RIPOR/MERGE/CAT-ID2），CaLIR 在所有指标（R@5/10/100, NDCG@10/100）上均最优。以最强基线为参照，ESCI-us 上 R@100 提升超过 10%，ESCI-es 也有显著提升。消融显示 HSR、QRE 和 RCD 各自贡献显著，去除任何模块都会导致性能下降。

**一句话启示**：利用电商天然的类目层级作为隐式推理的监督信号，在连续空间完成意图规划再解码，是平衡效果与效率的关键。
