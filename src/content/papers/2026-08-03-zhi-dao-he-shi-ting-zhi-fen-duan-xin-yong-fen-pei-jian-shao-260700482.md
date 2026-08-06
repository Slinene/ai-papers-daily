---
title: 'Know When to Stop: Segment-Level Credit Assignment for Reducing Overthinking'
title_zh: 知道何时停止：分段信用分配减少过度思考
authors:
- Chia-Hsuan Lee
- Sihui Dai
- Mingyang Zhou
- Isha Slavin
- Hsuan Su
- Shi-Xiong Zhang
- Sambit Sahu
- William Campbell
affiliations:
- Capital One
arxiv_id: '2607.00482'
url: https://arxiv.org/abs/2607.00482
pdf_url: https://arxiv.org/pdf/2607.00482
published: '2026-08-03'
collected: '2026-08-06'
category: Training
direction: LLM推理训练·信用分配
tags:
- Overthinking
- Credit Assignment
- RLHF
- GRPO
- Math Reasoning
- LLM Training
one_liner: 利用推理链中的中间答案承诺作为廉价代理，分段分配信用以抑制无益自我反思
practical_value: '- 在构建 Agent 或推荐系统的多步推理链路时，可借鉴「中间答案承诺」作为信号，自动评估后续步骤是否有助于任务目标，从而提前终止无用的推理分支，降低
  token 消耗与延迟。

  - 在 RLHF 或 GRPO 训练中，可尝试分段信用分配，而非仅对整个轨迹赋分，以更精细地鼓励有效推理、抑制重复验证等低效行为。

  - 对于需要多轮交互的对话式推荐或搜索 Agent，可以引入“漂移检测”，若当前回答远离正确方向，则触发策略调整，避免陷入过长的无意义探索。

  - 该方法无需额外人工标注或过程奖励模型，仅利用最终答案标签即可实现分段优势塑形，在资源有限的业务场景下性价比高。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：推理语言模型在数学问题中常表现出过度思考（重复验证、方法切换、自相矛盾），即使控制长度，错误轨迹中的无效自我反思率也更高。现有方案需昂贵的过程标注，难以规模化。本文发现，推理链中模型会自发给出中间答案（如“答案是X”），将其与真实答案比较即可廉价判断后续反思是否有效。

**方法关键点**：提出 DASH，一种分段信用分配方法。在 GRPO 基础上，将推理轨迹按中间答案承诺切分为段，每段根据其最终答案候选人正确性与否赋予优势值：若段内答案正确，则该段获得正优势；若答案错误或从中途偏离，则负优势。无需额外 step-wise 监督，仅利用 ground truth 答案标签。训练时优化段级优势，鼓励走向正确答案的推理片段，抑制导致偏离的片段。

**关键结果**：在竞赛级数学基准（AIME、MATH-500、AMC23 等）上，DASH 取得了平均 59.45% 的最高准确率，高于 Dr.GRPO 的 58.1% 和 GRPO 的 56.95%，尤其在过度思考普遍的任务上提升明显。同时，模型过度思考行为减少，自我纠正更加高效。
