---
title: Local Support Learning
title_zh: 局部支持学习：无需旧数据的持续学习与遗忘缓解
authors:
- Assaf Ben-Kish
- Akarsh Kumar
- James Glass
- Raja Giryes
affiliations:
- Tel Aviv University
- MIT CSAIL
arxiv_id: '2610.02126'
url: https://arxiv.org/abs/2610.02126
pdf_url: https://arxiv.org/pdf/2610.02126
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: 持续学习 · 灾难性遗忘缓解
tags:
- Continual Learning
- Catastrophic Forgetting
- GMM
- Adapter
- LLM
- Local Support Learning
one_liner: 提出 Local Support Learning，用 GMM 门控使 adapter 只在当前分布激活，无需旧数据缓解大模型灾难性遗忘
practical_value: '- 对线上推荐/搜索模型做持续增量更新时，可用 LSL 的 adapter + GMM gate 结构：每个新数据周期训练新 adapter，gate
  让 adapter 只在当前数据分布上激活，旧分布数据自动路由到原始权重，无需回放旧数据即可缓解遗忘。

  - GMM 门控比普通 MLP classifier 更适合 OOD 拒绝，因其似然在训练分布外快速衰减。在推荐系统多任务/多领域路由中可借鉴：为每个领域/任务建
  GMM 门控，实现软路由与分布漂移检测。

  - 方法内存和计算高效，支持 7B 参数模型，可迁移到生成式推荐（如 Semantic ID 生成）的持续学习场景：新类目上线时只增加局部 adapter，不破坏旧类目生成能力。

  - 工程实现上，GMM 的均值/方差可流式更新或 EMA 维护，避免存储原始激活，适合实时更新的推荐系统。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：大模型持续微调常导致灾难性遗忘，现有方法要么需要旧数据，要么存储旧模型或额外正则，成本较高。论文把遗忘视为权重矩阵输入空间的几何问题，提出一种自然保留目标，指出普通梯度更新在该目标下是次优的。

方法关键点：Local Support Learning (LSL) 在新学习阶段同时训练两个组件——标准权重 adapter 和门控函数。adapter 正常最小化当前任务损失；门控只允许 adapter 在其训练分布上激活，使更新局部化。核心挑战是门控要在当前阶段数据上训练，却能对其他阶段数据保持关闭。作者用 Gaussian Mixture Model (GMM) 作为门控，其似然在训练分布外快速衰减，天然对旧数据关闭。多个阶段可组合多个 adapter+gate 模块。

关键结果：在 7B 参数的 LLM 上验证，经过多个训练阶段仍能保留预训练和微调能力；方法内存和计算开销低，对超参数鲁棒，并显示出扩展潜力。
