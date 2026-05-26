---
title: 'Spectral Retrieval: Multi-Scale Sinc Convolution over Token Embeddings for
  Localized Retrieval in LLM Multi-Agent Systems'
title_zh: 谱检索：基于 token 嵌入多尺度 sinc 卷积的局部化重排序
authors:
- Andrea Morandi
affiliations:
- Cisco Systems, Inc.
arxiv_id: '2605.24764'
url: https://arxiv.org/abs/2605.24764
pdf_url: https://arxiv.org/pdf/2605.24764
published: '2026-05-23'
collected: '2026-05-26'
category: RecSys
direction: 多尺度重排序 · 局部化检索
tags:
- Spectral Retrieval
- Multi-Scale Sinc Convolution
- Re-ranking
- Dense Retrieval
- Multi-Agent Retrieval
- Late Interaction
one_liner: 在 token 嵌入上施加多尺度 sinc 卷积，以 max-over-scales 聚合实现逐 token 至均值池的平滑插值，显著提升窄片段相关性召回
practical_value: '- **无训练即插即用的重排序器**：直接复用现有双塔模型的 token 级嵌入，只需在候选文档（K=100 左右）上做多尺度卷积+max聚合，代码量极小，不改变索引和召回阶段，适合快速上线。

  - **多智能体角色感知检索**：每个 agent 用同一 query encoder 但不同 prompt，谱检索可让同一份文档对不同 agent 产生差异化的高得分（安全
  agent 看到漏洞段落，运营 agent 看到维护记录），丰富辩论输入，避免所有 agent 拿到相同 top-k。

  - **与 ColBERT 正交互补**：谱检索相当于单 query 向量版的 ColBERT，二者可堆叠；若已有 ColBERT 索引，可直接加多尺度卷积提升长文档中的局部匹配，成本仅增加
  O(K·S·N·d)。

  - **尺度网格选择简单**：默认 {1,3,5,7,10,15,20,30} 覆盖窄到宽的相关性宽度，无需调参；对于电商中商品描述（短文本）可缩为 {1,3,5}，对于长法律/政策文档可增加
  L=100 端点，计算开销线性增长。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
单向量检索（均值池化+余弦相似度）在相关性集中在文档的短短几行时严重失效，因为短片段被周围 token 平均稀释。这在多智体 LLM 系统中尤其致命：如安全运维 agent 需要匹配某个 runbook 中的几行操作步骤，但整页文档均值为通用话题，导致与 query 的余弦相似度无法区分。现有方案如 ColBERT 通过存储每 token 嵌入并做 MaxSim 解决，但索引膨胀数十倍。  

**方法**  
提出谱检索（Spectral Retrieval）作为第二阶段的插件式重排序器。它复用 ColBERT 式的每文档 token 嵌入矩阵，但用**多尺度归一化 sinc 卷积 **沿 token 轴平滑：  
- 尺度 L=1 时为恒等映射，等价于逐 token MaxSim；  
- L→∞ 时 kernel 变为均匀，等价于均值池余弦；  
- 中间尺度相当于低通滤波，可捕获不同宽度的局部相关性。  
对每个候选文档，在每个尺度 L 上计算卷积平滑后每 token 与 query 的余弦相似度，取 **max over positions**，最后在所有尺度上取 **max** 作为该文档得分。该得分天然不低于 MaxSim 与 MeanCos 中的较大者（端点恢复保证）。计算复杂度 O(K·S·N·d)，K 为候选池大小，S 为尺度数，N 为 token 数。  

**关键实验**  
- **合成基准**：1000 篇 50-500 token 的文档，植入单点相关性尖峰（余弦 α）。均值池 Recall@10 始终 ≈0.02（随机水平），而谱检索在 α=0.60 时达到 1.0，且过渡带匹配 token 级别噪声阶统计预测。  
- **LIMIT-small 公开基准**：使用 frozen all-mpnet-base-v2 编码器，谱检索将 Recall@10 从 0.33 提升至 0.90，MRR 从 0.22 提升至 0.79，严格的 Success@10（两个相关文档均在 top-10）从 0.12 提升至 0.84，**无需重训练编码器**。  

**核心直觉**  
当相关性宽度未知时，在少数几个尺度上取最大值是一种廉价且鲁棒的上报方式——窄尖峰被 L=1 捕获，段落级匹配被中间尺度捕获，文档级主题匹配被大尺度捕获。该思路可直接应用于商品搜索中长描述的关键信息提取，或 Agent 间基于共享知识库的差异化上下文供给。
