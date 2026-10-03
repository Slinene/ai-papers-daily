---
title: 'CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning'
title_zh: CorrGRPO：多奖励学习的相关性归一化 GRPO
authors:
- Wenbin Hu
- Huihao Jing
- Haochen Shi
- Yuxuan Liu
- Haoran Li
- Yangqiu Song
affiliations:
- Hong Kong University of Science and Technology
arxiv_id: '2609.36820'
url: https://arxiv.org/abs/2609.36820
pdf_url: https://arxiv.org/pdf/2609.36820
published: '2026-09-28'
collected: '2026-10-03'
category: Training
direction: 多奖励 RL · GRPO 归一化
tags:
- GRPO
- multi-reward RL
- Pearson correlation
- advantage normalization
- LLM training
- agent security
one_liner: 将 GRPO 多奖励优势归一化从协方差改为 Pearson 相关，消除大方差奖励主导，提升代码/工具/Agent 安全多目标训练效果
practical_value: '- 工程实现简单：只需在 group advantage 分母中用相关矩阵元素和替换协方差和，分子保持 centered total
  reward；论文 Listing 1 可直接作为现有多奖励 GRPO 训练代码的改造模板。

  - 当业务奖励量纲/方差差异大（例如 CTR、转化、时长、多样性、安全分）时，CorrGRPO 可避免大方差目标主导优势缩放，同时保留预设目标权重；适合作为多目标
  RL 的默认 advantage normalizer。

  - 高度相关的奖励（点击与转化、多个可用性指标）会被相关归一化自动去冗余，避免重复奖励放大更新；在 reward hacking 或目标一致性强时尤其有用，可辅助探索。

  - 训练动态上 CorrGRPO 保留更高策略熵，减缓 entropy collapse，有利于持续探索和发现高奖励策略；可与 KL 系数、DAPO/CISPO
  等现有 RL 方法结合。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：多奖励 RL 在 LLM 训练中普遍，但 GRPO 对多奖励直接求和后做组内标准差归一化，其分母等价于所有奖励协方差之和。协方差受奖励尺度影响，大方差奖励会主导归一化，压制小尺度但有区分度的奖励信号，导致多目标优化失衡。

方法关键点：
- 从协方差视角重写 GRPO：优势分母为 √(Σ_l Σ_m Cov(R_l, R_m) + ε)，聚合了方差和两两协方差。
- CorrGRPO 将分母中的 Cov(R_l, R_m) 替换为 Pearson 相关系数 ρ_lm，分子保持 centered total reward 不变；零方差奖励对应行列置零。
- 每个奖励在分母对角线贡献固定为 1，off-diagonal 仅反映相关性，从而消除尺度权重。
- 在相同策略参数下，CorrGRPO 优势是 GRPO 优势的正标量倍，保持 group 内梯度方向，只自适应调整幅度；可兼容 DAPO/CISPO/GDPO。

关键实验：在代码生成（LeetCodeDataset + HumanEval/MBPP/LCB v6）、工具调用（RLLA-4K + API-Bank）、Agent 安全（AgentDojo/ASB/InjecAgent）三个多奖励场景，模型 0.5B–8B。相比 GRPO/GDPO，代码平均 Pass@1 在 4 个模型尺度分别提升 2.09、0.80、2.27、4.21 个百分点；工具调用 all-exact 提升 1.40–4.23 个百分点；代理安全上 3B 模型 AgentDojo Joint Accuracy 从 60.13% 提升至 89.62%，ASB Joint Accuracy 也持续提升，InjecAgent 攻击成功率从 8.80% 降至 5.52%。

最值得记住的一句话：多奖励 GRPO 中，大方差奖励会通过协方差主导优势缩放；用 Pearson 相关替换协方差既保留奖励权重，又让优势幅度对相关性而非尺度敏感。
