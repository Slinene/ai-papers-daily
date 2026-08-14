---
title: 'FSGR: Mitigating Token Frequency Bias for Fair SID-Based Generative Recommendation'
title_zh: FSGR：缓解 SID 生成式推荐中的 Token 频率偏差
authors:
- Yuchen Zheng
- Sihan Xu
- Jingwen Yang
- Xiangrui Cai
- Haiwei Zhang
- Xiaojie Yuan
affiliations:
- Nankai University
arxiv_id: '2608.12845'
url: https://arxiv.org/abs/2608.12845
pdf_url: https://arxiv.org/pdf/2608.12845
published: '2026-08-13'
collected: '2026-08-14'
category: GenRec
direction: 生成式推荐 · Semantic ID 公平性
tags:
- Semantic ID
- Generative Recommendation
- Token Frequency Bias
- Fairness
- RQ-VAE
- LLM4Rec
one_liner: 提出 FSGR 框架，在 SID 构建与 LLM 训练两端联合缓解 Token 频率偏差，平均 Gini 公平性提升超 20%
practical_value: '- 在 RQ-VAE 生成 Semantic ID 时，用 mini-batch 内 OT 对齐均匀边际分布（Sinkhorn-Knopp
  + KL）替代纯最近邻量化，可显著提升 codebook 覆盖率（实验中 Coverage 从 0.67/0.78 升到 0.999/1.0），缓解冷门类目获得高热度
  token 不足的问题。业务中若已有 SID 或 item-id 量化模块，可低成本引入该正则项。

  - 对 LLM 做 SID 生成时，先标准 CE 预训练，再在第二阶段对 SID 预测 logits 加对数频率先验（b=-log(f+ε)），并按层设置校准温度（浅层弱、深层强）。这一分层温度技巧直接适配电商类目层级：粗粒度类目不应被强校准，细粒度长尾靠深层强化校准。

  - 评估生成式推荐的 item-side fairness 时，不要只看整体 Recall/NDCG，用生成 token 频率分布的 Gini coefficient
  做监控，能捕捉头部 token 过度曝光；FSGR 达到平均 Gini 改善 20%+，且准确率几乎不降。

  - 该框架与 LoRA 微调兼容（LLM 用 8-bit AdamW + LoRA），适合工业级大模型推荐侧的落地；可直接把 HFC 作为插件用于现有 SID
  生成式推荐系统。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
Semantic ID (SID) 生成式推荐取得了显著成功，但存在被忽视的 Token Frequency Bias：高频 SID token 被系统性过度预测，低频 token 预测不足，导致曝光集中在头部类别。该偏差源于 SID 构建阶段 codebook 利用率不平衡，以及推荐训练阶段 popularity bias 与最大似然估计（MLE）目标的叠加。现有 SID 方法关注 codebook 质量，忽略下游公平性；LLM 通用 debiasing 方法因 SID 的层次语义而表现次优。

**方法关键点**  
提出 FSGR，包含两个模块：  
- **Balanced Semantic Quantization (BSQ)**：在 RQ-VAE 基础上，引入 OT-based Assignment Optimization (OTA)，在 mini-batch 内将量化建模为最优传输问题，用 Sinkhorn-Knopp 求解均匀边际分布，并通过 KL 散度对齐软分配；同时设计 Dual-Criteria Re-anchor (DCR) 机制，周期性识别 dead codewords，按“高运输成本区域（几何空洞）”或“高密度区域”两种准则重新锚定。  
- **Two-Stage Recommendation Training**：第一阶段用标准交叉熵做语义对齐预训练；第二阶段用 Hierarchical Frequency Calibration (HFC)，对 SID 预测 logits 加对数频率先验 b=-log(f+ε)，并按层设置校准温度 τ_l = l/L，浅层弱校准、深层强校准，适配 SID 层次语义。

**关键实验**  
在 Amazon Luxury Beauty、Industrial and Scientific、Software 三个数据集上，基于 TIGER、Llama3.1-8B、Qwen3-8B 三个 backbone 评估。对比 RQ-VAE、RT、QuaSID、MiLe、WAKL。BSQ 在 TIGER 上 Gini 明显降低（Beauty: 0.5494 vs 0.7310）；完整 FSGR 在 Llama 和 Qwen 上 Gini 最低（Beauty: 0.4976/0.5128 vs 0.7174/0.7368），平均 Gini 改善超 20%，Recall/NDCG 保持 competitive。消融实验证明 BSQ 和 HFC 均必要；Codebook Coverage 接近 100%，Gini 显著下降；HFC 的层级温度优于 reverse 和 fixed 策略。

**最值得记住的一句话**  
SID 生成式推荐的 token 频率偏差是 codebook 不平衡与 MLE 训练双重放大所致，必须在 SID 构建端和 LLM 训练端同时做平衡与频率校准，才能有效实现公平性与准确率的兼顾。
