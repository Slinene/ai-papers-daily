---
title: 'Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement
  Learning from Execution Feedback'
title_zh: 写、执行、精炼：通过执行反馈强化学习训练技能优化器
authors:
- Kang Peng
- Zhiwei Zhang
- Yichen Zhang
- Zezhong Wang
- Yiming Du
- Geng Tu
- Baojun Wang
- Bin Liang
- Ruifeng Xu
- Kam-Fai Wong
affiliations:
- Harbin Institute of Technology, Shenzhen
- The Chinese University of Hong Kong
- MoE Key Laboratory of High Confidence Software Technologies
- Harbin Institute of Technology, Harbin
- Huawei Technologies Co., Ltd.
arxiv_id: '2608.17587'
url: https://arxiv.org/abs/2608.17587
pdf_url: https://arxiv.org/pdf/2608.17587
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent 技能优化训练 · 执行反馈强化学习
tags:
- Skill Optimization
- GRPO
- Tool Use
- Execution Feedback
- Agent
- Phase-wise Self-Bootstrapping
one_liner: 训练独立 Skill Optimizer，用执行反馈做 phase-wise GRPO，让 4B 模型优化 agent 技能超过通用大模型
practical_value: '- 在电商导购、客服、广告投放等 Agent 系统中，把「策略 prompt / skill」当作可优化参数：冻结执行模型，单独训练一个小模型改写
  skill，能获得比直接换更大 LLM 更稳定的收益；执行器冻结可以让优化信号只归因到 skill 本身。

  - 如果业务有程序化校验指标（订单完成、API 参数合法、库存/价格约束、终态匹配），优先用 verifier 做 reward，不要用 LLM 打分；配合组内相对优势
  GRPO，能避免任务难度差异淹没候选策略差异。

  - 构建 replay buffer 时，只保留同一 skill 下「一次成功 + 一次失败」的 paired trajectories 作为下一轮优化样本；这种
  mixed-outcome 状态能定位 skill 未约束的分支，比单条失败轨迹更有诊断价值。

  - 生产环境建议迭代 1-2 轮即停止：实验显示 2 轮修订后收益饱和，第 3 轮可能倒退；skill 文档用 name/description/workflow/notes
  四段式，agent 指令更稳定可维护。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
现有专家编写的 skill 能显著提升 tool-using agent，但 agent 自己编写的 skill 反而比不使用 skill 差 8-11 点。推理时循环修 skill 只修复当前 artifact，不会改善下一次写 skill 的模型。问题在于：如何把中间 skill 的执行经验组织成优化器的训练状态？

**方法关键点**
- 框架 WER 分离 Skill Optimizer（4B）与冻结的 executor：optimizer 只输出 markdown skill，不进入工具环境；executor 多次执行候选 skill，程序化 verifier 评分。
- 状态 x=(query, tool context, history, current skill, execution evidence)，优化目标是 skill 文档策略。reward = 1/3(Rfmt + Rtask + Rlen)，其中 Rtask 由 verifier 判断最终状态是否匹配参考解；采用 GRPO group-relative advantage 更新。
- phase-wise self-bootstrapping：每 phase 保留 n=2 rollouts 中恰好一成一败的 mixed-outcome 记录；下一 phase 把同一 skill 的成功/失败轨迹原样拼接为 refinement state，形成 revision tree，让 optimizer 从自己上一轮输出的后果中学习。

**关键实验**
- 数据集：BFCL v4 multi-turn（200 tasks）与 τ²-bench。
- 对比 baseline：No Skill、GPT-5.1 Seed Skill、Qwen3-4B 未训练优化器、Skill-R1、Trace2Skill。
- WER 相对 No Skill 平均 Pass@1 提升 7.80（BFCL）/ 3.85（τ²-bench）；相对同 backbone 未训练优化器提升 9.35 / 10.29。
- 4B 优化器在 BFCL v4 达 76.63%，超过 GPT-5.5、DeepSeek-V4-Flash、Gemini 3.5 Flash、Claude Sonnet 4.6 等通用模型当 optimizer。
- Phase 1→3 单调提升 69.35→71.29→76.63；推理深度 2 轮后饱和，第 3 轮略降至 75.33。

**最值得记住的一句话**
让优化器从自己上一轮产出的 mixed-outcome 成功/失败轨迹中学习「差一点就成功」的诊断状态，比单纯 inference-time 修 skill 更本质。
