---
title: 'Leaf Values as Coordinates: Exact Contrastive Explanation for Gradient-Boosted
  Ensembles'
title_zh: 叶子值作为坐标：梯度提升集成的精确对比解释
authors:
- Emanuele Luzio
affiliations:
- Independent Researcher
arxiv_id: '2608.19127'
url: https://arxiv.org/abs/2608.19127
pdf_url: https://arxiv.org/pdf/2608.19127
published: '2026-08-19'
collected: '2026-08-21'
category: Other
direction: 可解释 AI · 反事实解释
tags:
- contrastive explanation
- gradient boosting
- recourse
- interpretability
- leaf embedding
- tabular data
one_liner: 将 GBDT 每棵树叶子值视为坐标，使模型变为线性求和，从而获得精确稀疏对比解释与可行动反事实建议
practical_value: '- 若业务中大量使用 GBDT/LightGBM/XGBoost 做 CTR/CVR 排序或风控评分，可将每棵树的叶子值作为用户/物品的稠密向量表示（deterministic
  leaf embedding），该表示上模型是线性加和，适合作为解释层或后续线性模型输入，并可直接定位高贡献树与具体分裂条件。

  - 对线上 bad case 做对比解释：取两个预测差异大的样本，计算叶子坐标差向量，非零项即导致差异的树和对应特征区间；无需 SHAP 等近似归因，可直接追溯到真实
  split，适合模型调试与审计。

  - 反事实/行动建议：在电商推荐、用户运营或信用额度场景中，可生成“用户做出哪些可行动改变可提升推荐/优惠资格/评分”的建议；必须显式排除不可变或不可行动特征（年龄、历史违约等），该方法在限制可行特征后仍比最强基线更有效（58%
  vs 41%），说明业务部署时应把可行性约束纳入生成与评估。

  - 评估指标要加入可行动性：标准反事实评估只看 validity/proximity，会高估不可执行建议；实际系统需统计可行动比例，可借鉴作者的做法，将不可行特征作为
  mask 或约束参与生成与评测。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：GBDT 预测本质是 M 棵树各取一个叶子值求和，通常只被视为实现细节。作者发现若把每个实例的叶子值向量 φ(x) ∈ R^M 作为坐标，则模型在该坐标系下是完全线性的：f(x) = 1^T φ(x)。所有非线性被推入已有精确定义的 φ 映射，因此无需在原始特征空间做近似可加假设。

**方法关键点**：利用该表示做对比解释。两个实例的 φ 差向量在它们共享叶子的坐标上严格为零，分数差距只由少数分叉树的坐标携带，每个非零项可追溯到具体树的具体分裂条件。基于此构建 recourse 方法，为个体生成可行动的特征修改建议，并显式排除不可变特征。

**关键结果**：在 5 个表格数据集上 repeated cross-validation 评估，推荐结果重构模型决策的误差低至 6.2×10⁻¹⁵，审计者可独立复算。信用数据集上 effort vs realism 达到 Pareto 非支配。限制为可行动特征后，方法保留 58% 有效性，最强基线仅 41%；标准评估因从不询问建议是否可执行而无法发现这一差异。
