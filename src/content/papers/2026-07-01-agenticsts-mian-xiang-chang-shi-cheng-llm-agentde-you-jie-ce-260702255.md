---
title: 'AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents'
title_zh: AgenticSTS：面向长时程LLM Agent的有界内存测试床
authors:
- Xiangchen Cheng
- Yunwei Jiang
- Jianwen Sun
- Zizhen Li
- Chuanhao Li
- Xiangcheng Cao
- Yihao Liu
- Fanrui Zhang
- Li Jin
- Kaipeng Zhang
affiliations:
- Alaya Lab
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Nankai University
- University of Science and Technology of China
arxiv_id: '2607.02255'
url: https://arxiv.org/abs/2607.02255
pdf_url: https://arxiv.org/pdf/2607.02255
published: '2026-07-01'
collected: '2026-07-03'
category: Agent
direction: Agent 有界内存与模块化评估
tags:
- bounded-memory
- typed-retrieval
- long-horizon-agent
- ablation-study
- Slay-the-Spire
- agent-evaluation
one_liner: 用类型化检索组装提示替代累积上下文，保持内存有界并支持单层消融分析
practical_value: '- **长会话 Agent 的上下文管理**：电商顾问或搜索助手等场景需要多轮交互，可借鉴“类型化检索组装”思路，将观察、工具结果、反思等分门别类存储，每次决策仅提取相关片段拼接成新提示，避免无限追加历史导致成本飙升与效果混杂。

  - **模块化消融与迭代**：在推荐对话系统中，可将知识库、用户画像、对话状态等作为独立内存层，通过切换检索策略快速验证各自贡献，类似论文中对技能层的消融实验，指导架构演进。

  - **工程稳定性**：有界提示保证每次推理的 token 数恒定，利于延迟控制和预算管理，避免长上下文带来的 KV cache 膨胀和推理速度抖动。

  - **可复现的评估方法**：论文提供的轨迹数据和实验脚本，可作为构建面向推荐/搜索 Agent 的评测框架参考，尤其适合需要数百步决策的复杂场景（如比价助手、旅行规划
  Agent）。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：长时程 LLM Agent 通常将历史观察、工具调用和反思全部追加到 prompt 中，导致上下文膨胀且各个内存组件的影响混杂难分。为系统研究内存层如何影响决策，需要一种能隔离各层的可控记忆机制。

**方法**：提出“有界合约”——每次决策时，从零构建一个全新的用户消息，该消息由一系列类型化检索模块组装而成（如近期战斗日志、已习得技能、全局状态等），不附加任何原始决策记录。这样 prompt 长度保持恒定，任意内存层均可单独消融。实例化在游戏《Slay the Spire 2》中，该游戏需要数百步战术与战略决策，难度较高（人类胜率16%，前沿 LLM 零胜）。

**结果**：在固定模型 A0 上，开启技能触发层后胜率从 3/10 提升到 6/10（Fisher 精确检验 p≈0.37，方向性显著）。发布可复现测试床：298 条完整轨迹，含条件标签、内存/技能快照、prompt 记录和分析脚本，为研究多内存层交互提供基准。
