---
title: 'Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models'
title_zh: Complete-muE：面向MoE模型的最优超参数迁移与缩放
authors:
- Hongwu Peng
- Ohiremen Dibua
- Yuanjun Xiong
- Yifan Gong
- Jianming Zhang
- Yan Kang
affiliations:
- Adobe Research
arxiv_id: '2605.23893'
url: https://arxiv.org/abs/2605.23893
pdf_url: https://arxiv.org/pdf/2605.23893
published: '2026-05-22'
collected: '2026-05-25'
category: Training
direction: MoE 超参数迁移 · dense-to-MoE 迁移
tags:
- MoE
- hyperparameter transfer
- μP
- SDE
- scaling law
- AdamW
one_liner: 提出 Complete-muE 双桥框架，实现从密集 FFN 到任意 MoE 配置的超参数零成本迁移，实现“调参密集一次，迁移所有 MoE”。
practical_value: '- **MoE 推荐模型快速冷启动**：在电商推荐系统中采用 MoE 结构时，可先用小规模密集模型调优超参数，再通过 Complete-muE
  规则直接迁移到各类 MoE 配置（多专家、稀疏度、共享专家等），省去高昂的超参搜索成本。

  - **Agent 多智体路由的超参数复用**：多智能体系统中的路由网络若设计为 MoE，可从单智能体密集策略网络迁移学习率和初始化，加速 MoE 路由策略的收敛。

  - **生成式推荐的 MoE 架构探索**：在生成式推荐（例如使用 transformer 生成行为序列）中，可先将模型设计为密集 FFN 调参，随后灵活扩展为
  MoE 并迁移超参数，无需重新搜索。

  - **AdamW 超参统一缩放规则**：文中的完整 μE 规则（宽度和专家数缩放下的 LR、WD、初始化方差调整）可直接嵌入训练框架，在模型放大或改变专家数时自动调整超参，提升工程效率。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有超参数迁移工具 μP 和 SDE 分别要求固定架构和固定每步 token 数，无法处理 MoE 中架构和专家 token 数同时变化的场景。论文目标是将密集 FFN 上调优的初始化与 AdamW 超参稳定迁移到任意 MoE 配置。

**方法**：设计双桥系统。桥 I：密集 FFN → 密集 MoE，使用 active-width μP（专家宽度 h 视为 active width）并结合归一化路由器尺度。桥 II：密集 MoE → 稀疏 MoE，通过激活专家数 a 的缩放，发现 SDE 一阶学习率和权重衰减修正项恰好抵消，仅剩有界的 σ₀ 漂移。最终形成 Complete-μE 规则，覆盖激活专家数、总容量、粒度、共享/组均衡等所有 MoE 变化轴，也兼容一般 Transformer 的宽度、深度、批量、训练步数变化。

**结果**：语言模型和扩散模型预训练实验显示，单组密集模型调优的超参数可直接迁移到多种 MoE 配置，最优值仅有微小漂移（与桥 II 的非严格 SDE 行为一致），实现“调参密集一次，迁移所有 MoE”。在模型容量扩展时，MoE 可获得比密集模型更快的收敛速度提升，且无需昂贵超参搜索。
