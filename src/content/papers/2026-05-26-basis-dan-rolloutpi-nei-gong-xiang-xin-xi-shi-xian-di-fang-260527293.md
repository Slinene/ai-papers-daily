---
title: 'BASIS: Batchwise Advantage Estimation from Single-Rollout Information Sharing
  for LLM Reasoning'
title_zh: BASIS：单Rollout批内共享信息实现低方差优势估计的LLM推理后训练
authors:
- Shijin Gong
- Erhan Xu
- Kai Ye
- Francesco Quinzan
- Giulia Livieri
- Chengchun Shi
affiliations:
- University of Science and Technology of China
- London School of Economics and Political Science
- University of Oxford
arxiv_id: '2605.27293'
url: https://arxiv.org/abs/2605.27293
pdf_url: https://arxiv.org/pdf/2605.27293
published: '2026-05-26'
collected: '2026-05-27'
category: Reasoning
direction: RLVR · 批内优势估计削减方差
tags:
- RLVR
- Advantage Estimation
- Batchwise Information Sharing
- LLM Reasoning
- Variance Reduction
- GRPO
one_liner: 利用跨提示的批内奖励加权平均，仅需单次采样即可获得比GRPO8次采样更准的价值估计，训练时间减半且性能接近多轮次基线。
practical_value: '- **批内信息共享替代多采样**：在电商推荐或Agent强化学习中，若每个请求只产生一条轨迹（如一次推荐列表），可以利用同一批次内其他请求的奖励，通过加权平均估计当前请求的基线价值，相当于用“横向”信息替代“纵向”重复采样，降低方差而不增加采样成本。

  - **离线价值表+在线校准套路**：先利用参考模型（例如上线前的模型）对每个提示采样少量结果，构建离线初始价值估计（如KL‑正则化最优价值），训练时再通过最小化误差在线选择一个温度参数β来校准，这种“离线预热+在线自适应”的模式可迁移至需要稳定价值估计的场景，比如生成式推荐的RL微调。

  - **自适应权重避免极端噪声**：当某些提示的预估价值接近0或1时，贝努利方差趋于0会导致权重爆炸，本文引入“活跃集”与回退到零基线的做法，可借鉴到其他基于二进制奖励（如点击/不点击）的批内加权方案中，防止数值不稳定。

  - **防止策略坍塌的简单手段**：实验表明，更准确的优势估计能避免单轨迹REINFORCE类算法在训练中后期性能急剧下降的问题，对于希望用单轨迹RL高效微调推荐策略的实践者，引入批内信息共享可能是一种低开销的防坍塌方案。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
当下LLM推理后训练（RLVR）中，准确的价值估计能降低策略梯度方差、提升样本效率，但准确估计常以昂贵计算为代价：PPO需额外价值网络，GRPO需同一提示多次采样。单次采样算法（如REINFORCE++）虽计算便宜，但基线估计粗糙，训练不稳定甚至坍塌。本文旨在解决这一“计算效率-样本效率”权衡。

**方法关键点**
- **离线价值初始化**：利用KL正则化最优策略的闭式解，在训练前从参考模型采样并离线计算每个提示的初始价值估计。
- **批内加权平均**：为每个提示构建基线时，使用同一批次其他提示的奖励的加权平均，权重由估计的值和方差按BLUE原则动态计算（类似最优线性无偏估计），且强制排除自身奖励。
- **在线校准**：通过最小化基线估计与当前奖励的均方误差，在预定义的β网格上自适应选择校准参数，使离线初始值适应策略演化。
- **活跃集与回退**：当提示的预估价值极接近0或1时，贝努利方差极小，会导致数值不稳定，此时将该提示移出活跃集并回退到零基线。

**关键结果**
- 价值估计MSE：在Qwen2.5-Math-7B上，BASIS比REINFORCE++降低69%，单rollout MSE甚至低于GRPO使用8个rollout的估计。
- 策略优化：在Qwen3-4B+DAPO-Math-17K训练，评估7个数学基准。BASIS仅训练150步（一半计算量），平均性能接近8‑rollout GRPO/GPG/GSPO，且大幅优于vanilla单rollout和REINFORCE++基线，最大提升达44.8个百分点，并有效防止训练后期性能崩塌。
