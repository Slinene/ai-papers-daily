---
title: Causal Modeling of Adverse Pregnancy Outcomes via Adaptive LLM Proposals
title_zh: 基于自适应 LLM 提议的不良妊娠结局因果建模
authors:
- Kavimayil P. Komarasamy
- Saurabh Mathur
- Ameet Soni
- David M. Haas
- Kristian Kersting
- Sriraam Natarajan
affiliations:
- The University of Texas at Dallas
- Technical University of Darmstadt
- Swarthmore College
- Indiana University School of Medicine
- Hessian Center for AI (hessian.ai)
arxiv_id: '2608.21079'
url: https://arxiv.org/abs/2608.21079
pdf_url: https://arxiv.org/pdf/2608.21079
published: '2026-08-21'
collected: '2026-08-24'
category: Reasoning
direction: LLM 自适应提议的因果发现
tags:
- Causal Discovery
- LLM as Proposal
- Neurosymbolic
- Estimation of Distribution
- Medical AI
one_liner: 将 LLM 作为自适应提议分布，按数据评分迭代生成因果图，恢复全部专家边并发现新边
practical_value: '- 在需要 LLM 生成结构化对象（因果图、推荐路径、用户特征关系）时，建议用 Sample-Evaluate-Update 循环替代
  one-shot：批量采样候选 → 用业务/数据打分 → 将 top-K 候选作为 in-context examples 喂回 LLM，能显著提升结构正确性和稳定性。

  - 可把先验业务规则编码为 forbidden edges/硬约束，在 LLM 生成阶段直接过滤非法候选，避免后续修复成本；这与电商场景中时间顺序、曝光/点击因果限制、类目层级约束非常类似。

  - 用 top-K 候选的“共同边/共同项”压缩表示替代全量候选列表，最多可减少 3 倍 prompt token，同时保持接近的性能；适合在线 Agent 或
  RAG 里做预算受限的 LLM 探索。

  - 结构评分上用决策树局部结构替代 BIC 的 full CPT penalty，更适合高基数离散特征或稀疏观察数据；在推荐系统里做轻量因果图/特征依赖建模时可以复用这一
  trick。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
不良妊娠结局（APOs）如早产、妊娠糖尿病等，因果结构复杂、观察数据稀缺、干预实验受限。纯数据驱动的因果发现（PC、FCI）在数据少、噪声高时失效；LLM 虽然能提供广泛领域先验，但 one-shot 生成不稳定、不能区分因果与相关，且对 prompt 敏感。现有 LLM + theory refinement 又容易陷入局部最优。

## 方法关键点
- **CLARA 框架**：把 LLM 当作自适应提议分布，实施 Generate-Evaluate-Update 循环，借鉴 MIMIC 随机优化。
- **生成**：用 LLM 批量采样候选因果图，并利用 forbidden edges（如时间顺序）过滤非法候选。
- **评估**：用 TreeBIC 替代标准 BIC；每个局部条件用决策树表示，允许 Context-Specific Independence，降低对高基数 parent 配置的过度惩罚。
- **更新**：从 history 中选 top-K 高评分图，构造 in-context representation 喂回 LLM；支持 full graphs 或共同边压缩表示两种方式。
- **聚合**：最终对 top-K 图做 union，并处理 cycle。

## 关键结果
- 在合成 ALARM 数据集上，CLARA 的 SID 最低。以 GPT-5.2 为例，CLARA SID=139.8，显著优于 one-shot LLM（205.7）、LLM+theory refinement（194.2）、PC（314）、FCI（368）；且对 Llama-3.3-70B 同样有效。
- 在真实 nuMoM2b 临床数据上，CLARA（GPT-5.2）SID=0.0，完美恢复专家图；恢复全部 31 条专家验证边，并额外提出 30 条边，其中 87% 被临床专家评为 confirmed，13% 为 plausible。
- CLARA 对数据量和噪声鲁棒：数据从 3k 到 9k、噪声从 20% 到 60%，SID 保持稳定；PC/FCI 在同样设置下恶化或非单调。
- 共同边压缩表示减少 prompt token 最多约 3 倍，性能与 full graphs 接近。

**最值得记住**：LLM 的 broad prior 不直接等于可靠答案，但把它放到“数据打分的迭代重采样”回路里，既能继承领域先验，又能用经验证据纠偏；在 medical 等数据稀缺、错误成本高的场景，这是比 one-shot 或纯 greedy refinement 更稳的神经符号范式。
