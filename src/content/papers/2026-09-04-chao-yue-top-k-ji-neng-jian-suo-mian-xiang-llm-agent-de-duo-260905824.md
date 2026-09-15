---
title: 'Beyond Top-k Skill Retrieval: Diversity-Aware Skill Routing for LLM Agents'
title_zh: 超越 Top-k 技能检索：面向 LLM Agent 的多样性感知技能路由
authors:
- Wang Wei
- Tiankai Yang
- Samyadeep Basu
- Hongjie Chen
- Yue Zhao
- Zhengzhong Tu
- Xiyang Hu
- Franck Dernoncourt
- Ryan A. Rossi
- Hoda Eldardiry
affiliations:
- Virginia Tech
- University of Southern California
- Adobe Research
- Dolby Labs
- Texas A&M University
arxiv_id: '2609.05824'
url: https://arxiv.org/abs/2609.05824
pdf_url: https://arxiv.org/pdf/2609.05824
published: '2026-09-04'
collected: '2026-09-15'
category: Agent
direction: LLM Agent 技能路由 · 多样性子集选择
tags:
- DPP
- Skill Routing
- Diversity
- LLM Agents
- Subset Selection
- Reranking
one_liner: 用 DPP 多样性选择与 query-residual 核，在技能路由中平衡相关性与非冗余，提升多技能任务覆盖
practical_value: '- 在电商/广告 Agent 需要从大型技能/工具库中为复杂 query 选择多个互补技能时，不要只用 pointwise top-k；可加
  DPP 选择步骤，用质量分 × 相似度核构造行列式点过程，平衡相关性与非冗余。

  - 构造 DPP 相似度核时，先从技能 embedding 中减去 query 对齐分量（residual），避免惩罚因共享 query 相关性而相似的互补技能；对多技能任务尤其有效，可减少有用技能被误杀。

  - 工程实现上，仅对检索到的 top-M 候选（如 50）做贪心 MAP，配合 incremental Cholesky 更新，开销小，适合线上 Agent 路由；候选集大小
  M 和 residual 混合系数 λ 可调。

  - 该方法对搜索/推荐中的多样性重排、多模型路由、多工具组合选择也有直接借鉴意义：在相关性分数基础上增加 query-conditioned 多样性约束，能提升列表对复杂意图的覆盖度。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM Agent 越来越多依赖外部技能，但面对数千到数万规模的技能库，如何为复杂用户请求选择合适的技能成为瓶颈。现有 skill router 通常独立地按 query 相关性对候选技能打分并取 top-k，忽略了技能间的冗余；多步骤任务往往需要多个互补技能，而 top-k 可能返回多个功能重叠的技能，浪费 context budget 并遗漏必要能力。因此，技能路由不应只是相关性排序，还应是互补集合选择。

**方法关键点**
- 在 standard retrieve-and-rerank 之上引入 DPP 子集选择：先由 retriever 召回 top-M 候选，reranker 给出质量分 q_i(x)，再用 DPP 核 L_ij = q_i(x) φ_x(s_i,s_j) q_j(x) 选择 k 个技能。
- 关键设计是 query-residual diversity kernel：先从技能 embedding e_i 中减去 query 对齐分量 (e_i^T e_x)e_x，得到残差 r_i，再用混合 λ 得到 z_i；相似度 φ_x(s_i,s_j) = (1 + z_i^T z_j)/2。这样惩罚的是 query 正交方向上的重叠，而非因共享 query 相关性带来的相似，避免误删互补技能。
- 推理采用贪心 MAP，首步自动选择质量分最高的技能，后续步根据 log-det 边际增益选择补充技能；用 incremental Cholesky 更新加速。

**关键实验**
在 SkillRouter benchmark（75 个 expert-verified queries，约 80K 候选技能，含单技能与多技能子集）上，DSR 保持与 SkillRouter 相同的 retriever 和 reranker，仅改变最终选择层。整体 Recall@20 从 0.754 提升到 0.768，Full Coverage@20 从 0.560 到 0.573；@50 时 Recall 提升到 0.808，Full Coverage 提升到 0.633。多技能子集收益更明显：@20 Recall 0.704→0.739，Full Coverage 0.458→0.492；@50 Recall 0.704→0.773，Full Coverage 0.458→0.551。消融显示，标准 cosine kernel 的多技能 FC@10 仅 0.254，而 query-residual kernel 达到 0.441；reranker quality 比 embedding quality 更强。

**最值得记住的一句话**
大规模技能路由应同时优化 query 相关性与技能集合的非冗余性，且多样性惩罚应在 query-residual 空间计算，才能保留共享任务上下文但功能互补的技能。
