---
title: Self-Evaluating Recursive Agents
title_zh: 自评估递归智能体（SERA）
authors:
- TianYi Lyu
- Xiaozhe Li
- Yang Li
- Yongkang Chen
- Kefei Tian
- Junbo Niu
- Zican Hu
- Hongbo Liu
- Mingliang Xiong
- Qingwen Liu
affiliations:
- Tongji University
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiaotong University
- Peking University
- Nanjing University
arxiv_id: '2610.04902'
url: https://arxiv.org/abs/2610.04902
pdf_url: https://arxiv.org/pdf/2610.04902
published: '2026-10-03'
collected: '2026-10-20'
category: MultiAgent
direction: 递归多智能体训练 · 可学习 rubric 评估
tags:
- Recursive Agents
- Self-Evaluation
- RL
- Rubric
- MultiAgent
- Tree Search
one_liner: 训练递归智能体生成与学习对齐的 rubric，以自我评估子任务，降低外部监督并提升执行与分解能力
practical_value: '- 把中间步骤/子任务的 reward 从外部 judge 迁移到策略自产 rubric：训练阶段用少量外部 verified
  outcome 做 ranking loss 锚定，执行时用模型自己的 rubric 打分。对推荐链路中的多步策划/生成类 Agent，可显著降低线上 LLM
  judge 调用成本（文中 TextWorld judge calls 和 tokens 下降 4-5 倍）。

  - 当评判器和执行器共享同一个模型权重时，不要用最终任务 reward 直接训练 rubric，否则两者会共适应、分数虚高；应使用 verified outcome
  的 pairwise ranking loss（带 margin）训练。这点可迁移到“同一模型既做推荐生成又做事后评估”的场景。

  - 分解质量需要单独 reward：用 leaf-coverage（成功任务的 delegation 子树覆盖叶子比例）训练分解动作，在依赖链、共享状态、资源冲突等
  interdependent 任务上增益明显；对应到电商场景，适合训练复杂活动策划拆解给多个子 agent 时使用。

  - 训练得到的 rubric 可以在推理时作为 tree search 的节点选择器，自产候选分支并按 rubric 分数保留最优，无需额外训练即可提升效果；对搜索/推荐中的多路召回或规划路径选择有借鉴意义。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
递归 agent 将任务分解为树状结构，但中间子任务通常无 ground truth。现有方法用 verifier 或 LLM judge 给每个节点打分，存在三个问题：信号粗粒度（二元成功/失败）、成本高（每个节点需要外部调用）、无法评估分解质量。核心难点在于共享权重同时承担分解、解决、评估三个能力，需要各自的训练信号。

## 方法关键点
- **执行 reward**：父 agent 在委派前生成加权 rubric（自然语言成功标准 + 权重），冻结；子 agent 完成后由同一 policy 打分，产生连续节点分数。
- **rubric 训练**：不直接用任务 reward 优化 rubric（避免与求解能力共适应），而是克隆状态、采样 counterfactual rollouts，用外部 verified outcome 构造 pairwise ranking loss，让 rubric 把成功排在失败之前，并设置 margin δ。
- **分解 reward**：leaf-coverage 奖励 delegation 事件，即 root success × 该子树叶子数/总叶子数，直接奖励承担结构性负载的委派。
- **优化方式**：三种 reward 交替更新，比例 execution:decomposition:rubric = 16:2:2；使用 CISPO policy gradient、leave-one-out baseline 和 inverse-depth weighting。

## 关键结果
在 TextCraft-Synth 和 TextWorld-Sync 上，SERA 平均成功率分别为 74.31% 和 65.07%，比递归多智能体基线 RAO 提升 5.38 和 13.14 个百分点。消融表明，训练 rubric generation 是最大增益来源，而没有训练的 rubric 收益有限甚至不稳定。外部监督调用显著下降：TextWorld judge calls 从 147.80K 降至 35.79K（约 4.1×），输入 tokens 下降约 5.1×。推理时用学习到的 rubric 做自底向上树搜索选择，TextWorld-Sync 再加 2.43 点，且 trained policy judge 与外部 Kimi judge 表现相当。

**最值得记住的一句话**：训练策略生成对齐的 rubric 是驱动增益的关键，因为同一组权重同时评估和执行，学习评判子任务会锐化求解能力。
