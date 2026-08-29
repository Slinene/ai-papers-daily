---
title: 'Beyond Parallel Blindness: Information Floors and Model Gaps in Block Drafting'
title_zh: 超越并行盲区：块草稿中的信息地板与模型差距
authors:
- Xinwei Qiang
- Xiang Fang
- Chang Chen
- Yue Guan
- Yufei Ding
affiliations:
- University of California San Diego
arxiv_id: '2608.27339'
url: https://arxiv.org/abs/2608.27339
pdf_url: https://arxiv.org/pdf/2608.27339
published: '2026-08-27'
collected: '2026-08-29'
category: LLM
direction: LLM 推理加速 · 块草稿信息瓶颈
tags:
- Speculative Decoding
- Block Drafting
- Information Floor
- Model Gap
- LLM Inference
one_liner: 区分块草稿的固有信息损失与草稿器模型差距，量化短程条件可消除的上限损失
practical_value: '- 在电商/Agent 的 LLM 推理服务中上 speculative decoding 时，先估计目标模型在目标块大小下的信息地板，判断草稿器是受信息约束还是模型能力限制；不要只凭
  accepted length 做调优决策。

  - 全并行块草稿的最后槽位信息损失上限约 0.286，考虑对块内前几个 token 采用串行或半串行生成（哪怕多一次前向），可移除 86–100% 的地板，对延迟敏感的对话式推荐/Agent
  响应可能收益明显。

  - DFlash/DSpark 的拒绝主要来自模型差距而非信息缺失，说明提升草稿器对前序已实现 token 的条件建模（如增量更新隐藏状态）比盲目加大块大小更有效。

  - 该方法可迁移到 Agent 多步 LLM 调用链中，用信息地板分析并行化提案的固有损失，优化工具参数生成、多候选推理的延迟与质量权衡。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：块草稿（block drafting）在一次前向中生成多个 token，但并行性导致每个位置的提案在其前序目标 token 实际产出前就必须确定，损失包含两部分：块内路径信息缺失和可观察信息建模不充分，接受长度无法区分二者，阻碍定位瓶颈。

方法：定义信息地板（information floor）：在指定条件顺序下最小的期望拒绝率；实际拒绝高于地板的部分为模型差距（model gap）。从目标模型 rollouts 估计地板和差距，覆盖 4 个领域、4 个开放权重目标和 1 个前沿 API 目标。

关键结果：Qwen3-4B 全并行地板在最后槽位达 0.286，即最佳提案每槽接受率上限仅 71%；一个已实现 token 可移除 86–100% 的地板，表明短程条件价值极高（独立互信息分析也验证）；当前草稿器显著高于地板，DFlash 最后槽模型差距占拒绝的 43–64%，DSpark 的 oracle 条件拒绝中达 85–92%。
