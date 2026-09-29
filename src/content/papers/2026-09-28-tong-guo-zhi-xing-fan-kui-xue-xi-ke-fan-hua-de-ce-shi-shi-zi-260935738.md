---
title: Harness Learning Enables Generalizable Test-Time Adaptation
title_zh: 通过执行反馈学习可泛化的测试时自适应 Harness 修订
authors:
- Alvin Zhang
- Xuecheng Liu
- Zixuan Wang
- Fahim Tajwar
- Daman Arora
- Ruslan Salakhutdinov
- Daniel Khashabi
- Yuda Song
- Andrea Zanette
affiliations:
- Carnegie Mellon University
- Johns Hopkins University
arxiv_id: '2609.35738'
url: https://arxiv.org/abs/2609.35738
pdf_url: https://arxiv.org/pdf/2609.35738
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent harness 自适应与元学习
tags:
- harness learning
- test-time adaptation
- meta-learning
- GRPO
- LLM agent
- code revision
one_liner: 训练一个 proposer 用执行反馈修订 frozen solver 的 harness，实现无需参数更新的测试时自适应与跨任务泛化
practical_value: '- 在电商/Agent 工作流里，可把「query 改写、检索重排、工具调用、结果校验」等串成可执行 harness，用一个较小的
  proposer 模型（4B 足够）只改 harness 代码、不改主模型参数，测试时用业务反馈迭代修订，降低大模型频繁微调成本。

  - 训练 proposer 时，反馈问题和打分问题要拆开：反馈用于构造下次 revision 的 execution report，打分用于 RL reward，避免
  reward hacking；GRPO 的 reward 建议加上 edit validity 和可执行性 bonus，能明显降低无效 proposal 比例。

  - 测试时不要只做 one-shot 修订：用 small proposal budget 做多轮 sequential revision，每轮基于 development
  score 保留当前最优 harness；论文在 QA 场景里 10 轮总预算 80 次 proposal 能超过独立 80 次 proposal 的 oracle
  best，适合在线 A/B 式自适应。

  - 对多跳检索/问答类 pipeline，可学习让 harness 把「用于生成下一跳 query 的摘要」和「最终 answer 的证据」分离：query 生成用摘要，answer
  直接读原始 passage，这种结构在跨域 QA 上更稳。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM agent 的能力不只由模型权重决定，还由 harness——组织模型调用、工具使用和信息流的可执行程序——决定。不同任务需要不同 harness，而手工设计成本高、反馈驱动的修订往往难跨任务复用。因此把 harness revision 形式化为对可执行程序的 meta-learning：学习一个可迁移的修订策略，测试时只改 harness、不更新模型参数。

**方法关键点**：
- 定义 proposer πθ 作为 revision policy：输入任务描述、当前 harness 代码和 execution report，输出代码编辑；solver 全程 frozen。
- 外层用 GRPO 训练 proposer，reward 是修订后 harness 的任务得分 + 编辑有效性与执行成功 bonus；可选先用 teacher 的成功修订做 SFT 初始化。
- inner loop 中，proposer 采样 G 个 edit，Apply 到 parent harness，scoring questions 上评分并 Select 当前轮最优；Reasoning Gym 只保留高于 parent 的候选，QA 则直接选最高分。
- 两个评测：Reasoning Gym 用 Qwen3.5-4B proposer/solver，SFT 来自 35B teacher，覆盖 21 个 SFT family、5 个 RL family，OOD 评估 21 个未见 family；多跳 QA 用 Qwen3-4B proposer + 8B solver，HotpotQA 训练，MuSiQue 与 2WikiMultihopQA 做 OOD。

**关键结果**：
- Reasoning Gym 的 21 个 unseen family 上，单步修订平均 held-out score 从 Base 的 0.32 提升到 RL 后 0.62；平均 proposal 质量超过 35B teacher（0.62 vs 0.56），尽管 teacher 在 oracle best-of-8 上更高。
- 多跳 QA 上，RL proposer 在 10 轮 sequential revision 中持续提升，MuSiQue 从独立修订平均 0.15 EM 提升到 10 轮后 0.27；unseen benchmark 上，10 轮最终 harness 平均超过 80 个独立 proposal 的 oracle best。
- 只在单个 revision 上训练，就能产生多轮 iterative improvement；额外训练 revision sequence 并未带来一致收益。

**最值得记住的一句话**：一个只需在单步 revision 上训练的轻量 proposer，可以学会一种可迁移的 harness 修订能力，在测试时对 frozen agent 的可执行程序做多轮自适应并泛化到未见任务。
