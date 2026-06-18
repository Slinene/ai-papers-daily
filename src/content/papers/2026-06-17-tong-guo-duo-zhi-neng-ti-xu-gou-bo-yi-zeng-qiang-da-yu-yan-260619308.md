---
title: Enhancing Decision-Making with Large Language Models through Multi-Agent Fictitious
  Play
title_zh: 通过多智能体虚构博弈增强大语言模型决策能力
authors:
- Leyang Shen
- Yang Zhang
- Xiaoyan Zhao
- Chun Kai Ling
- Tat-Seng Chua
affiliations:
- National University of Singapore
arxiv_id: '2606.19308'
url: https://arxiv.org/abs/2606.19308
pdf_url: https://arxiv.org/pdf/2606.19308
published: '2026-06-17'
collected: '2026-06-18'
category: MultiAgent
direction: 多智体虚构博弈均衡求解决策纠缠
tags:
- Multi-Agent Fictitious Play
- Equilibrium-Seeking
- Stance Entanglement
- LLM
- Decision-Making
- Game Theory
one_liner: 提出多智能体虚构博弈范式，以博弈均衡迭代求解立场纠缠的决策问题，提升决策质量与鲁棒性
practical_value: '- **广告竞价策略优化**：将广告主、平台、用户等利益方建模为 Agent，利用 MAFP 迭代寻找均衡出价，替代固定规则或单智能体生成，可提升策略的鲁棒性与对抗性。

  - **搜索排序多方博弈**：在搜索场景中，商品、商家、用户之间存在立场纠缠，可借鉴 MAFP 将排序决策视为多方博弈过程，通过虚构博弈逐步逼近满足多方目标的排名均衡。

  - **推荐系统供需均衡**：在双边市场中，用户偏好与商家收益相互依赖，MAFP 范式可帮助推荐系统在长期交互中找到帕累托改进，避免陷入局部最优。

  - **Agent 协作训练与自对弈**：MAFP 可作为一种多智能体自我博弈的训练框架，无需外部对手即可暴露策略弱点，可用于生成式推荐模型的对抗训练或自动 prompt
  调优。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 驱动的多智能体系统（MAS）在分工协作执行任务上表现突出，但难以处理现实中常见的决策问题——各利益方立场相互纠缠，决策彼此依赖，无法孤立求解。现有 MAS 的“分而治之”范式仅能降低执行复杂度，无法应对这种立场纠缠（stance entanglement）带来的决策复杂度。

**方法**：提出 **Multi-Agent Fictitious Play (MAFP)**，将各利益方立场建模为独立 Agent，决策过程转化为均衡寻找过程。基于博弈论中的虚构博弈（fictitious play），每个 Agent 在每次迭代中，根据其他 Agent 历史决策的经验分布做出最优响应（best response）。迭代过程中，Agent 相互暴露并修正策略弱点，逐步收敛到稳健的均衡策略。

**结果**：在需要预先制定策略的竞争性决策任务上，MAFP 在**锦标赛强度**（比赛胜率）和**鲁棒性**两个互补指标上均显著优于单轮对话和多轮讨论基线，验证了该范式在破解立场纠缠上的有效性。
