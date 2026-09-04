---
title: Towards a Statistical Understanding of Mixture-of-Experts
title_zh: 混合专家架构的统计理解：路由、稀疏激活与共享专家的风险界
authors:
- Siyuan He
- Bokai Yang
- Jie Hu
- Ziwen Gao
- Yuhong Yang
affiliations:
- Tsinghua University
- East China Normal University
- Beijing Institute of Mathematical Sciences and Applications
arxiv_id: '2609.03501'
url: https://arxiv.org/abs/2609.03501
pdf_url: https://arxiv.org/pdf/2609.03501
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: MoE 统计学习理论 · 稀疏路由与共享专家
tags:
- Mixture-of-Experts
- Top-K Routing
- Shared Experts
- Oracle Risk Bounds
- Sparse Activation
- Statistical Learning Theory
one_liner: 用局部化聚合视角统一分析 MoE，给出稠密/Top-K 路由与共享专家的 oracle 风险界
practical_value: '- 在推荐排序模型用 MoE 时，把共享专家设计为全场景/全域公共塔，路由专家只学不同场景、人群或物品类的残差；可减少路由专家重复学习公共模式，降低有效复杂度并稳定训练。

  - 做大容量稀疏 MoE 时不要只加专家数 M：理论显示近似误差随 M/K 的 1/d 次方下降，但路由估计代价约 M d/n log(M d n)，应结合线上数据量选择
  M 和 K，避免专家数远超样本可支撑规模。

  - Top-K 路由对边界敏感：高维稀疏特征下线性路由容易在决策边界附近频繁切换 active expert；可加入路由参数分离正则/边界稳定性约束，并监控 mini-batch
  上 active set 稳定性。

  - 可将论文中的“离散化候选路由 + 在线指数加权聚合”作为路由蒸馏或稳定化 baseline，不直接依赖端到端非凸联合优化，也能得到可解释的路由不确定性。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

动机：现代大模型 MoE 通过 input-dependent router 激活少量专家提升容量，但路由、稀疏 Top-K 和共享专家的统计作用长期缺少非参数/误设定下的刻画。已有理论多假设参数化或正确给定模型，难以解释 overparameterized、非凸端到端训练中的结构问题。

方法关键点：
- 把 MoE 看成协变量依赖的局部化聚合：dense softmax 是平滑加权，Top-K 是硬选择；固定 K 时只要总专家 M 增长，Top-K 常数专家仍可一致逼近 CR(X)（Prop 2.2），说明稀疏激活未必牺牲表达能力。
- 固定 M 时，Top-K 近似误差上界约为 L√d/(2 floor((M/K)^{1/d}))，优于全局平均；但 uniform norm 下 Top-K 类的 metric entropy 无穷大，L2 下依赖边界概率控制。
- 在线训练框架把专家视为随数据演化的 plug-in 组件，router 用离散化 η-net + 指数加权聚合估计，避免全局非凸优化假设；得到 oracle 风险分解：近似误差 + 专家累积学习误差 + 路由估计误差。
- Dense softmax 风险上界：A_soft + M_R(ā_n2^2+ā_n3^2) + M_R d/n log(M_R d n)；Top-K 额外增加 M_R d/n log(1/r_MR)。
- 共享专家的核心作用是剥离公共结构，路由专家只学残差；Example 3.9 中振荡复杂度从 O(L^4/log^2 M_R) 降到 O(1/log^2 M_R)。

关键结果：纯理论论文，无实验数据集；核心是 Prop 2.3、Theorem 2.4、3.8、4.7 及 Example 3.9。最值得记住：MoE 表达力不仅来自专家本身，更来自路由的局部化聚合；共享专家应承载公共结构，让路由专家只处理局部残差。
