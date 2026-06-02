---
title: Time-Aware Diffusion based on Preference Disentanglement for Generative Recommendation
title_zh: 基于偏好解耦的时间感知扩散生成式推荐
authors:
- Bangguo Zhu
- Peng Huo
- Yuanbo Zhao
- Zhicheng Du
- Jun Yin
- Senzhang Wang
affiliations:
- Central South University
- National Super Computing Center (Tianjin)
- Renmin University of China
- Hong Kong Polytechnic University
arxiv_id: '2606.01670'
url: https://arxiv.org/abs/2606.01670
pdf_url: https://arxiv.org/pdf/2606.01670
published: '2026-06-01'
collected: '2026-06-02'
category: GenRec
direction: 生成式推荐 · 时间感知扩散与偏好解耦
tags:
- Generative Recommendation
- Diffusion Models
- Semantic ID
- Preference Disentanglement
- Time-Aware Masking
- Sequential Recommendation
one_liner: 首次将时间演化偏好解耦为长期与短期，并融入扩散过程的非均匀掩码，提升生成式推荐。
practical_value: '- 非均匀掩码策略可迁移至电商序列推荐：对近期交互和行为突变点施以更高掩码率，迫使模型学习短期兴趣与长期规律的权衡，提升下次购买预测。

  - 两阶段训练（warm‑up + time‑aware）如同预训练‑微调，先在通用语义空间学习 SID 共现，再注入时间与偏差信号，工程上易于实现且稳定。

  - 偏好解耦思路（period 偏好 + point 偏好）可直接用于 Agent 决策序列建模，区分持久策略与情境突变，提高多智体协作中的策略生成质量。

  - 约束解码与 Trie 树的结合确保生成 SID 对应有效物品，避免幻觉，适合落地到电商生成式召回或 query 推荐中。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有扩散式生成推荐对所有历史交互施加均匀噪声，忽略用户偏好的强时间演化特性：长期兴趣稳定持续，短期兴趣因热点或突发事件而突变。这种均匀假设导致模型无法区分关键信号，限制生成质量。  

**方法关键点**  
- **语义 ID 生成**：用 Qwen3‑Embedding‑8B 提取物品 4096 维语义向量，再通过 RQ‑KMeans 量化为 4‑token 离散 SID，构建具有层次语义的离散空间。  
- **偏好解耦**：将用户偏好拆解为 **period preference**（基于时间位置单调递增，反映长期积累）与 **point preference**（相邻物品语义偏差，捕捉兴趣突变）。  
- **时间感知掩码扩散**：前向过程不再是均匀掩码，而是根据两种偏好的加权融合为每个物品分配掩码概率 \(p_j\)，并用幂律长曲线动态平衡长期/短期贡献。掩码后使用 Transformer 重建被掩码的 SID 令牌，损失按掩码概率加权，让模型更关注近期与突变点。  
- **两阶段训练**：先进行 warm‑up 阶段用随机均匀掩码学习 SID 共现，再用时间感知掩码进行推荐任务适配，保证训练稳定。推理时通过前缀树约束解码生成有效物品。  

**关键实验**  
- 数据集：Amazon 三个子类（Beauty、Sports、Toys），留一法评估，全量排序。  
- 对比方法：传统序列推荐（SASRec、BERT4Rec 等）、SID 生成式推荐（TIGER、LC‑Rec）、扩散推荐（PreferDiff、DDSR、PreferGrow）。  
- 结果：在 Beauty 上 HR@20 达到 0.1207，相对最佳基线提升 24.56%；Sports 上 HR@20 提升 29.21%，NDCG@20 提升 25.45%；Toy 上 HR@20 提升 10.88%。消融显示去掉任一偏好或均匀掩码都会显著下降。  

**核心结论**  
时间感知非均匀扩散对生成式推荐至关重要，偏好解耦能同时捕捉长期稳定性与短期兴趣偏差，大幅优于均匀扩散范式。
