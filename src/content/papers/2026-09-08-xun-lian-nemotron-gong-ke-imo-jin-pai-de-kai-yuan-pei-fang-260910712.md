---
title: 'An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics'
title_zh: 训练 Nemotron 攻克 IMO 金牌的开源配方
authors:
- Ivan Moshkov
- Stephen Ge
- George Armstrong
- Wei Du
- Sadegh Mahdavi
- Igor Gitman
affiliations:
- NVIDIA
arxiv_id: '2609.10712'
url: https://arxiv.org/abs/2609.10712
pdf_url: https://arxiv.org/pdf/2609.10712
published: '2026-09-08'
collected: '2026-09-11'
category: Reasoning
direction: 数学证明生成 · 测试时搜索与RL
tags:
- IMO
- test-time compute
- verifier
- RL
- multi-model ensemble
- open-source
one_liner: 开源三 checkpoint 生成-验证-精炼管线在 IMO 2026 达 30/42 金牌线，并发布后训练与推理全栈
practical_value: '- 多模型/多后训练 checkpoint 的异构集成比单模型增加采样次数更有效：在生成商品标题、搜索 query 或 Agent
  动作方案时，同等 token 预算下分配多个互补模型生成候选，比单模型重复采样更容易覆盖不同解空间，类似推荐中的 ensemble diversity。

  - 把「搜索期验证」与「最终选择」解耦：搜索期验证需要低假接受和可操作的反馈，最终选择需要更贴近真实奖励的昂贵评分器；对应粗排/精排/重排的分离，且最终重排可投入更多算力，不必复用搜索期评分。

  - 验证器错误代价不对称：假接受导致搜索提前终止且不可恢复，假拒绝只增加时间和成本；在业务 pipeline 中若线上错误代价高，应设计保守阈值，并允许延迟恢复。

  - 保留候选池和跨轮精炼：搜索中不直接丢弃高分但未过验证的候选，下一轮继续精炼；适合电商/Agent 中长尾候选，避免 aggressive triage 淘汰后期有价值方案。此外记录
  token/GPU 小时资源核算有助于生产部署预算规划。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
IMO 是顶级数学推理测试，近两年自然语言模型已能夺金，但如何系统性复现仍未完全公开。本文以 Nemotron-3-Ultra 550B-A55B 为基础，研究后训练与测试时推理选择对自然语言证明生成的影响，目标提供可复现金标准系统。

**方法关键点**  
- 从 GA 版 Nemotron-3-Ultra 出发，训练两个 specialist：SFT（监督微调，426K 长上下文，414,890 条多轨迹语料）与 RL（异步强化学习，9,597 道题，移除自分析奖励）。三个 checkpoint 在推理中分别承担生成、验证、精炼。
- 提交系统两阶段：高计算搜索阶段，每轮由 8 个互补提示模板 × 3 模型 × 16 次采样产生 384 个候选；验证由 RL+SFT 各 8 次判决组成，全票 1 才接受；未接受则选 top-16 候选精炼，最多 8 轮。最终选择阶段，对每个 finalist 用 GA+RL+SFT 各 16 次 IMO-style 判决（共 48 次）按均分排名，tie-break 选更短证明。
- 全程自然语言，无形式验证器/外部工具/联网。

**关键实验与数字**  
- IMO 2026 正式得分 30/42，超过金牌线 29；P1/P2/P4/P5 满分，P3/P6 各得 1 分。提交证明在约 707M tokens / 1,464 GPU-hours 内找到，整场比赛总消耗 2.31B tokens / 4,800 GPU-hours。
- 30 题开发集上，单 checkpoint 最终分数：GA 162, RL 180, SFT 165；三模型集成 188（满分 210），明显超过单模型。
- 验证器审计：RL+SFT 全票通过假接受率仅 1.1%，但假拒绝率 81.3%；保守设计旨在避免搜索提前停止在错误证明上。
- 预算分配实验：RL 128 采样加到 256 只多解 1 题，但加入 SFT 64 采样显著提升；不同 checkpoint 的多样性比单模型加倍更有价值。

**最值得记住的一句话**  
单纯扩展生成预算不够，收益来自互补后训练模型、验证引导的精炼，以及最终评估阶段的高计算投入。
