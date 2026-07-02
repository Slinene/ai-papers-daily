---
title: 'Diffusion-GR2: Diffusion Generative Reasoning Re-ranker'
title_zh: 扩散生成式推理重排器 Diff-GR2：将自回归重排器加速 2.4-3.5 倍并维持精度
authors:
- Zhuoxuan Zhang
- Kangqi Ni
- Yuhang Chen
- Mingfu Liang
- Xiaohan Wei
- Yunchen Pu
- Fei Tian
- Chonglin Sun
- Frank Shyu
- Adam
affiliations:
- Meta AI
- UNC Chapel Hill
arxiv_id: '2607.01170'
url: https://arxiv.org/abs/2607.01170
pdf_url: https://arxiv.org/pdf/2607.01170
published: '2026-07-01'
collected: '2026-07-02'
category: RecSys
direction: 扩散模型加速推理重排器
tags:
- Block-Diffusion
- Re-ranker
- On-policy Distillation
- RLHF
- Semantic ID
- LLM
one_liner: 通过转换微调、在线蒸馏与强化学习三阶段方法，将自回归推理重排器转为块扩散模型，在 Amazon Beauty 上获得 2.4-3.5 倍吞吐提升且精度几乎无损。
practical_value: '- 将自回归推理重排器转换为块扩散解码器可大幅降低序列推理成本，适合高 QPS 场景；转换微调（CFT）能直接让模型学会输出合法排列，省去外部约束解码器。

  - 使用在线策略蒸馏（OPD）在模型自产轨迹上由 AR 教师提供 token 级监督，可有效消除训练-推理分布不匹配，对任何生成式重排任务的 precision
  恢复有直接借鉴意义。

  - 在 OPD 之后接 RL 阶段（基于排名提升和格式奖励）能在几乎不增加额外推理成本的情况下进一步提升 top-1 与 top-3 指标，可作为电商重排线上迭代的标准管线。

  - 块扩散的 KV cache 与预填充摊销机制使得长 prompt（如用户历史 + 候选集）的重排延迟更低，这一工程实践可直接迁移至 LLM 推荐系统的在线推理部署。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：自回归（AR）推理重排器虽准确，但逐 token 生成的成本限制了其在高吞吐场景的应用。块扩散语言模型通过并行去噪可以大幅减少顺序前向步数，但直接替换解码器会导致两个精度损失：(1) 结构性问题：并行解码会生成重复、遗漏或非法候选标识符；(2) 分布性问题：微调基于教师固定轨迹，与推理时学生自己解码的分布不匹配。本文旨在最小化转换带来的精度损失。

**方法关键点**：
- **初始化**：从已训好的 AR 重排器 GR2（Qwen3-8B）权重初始化块扩散模型，保持 KV cache 友好的块因果注意力。
- **阶段 1：转换微调（CFT）**：用掩码扩散目标对 AR 初始化的扩散模型微调，使模型学会自主生成合法排列，无需外部约束解码器，恢复大部分精度。
- **阶段 2：在线策略蒸馏（OPD）**：学生模型在真实块扩散解码分布下采样轨迹，由冻结的 AR 教师提供密集的 token 级 KL 监督，直接解决 off-policy 不匹配问题。
- **阶段 3：强化学习（RL）**：在 OPD 策略之上，用排名提升奖励和条件格式奖励进行 GRPO/DAPO 式优化，应用轨迹回放重要性比率，进一步收复剩余精度差距。

**关键结果**：
- 数据集：Amazon Beauty，10 候选重排，Recall@K 和 NDCG@3 评测。
- 对比：预排序底限（0.2811），AR 教师（0.2960）。
- 仅靠 CFT 将 Recall@1 恢复至 0.2930，OPD 提升至 0.2944，OPD→RL 达到 0.2951，几乎齐平 AR 教师；top-3 指标甚至超越教师。
- 解码吞吐：AR 71 tok/s，Diff-GR2 可达到 172–246 tok/s（2.4–3.5× 加速），且可通过置信阈值 τ 调节速度-质量边界。
- LLM-as-judge 评估显示推理质量无系统退化。

**核心启示**：从 AR 到扩散的转换不必然牺牲精度，关键在于通过 CFT 继承格式能力、OPD 对齐在线分布，再用 RL 精调排名目标。
