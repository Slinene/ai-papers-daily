---
title: Calibrated Early Termination with Bounded Optimality Gaps for Constrained Vector
  Search
title_zh: 约束向量搜索的校准早停与有界最优间隙
authors:
- Xinyu Zhang
- Jingze Li
- Baihua Zheng
- Weiwei Sun
affiliations:
- Fudan University
- Singapore Management University
arxiv_id: '2611.16148'
url: https://arxiv.org/abs/2611.16148
pdf_url: https://arxiv.org/pdf/2611.16148
published: '2026-11-12'
collected: '2026-11-13'
category: RecSys
direction: 图索引早停的风险约束最优停止规则
tags:
- Vector Search
- Early Termination
- Graph Index
- Calibration
- Constrained k-NN
- Optimality Gap
one_liner: 提出 CaST 早停规则，对带类别配额约束的图向量检索提供概率校准，并给出与类最优成本差距的有界保证
practical_value: '- 召回服务中使用图索引（HNSW 等）做向量检索时，可将停止条件从固定 hops/候选数改为校准的单调阈值规则：根据已观察到的
  visited nodes 统计量是否超过阈值决定早停，保证每查询精确概率≥1-ε；这对电商类目配额（如每类最多贡献多少 SKU）的高可靠召回尤其有用。

  - 离线评估流程可复用：用日志查询回放，把停止规则族定义为对观测单调的 staircase 函数，利用动态规划离线求解最优阈值链；再通过固定序列二项检验在线校准，避免过拟合和多重检验问题。

  - 用 Lagrangian weak duality 推导类最优下界，可以在不枚举所有规则的情况下量化当前规则与最优的 cost gap，适合业务中评估停止策略是否有优化空间，若
  gap 接近 1 则无需进一步调参。

  - 对于 Agent/RAG 中向量检索延迟敏感场景，借鉴 CaST 的 risk-constrained stopping 可以在保证检索精度下限的同时降低平均延迟，比只优化
  average recall 的 learned early termination 更可靠。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：向量搜索是推荐和 RAG 的检索层，许多应用限制每类最多贡献多少答案（constrained k-NN）。图索引用 best-first traversal 查询，停止位置同时决定成本和答案是否精确。现有 learned early-termination 方法只优化平均 recall，不保证单查询的精确概率；多重检验能校准规则，但无法知道与最优规则的差距。

**方法关键点**：声明规则可用的观测，考虑对所有观测单调的规则族。将风险约束停止转化为序多胞体上的线性规划，Lagrangian minimizer 形成嵌套的 staircase 规则链，用动态规划精确求解。沿链做固定序列二项检验得到校准规则 CaST，失败概率≤ε，置信度 1-δ。Lagrangian weak duality 在所有风险水平上一次给出类最优下界，无需 union bound。

**关键结果**：在两个百万条目数据集上回放日志查询，CaST 在风险水平 0.03 至 0.10 下成本最多为类最优的 1.132 倍（95% 联合置信）；在 held-out 查询上，CaST 比其他校准规则更快，其他规则平均耗时多 4.8% 至 45.5%。
