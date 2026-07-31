---
title: Restoring Collaborative Signals in Semantic-ID Generative Recommendation via
  Personalized Natural Language
title_zh: 通过个性化自然语言恢复语义ID生成式推荐中的协同信号
authors:
- Changjiang Han
- Qingyang Li
- Yaqiang Zang
- Jikun Kang
- Pinghua Gong
- Xue Liu
- Bowei He
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- JD.com
- Salesforce
- McGill University
- Mila
arxiv_id: '2607.27682'
url: https://arxiv.org/abs/2607.27682
pdf_url: https://arxiv.org/pdf/2607.27682
published: '2026-07-30'
collected: '2026-07-31'
category: GenRec
direction: 生成式推荐 · Semantic ID + 协同注入
tags:
- Semantic ID
- Collaborative Filtering
- Generative Recommendation
- Inference-Time Reranking
- Hierarchical Poisson Factorization
- Natural Language Bridge
one_liner: 在冻结的生成式推荐模型上，利用自然语言标签重建协同因子，层级重排候选，修复语义ID缺失的协同信号
practical_value: '- 对已有生成式推荐模型，**无需重新训练**，即可在推理时注入协同信号：用二阶共现矩阵（HPF分解）构建项目协同签名，作为重排序的附加分数，成本仅为
  O(d) 点积。

  - 将用户画像转化为**自然语言标签**（用LLM从历史行为总结），再通过一个**可学习的桥接分布 P(f|t)** 映射到协同因子空间，生成查询向量。这比直接使用历史item-embedding均值更可控、可解释、可编辑。

  - 推理时采用**层级差异化干预**：粗粒度代码做候选扩展，中粒度代码做残差重排，细粒度代码仅加库存约束，保持波束预算不变，直接提升 hit@10 约 4 个百分点（OneRec-8B）。

  - 该方法天然解耦内容与协同信号，无需修改 SID 码本，适合**迁移到其他 semantic-ID 生成器**（包括编解码器），具有较低耦合性。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：基于语义 ID（SID）的生成式推荐将物品表示为离散编码序列，但内容编码与协同信号存在竞争，紧凑的 SID 无法同时承载两者，导致协同信息表达不足。因此，即使启用链式思考推理，模型也难以将自然语言偏好转化为正确的 SID 预测，直接“思考”甚至可能降低准确率。

**方法关键点**：
1. **离线建立协同因子空间**：计算物品二阶共观矩阵 C，用分层泊松分解（HPF）得到每个物品的协同签名 ϕ_i，并按 SID 前缀聚合为前缀签名 sig(s_a, s_b)。
2. **自然语言桥接**：用 LLM 将用户历史总结为受众意图和风格标签，学习一个平滑的分布 P(f|t) 将标签映射到协同因子空间，生成用户的协同查询向量 q_u（无需读取测试集物品）。
3. **层级注入与重排**：在冻结的生成骨干（如 OneRec）推理时，对粗粒度码 s_a 做候选扩展（加协同项 softmax 增强），中粒度码 s_b 做残差重排（直接加上 q_u·sig(s_a, s_b)），细粒度 s_c 仅保留库存约束，不增加波束宽度。

**关键实验结果**：
- 数据集：RecIF 基准的 GT-disjoint 子集（826 个 next-item 预测样本）。
- 对比基线：Base（无干预）、Sem（文本相似度重排）、Hist（历史物品均值因子查询）。
- OneRec-8B：Ours 将 hit@10 从 11.14 提升至 15.50，NDCG@10 从 6.30 到 9.59；增益集中于 s_b 重排，且 HPF 表示远优于 SVD 或 K-means。
- 自然语言桥接重建的查询与原始行为查询性能相当，且能区分不同用户受众（排序级 +8.3 百分位，p<1e-4），但区分度尚有限，源于当前画像粒度粗。

**一句话结论**：用自然语言标签构建协同因子桥，无需改模型即可注入流失的协同信号，让 SID 生成真正利用群体行为信息。
