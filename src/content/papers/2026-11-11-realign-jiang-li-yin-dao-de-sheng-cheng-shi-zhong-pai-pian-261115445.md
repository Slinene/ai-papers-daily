---
title: 'ReAlign: Reward-Guided Preference Alignment for Generative Re-Ranking'
title_zh: ReAlign：奖励引导的生成式重排偏好对齐
authors:
- YaChen Yan
- Liubo Li
affiliations:
- Intuit Credit Karma
arxiv_id: '2611.15445'
url: https://arxiv.org/abs/2611.15445
pdf_url: https://arxiv.org/pdf/2611.15445
published: '2026-11-11'
collected: '2026-11-13'
category: GenRec
direction: 生成式重排 · 奖励引导偏好对齐
tags:
- Generative Re-ranking
- Reward Model
- Preference Optimization
- Survival Exposure
- Multi-Objective
- Listwise Utility
one_liner: 用 survival 曝光建模与多目标 reward 对齐候选感知生成器，提升生成式重排的 listwise 效用
practical_value: '- 重排 reward model 可借鉴：将 listwise 奖励分解为 survival exposure × item
  value。电商 feed 流/搜索广告重排里，用户曝光随位置衰减不是简单固定 discount，可以用离散时间 survival 过程拟合退出位置，和曝光日志对齐；同时用多目标
  head + uncertainty weighting 替代人工加权融合，让点击/时长/转化等目标在训练时自动平衡，推理时再按业务权重加权。

  - 生成器训练两阶段：先监督预训练模仿线上曝光列表，再奖励引导偏好对齐。线上直接冷启动做 RL/DPO 容易崩，先在曝光数据上预训练得到稳定的 next-item
  策略，再用 reward model 对候选列表池做分布对齐 + 排序对齐，温度用 pool 内标准化奖励 gap 调制，能规避 reward 绝对尺度不稳定问题。

  - 候选感知的 matching decoder 是实用的生成式重排架构：encoder 对候选集做 context-aware 编码，decoder 每步生成
  query 与剩余候选做内积打分 + mask 去重，避免全 item 词表，天然限制在顶部候选集，适合低延迟线上重排。serving 时只用生成器，reward
  model 只参与训练，推理开销小。

  - list pool 构造应混合历史曝光列表、生成器采样列表和替代重排策略，避免只用模型自身采样导致 self-confirmation bias。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

重排是推荐系统的最后阶段，候选列表虽短但排列空间阶乘增长，列表效用受曝光衰减、item 竞争/互补等 intra-list 交互影响。现有两阶段 generator-evaluator 方法解耦列表生成与评估，生成器无法直接获得 listwise 效用信号；单阶段 scoring 方法不显式搜索排列空间。此外，listwise reward 估计常把曝光和多目标混成单一标量，偏好训练对 reward 绝对尺度敏感，冷启动时不稳定。

**方法关键点**

- **Reward model**：将 listwise reward 分解为 sum over positions 的 reaching probability × item value。曝光建模为离散时间 survival 过程，用 hazard head 预测退出概率，reaching probability 为 survival 函数；item value 使用 K 个 per-objective head，weighted logistic regression 处理稀疏非负标签，uncertainty-based multi-task weighting 自动平衡目标。
- **Generator**：candidate-aware encoder-decoder。encoder 对候选集做上下文编码，decoder 每步生成 query 与剩余候选内积打分，softmax 选择并 mask 去重，限制在候选集内自回归生成排序。
- **两阶段训练**：先在日志曝光列表上监督预训练；再用 reward model 对多样 list pool 打分，post-training 结合 distribution alignment（pool 内标准化 reward 的 softmax 交叉熵）与 ranking alignment（PRO 风格 one-vs-rest，温度由标准化 reward gap 调制）。within-pool standardization 让训练对 reward 绝对尺度和偏差鲁棒。
- **推理**：仅使用生成器贪心解码，reward model 不参与线上。

**关键实验**

在 KuaiRand 和 Avito 两个数据集上对比 DNN、PRM、PIER、CAVE。KuaiRand 上 NDCG 达到 0.8551，超过最强 baseline CAVE 的 0.8450；Avito 上 NDCG 达到 0.7476，超过 CAVE 的 0.7372；uAUC 也一致提升。Ablation 显示：去掉 survival 曝光模块 NDCG 下降约 2.1 个点；去掉多目标设计下降约 0.64 个点；post-training 去掉 within-pool standardization 下降最大；单阶段预训练或 post-training 均明显低于两阶段。

**最值得记住的一句话**

把重排的 listwise reward 显式分解为“用户到达概率 × 位置 item 价值”，并用 pool 内标准化奖励做分布+排序双重对齐，是让生成式重排稳定拿到收益的关键。
