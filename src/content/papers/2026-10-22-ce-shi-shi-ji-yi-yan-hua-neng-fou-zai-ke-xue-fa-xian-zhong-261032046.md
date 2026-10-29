---
title: Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific
  Discovery?
title_zh: 测试时记忆演化能否在科学发现中超越测试时训练？
authors:
- Yepeng Liu
- Shengmai Chen
- Xuandong Zhao
- Chengzhi Liu
- Dawn Song
- Xin Eric Wang
- Yuheng Bu
affiliations:
- UC Santa Barbara
- UC Berkeley
arxiv_id: '2610.32046'
url: https://arxiv.org/abs/2610.32046
pdf_url: https://arxiv.org/pdf/2610.32046
published: '2026-10-22'
collected: '2026-10-29'
category: Training
direction: 测试时记忆演化替代权重更新
tags:
- Test-Time Adaptation
- External Memory
- Scientific Discovery
- Efficient LLM
- Agentic Workflow
one_liner: 提出TTME：不更新权重，通过外部记忆持续沉淀经验指导后续发现，性能优于TTT且算力降八成以上
practical_value: '- 在电商/广告的 Agentic 搜索、选品/文案迭代场景，可用“外部经验记忆”替代线上微调：把每次 query/候选/收益反馈写入可检索
  memory，后续推理时检索相似案例，避免在线权重更新和灾难性遗忘。

  - 具体实现可借鉴 TTME：把成功/失败经验蒸馏成结构化条目（如状态→动作→奖励），用 memory read/write 控制探索；适合低延迟、高吞吐的推荐对话
  Agent。

  - 计算成本收益可指导工程：类似 Qwen3-8B 规模下，外部记忆方法比在线训练省 80%+ FLOPs、约一半 runtime，适合边缘/实时决策。

  - 需注意论文在数学发现任务上验证，迁移到业务前应先在自有任务上对比 TTT、无适应和 memory 方案的收益/复杂度。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：TTT 让开放权重 LLM 在科学发现上超过闭源推理框架，但在线权重更新带来额外算力成本，扩展到更大模型受限。

方法：提出 Test-Time Memory Evolution (TTME)，作为即插即用的测试时适应方法：不更新模型权重，通过持续更新外部记忆，把发现过程中的经验蒸馏成可复用知识，引导后续探索。为公平比较，在同一发现框架下只替换适应方法。

结果：在五个数学任务上，TTME 全部优于 TTT；FLOPs 降低 82.8–84.6%，运行时间减少 47.7–58.4%。结论：在评估的发现场景下，TTME 是比 TTT 更有效且更省算力的选择。
