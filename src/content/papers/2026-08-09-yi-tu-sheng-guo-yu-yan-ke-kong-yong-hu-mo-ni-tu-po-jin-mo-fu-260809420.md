---
title: 'Intent Speaks Louder: Controllable User Simulation Beyond Response Imitation'
title_zh: 意图胜过语言：可控用户模拟突破仅模仿回复
authors:
- Bo Wang
- Ruixing Zhang
- Yunqi Liu
- Yang Zhang
- Liangzhe Han
- Tongyu Zhu
- Leilei Sun
affiliations:
- Beihang University
arxiv_id: '2608.09420'
url: https://arxiv.org/abs/2608.09420
pdf_url: https://arxiv.org/pdf/2608.09420
published: '2026-08-09'
collected: '2026-08-12'
category: Agent
direction: 用户模拟 · 意图可控生成
tags:
- UserSimulation
- IntentControl
- RLHF
- SFT
- DialogueSystem
one_liner: 提出 UserIDA，通过显式逐轮意图指令实现可控用户模拟，意图准确率大幅领先基线
practical_value: '- 对话式推荐/搜索 Agent 评估：构建用户模拟器时，显式注入每轮交互意图（如澄清需求、修正误解、接受结果），可生成更真实的用户行为流，用于离线评测
  Agent 的意图理解与响应能力。

  - 训练数据增强：对于电商导购、搜索 query 改写等场景，可按指定意图（补充细节、否定前序推荐）批量生成对话样本，缓解多样性不足，降低人工标注成本。

  - 意图-表达解耦设计：借鉴 UserIDA 将“意图选择”与“语言生成”分离的思路，在推荐对话系统内单独规划下一步交互目标，再调用 LLM 生成对应文本，提升多轮交互的连贯性与成功率。

  - 强化学习校正技巧：在指令遵循类生成任务中，可采用 group-based RL，让意图违背的候选回复在奖励排名中低于合规项，以温和方式强化约束，避免直接惩罚导致生成质量下降。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：用户模拟器是训练交互式助手（如对话推荐Agent）的关键环境，但生成下一轮用户回复本质上一对多：相同上下文可对应多种合理延续，不同延续蕴含不同局部交互意图（如接受、修正、质疑）。仅追求语言流畅易导致意图错位，使对话偏离真实用户行为。核心洞察：可控用户模拟应**将“该轮实现什么交互意图”与“怎么用语言表达该意图”解耦**。

**方法**：提出 UserIDA（用户意图-指令对齐），定义六类交互意图（提供信息、要求澄清、纠正、接受、拒绝、完成），将意图作为每轮显式指令。首先通过有监督微调（SFT）让模型学会按指令生成回复；随后引入**意图校准策略优化**（group-based RL），在混合质量-意图-风格奖励中，要求意图违背的候选回复排在合规回复之后，既保持回复整体质量又强化意图遵循。

**结果**：在公开基准 LMSYS-USP 上，UserIDA 的意图准确率达 **86.6%**，比最强专用用户模拟器基线提升 **24.3 个百分点**，且语义和风格相似度均有提高。在上下文干预测试中，**91.7%** 的对话状态能实现至少四种目标意图，而最强外部基线仅 22.9%。实验表明，逐轮意图控制是用户模拟中回复保真度之外的另一关键维度。
