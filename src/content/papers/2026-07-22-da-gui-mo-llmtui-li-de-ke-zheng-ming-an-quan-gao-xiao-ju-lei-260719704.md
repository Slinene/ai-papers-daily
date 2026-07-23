---
title: Efficient Clustering with Provable Guardrails for LLM Inference at Scale
title_zh: 大规模LLM推理的可证明安全高效聚类
authors:
- Longshaokan Wang
- Wai Tsang Keung
- Punit Ghodasara
- Roman Wang
- Ali Dashti
- Francesc Moreno-Noguer
affiliations:
- Amazon
arxiv_id: '2607.19704'
url: https://arxiv.org/abs/2607.19704
pdf_url: https://arxiv.org/pdf/2607.19704
published: '2026-07-22'
collected: '2026-07-23'
category: RecSys
direction: 高效聚类 · LLM推理加速
tags:
- Efficient Clustering
- LLM Inference
- Set Cover
- Guardrails
- Personalization
- Scalability
one_liner: 两阶段聚类通过贪心集合覆盖确保每用户与代表相似度达标，实现50倍LLM推理成本缩减
practical_value: '- 当需要对海量用户接入LLM时，先用Mini-batch K-Means粗分，再在各簇内贪心选取代表，强制相似度≥α且属性完全匹配。该策略复杂度$O(n^2
  d/K)$，调大初始簇数$K$可线性加速并降内存，适合千万级用户场景。

  - 贪心选择的簇大小高度偏斜，可主动丢弃长尾小簇（例如仅保留4%的簇覆盖90%用户），进一步压缩下游推理量，配合上游过采样补偿掉落的用户。

  - 对合规属性（如年龄、性别）直接在匹配矩阵中要求相等，提供可证明保证，杜绝跨属性推荐风险，适合电商推荐中安全滤波环节。

  - 生产验证表明用户-代表embedding相似度与推荐相关性高（Pearson r=0.781），可直接用相似度阈值替代代价高昂的LLM评估，节省质量评估成本。'
score: 10
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：电商推荐中为3800万用户逐一调用LLM生成个性化查询和审核推荐，成本高达百万美元且耗时数百天。将用户聚类后仅对代表调用LLM是自然思路，但必须确保每个样本与代表足够相似且满足关键属性（如家庭构成），否则会带来不相关甚至安全隐患。现有聚类方法无法同时支持可配置相似度下界、属性精确匹配和千万级可扩展性。

**方法**：
- 形式化：每个用户必须分配到某个代表，使得embedding余弦相似度≥α且属性完全相等。
- 两阶段算法：① Mini-batch K-Means生成$K$个初始簇；② 在每个簇内计算成对相似度与匹配矩阵，通过Johnson–Chvátal贪心集合覆盖迭代选取覆盖最多未匹配用户的代表，直到全部覆盖。
- 可选重分配：将用户重新分配给最相似的代表，提升平均相似度，而不改变代表集合。
- 复杂度：时间$O(nd + n^2 d / K)$，内存$O(nd + n^2 / K^2)$，当$K$与$n$成比例时整体线性。

**关键结果**：
- 在购物人设/AG News等数据集上，相比K-Means、Agglomerative等基线，本方法在相同簇数下保证所有样本相似度不低于阈值，而基线有3–21%样本违反约束；速度快10–1000倍。
- 生产A/B测试：对3800万用户聚类，下游LLM查询生成和营销审核成本从$1.13M/508天降至$2.2万/10天，推荐相关性仅下降0.7%。

**核心启示**：将聚类视为受约束的集合覆盖问题，用贪心选择获得可证明的安全边界，是平衡LLM成本与推荐质量的规模化利器。
