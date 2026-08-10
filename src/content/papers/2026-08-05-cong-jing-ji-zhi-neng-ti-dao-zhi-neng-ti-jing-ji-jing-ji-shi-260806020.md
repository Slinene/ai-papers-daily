---
title: 'From Economic Agents to Agentic Economies: A Systems Blueprint for Economic
  World Models'
title_zh: 从经济智能体到智能体经济：经济世界模型的系统蓝图
authors:
- Jiale Han
- Xiang Li
- Jing Qian
- Wenyuan Gu
- Pin Gao
- Ye Luo
- Hongyuan Zha
- Dacheng Tao
- Benyou Wang
- Lin William Cong
affiliations:
- Shenzhen Loop Area Institute
- School of Data Science, The Chinese University of Hong Kong, Shenzhen
- University of Hong Kong
- Nanyang Technological University
arxiv_id: '2608.06020'
url: https://arxiv.org/abs/2608.06020
pdf_url: https://arxiv.org/pdf/2608.06020
published: '2026-08-05'
collected: '2026-08-10'
category: MultiAgent
direction: 多智能体仿真与经济机制设计
tags:
- economic-world-model
- multi-agent-simulation
- LLM-agents
- institutional-evolution
- sim-to-real
- agentic-economy
one_liner: 提出六层经济世界模型能力阶梯，驱动多智能体从规则到自进化、制度内生与虚实对齐
practical_value: '- 借鉴六层能力阶梯设计推荐/广告系统的演进路线：从固定策略到 LLM 驱动的自适应 Agent，再到自进化智能体，可规划 Agentic
  推荐能力的长期迭代方向。

  - 用经济世界模型作为「沙盒」离线评估推荐策略：构建多智能体仿真环境，模拟用户、商家、平台交互动态，测试竞价、排序、冷启动等策略的系统性长期效果。

  - 内生制度演化的思想可迁移至推荐市场的机制设计：让计价、流量分配、出价规则由智能体在仿真中自适应调整，自动发现更优的市场机制。

  - 利用 LLM 驱动异构 Agent 行为建模，低成本仿真复杂用户和广告主行为，替代部分线上 A/B 实验的预评估。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：传统经济建模依赖均衡分析，难以从异质智能体微观交互内生地涌现宏观动态。经济世界模型(EWM)旨在构建生成式模型，让多智能体在市场中通过信念、行动与制度互动生成经济演化，但现有实现缺乏统一的系统蓝图，且高阶自进化、制度内生及虚实对齐严重不足。

**方法关键点**：
- 提出 **六层能力阶梯**：L1 固定规则世界 → L2 自适应智能体 → L3 LLM 驱动智能体 → L4 自进化智能体 → L5 制度演化世界 → L6 虚实对齐经济孪生。
- 通过系统文献综述，将现有工作映射到各层级，识别当前研究稀疏的高层能力。
- 给出每个层级的实现要素与技术路线，如 L3 强调用 LLM 模拟智能体的信念与决策，L5 引入内生制度变化等。

**结果**：综述显示绝大多数工作停留在 L1-L3，L4-L6 的系统很少，自进化、内生制度与实证对齐是明显空白，为后续研究提供了路线图。
