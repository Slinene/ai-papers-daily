---
title: Spectral Biclustering-Driven Scalability for Post-Hoc Explainability in Recommender
  Systems
title_zh: 谱双聚类驱动的可扩展后验推荐系统解释方法
authors:
- Jose L. Salmeron
- Irina Arévalo
affiliations:
- CUNEF Universidad, Madrid, Spain
- Universidad Politécnica de Madrid, Madrid, Spain
arxiv_id: '2607.19189'
url: https://arxiv.org/abs/2607.19189
pdf_url: https://arxiv.org/pdf/2607.19189
published: '2026-07-21'
collected: '2026-07-25'
category: RecSys
direction: 推荐解释性 · 块删除诊断
tags:
- post-hoc explainability
- spectral biclustering
- block-deletion
- scalability
- model-agnostic
one_liner: 提出用谱双聚类将用户-物品分块，以块删除诊断替代逐个观察删除，在保持后验解释能力的同时大幅降低重训练成本
practical_value: '- **块删除诊断作为线下模型探查工具**：在电商推荐场景中，可以用谱双聚类将用户分群、商品归类，然后对每个交互块执行删除并重训练，以发现模型是否过度依赖某些“用户×商品”局部模式（如刷单集中、季节性爆款），提前识别脆弱点。

  - **可解释性报告生成**：对于运营或业务方，可以用块级解释代替个体解释，例如：“30-40岁女性×母婴品类”这个块对高排名推荐有支撑作用，移除后Top-10命中率下降15%，即能说明该群体对母婴推荐信号的依赖，辅助制定品类策略。

  - **计算成本固定的后验分析管道**：该方法将重训练次数从O(N)降至O(k²)（k为块数），可以固定分析预算。实际落地时，可根据预算选择块数，实现可调的分辨率-效率权衡，适合百万级用户-物品矩阵的周期性诊断。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有推荐系统后验解释方法（如观察删除诊断）需对每个用户或物品独立去除后重训练，计算成本随数据规模快速增长，难以实际应用。急需一种可扩展的事后诊断框架，既能揭示推荐决策的依赖结构，又不引入过重的计算负担。

**方法**：提出基于谱双聚类的块删除诊断框架。流程：① 对用户-物品交互矩阵施加谱双聚类，将用户和物品同时划分成块（block）；② 定义块删除操作，移除整个交互块中的所有交互；③ 对原始模型在删除块后的数据上重训练，比较推荐列表的变化（如排名偏移、命中率变化），从而解释该块的证据类型（支撑或损害）和影响程度。框架对模型类型无依赖，可适用SVD、NCF等代表性模型。

**关键结果**：在MovieLens和Amazon数据集上实验发现：(1) 高排名推荐对特定交互块更敏感，部分块作为支持证据，部分块有负面效果；(2) 不同用户群组对块移除的敏感度不同，反映对局部交互模式的依赖异质性；(3) 块删除带来的诊断信息无法从标准准确率指标直接读出，证明该方法补充了传统评估的盲区。
