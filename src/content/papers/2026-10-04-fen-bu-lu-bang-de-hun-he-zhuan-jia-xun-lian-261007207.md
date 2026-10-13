---
title: Distributionally Robust Mixture-of-Experts Training
title_zh: 分布鲁棒的混合专家训练
authors:
- Xin Teng
- Muxiao Li
- Hongyi Wen
affiliations:
- New York University
arxiv_id: '2610.07207'
url: https://arxiv.org/abs/2610.07207
pdf_url: https://arxiv.org/pdf/2610.07207
published: '2026-10-04'
collected: '2026-10-13'
category: Training
direction: MoE训练 · 分布鲁棒优化
tags:
- MoE
- DRO
- Load Balancing
- Expert Specialization
- Pretraining
one_liner: 提出DRMoET，将MoE专家作为内生DRO组，动态加权高损失路由结果，提升路由鲁棒性和下游性能
practical_value: '- 在电商/广告的大规模MoE推荐模型中，可在现有负载均衡之外引入DRMoET式的专家级损失加权：用EMA平滑的激活加权损失动态调整每个专家的训练权重，无需修改前向路由，即可提升非热门专家在流量波动或分布偏移时的表现，降低线上指标抖动。

  - 将「内生组DRO」思想迁移到多任务学习或用户分群：不依赖预定义分组，而是根据模型当前的路由/分配结果动态识别高损失子群，进行针对性加权，比固定分组更适应数据分布变化。

  - 工程实现上，该方法只需维护每层专家数的EMA状态和权重（O(LE)标量），计算开销可忽略，且权重detach避免干扰主损失；可低成本部署到现有训练框架，作为对load-balancing的补充。

  - 用forced misrouting probe（强制选择中位专家）评估模型对非最优路由的鲁棒性，可作为线上路由策略变更前的离线诊断工具。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
MoE通过稀疏路由降低单token计算量，但路由不完美时，token可能被发送到训练不足的专家，导致高损失。传统辅助负载均衡损失只均衡流量，不均衡专家能力，甚至可能损害专家专业化。核心问题是路由鲁棒性——模型在非最优路由下的表现。

## 方法关键点
- **专家作为内生DRO组**：每层每个专家是一个鲁棒性组，由当前路由器动态产生，而非预定义外部组。
- **激活加权损失归因**：对每个专家计算 `路由概率 × 激活范数` 的加权损失（stop-gradient），反映该专家实际处理的token损失。
- **EMA平滑与熵正则softmax更新**：用EMA平滑专家损失，然后通过 `softmax(μ + η * loss_hat)` 更新每层专家权重μ，对高损失专家赋予更高权重。
- **目标函数**：反向传播时使用detach的μ对专家损失加权求和，不引入额外辅助损失，保持标准MoE前向/反向计算。
- **收敛保证**：概率空间softmax更新等价于entropic mirror ascent，提供收敛到stationarity的理论分析。

## 关键实验
- **数据与模型**：DataComp-LM，FLAME-MoE配方，两个规模：290M-746M（33.5B tokens）和1.7B-10.3B（67B tokens），top-k路由（k=8，含2共享专家）。
- **对比baseline**：标准FLAME-MoE（含load-balancing loss）和auxiliary-loss-free balancing。
- **主要结果**：10.3B总参数规模下，DRMoET将七任务平均分从0.6625提升到0.6767（+1.42个百分点），aux-free baseline为0.6431。
- **机制分析**：专家损失标准差降低8.58%，强制mid-k误路由下超额损失降低4.3%，专家domain specialization指标提升（互信息+12.9%，competence advantage+30.2%）。训练吞吐无下降。

## 最值得记住的一句话
稀疏MoE的可靠性不仅取决于负载均衡，更取决于专家在非最优路由下的能力；通过分布鲁棒目标提升高损失路由结果，可以显著增强下游性能。
