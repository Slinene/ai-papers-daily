---
title: 'RetrievalFormer: A Dual-Encoder Transformer for Efficient Approximate Nearest
  Neighbor Retrieval and Cold-Item Recommendation'
title_zh: 保持索引开放：共享搜索与推荐系统的推荐侧成本
authors:
- Theodore Rogers
- Joe Standerfer
- Dmitrii Timoshenko
- Haoxue Li
- Zuhaib Akhtar
- Soyoung Yang
affiliations:
- Amazon Web Services
arxiv_id: '2608.24079'
url: https://arxiv.org/abs/2608.24079
pdf_url: https://arxiv.org/pdf/2608.24079
published: '2026-08-25'
collected: '2026-08-26'
category: RecSys
direction: 双塔检索 · 冷启动与统一索引
tags:
- Dual-Encoder
- Cold-Start
- Sequential Recommendation
- Unified Search and Recommendation
- Full-Softmax
- ANN
one_liner: 量化双塔架构在统一搜索推荐索引中的推荐侧损失与冷启动收益，揭示训练目标的质量-规模权衡
practical_value: '- 双塔架构同时服务搜索和推荐，新物品通过特征编码零样本打分，无需重训即可加入索引，适合电商新品冷启动；ID-softmax 模型需要重训才能覆盖新物品，工程上不可接受。

  - 训练目标选择至关重要：full-softmax cross-entropy 比 sampled InfoNCE 在小目录上显著提升召回（MIND-small
  +54%，ML-1M +6.9%），但显存随目录线性增长，10万级目录即 OOM。实践中可按目录规模选择：<1万用 exact full-softmax，更大规模用采样负样本并做修正。

  - 冷启动评估应使用严格 zero-leakage item holdout 协议，避免信息泄漏；特征塔 + 冷冻 CF 融合（简单标量加权）即可同时获得冷启动和暖启动双优，无需额外训练。

  - 检查数据 pipeline 中的时间戳精度：float32 量化可能静默改变 LOO 目标，建议用整数时间戳并加 build gate 校验，否则跨模型比较不公平。

  - 百万级以下目录，exact full-catalog scan 延迟已足够低（<30ms），ANN 近似索引没有收益且损失召回；超过百万再考虑 IVF-PQ/HNSW，但要关注索引召回对最终指标的影响。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生产平台越来越倾向于用一个共享双塔索引同时服务搜索和推荐。但搜索没有探索槽，新物品必须从特征直接可打分，否则密集检索通道对新库存是暗的。本文量化这种“保持索引开放”的架构在推荐侧的成本，以及它在严格冷启动下的收益。

**方法关键点**：
- **RetrievalFormer**：双塔架构，用户塔为因果 transformer（prefix-LM），编码历史交互；物品塔为 AttentionFusion（Set-Transformer），编码异质特征；共享 embedding 表；打分取点积。
- **两种训练配方**：sampled InfoNCE（混合负样本） vs full-softmax cross-entropy（全目录打分+学习偏置）。后者准确率更高但显存随目录线性增长，是核心权衡。
- **严格冷启动协议**：20% 物品全局随机 holdout，所有涉及冷物品的交互从训练删除；对比 DropoutNet、Heater、ALDI 等专用冷启动基线。
- **评估协议**：全目录无掩码排序，Recall@20/NDCG@20，并报告 Echo@20 已见项诊断；挖掘出 RecBole float32 时间戳 bug 导致 19.7% 用户 LOO 目标错乱。

**关键实验**：
- **暖启动代价**：MovieLens-1M 上 RetrievalFormer Recall@20 0.3739，达到最强基线 DIF-SR 0.3944 的 94.8%（NDCG@20 损失 11.4%）；MIND-large 上差距缩至 0.8-3.6%，但排名第六/七。
- **冷启动收益**：内容塔冷启动 Recall@20 0.172±0.006，是 ALDI 的 1.4 倍、训练无 floor 的 3 倍；与冻结 MF 融合后冷 0.172 / 暖 0.276，双轴均超专用基线。
- **训练目标**：full-softmax CE 替换 sampled InfoNCE，MIND-small 提升 54%，ML-1M 提升 6.9%；但 240K 目录 OOM，暴露质量-规模墙。
- **服务成本**：百万级以下 exact scan 足够快，ANN 没有收益且索引召回仅 2.8%@top-K；双塔与 ID-softmax 检索阶段成本对称。

**最值得记住的一句话**：双塔保持索引开放的代价是暖启动准确率损失 5.2%（ML-1M），但换来冷启动 1.4 倍优势；训练目标从采样切换到 full-softmax 是最大的单点准确率杠杆，但受显存墙限制，无法扩展到统一目录规模。
