---
title: Intuition-Guided Latent Reasoning for LLM-Based Recommendation
title_zh: 直觉引导的潜在推理用于大语言模型推荐
authors:
- Chang Liu
- Yimeng Bai
- Xiaoyan Zhao
- Yang Zhang
- Qifan Wang
- Fuli Feng
- Wenge Rong
affiliations:
- Beihang University
- University of Science and Technology of China
- The Chinese University of Hong Kong
- National University of Singapore
- Meta AI
arxiv_id: '2606.27684'
url: https://arxiv.org/abs/2606.27684
pdf_url: https://arxiv.org/pdf/2606.27684
published: '2026-06-26'
collected: '2026-06-29'
category: GenRec
direction: 生成式推荐 · 潜在推理直觉引导
tags:
- LLM-Based Recommendation
- Latent Reasoning
- Recommendation Intuition
- Beam Search
- BPR Loss
- Sequential Recommendation
one_liner: 提出 IntuRec，通过 top-K 候选集构建推荐直觉，注入推理起始点，大幅提升 LLM 潜在推荐推理的准确性和效率
practical_value: '- 可用 top-K 候选集约束 LLM 潜在推理的起始点：先在 ISE 阶段用标准的 next-token loss 训练 LLM
  生成候选，再用 beam search 产出离线候选集，作为“直觉”源——这套流程可直接嵌入现有的生成式推荐管线，提升推理起始点的语义匹配度。

  - TACB（目标感知候选平衡）可复用：训练时按验证集正样本覆盖率动态调整候选集中目标物品的保留概率，能有效防止捷径学习，维持训练-评测分布一致，适合迁移到所有需要从候选池中学习偏好表征的场景。

  - IDAE 双注意力编码器设计值得借鉴：对每个候选物品独立做 self-attention 提取物品级表示，再用 cross-attention 以初始状态作为
  query 融合历史信息，生成直觉嵌入——这种结构可应用于精排或召回链路，用轻量 attention 融合候选与用户历史，生成高质量起始向量。

  - BPR 直觉对齐损失提供了一种偏好信号注入方式：强制直觉嵌入比负例更靠近目标物品嵌入，可在不增加标签成本的情况下为隐空间推理提供监督，尤其适合在缺乏显式反馈时，对齐候选与用户真实偏好。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有 LLM 潜在推荐推理方法（如 LatentR3）对中间推理过程缺乏约束，初始状态往往与目标物品的嵌入空间相距甚远，导致推理路径滑入次优区域。受认知科学启发——人类多步推理前会形成直觉性先验来剪枝搜索空间——本文提出用“推荐直觉”（top-K 候选集）来锚定推理起点，提升推理轨迹的准确性和效率。

**方法关键点**：
- **两阶段框架 IntuRec**：第一阶段 ISE（直觉源抽取）在序列推荐设定下微调 LLM，用 beam search 生成 top-K 候选作为直觉源；第二阶段 IRI（直觉表示注入）将候选集编码为单个嵌入，注入潜在推理的第一个隐藏状态，再执行 autoregressive 推理。
- **TACB 目标感知候选平衡**：根据验证集目标物品覆盖率动态控制训练时候选集里保留目标的概率，防止输入中直接包含目标造成的捷径学习，同时保持训练-评测分布一致。
- **IDAE 双注意力编码器**：对每个候选物品的 token 序列做 self-attention + last-token pooling 得到物品向量，再以推理初始状态为 query 做 cross-attention 融合全局信息，产出直觉嵌入。
- **BPR 直觉对齐损失**：引入对比学习额外监督，鼓励直觉嵌入与目标物品嵌入的余弦相似度高于负例，防止编码器因只看到高质量候选而产生结构性偏差。

**关键结果**：在 Amazon 的 CDs、Toys、Games 三个子集上评估。以 Qwen2.5-1.5B 为底座，IntuRec-D（基于 D³ 骨干）取得 SOTA：CDs 上 Recall@5 0.1174、NDCG@5 0.0933；Toys Recall@5 0.0922；Games Recall@5 0.0751。消融证实 TACB、IDAE 的 self/cross-attention、BPR 损失均显著贡献；可视化显示 IntuRec 的直觉嵌入明显更接近目标物品，且形成各向异性偏好流形；超参数分析表明候选集大小 K≈15 最佳，而推理步数 N=1 即达峰值，说明高质量初始化可极大减少推理所需步数。
