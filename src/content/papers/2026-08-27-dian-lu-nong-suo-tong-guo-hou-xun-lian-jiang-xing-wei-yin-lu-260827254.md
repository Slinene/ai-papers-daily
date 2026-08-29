---
title: 'Circuit Condensation: Post-Training that Concentrates a Behavior''s Causal
  Circuit'
title_zh: 电路浓缩：通过后训练将行为因果电路集中化
authors:
- Sai Adith Senthil Kumar
affiliations:
- George Mason University
arxiv_id: '2608.27254'
url: https://arxiv.org/abs/2608.27254
pdf_url: https://arxiv.org/pdf/2608.27254
published: '2026-08-27'
collected: '2026-08-29'
category: Training
direction: 训练后因果电路压缩
tags:
- mechanistic interpretability
- causal circuits
- post-training
- LoRA
- faithfulness
one_liner: 后训练低秩适配器逐轮剪枝低归因边，将行为压缩为更小且保真的因果电路
practical_value: '- 可借鉴其“归因-剪枝-低秩适配器回填”流程，对业务大模型做能力定位与裁剪：先对目标行为（如商品类目识别、query 意图分类）做边归因，逐轮剪掉低贡献边并用
  LoRA 适配器保持输出分布，在性能与通用能力不降的前提下得到更小的可审计子网络。

  - 该方法强调验证剪枝后任务性能和通用能力均保留，可作为推荐/搜索模型剪枝或蒸馏时的验收标准，避免只优化单一指标而损害泛化。

  - 配对消融揭示边间依赖，提醒在推荐系统中评估特征或模块贡献时不能只看单变量消融；可设计成对/组合消融实验，发现模块间的补偿与冗余。

  - 整体更偏可解释性学术贡献，直接迁移到电商生产链路需额外工程化，但低秩适配器匹配原模型分布的做法可复用于行为保真压缩。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：机械可解释性常通过电路解释模型行为，但冻结发现常返回数百条边，难以检查、比较或穷尽验证。

方法：提出 Circuit Condensation，在训练后通过多轮迭代将行为浓缩到更小因果图。每轮对边做归因，剪除低归因边，训练低秩 adapter 让剩余子图匹配原模型输出分布；只有当任务性能和通用能力均保持时才接受剪枝。

结果：在 4 种行为、8 个模型上，30/32 设置中浓缩电路小于最强冻结基线，平均缩小 8.1 倍，最高 316 倍。去除权重更新仅做搜索得到更大电路，证明权重更新是缩小的关键。穷举 19 个电路的所有子集发现 11 个不可再约简，其余存在可移除边；配对消融暴露边间依赖，说明不能单独理解边效应。在间接宾语识别任务上，浓缩电路只保留 24 个头，其中 17 个有文献记载角色，而对等冻结电路有 61 个头、36 个无记录。浓缩电路能跟踪原模型的下一 token 分布并预测其错误，表明得到的是已发表机制的充分子电路而非重构。
