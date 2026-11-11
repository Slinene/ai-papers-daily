---
title: Closing the BF16-FP16 Convergence Speed Gap in RL Post-Training with Stochastic
  Rounding
title_zh: 用随机舍入缩小RL后训练中BF16与FP16的收敛差距
authors:
- Mahdi Nazemi
- Oleg Rybakov
- Tijmen Blankevoort
- Asit Mishra
- Carlo del Mundo
affiliations:
- NVIDIA
arxiv_id: '2611.13545'
url: https://arxiv.org/abs/2611.13545
pdf_url: https://arxiv.org/pdf/2611.13545
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: 混合精度RL训练 · 随机舍入
tags:
- BF16
- FP16
- stochastic rounding
- RL post-training
- mixed precision
- LLM
one_liner: 发现低学习率下BF16权重粘滞导致RL收敛慢于FP16，提出对FP32影子权重转BF16使用随机舍入，匹配收敛并降低KL
practical_value: '- 在RL post-training或RLVR中用BF16且学习率较低时，先排查权重粘滞：FP32 master weights
  cast到BF16时小更新可能被round-to-nearest吞掉。可直接在cast处改stochastic rounding，改动小、无需调学习率。

  - 如果暂时不能改rounding，可尝试提高BF16学习率追平FP16收敛，但要监控KL drift；对推荐/Agent策略微调这类对policy稳定性敏感的场景，SR比单纯提LR更安全。

  - FP16需要loss scaling且动态范围窄，reward/advantage波动大的RL任务易溢出；BF16+SR保留BF16动态范围，省去loss
  scaling工程，更适合大规模RL训练集群。

  - 方法可推广到其他低学习率混合精度训练，如SFT/对齐后训练；建议在训练框架的quantizer里配置rounding mode，A/B对比收敛曲线与KL。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：BF16预训练常用，但在RL post-training的低学习率设置下，混合精度BF16训练收敛明显慢于FP16。原因是权重粘滞：FP32 shadow weights经round-to-nearest量化到BF16时，小更新不足一个ULP，用于rollout和训练的BF16权重不变，多个optimizer steps后才能反映更新。提高BF16学习率可以缓解粘滞、追平FP16收敛，但会增大与reference model的KL divergence。

方法：在将FP32 shadow weights量化到BF16时改用stochastic rounding，即按小数部分概率向上取整，使小更新有机会改变BF16权重，减少粘滞。

结果：在Qwen3-30B-A3B、DeepSeek-R1-14B、DeepSeek-R1-1.5B等模型和MATH/DAPO等可验证奖励任务上，BF16+SR的reward轨迹与FP16几乎重合，同时KL divergence低于使用更大学习率的BF16；保留BF16更宽的动态范围，无需loss scaling。
