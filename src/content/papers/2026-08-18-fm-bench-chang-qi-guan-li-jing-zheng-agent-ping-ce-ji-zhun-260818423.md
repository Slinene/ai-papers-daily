---
title: 'FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents'
title_zh: FM-Bench：长期管理竞争 Agent 评测基准
authors:
- Tianyou Wang
- Chongyang Gao
- Kezhen Chen
- Chen Dong
- Yinghao He
- Donghan Li
- Wangcheng Xu
- Hongjiu Zhang
- Chi Li
affiliations:
- AnalogyAI
arxiv_id: '2608.18423'
url: https://arxiv.org/abs/2608.18423
pdf_url: https://arxiv.org/pdf/2608.18423
published: '2026-08-18'
collected: '2026-08-22'
category: Eval
direction: LLM Agent 长期管理评测基准
tags:
- LLM Agents
- Long-Horizon
- Multi-Agent
- Benchmark
- Memory
- Behavior Analysis
one_liner: 15 个前沿 LLM 在 20 年共享足球管理世界中评测，结果由可解释管理行为而非模型规模与 token 消耗决定
practical_value: '- 把记忆管理作为 Agent 能力来评测：业务中若采用“每次决策点新会话+自维护 notebook”的模式，可将 notebook
  连续快照的 TF-IDF 余弦相似度作为记忆健康度指标，警惕 append-only（>0.9）和完全重写（<0.25）两种失效；不要把长期上下文截断/摘要交给
  harness 隐式做，否则评测分数部分反映的是脚手架而非模型。

  - 奖励函数要显式反囤积与末期衰减：FM-Bench 对超额现金按 0.3 计入净资产，且正分乘 ρ=(t/T)^1.5，迫使 agent 权衡“安全持有现金”的隐性机会成本；电商/广告预算分配中同样可以给闲置预算或过时策略加递减折扣，防止
  agent 永远选局部安全动作。

  - LLM 无法从数百次拒单中学会市场真实价格（中位 30 次报价才成交 1 次）：在竞价/谈判 Agent 上，应显式给模型维护一个可查询的 bid-ask
  历史或先验价格分布，而不是只把 rejection 当反馈；Solo 与 Arena 的行为对比（出价频率 0.5→4.6/季）说明策略强度需按对手自适应。

  - 上线前做共享经济体评测：固定对手的 solo 榜第一会形成 dynasty，但 Arena 中冠军在 10 个模型间轮换、卫冕只成功 2/19，说明反自适应环境能揭示策略真实韧性；推荐/流量分配策略也应放入多个
  Agent 争抢同一批库存/用户预算的共享仿真，而非仅做静态 A/B。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM agent 在短周期、无竞争任务上已可靠，但真实管理要求在一个随决策改变的世界里长时间运营组织，面对隐藏信息、累积后果、反自适应市场和多目标压力。现有 long-horizon bench 无竞争，multi-agent 竞技又太短，FM-Bench 同时压满两个维度。

**方法关键点**：
- 环境：20 个游戏年、约 340-400 个决策止点、26 个工具，足球俱乐部经营：选秀、转会、续约、设施与青训投资、排阵、董事会压力。
- 确定性引擎，评分由机制累积计算，无 LLM judge。分数 = 18·ln(1+H/60)+10·sign(VA)·ln(1+|VA|/40)+6·ln(1+M/80)，对早退有 ρ 折扣。
- 记忆设计：每个 stop 是全新对话，唯一跨 stop 状态是 agent 自写 notebook；记忆整理能力本身被测量。
- 四个需求各配机制：隐藏信息=永久偏置的球探区间；累积后果=青训/设施多年回报+破产/下课螺旋；反自适应市场=拒单抬隐藏要价、反复交易加价、谈判冷却；多目标=董事会联合评判成绩与财务。

**关键实验与数字**：
- 15 个前沿模型 + 脚本锚点；solo 三 seed 与 Arena 共享世界。oracle 95.54，claude-fable-5 90.94，kimi 88.49，gpt-5.6-terra 86.66；脚本盲锚大多死亡。Arena 冠军在 10 个模型间轮换，claude-fable-5 仍最高 76.26。
- 行为分解：末期削减慢回报投资 rs=-0.58，现金占净资产比 rs=-0.50，提前续约 lead rs=+0.45；token spend 与分数无关。
- 价格发现：成交中位 30 次报价 vs oracle 1 次；人类首次玩家最好 74.64，落在模型底部。

**最值得记住的一句话**：在长周期竞争管理里，模型规模、价格、token 花费都不预测结果，区分好坏的是可解释的管理行为——按剩余时间削减慢回报投资、不囤现金、提前续约。
