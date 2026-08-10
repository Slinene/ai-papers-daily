---
title: 'Modular TTT: Rethinking Test-Time Training as Composable Modules'
title_zh: 模块化测试时训练：将 TTT 重新思考为可组合模块
authors:
- Bohao Tang
- Zhen Qin
- Yuqi Pan
- Zheng Li
- Pengfei Liu
- Ya Zhang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- ByteDance Seed
arxiv_id: '2608.07110'
url: https://arxiv.org/abs/2608.07110
pdf_url: https://arxiv.org/pdf/2608.07110
published: '2026-08-06'
collected: '2026-08-10'
category: Other
direction: 序列建模 · TTT 框架
tags:
- Test-Time Training
- Sequence Modeling
- Modular Design
- Ablation Study
- Online Learning
- TTT
one_liner: 提出模块化 TTT 框架，将内部学习器建模为有向无环图，系统消融组件并发现关键设计原则
practical_value: '- 可尝试用 TTT 替代 Transformer 做用户行为序列建模，受益于其在线学习特性，可能更高效处理长序列。

  - 模块化设计思想可借鉴到推荐系统的特征交互或模型组件，将学习率、损失函数等也作为可配置模块，便于消融和新设计。

  - 消融结论直接可用：使用单层非线性快权重网络，避免深度网络和归一化，采用小学习率初始化与权重衰减，可减少实现踩坑。

  - 业务中若需轻量、增量更新的序列模型，TTT 的 fast-weight 机制可能比 Transformer 更节省 inference 开销，适合实时推荐场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 Test-Time Training (TTT) 变体各自硬编码，难以隔离组件作用和设计新方法，缺少统一视角。

**方法**：提出 Modular TTT，将内部学习者表示为有向无环图，将快权重网络、损失函数、学习率、权重衰减、归一化等暴露为可组合模块，自动合成完整的 TTT 计算图，包括训练视图的前向/后向和因果查询视图规则，支持灵活消融。

**关键发现**：
- 小学习率初始化、权重衰减、单层非线性激活（如 Swish）可提升性能；MSE 与内积损失表现相当。
- 更深的快权重网络和归一化会因激活值过大而损害性能，残差连接和门控几乎无收益。
- 基于上述原则训练了 410M 和 1.45B 参数模型，在 100B tokens 上训练，训练 loss 与 benchmark 性能可比 Gated DeltaNet。
