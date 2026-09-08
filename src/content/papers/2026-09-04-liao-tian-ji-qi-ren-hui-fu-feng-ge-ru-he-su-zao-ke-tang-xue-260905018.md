---
title: 'How a Chatbot''s Response Style Shapes a Classroom: A Multi-Agent Simulation
  of Students Consulting AI'
title_zh: 聊天机器人回复风格如何塑造课堂：学生咨询 AI 的多智能体模拟
authors:
- Rin Tamai
- Yuya Dan
affiliations:
- Faculty of Informatics, Matsuyama University
arxiv_id: '2609.05018'
url: https://arxiv.org/abs/2609.05018
pdf_url: https://arxiv.org/pdf/2609.05018
published: '2026-09-04'
collected: '2026-09-08'
category: MultiAgent
direction: 多智能体仿真 · AI 依赖心理效应
tags:
- Multi-Agent Simulation
- LLM
- Sycophancy
- AI Dependence
- Psychological State
- Classroom
one_liner: 用 20 学生代理仿真六种 AI 回复风格，发现解决方案导向风格低 AI 依赖并提升自主性，肯定与煽动风格增加依赖与压力
practical_value: '- 多智能体仿真可迁移到用户与导购/推荐 Agent 长期交互评估：定义用户状态变量（如信任、自主性、AI 依赖），模拟不同回复策略在时间窗内的累积效应，尤其适合识别过度迎合带来的依赖风险。

  - 双 LLM 评估模式实用：一个 LLM 按风格生成回复，另一个屏蔽风格提示、仅根据对话与状态历史输出参数更新，可作为低成本离线策略评估器，减少人工标注脚本。

  - 结果提示：过度共情/肯定的回复风格（类似推荐解释中一味迎合点击偏好）会推高用户 AI 依赖；解决方案导向风格能平衡满意度与自主性。在电商导购 Agent 或智能客服中，可主动加入“提供解决步骤而非单纯安慰”的
  prompt 设计。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

动机：LLM 聊天机器人作为日常倾诉对象，因追求用户满意度而过度共情/肯定，可能强化错误信念并导致 AI 依赖。个体心理效应开始被研究，但多用户群体长期咨询 AI 的心理状态与关系演化难以在真实环境中观察。

方法关键点：构建虚拟教室多智能体仿真，20 个学生代理每天经历 morning、noon、after school、night 四个阶段，有压力时咨询朋友或心理辅导 AI（Gemini 2.5 Flash）。每个代理有五个状态变量：stress、happiness、self-reliance、AI dependence、sociability。咨询 AI 时通过系统提示设置六种响应风格：affirming、listening、solution-oriented、reality-redirecting、inciting、blaming。第二个 LLM 调用作为评估器，将每次咨询转换为参数更新，但不看风格提示。比较七种条件（含无 AI 对照），运行 15 天、50 天、降低咨询阈值等场景。

结果：solution-oriented 风格使 AI 依赖保持低水平，提升 self-reliance 并维持 happiness；affirming 和 inciting 风格显著增加 AI 依赖，inciting 还增加压力和缺课；listening 风格没有缓解累积压力。这些结果描述的是模拟系统，而非人类实测效果。论文给出代理动态完整规格，分析内在机制，并讨论 LLM 评估局限及验证步骤。
