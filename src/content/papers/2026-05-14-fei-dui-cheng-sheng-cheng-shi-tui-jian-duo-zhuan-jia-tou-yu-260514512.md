---
title: Asymmetric Generative Recommendation via Multi-Expert Projection and Multi-Faceted
  Hierarchical Quantization
title_zh: 非对称生成式推荐：多专家投影与多面层次量化
authors:
- Bin Huang
- Xin Wang
- Junwei Pan
- Yongqi Zhou
- Yifeng Zhou
- Zhixiang Feng
- Shudong Huang
- Haijie Gu
- Wenwu Zhu
affiliations:
- Tsinghua University
- Tencent
arxiv_id: '2605.14512'
url: https://arxiv.org/abs/2605.14512
pdf_url: https://arxiv.org/pdf/2605.14512
published: '2026-05-14'
collected: '2026-05-15'
category: RecSys
tags:
- Generative Recommendation
- Semantic IDs
- Vector Quantization
- Mixture-of-Experts
- Hierarchical Quantization
- Sequential Recommendation
one_liner: 提出AsymRec框架，解耦输入输出表示，用连续专家投影缓解输入端信息瓶颈，用多面子空间残差量化防止输出端维度坍塌，平均NDCG@10提升15.8%
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐（GenRec）将物品表示为离散语义ID，并对称地用于模型输入与预测目标。这种设计存在**双重信息瓶颈**：(1) **输入端**：有损量化丢弃了细粒度语义，且离散ID嵌入在训练中偏向高频热门物品，导致冷物品泛化差；(2) **输出端**：简单量化的离散目标重建误差高，码本碰撞严重，监督信号不精确，而直接预测连续向量又易引发维度坍塌。

### 方法关键点
**AsymRec** 采用非对称连续-离散框架，解耦输入输出表示：
- **Multi-expert Semantic Projection (MSP)**：将原始连续语义嵌入通过 Mixture-of-Experts 直接投影到 Transformer 隐藏空间，旁路离散ID查找。多个专家（2层MLP）由门控网络加权，保留语义拓扑结构，改善冷物品与长尾物品的表示质量。
- **Multi-faceted Hierarchical Quantization (MHQ)**：先将嵌入经可学习投影映射到多个正交子空间，在每个子空间内进行多层残差量化（RQ），码本采用EMA更新稳定优化。同时引入子空间能量均衡损失与投影矩阵正交正则化，防止信息坍塌至少数子空间。最终每个物品获得由 M×L 个码本索引组成的结构化离散码字，提供高保真监督信号。
- **训练与推理**：Transformer 解码器以 MSP 输出的连续表示作为输入，预测 MHQ 产生的多面层级语义ID；推理时使用图约束解码保证生成有效性。

### 关键实验结果
在 Amazon 四个子集（Sports、Beauty、Toys、CDs）上，AsymRec对比12个基线（含Caser、SASRec、BERT4Rec、TIGER、RPG等），**NDCG@10平均提升15.8%**，所有数据集均达最优。消融实验表明：
- 替换连续输入为离散ID，性能下降；冷物品区间 Recall@10 大幅下滑，证实 MSP 缓解了流行度偏差。
- 改用连续输出直接回归，Transformer 输出有效秩从178.1锐减至99.5，NDCG@10明显下降，验证离散目标防止维度坍塌的必要性。
- MHQ用更少的总码本数（如8子空间×3层=24 tokens）即可超越标准乘积量化（64 tokens），且能量均衡与正交正则化进一步提升了量化质量。
在线A/B测试中，部署于大型广告平台pCVR系统，**总消耗提升1.4%，GMV提升1.9%**，证实方法在工业级场景的有效性。

> 一句话：解耦输入连续投影与输出结构化离散量化，是打通生成式推荐双重瓶颈的关键。
