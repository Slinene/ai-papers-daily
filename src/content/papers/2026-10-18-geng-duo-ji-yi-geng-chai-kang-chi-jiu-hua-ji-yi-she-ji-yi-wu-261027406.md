---
title: 'More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM
  Agents'
title_zh: 更多记忆更差？抗持久化记忆设计抑制 LLM Agent 错误复现
authors:
- Ruhan Wang
- Kishan Panaganti
- Dongruo Zhou
affiliations:
- Indiana University
- Tencent HY
arxiv_id: '2610.27406'
url: https://arxiv.org/abs/2610.27406
pdf_url: https://arxiv.org/pdf/2610.27406
published: '2026-10-18'
collected: '2026-10-21'
category: Agent
direction: LLM Agent 记忆与自改进机制
tags:
- Agent Memory
- Error Reproduction
- Self-Improvement
- Abstraction
- Contextual Bandit
- LLM Agents
one_liner: 提出 Anti-Persistence 记忆：只存轨迹和结果，抽象按需合成并丢弃，抑制错误复现，提升成功率并降低成本
practical_value: '- 在电商/推荐 Agent 的记忆设计中，优先持久化原始交互轨迹和结果日志，而非规则、总结或技能等抽象内容；抽象只在当前任务中按需合成，使用后立即丢弃，防止错误抽象跨任务固化。

  - 可借鉴其自适应模式选择：定义多种经验使用模式（直接复用轨迹、模仿成功行为、提炼任务策略、生成纠错规则），用轻量 contextual bandit 结合任务相似度、时间衰减和
  UCB 探索项来选，比固定策略更鲁棒。

  - 奖励信号中加入成本惩罚 r = clip(y - λκ, -1, 1)，λ 设小值（如 0.05）能鼓励选择性合成，在保持成功率的同时控制 LLM 调用量，适合线上成本敏感场景。

  - 注意“错误复现”路径：即使删除错误抽象，其影响仍可能通过被影响的轨迹进入后续合成；评估记忆系统时应追踪历史暴露来源，而非只做简单剪枝或屏蔽。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM Agent 通过外部记忆存储自身执行经验进行自改进。常见做法是持久化从轨迹中提炼的抽象知识（规则、总结、技能），以便跨任务复用。但错误抽象被检索复用后，不仅直接影响当前决策，还会通过产生的轨迹成为后续抽象合成的输入，从而让错误间接“复现”并持续存在。现有维护机制（评分、剪枝、精炼）难以根除这种经由历史轨迹的间接反馈。

## 方法关键点
- **Anti-Persistence 设计**：只持久化原始轨迹和结果日志，不持久化任何抽象；抽象仅在当前任务执行前按需合成，使用后丢弃。
- **四种经验使用模式**：`none`（直接复用检索到的轨迹）、`imitation`（提炼成功轨迹中的可复用行为模式）、`strategic`（蒸馏高阶子目标与规划）、`corrective`（从失败轨迹生成规避规则）。
- **自适应模式选择**：用轻量 contextual bandit 从四种模式中选择。基于相似历史任务的奖励（任务成功减合成调用成本），结合任务相似度、时间衰减和 UCB 探索项。检索分两步：先从结果日志检索相似任务选模式，再按模式从轨迹记忆检索经验。
- **成本感知奖励**：`r = clip(y - λκ, -1, 1)`，κ 为实际合成调用次数，λ 默认 0.05，只惩罚额外合成调用。

## 关键实验
在 ALFWorld、WebShop、ScienceWorld 三个基准，Llama-4-Scout、Qwen3-Coder-Next、Gemma-4-31B-it 三个骨干上，进行 10 轮自改进。
- Anti-Persistence 平均成功率 59.9%，高于轨迹记忆 53.5%、抽象记忆 49.0%、联合记忆 49.3%，也优于最强基线 Reflexion 的 52.9%。
- 同时平均 LLM 调用成本最低（9.3 vs 轨迹 9.5、抽象 10.2、联合 9.5）。
- 消融表明，丢弃抽象优于持久化抽象（最大正收益 +28.0%），bandit 选择优于固定模式或随机选择。

## 最值得记住的一句话
把经验累积与抽象持久化分离，按需合成临时抽象，能抑制错误复现并同时提升效果和降低成本。
