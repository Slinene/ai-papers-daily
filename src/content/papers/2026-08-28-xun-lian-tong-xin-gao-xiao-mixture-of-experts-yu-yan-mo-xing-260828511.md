---
title: Training Communication-Efficient Mixture-of-Experts Language Models with Layer
  Re-Configuration
title_zh: 训练通信高效 Mixture-of-Experts 语言模型的层重配置方法
authors:
- Simeng Sun
- Roger Waleffe
affiliations:
- NVIDIA
arxiv_id: '2608.28511'
url: https://arxiv.org/abs/2608.28511
pdf_url: https://arxiv.org/pdf/2608.28511
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: 通信高效 MoE 架构训练优化
tags:
- MoE
- Communication-Efficient
- Hybrid Mamba-Transformer
- Expert Parallelism
- Layer Re-Configuration
- Training Efficiency
one_liner: 减少 MoE 层数并用 Mamba-2 和密集 FFN 补深度，在匹配参数下降低专家并行通信和训练 GPU 小时 30-35%
practical_value: '- 如果业务里用 MoE LLM 做召回/粗排/reranker 或生成式推荐，可尝试把 MoE 层从每个 token-mixing
  后都放一个改为稀疏放置，例如 52 层 hybrid 模型只保留 8 个 MoE 层，其余用 Mamba-2 和 dense FFN 补深度，理论上 all-to-all
  调用从 23q 降到 8q，实际训练 GPU 小时省 30% 以上。

  - 层排序不要随机，采用 phased-greedy：先把 attention 和 channel-mixing 块按虚拟块分配到 Mamba spine，避免连续
  channel-mixing，attention 放在 token-mixing 尾部；实验中比 21 个受约束随机排序的验证损失低约 1.8σ。

  - 连续堆叠 softmax attention 容易 rank collapse 导致训练发散；如果用 token-mixing-heavy 架构，优先用 Mamba-2/线性注意力作为主干，比
  softmax attention 稳定得多。

  - 评估架构改动要直接看 GPU-hours 而非理论 FLOPs/参数量；本文的模型形状搜索用 L_E*K 作为通信代价代理，在参数匹配候选中选该值最小者，可复用到自己的搜索流程。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：MoE 训练中 expert parallelism 的 all-to-all token dispatch/combine 通信量随 MoE 层数 L_E、序列长度 S、batch size、routed top-K 线性增长，常常占据端到端训练时间的大头。已有系统级优化（DeepEP、Megatron-Core、LatentMoE）降低单次通信或隐藏延迟，但架构层面减少通信量的工作较少；Switch/GShard 虽把 MoE 放在每隔一个 FFN，但仍然保持 token-mixing/channel-mixing 的规则交替，L_E 依然较高。

**方法关键点**：
- 提出 CE-MoE：大幅减少 MoE 层数 L_E，用更多 Mamba-2 和 dense FFN 层补足深度，形成 token-mixing-heavy 的异构层模式；例如 52 层 baseline（23 Mamba + 6 attention + 23 MoE）变成 30 Mamba + 6 attention + 8 MoE + 8 dense FFN，MoE all-to-all 调用从 23q 降到 8q，通信量降低约 47.8%。
- 连续 token-mixing 层会导致 rank collapse：实验显示 7 层连续 softmax attention 出现 loss spike 甚至发散，而 Mamba-2 在相同学习率下稳定；用 stable/effective rank 测量，Mamba-2 保持更高 token 多样性。因此用 Mamba-2 作为主干，attention 稀疏放置。
- 用 phased-greedy 算法生成层顺序：将 attention 和 channel-mixing 块均匀分布在 Mamba spine 上，注意力放在 token-mixing 尾部，避免连续 channel-mixing。
- 模型形状搜索：固定 hidden size，对 dense FFN 宽度、per-expert MoE FFN 宽度、shared expert 宽度、专家数、top-K 做网格搜索，约束 total/activated 参数匹配，选择最小 L_EK 作为通信代价代理。

**关键实验**：在 2B-A0.5B 到 31.5B-A3.5B 五个尺度、Hybrid Mamba-2 模型上，相同 global batch size 下，CE-MoE 减少 GPU-hours 30.5%-35.0%，验证损失与 baseline 接近。31.5B-A3.5B 同 tokens 设置下成本降低 33.3%，平均下游分数从 58.37 提升到 58.65；更大 GBS 并用 1.25x tokens 训练时，成本仍比 baseline 低 26.1%，平均分数提升到 59.36。LatentMoE 变体 CE-LatentMoE 在 1.25x tokens 下成本低 20.9%，平均分数从 60.77 提升到 62.36。推理吞吐上，31.5B 模型在输入 2048/8192、输出 128-2048 时 CE-MoE 提高 28-36%。

**最值得记住的一句话**：把 MoE 层从每个 token-mixing 后都放一个，改为稀疏地只放少数几个，其余用 Mamba-2 + dense FFN 补深度，即可在匹配质量下省约 1/3 GPU-hours。
