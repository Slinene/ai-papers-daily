---
title: 'Relational Retrieval: Leveraging Known-Novel Interactions for Generalized
  Category Discovery'
title_zh: 关系检索视角下的广义类别发现
authors:
- Yulin Xu
- Chunqi Guo
- Yuanzhen Shuai
- Jianyuan Ni
arxiv_id: '2605.09420'
url: https://arxiv.org/abs/2605.09420
pdf_url: https://arxiv.org/pdf/2605.09420
published: '2026-05-10'
collected: '2026-05-17'
category: Other
direction: 广义类别发现·关系模式匹配
tags:
- Generalized Category Discovery
- Relational Pattern Consistency
- Semi-supervised Learning
- Novel Class Discovery
- Soft Decomposition
one_liner: 提出关系模式一致性，通过双向知识转移耦合已知与未知数据，实现类别发现
practical_value: '- 电商用户分群场景中，当部分用户行为模式已知而需挖掘新类别时，可借鉴RPC的关系一致性约束：用新样本与已知类别原型的距离关系作为可靠信号，替代直接伪标签，减少噪声传播。

  - 推荐系统冷启动物品隐式类别发现：新物品与已知物品的交互模式可映射为关系特征，利用One-vs-All软分解避免硬分配错误，提升冷启动类别推断的鲁棒性。

  - 多智体Agent未知任务类型识别：将已知任务视为原型，新任务执行迹与各原型的交互模式进行关系匹配，实现自适应任务分配，无需大量标注。

  - 训练策略中双向知识转移设计可复用：已知类特征对齐（保留判别性）+ 新类关系保持（挖掘不变模式），组合提升整体表示质量，适用于半监督表示学习任务。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：广义类别发现（GCD）要求模型同时识别已知类别和发现新类别，但现有方法常独立处理标记与未标记数据，忽略了二者间的交互。这种分离导致已知知识无法充分引导新类别挖掘，且未标记数据难以反过来优化已知类表示。

**方法关键点**：提出**关系模式一致性**（Relational Pattern Consistency, RPC），将GCD重铸为关系检索问题，实现双向知识转移。
- 使用**One-vs-All分类器**对未标记数据做软ID/OOD分解，生成样本的已知类归属软标签，避免硬划分错误。
- **已知类保留**：通过语义行为对齐，将标记数据的判别性模式迁移到未标记数据，强化已知类表征。
- **新类别发现**：利用样本与已知类原型间的**关系不变性**：同一类别样本对各已知原型的关系向量应高度一致。据此将不可靠的伪标签转化为可靠的关系模式匹配，引导聚类。

**结果**：在通用物体识别和细粒度类别发现基准上均取得SOTA，验证了双向关系建模的有效性。实验还表明关系匹配比传统伪标签更鲁棒，尤其在细粒度场景下提升显著。
