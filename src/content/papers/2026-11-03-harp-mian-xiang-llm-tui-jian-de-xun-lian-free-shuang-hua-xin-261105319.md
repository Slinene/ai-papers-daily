---
title: 'HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation'
title_zh: HARP：面向 LLM 推荐的训练-free 双画像 Agent 通信
authors:
- Zhen Tao
- Xun Zhou
- Xuhui Chen
- Ziyue Qiao
- Qingqiang Sun
affiliations:
- Harbin Institute of Technology, Shenzhen
- Great Bay University
- Shenzhen Loop Area Institute
arxiv_id: '2611.05319'
url: https://arxiv.org/abs/2611.05319
pdf_url: https://arxiv.org/pdf/2611.05319
published: '2026-11-03'
collected: '2026-11-04'
category: RecSys
direction: LLM Agent 推荐 · 双 Profile 通信
tags:
- LLM Recommendation
- Agentic Communication
- Dual Profile
- Homophily
- Retrieval
- Training-Free
one_liner: 将 LLM 推荐重构为用户-物品双 Profile 通信，用检索侧同质性门控和反思更新提升推荐准确率
practical_value: '- 将用户与物品建成 schema 对齐的双 Profile（用户：interests/quality_bar/context/behavior，物品：serves/quality_signal/context/audience），物品侧用规则抽取零额外
  LLM 调用，降低大规模 item 画像成本

  - 把 profile 相似度作为检索阶段的门控因子（BaseScore * (α+(1-α)H)）重排序候选，而不是拼进 reranker prompt，避免
  context 带宽被挤占，实测是最大收益来源

  - 用户画像更新采用单次 reflective pass + 确定性 critic 门控：基于最近 hit/miss 案例生成候选画像，只接受覆盖度更高的提案，防止无梯度更新造成画像漂移

  - 通道分解设计（pairwise disjoint + 线性加权）让 homophily 分数按通道可加性独立归因，便于线上 debug 和分通道调权'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有 LLM-based agentic 推荐只给用户建结构化 profile，item 侧没有对齐的 self-description；用户 profile 仅被注入带宽受限的 reranker prompt，无法影响 retrieval 阶段；且 warmup 后 profile 冻结，缺乏基于反馈的更新机制。这阻碍了 user-item 间的有效语义匹配。

**方法关键点**：将 LLM 推荐重铸为四阶段 agentic 通信（BUILD–TRANSMIT–UNDERSTAND–SYNC），诊断出三个缺口。HARP 在冻结 LLM 上加三个训练-free 算子：① 对称双 Profile：用户 profile 由 LLM 生成，item profile 通过规则抽取（零额外 LLM 调用），双方共享四通道 schema（preference/quality/context/audience），且通道间 disjoint；② 检索侧同质性门控：定义 profile-level homophily H(φ_u, φ_i)=Σ w_c sem(φ_u^c, φ_i^c)，在 retrieval 阶段用单调 gate g(H)=α+(1-α)H 乘到 BaseScore 上（α=0.4/0.3 for user-item/user-user），而非注入 reranker prompt；③ 单次反思更新：根据 warmup 中的 hit/miss 案例用 CoT 生成候选 profile，再用保守 critic（确定性覆盖检查）接受或拒绝，实现 in-context 画像进化。

**关键实验**：在 InstructRec 的四个数据集（Books、Goodreads、MovieTV、Yelp）上，以 gpt-4o-mini 为冻结 backbone，对比传统（LightGCN/SASRec/P5）、单边 agent（Vanilla LLM/iAgent/AgentCF/RecBot/i2Agent）和 memory-augmented（MemRec）基线。HARP 在所有指标上最优，Hit@1 相对最强已发表基线提升 +6.9%~+24.0%（Yelp 最大 +24.0%），Holm 校正后 p<1e-9。Ablation 显示检索侧 gate 是主引擎：MONOLOGUE→DIALOGUE 在 Yelp 子集上 H@1 提升 +5.7pp，而仅 prompt 注入（CONSULT）与 MEMORY 持平；说明 profile 信号应在 retrieval 阶段消费。

**最值得记住的一句话**：让物品也“说话”，并把 user-item profile 对齐后的 homophily 用做检索门控，是 LLM 推荐中低成本高收益的训练-free 改进。
