---
title: 'Build, Don''t Play: Self-Improving LLM Research Agents Develop a Hearthstone
  Battlegrounds AI That Rivals Top Players'
title_zh: 构建而非游玩：自改进 LLM 研究代理造出匹敌顶尖玩家的炉石酒馆战棋 AI
authors:
- Changlian Ma
- Limin Wang
affiliations:
- Nanjing University
- Shanghai AI Laboratory
arxiv_id: '2610.33845'
url: https://arxiv.org/abs/2610.33845
pdf_url: https://arxiv.org/pdf/2610.33845
published: '2026-10-23'
collected: '2026-10-27'
category: MultiAgent
direction: 多代理自改进与 RL 训练
tags:
- LLM Agents
- Self-Improving
- PPO
- Game AI
- Sim-to-Real
- Research Automation
one_liner: 自改进 LLM 研究代理系统 AutoTavern 从零构建模拟器和 PPO 策略，训练出的 AI 在天梯表现超越顶尖人类玩家
practical_value: '- 将 LLM 用于「构建工具/策略」而非「直接实时决策」：让 LLM 离线生成模拟器、校准对手、特征或规则，在线推理仍用轻量模型，可兼顾效果与延迟，适合推荐系统实时打分场景。

  - 类型化研究记忆 + 验证门（verification gates）值得借鉴：把实验结论、模型改动历史、A/B 结果存成结构化条目，新代理或新方案先过验证再采纳，减少
  LLM 幻觉导致的上线事故。

  - 用 PPO 训练策略时，对手/用户模拟器必须校准到真实分布（calibrated to real games），否则 sim-to-real gap 会毁掉效果；电商推荐做
  RL 时应定期用真实日志更新用户模拟器。

  - 构建专用决策 benchmark（类似 TavernBench），同时评测效果指标和推理延迟：LLM 在推荐决策上可能准确率高但延迟达数十秒，无法满足在线约束，必须评测真实时间窗口内的可用性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
LLM 代理能否从原始数据出发，独立完成一个困难的真实问题，构建出与人类对抗的系统？选用炉石传说酒馆战棋（八人自走棋，随机商店与战斗、隐藏信息、近千张交互卡牌）作为测试场。

**方法关键点**  
AutoTavern 由多个专业化 LLM 研究代理组成，共享类型化研究记忆；每个声明（claim）必须通过验证门，实时对战闭环反馈让代理同时改进模拟器、对手和策略，并用同一反馈优化自身研究流程；人类只设定目标和模糊机制规则。

系统在 20 天内构建了 TavernGym（首个忠实还原正式服全部内容的模拟环境），并交付 23 版 TavernAgent，使用 PPO 针对校准到真实对局分布的对手训练。

**关键结果数字**  
TavernAgent 能独立在实时天梯打完整局：评分从 6000 升至约 15000；公开排行榜口径下，最后 20 局平均名次 1.60，第一名率 80%，优于服务器前十玩家各项统计（2.34，59%）。TavernBench（960 任务/40 场景）中，TavernAgent 解答 91% 的运营任务，前沿 LLM 最高 63%；决策耗时 0.03 秒，LLM 最多需 26 秒；在实时回合 1 秒约束内保持 90% 正确率，无 LLM 超过 26%。结论：LLM 代理构建系统的能力远强于亲自玩游戏。
