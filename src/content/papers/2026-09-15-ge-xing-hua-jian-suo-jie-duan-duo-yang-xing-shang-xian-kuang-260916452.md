---
title: 'PCap: Personalized Retrieval-Stage Diversity Capping in Facebook Marketplace'
title_zh: 个性化检索阶段多样性上限框架：Facebook Marketplace 的 PCap
authors:
- Guangchao Yuan
- Janis Fuh
- Christopher Choate
- Xun Tang
- Wenqi Zhu
- Chengyi Zhang
- Pavan Kumar Paalya Chandrashekar
- Jiang Han
- Jiangyuan Li
- Hongyan Wang
affiliations:
- Meta
arxiv_id: '2609.16452'
url: https://arxiv.org/abs/2609.16452
pdf_url: https://arxiv.org/pdf/2609.16452
published: '2026-09-15'
collected: '2026-09-16'
category: RecSys
direction: 检索阶段个性化多样性约束
tags:
- Personalized Retrieval
- Diversity Capping
- Retrieval-Stage Diversification
- Online A-B Testing
- Parameter Tuning Sequence
- E-commerce Recommendation
one_liner: 用 Shannon 熵将用户分桶，并在检索阶段施加个性化类目上限，在线 A/B 提升浏览深度与点击
practical_value: '- 在检索阶段做低成本多样性：按类目或内容分组施加 cap，在 shard 扫描和聚合层直接限制单组候选数，避免把所有多样性任务都压到
  ranker。适合多源召回、高延迟敏感的大规模推荐系统。

  - 用户多样性建模用 Shannon 熵而非 HHI：熵能纳入点击数量权重，避免只点 4 个类目和点 10 个类目被归一化成同样高分。归一化后等频分 6 桶，既保留个性化又降低短期噪声影响，工程上稳。

  - 高维参数不要手动调：多个桶乘数、source multiplier 组合巨大，用固定分配流量的在线顺序网格搜索 PTS，每轮收缩范围，比贝叶斯优化更透明、更适配现有
  QE 基础设施。

  - 个性化多样性资源应“边缘重”：实验显示中间桶用户中性配置无收益，低多样性用户需放宽 cap，高多样性用户需收紧 cap。个性化多样性只对偏好极端用户显著有效，中间人群不划算。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
Facebook Marketplace 的推荐系统依赖历史互动，容易形成反馈循环，加剧类目集中、内容同质化。多样性通常只在 ranker 阶段做，但检索阶段已决定下游候选池的多样性上限。因此，在检索阶段引入个性化多样性约束，既能改善用户浏览体验，又能避免跨多源召回下的候选偏向主导类目。

## 方法关键点
- **用户多样性打分**：基于最近滑动窗口点击行为，计算 FPT 类目分布上的 Shannon 熵，纳入用户 engagement volume；归一化后删除低点击用户，按熵值将用户等频分入 6 个多样性桶，桶 1 最集中、桶 6 最多样。
- **检索阶段 capping**：在 indexer-shard 扫描和聚合两层，对每个 FPT 类目设置上限。cap 由 source fetch count × source multiplier × 个性化 diversity multiplier 决定；低多样性桶采用更宽松 cap，高多样性桶采用更紧 cap，强制拓展候选类目覆盖。
- **自动化参数调优 PTS**：将高维桶乘数、source multiplier 映射到 Parameter Tuning Sequence，每轮固定控制臂、多个候选臂小流量运行数天，覆盖工作日/周末周期，然后根据指标收缩参数范围，等价于在线网格搜索。
- **实验设计**：两阶段在线 A/B，阶段 1 验证 uniform capping vs no capping，阶段 2 验证 PCap vs uniform capping。

## 关键结果
- Uniform capping 仅显著提升 VPV +0.3088%，PDP / MLI / sessions 无统计显著改善，说明只增加曝光不转化为深度互动。
- PCap 相对 uniform capping，VPV +0.2243%、PDP +0.2250%、Marketplace Sessions +0.1708%，均显著；MLI +0.1109% 不显著；平均延迟仅增加 0.8ms。
- 分桶多样性变化符合设计：bucket-1 多样性显著下降 -1.0537%，bucket-6 显著上升 +0.2469%，中间桶基本不变。
- PTS 自动调参发现最优乘数呈单调模式：中间桶接近中性，低多样性桶需要更大乘数放宽 cap，高多样性桶需要更小乘数收紧 cap。

## 最值得记住的一句话
检索阶段个性化多样性 capping 能以极低延迟代价提升浏览深度，但其收益主要来自偏好极端用户，中间用户无需额外个性化资源。
