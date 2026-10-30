---
title: 'Turing LLM Post-Training: Calibrated Distillation and Efficient Dynamic-MoE
  Execution'
title_zh: Turing LLM 后训练：校准蒸馏与高效动态 MoE 执行
authors:
- Yue He
- Jiahui Hu
- Shaman Tang
- Hua Zhou
- Qiman Wu
- Menglin Li
- Yizhao Wang
- Yuheng Zhang
- Da Zhu
- Zhou Wang
affiliations:
- Foundation Model Team, XPeng Inc.
arxiv_id: '2610.39876'
url: https://arxiv.org/abs/2610.39876
pdf_url: https://arxiv.org/pdf/2610.39876
published: '2026-10-29'
collected: '2026-10-30'
category: Training
direction: LLM 多教师蒸馏与 MoE 执行加速
tags:
- MoE
- On-Policy Distillation
- Multi-Teacher Distillation
- Reinforcement Learning
- LLM Post-Training
- Dynamic Routing
one_liner: 提出校准多教师在线蒸馏（C-MOPD）与动态 MoE 执行优化，四域能力整合分数达 0.9988 并实现 2.86 倍步骤加速
practical_value: '- **多任务/多场景模型统一**：电商搜索/推荐常需同时优化相关性、点击率、GMV、内容质量等多个目标。可仿照 C-MOPD，先对每个目标/场景独立训练
  RL specialist，再用多教师在线蒸馏整合到单一学生模型；冻结教师 + 学生在线 rollout 能缓解 exposure mismatch，保留各域增益。

  - **蒸馏 loss 校准**：不同任务的 token-level loss 尺度往往差异大，直接加权容易让大尺度任务主导。C-MOPD 的 teacher-wise
  loss-scale normalization（对每个 teacher 的 token losses 求标准差并做缩放、裁剪）简单有效，可在多目标蒸馏、Agent
  多能力整合中直接使用，降低调参成本。

  - **生成式推荐中的 Top-K 匹配**：对于生成式 item token / semantic ID 的蒸馏，只匹配 teacher 的 Top-K token
  分布可以避免学生被迫学习不相关长尾 token，减少计算和训练不稳定；同时 teacher-local renormalization 确保 student 的概率质量集中在有效支持内。

  - **动态 MoE 训练/推理优化**：如果业务模型采用动态 MoE（token 自适应专家数），RW32 这样的 width bounding 加 final-route
  replay 可保证训练与推理 router 一致性，减少显存和通信开销；异步 rollout 与 actor 更新重叠是通用的 RL 训练加速手段，可迁移到大规模
  Agent/推荐 RL 训练。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：现代 LLM 后训练常为不同能力（数学、代码、指令遵循、Agent 工具使用）独立训练 specialists，但单独部署多个 specialists 增加存储与服务开销。将互补能力整合到单一模型并保留 specialist 增益，是多任务能力整合的核心挑战。在动态路由 MoE 上，多教师蒸馏还面临教师 loss 尺度差异大、rollout–actor 循环中路由不一致等问题。

**方法关键点**：
- 三阶段流程：共享 SFT（5.27M 样本）→ 领域 RL 训练四个 specialist（GSPO，16 rollouts/prompt）→ C-MOPD 整合冻结的 specialists 到单个动态 MoE 学生。
- C-MOPD 核心：任务路由器为每个 prompt 选一个 teacher；学生在线生成轨迹，teacher 在其生成的 prefix 上计算 Top-K 局部支持，teacher 和学生分布重新归一化后做 reverse KL。
- 校准机制：对每个 teacher 的 token losses 求标准差（detached）并缩放（floor 0.1），再做 token-level clipping（cmax=5）；固定 teacher 权重（IF=0.3，其余 1.0），token_mean reduction。
- 执行路径：capacity-constrained Quantile Routing 后限制专家 dispatch width 至 32（RW32，P99 专家数约 19，超 32 的 token 仅 0.21%）；final-route replay 重用最终离散 expert assignments 并重算 routing weights，保证 rollout/actor 路由一致；AsyncOverlap 异步重叠 rollout 与 actor 更新，引入 one-step policy lag。

**关键实验结果**：
- 四域归一化整合分数 0.9988，每域至少保留 90.16% 的 specialist 增益；
- 在 K=32 下，full C-MOPD 得 0.9962，去掉归一化与裁剪降至 0.9724，仅保留归一化（无裁剪）为 0.9834；
- 支持大小 K=16 最优（macro 0.9988），clipping threshold cmax=5 最优；
- reasoning-enabled 数学与代码基准均值 85.92，超过 shared SFT（74.21）和 Qwen3-8B（80.33）；
- 执行优化将平均 step time 从 398.7s 降至 139.3s，实现 2.86 倍加速。

**最值得记住的一句话**：多教师在线蒸馏中，teacher-local Top-K 匹配 + 按教师 loss 标准差缩放并裁剪，能稳定整合多领域 specialists；动态 MoE 的 final-route replay 与异步 overlap 可将步骤时间缩短至约 1/3。
