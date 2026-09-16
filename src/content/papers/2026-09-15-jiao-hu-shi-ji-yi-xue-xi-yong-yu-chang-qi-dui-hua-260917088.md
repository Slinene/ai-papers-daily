---
title: Interactive Memory Learning for Long-Term Conversations
title_zh: 交互式记忆学习用于长期对话
authors:
- Cai Ke
- Jiangyue Yan
- Han Zhang
- Xin Liu
- Zike Yuan
- Yue Yu
- Hui Wang
- Ruifeng Xu
affiliations:
- Harbin Institute of Technology, Shenzhen
- Pengcheng Laboratory, China
arxiv_id: '2609.17088'
url: https://arxiv.org/abs/2609.17088
pdf_url: https://arxiv.org/pdf/2609.17088
published: '2026-09-15'
collected: '2026-09-16'
category: MultiAgent
direction: 多智能体协作记忆优化
tags:
- long-term memory
- multi-agent RL
- PPO
- LLM agent
- memory management
- test-time adaptation
one_liner: 提出 ICML 多智能体在线强化学习框架，Planner 与 Trigger 通过跨会话延迟奖励共同进化，实现记忆策略自演进
practical_value: '- 将记忆写入（Planner）和记忆召回（Trigger）拆成两个可学习策略，用 PPO 在线更新，适合客服/导购等用户偏好频繁变化场景；Planner
  过滤噪音控制上下文长度，Trigger 按当前 query 选择记忆。

  - 跨会话延迟奖励机制：把未来响应质量反传回当初的存储决策，解决记忆价值滞后问题，可迁移到电商中用户长期反馈对画像写入策略的反哺。

  - 用 Retrospective Session Synthesis 反向生成一致故事线并标注记忆依赖，做冷启动专家数据，可借鉴为合成用户会话数据训练记忆策略，缓解在线
  RL 稀疏奖励。

  - 实现 plug-and-play，不改闭源 LLM 权重，仅训练小模型策略，构造延迟约 63ms、检索约 13ms，对已有线上 LLM 对话系统做记忆增强成本低。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
长期对话中现有记忆管理多为静态启发式，信息被被动存档，无法根据用户需求变化自适应，导致过时偏好与新需求冲突。人类记忆是选择性编码、反馈更新，因此需要将记忆从被动档案转变为可学习、可交互的策略。

## 方法关键点
- 将长期对话建模为 POMDP，联合动作包含 Planner 的存储决策和 Trigger 的检索决策。
- 提出 Retrospective Session Synthesis：从种子会话反向生成一致 storyline，再正向标注 Planner 二值标签和 Trigger 检索标签，并加入 hard/soft negatives，得到专家数据做监督 warm-up，解决冷启动。
- ICML 框架包含两个 Actor-Critic 智能体：Planner 判断当前信息是否值得保存；Trigger 从动态记忆中选择最相关记忆用于生成回复。二者通过 PPO 在线共同优化。
- Cross-Session Truth Reward：Planner 存储时只有 proxy reward，当 Trigger 未来调用该记忆并产生 quality reward，将延迟奖励反传回存储决策，使存储目标对齐真实效用。

## 关键实验
在 MSC、Conversation Chronicles (CC)、GapChat (GC) 三个人类交互多会话数据集上评估，对比 Long Context、Mem0、A-Mem、MemoryOS、MemoryBank、LD-Agent、THEANINE 等。以 Qwen3-8B + Gemini2.5 为例，CC 上 Mauve 达 80.33，显著超过最佳 baseline；人工评估 ICML 在生成和记忆上胜率约 70-80%。消融显示去掉 Truth Reward 或 Evolution 下降最明显，Synthetic Data 在 0.25K-0.5K 最优。效率方面推理 tokens 稳定，构造延迟约 63ms，检索约 13ms。

最值得记住的一句话：把记忆管理从被动存档变成在线可学习策略，用未来响应质量反传回存储决策，是长期个性化对话的关键。
