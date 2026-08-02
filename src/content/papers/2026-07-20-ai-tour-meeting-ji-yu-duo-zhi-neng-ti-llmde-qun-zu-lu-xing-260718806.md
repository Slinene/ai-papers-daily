---
title: 'AI Tour Meeting: Group Travel Planning by LLM Agents'
title_zh: AI Tour Meeting：基于多智能体LLM的群组旅行规划框架
authors:
- Daisuke Kikuta
affiliations:
- NTT, Inc.
arxiv_id: '2607.18806'
url: https://arxiv.org/abs/2607.18806
pdf_url: https://arxiv.org/pdf/2607.18806
published: '2026-07-20'
collected: '2026-08-02'
category: MultiAgent
direction: 多智体协作模拟群组决策
tags:
- LLM Agents
- Multi-Agent Simulation
- Group Decision Making
- Persona-based Discussion
- Travel Planning
one_liner: 用多个具有不同人格的LLM Agent通过对话协商制定满足群组约束的行程，提供模拟与分析平台
practical_value: '- **群组推荐评估**：可用来模拟多个用户角色对推荐列表的协商与反馈，低成本测试群组推荐算法的满意度，尤其在电商的家庭出游保险、团队外卖点餐等场景。

  - **多Agent协商流程设计**：框架中的讨论工作流配置（轮次、发言顺序、决策规则）可直接复用到需要多方达成共识的电商Agent场景，例如智能客服中的多利益方协商（买家、卖家、平台）。

  - **用户模拟与画像注入**：通过定义不同人格的Agent（预算敏感型、景点偏好型等）来生成多样化的行为数据，可用于增强推荐模型的离线评估，或为强化学习环境生成模拟用户。

  - **监控与调试工具**：内置的对话记录、状态追踪和LLM部署接口，为多Agent系统的可观测性和快速实验提供了工程样板，可借鉴用于内部多智能体推荐编排的调试。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：群组旅行规划需平衡不同参与者的成本、时间、偏好等多目标，传统基于人的研究方法成本高且难以规模化。利用LLM Agents模拟用户参与讨论，可降低大规模行为分析成本，并可用于评估现有群组推荐系统。

**方法**：提出AI Tour Meeting框架，核心是多个基于LLM的Agent，每个Agent被赋予独特的人格（如预算限制、兴趣点）和约束。Agent通过多轮自然语言对话协商行程，框架提供配置代理角色、讨论工作流（发言顺序、达成共识规则）、过程监控以及LLM后端（如GPT-4）的统一接口。主要作为模拟工具，并无强制推荐算法，而是观察Agent在给定对话机制下如何收敛到满足群组约束的行程。

**关键结果**：系统验证确认框架能正确生成符合多人约束的行程。分析表明不同LLM模型和讨论轮次设置会显著影响最终行程的平衡性与时间效率，例如增加讨论轮次可提升行程对多数人偏好的满足度，但可能牺牲个别代理的极端约束。工具已开源供研究使用。
