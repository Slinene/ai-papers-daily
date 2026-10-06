---
title: 'LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches'
title_zh: LoGRA：用低秩梯度草图扩展LLM强化学习
authors:
- Shaokun Zhang
- Yifan Zhang
- Jian Hu
- Yueying Li
- Hao Zhang
- Binfeng Xu
- Jan Kautz
- Yi Dong
affiliations:
- NVIDIA
arxiv_id: '2610.06647'
url: https://arxiv.org/abs/2610.06647
pdf_url: https://arxiv.org/pdf/2610.06647
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: RL训练内存优化 · 低秩梯度草图
tags:
- RL
- Memory-efficient
- Low-rank gradient
- LLM
- KL control
- Training
one_liner: 通过低秩梯度草图压缩RL训练中的梯度和优化器状态，配合预测KL步长控制，大幅降低内存占用
practical_value: '- **资源受限下的RL训练**：电商/Agent场景若需对LLM做RL后训练但GPU显存有限，LoGRA能以约45%的内存节省保持性能，可让原本OOM的模型规模落地，适合中小团队。

  - **预测KL步长控制**：将每次更新的策略偏移限制在预设KL预算内，避免策略突变导致已学行为崩溃。在推荐/Agent在线持续学习中，可将该机制用于策略更新的稳定性控制。

  - **梯度压缩与同步复用**：LoGRA的压缩更新（低秩因子）可直接用于rollout策略同步，减少通信开销。分布式训练或多智能体协作中可借鉴：用低秩因子传输更新，降低网络负担。

  - **注意rank选择**：论文消融表明投影秩对性能影响最大（秩4→256提升约3个百分点），而投影矩阵刷新与否影响很小。在实践中应优先调大rank，无需频繁刷新投影。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
LLM强化学习（RL）后训练的内存开销巨大，Adam优化器的两个FP32矩估计量可达权重的数倍。例如7B模型BF16权重约14GB，而Adam状态需额外56GB。这让许多硬件上能推理的模型无法进行RL微调。现有方案如FSDP、LoRA、梯度压缩各有侧重，但LoGRA针对RL训练-生成循环，在梯度累积、更新、策略同步全链路使用低秩压缩，旨在保持性能的同时显著降低内存与通信成本。

## 方法关键点
- **低秩梯度草图**：对每个权重矩阵W，随机生成投影矩阵A（r×k，r≪min(d,k)），直接累积投影梯度S=G A^T（d×r），不存储全梯度。更新时用S A近似梯度，W←W−αη U A，其中U是sketch经优化器调整后的版本。投影可每步刷新，但实验表明刷新收益不大。
- **预测KL步长控制**：借鉴TRPO思想，在应用更新前估计更新后策略与当前策略的KL散度。利用局部二次近似，KL≈α² q(D)，其中q(D)通过token打分变化方差计算。根据预算δ，取α=min(α_max, √(δ/q(D)))，防止过大更新破坏策略稳定性。
- **RowAdam优化器**：对sketch的行进行自适应缩放，仅需d个二阶矩估计值，避免全参数Adam状态。

## 关键实验
在Qwen2.5-Math-1.5B/7B和Qwen3.8-27B上，使用DAPO-Math-7.5K训练，MATH-500评估。
- 内存：1.5B平均内存从9.18 GiB降至7.18 GiB（节省21.8%）；7B从31.82 GiB降至17.29 GiB（节省45.7%）。
- 性能：1.5B Pass@1 67.87%（LoGRA）vs 63.77%（Dense）；7B持平（约72.3%）；27B LoGRA达到71.52% Pass@1，而Dense Adam直接OOM。
- 长程稳定性：27B模型在Reasoning-Gym Hard混合任务上训练超1100步，宏验证分数从39.69%升至62.94%，未出现崩溃。
- 消融：投影秩对性能影响最大（4→256提升约3个百分点），投影刷新和分布类型影响很小；与LoRA相比，LoGRA内存更低但Pass@1略低，Pass@4略高。

## 最值得记住的一句话
低秩梯度草图+预测KL控制可在不损失性能的情况下大幅降低LLM RL训练内存，使原本OOM的27B模型能在单8-GPU节点稳定训练。
