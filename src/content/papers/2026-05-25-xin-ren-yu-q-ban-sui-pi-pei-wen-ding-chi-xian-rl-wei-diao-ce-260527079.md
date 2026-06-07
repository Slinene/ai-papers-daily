---
title: Trust Region Q Adjoint Matching
title_zh: 信任域 Q 伴随匹配：稳定离线 RL 微调流式策略
authors:
- Yonghoon Dong
- Kyungmin Lee
- Changyeon Kim
- Jaehyuk Kim
- Jinwoo Shin
affiliations:
- KAIST
- Seoul National University
arxiv_id: '2605.27079'
url: https://arxiv.org/abs/2605.27079
pdf_url: https://arxiv.org/pdf/2605.27079
published: '2026-05-25'
collected: '2026-06-07'
category: Training
direction: 离线强化学习 · 信任域约束 · 流匹配策略微调
tags:
- RL fine-tuning
- flow matching
- trust region
- off-policy
- adjoint matching
- dual descent
one_liner: 通过自适应控制路径空间 KL 散度，实现预训练流策略的稳定离线 RL 微调
practical_value: '- **生成式推荐模型微调**：若用 flow matching 生成用户行为或物品序列，TRQAM 提供了一种稳定的离线/在线
  RL 微调方法，通过路径空间 KL 约束防止微调后策略偏离预训练知识过远，避免遗忘。

  - **信任域参数自适应调度**：利用对偶梯度下降自动调整 λ 的方式，可迁移到任何需要控制 KL 散度的 RL 微调场景，无需手动调节信任域大小，增强鲁棒性。

  - **离线 RL 工程经验**：在离线数据上直接进行策略改进时，本方法不依赖在线交互，适合电商日志数据的高效利用；同时，通过将路径级 KL 表示为 λ 的解析形式，简化了信任域的实现开销。

  - **模型崩溃的预防**：本文揭示 critic 病态会放大梯度误差，这一发现提醒从业者在多步生成模型（如扩散模型）微调中，应监控 critic 条件数或选用信任域方法以稳定训练。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：预训练的流匹配（flow matching）策略能够表达丰富的行为分布，但直接通过采样链进行离线策略梯度优化会因反向传播多步采样过程而不稳定、计算昂贵。先前方法 QAM 将问题重新表述为无记忆随机最优控制（SOC），但继承了对 critic 误差敏感的问题：当 critic 病态时，小误差被放大，导致模型崩溃。

**方法**：提出 TRQAM，在 SOC 框架中引入信任域约束，限制更新后策略与预训练策略在路径空间上的 KL 散度。关键创新是将信任域参数 λ 整合进 SOC 动力学，并理论上证明路径空间 KL 可以表示为 λ 的闭形函数。通过投影对偶梯度下降自适应优化 λ，以一个预定义的 KL 预算精确控制策略偏离程度，实现稳定的离线 RL。

**结果**：在 50 个 OGBench 任务上，TRQAM 在离线 RL 和离线到在线 RL 设定下均一致超越现有方法。离线 RL 总成功率 68%，显著高于最强基线（46%），验证了信任域约束对稳定细调的关键作用。
