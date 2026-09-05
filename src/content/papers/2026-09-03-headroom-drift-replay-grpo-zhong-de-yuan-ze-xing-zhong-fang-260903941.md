---
title: 'Headroom-Drift Replay: A Primitive for Principled Replay Control in GRPO'
title_zh: Headroom-Drift Replay：GRPO 中的原则性重放控制原语
authors:
- Hyun Bin Park
- Du-Seong Chang
affiliations:
- Department of Artificial Intelligence, Sogang University
arxiv_id: '2609.03941'
url: https://arxiv.org/abs/2609.03941
pdf_url: https://arxiv.org/pdf/2609.03941
published: '2026-09-03'
collected: '2026-09-05'
category: Training
direction: GRPO 重放控制 · 样本选择
tags:
- GRPO
- Replay
- RL Post-training
- Reasoning Models
- Sample Selection
- Wall-clock Efficiency
one_liner: 将 GRPO 重放控制拆为按剩余学习价值排序的 Headroom 与按策略兼容性门控的 Drift，不改动 on-policy 流即减少交互成本。
practical_value: '- 在需要昂贵环境/用户交互的 RL 训练（如 Agentic Search、对话推荐、广告策略优化）中，可引入两层重放控制：先用
  Headroom 对历史 trajectory group 按剩余学习价值排序，再用 Drift 过滤与当前策略偏差过大的样本；保留 on-policy 新鲜流不变，避免大规模改动训练管线。

  - 把重放选择从训练 pipeline 中解耦成独立原语，方便在已有 GRPO/RLVR 代码上快速实验：只需修改 buffer 采样入口，无需加蒸馏、重要性加权或混合策略优化。

  - 如果业务中 rollout 成本主要在环境交互而非模型推理，优先评估 replay 的 wall-clock 收益；该工作表明在 Agentic Search
  中可比质量下显著降低耗时，适合交互式/仿真器昂贵的推荐智能体场景。

  - 注意 group-level 而非单条复用，保持 GRPO 比较组结构；复用时按 group 整组排序和过滤，避免破坏相对优势信号。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：RL-based post-training 在 reasoning model 上越来越受频繁 fresh rollout 生成拖累，尤其在 agentic 环境中环境交互占 wall-clock 成本的大头。Replay 可以复用历史轨迹，但现有方法常耦合在更大训练管线中，难以单独评估 replay 的贡献。

方法关键点：提出 Headroom-Drift Replay，作为 GRPO 的 group-level replay 控制原语。把复用拆成两个独立决策：Headroom 对存储的 group 按剩余学习价值排序；Drift 按与当前策略的兼容性进行门控过滤。fresh on-policy 流保持不变，不引入额外生成或训练机制。

关键结果：在数学推理、多模态推理和 Agentic Search 三个 benchmark 上，这一单一干预超过 naive replay，并在 Avg Mean@32 上匹配或超过更复杂的 replay 方法。在 Agentic Search 中，当环境交互占主导时，达到相近质量的同时 wall-clock 时间显著降低。
