---
title: 'Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards'
title_zh: TEV：用稠密进度奖励扩展长程智能体训练环境
authors:
- Wenbo Hu
- Shraman Pramanick
- Krishna Kumar Singh
- Nanyun Peng
- Kai-Wei Chang
- Yong Jae Lee
affiliations:
- Adobe Research
- University of California, Los Angeles
arxiv_id: '2610.18868'
url: https://arxiv.org/abs/2610.18868
pdf_url: https://arxiv.org/pdf/2610.18868
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: 长程智能体训练 · 环境合成与稠密奖励
tags:
- Long-horizon Agent
- Reinforcement Learning
- Reward Shaping
- Synthetic Environments
- Progress Reward
one_liner: 先构造完整隐藏世界再渲染损坏任务，并用进度势能奖励解决长程智能体 RL 的稀疏奖励，使开源模型逼近前沿。
practical_value: '- 在电商/广告 Agent 的复杂多步骤任务（商品知识图谱构建、营销活动搭建、数据管道修复）中，可采用 latent-world-first
  思路：先定义完整正确的目标状态（latent world），再反向渲染损坏输入和 workflow DAG，避免 prompt、任务、验证器各自生成导致的 artifact
  drift。

  - 用 workflow DAG 定义 progress contract，对每个关键中间节点做 prerequisite-gated 评分，作为 RL 稠密奖励；能有效解决
  GRPO 组内全失败时梯度为零的问题，在训练多步操作 Agent 时提升 sample efficiency。

  - 奖励塑形使用 R(τ)=1[pass]+λΦ(s_T)，λ=0.25，保证通过任务严格优于未通过，同时提供部分进度信号；实现时注意 turn-index normalization
  和 return-to-go γ=1，保持 credit assignment，避免后期 turn 的回报被整体均值稀释。

  - 合成环境时用 seeded generator 而非 LLM 直接生成，并在生成阶段加入 round-trip 验证和资格门（exploit resistance,
  progress validity, role independence），可保证可复现、可验证、无奖励黑客。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
长程 agent 能自主完成数小时到数天的经济任务，但开源模型受限于缺乏训练数据和有效配方。现有 agentic 训练语料（SWE-Smith、TMAX 等）规模大但短程，只提供 terminal pass/fail；长程任务只有人工标注 benchmark，数量少且仅作评测。长程任务合成难：既要足够复杂又要精确可验证，且奖励稀疏导致 GRPO 在组内全失败时梯度为零，浪费大量 rollout。

**方法关键点**  
- **Latent-world-first synthesis**：先用 seeded generator 构建完整正确的隐藏世界（领域状态与 workflow DAG），再渲染成干净输入文件，注入可控 corruption 得到 agent 初始状态。任务、严格验证器、进度势能都是同一 latent world 的函数，避免 artifact drift。  
- **TEV-GYM**：1,170 个验证环境，覆盖 7 个领域，中位 agent 时间 12.4 分钟，约为之前最耗时语料 6 倍；Pass@1 仅 29%，难度显著高于现有语料。  
- **Progress potential Φ(s)**：基于 workflow DAG 的节点和 prerequisite 定义，部分评分加权求和，范围 [0,1]，提供精确中间进展度量；满足 exploit resistance、progress validity、role independence 三个资格门。  
- **PPRS**：奖励 R(τ)=1[pass]+λΦ(s_T)，λ=0.25；用 turn-index 归一化和 return-to-go γ=1 保留 credit assignment，解决组内零优势问题。

**关键结果**  
- ALE-CM：TEV-9B Pass@5 提升 83%，TEV-27B Pass@5 提升 65% 至 0.28，匹配 GPT-6 Astra 和 Claude Opus 5。  
- TB 3.0/4.0 CM 子集：TEV-27B Pass@1 分别 +56% 和 +150%（2.5×），超过 GLM 5.2；TEV-320B（基于 GLM-5.3-Flash）在 TB4.0 Pass@1 达 0.37，仅次于三个前沿模型。  
- TB 2.1：TEV-9B Pass@1 +28%，TEV-27B 达 0.794，匹配 Claude Opus 4.8。  
- 消融：用 LLM 生成替代 latent world 或只用 terminal reward 均无提升；PPRS 比稀疏奖励 S@1 高 0.04，并在 27B 上使训练从不可行变为可完成。

**最值得记住的一句话**  
先构造完整正确的隐藏世界，再渲染损坏任务，并将进度势能作为稠密奖励，是让开源模型在长程 agent 任务上逼近前沿的关键。
