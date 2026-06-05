---
title: 'EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and
  Context Management'
title_zh: EvoDS：自我进化的自主数据科学智能体，具备技能学习与上下文管理
authors:
- Zherui Yang
- Fan Liu
- Yansong Ning
- Hao Liu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2606.03841'
url: https://arxiv.org/abs/2606.03841
pdf_url: https://arxiv.org/pdf/2606.03841
published: '2026-06-01'
collected: '2026-06-05'
category: MultiAgent
direction: 多智体自主技能学习与上下文管理
tags:
- self-evolving agent
- skill learning
- context compression
- multi-agent reinforcement learning
- data science agent
one_liner: 通过自主技能获取与自适应上下文压缩，让数据科学智能体自我进化，性能平均提升28.9%并消除token超限。
practical_value: '- **技能复用机制**：将常见数据处理流程封装为可重用技能（如特征工程、模型选择），类似在电商推荐Agent中，可将用户画像更新、召回策略切换等操作封装成技能，由Agent自主调用和组合，减少重复LLM调用。

  - **自适应上下文压缩**：把长上下文管理建模为强化学习控制问题，而非固定截断。在推荐系统Agent的多轮用户交互或长链路任务中，可学习保留与当前假设最相关的历史信息，避免上下文窗口溢出和关键信息丢失。

  - **两阶段多智体训练**：先用监督微调初始化任务执行能力，再通过基于结果的强化学习（如成功奖励）优化技能选择与上下文压缩策略。该方法可直接迁移到电商多智体系统（如买家助手+卖家分析协同）的训练，让智体在与环境交互中自我改进。

  - **工具选择层次化**：引入高层策划器（Planner）与低层执行器（Executor）的解耦设计，降低工具选择错误。电商场景中可分离“意图理解与方案制定”和“具体API调用”，提升复杂推荐流程的鲁棒性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有数据科学智能体（如MLAgentBench）受限于固定的动作空间和简单的上下文截断，无法跨任务积累可重用经验，长链路任务中易因上下文膨胀而失败。

**方法**：EvoDS提出两大核心机制——自主技能获取（ASA）与自适应上下文压缩（ACC）。ASA让智能体在任务中自动合成、验证并存储可执行技能（如数据清洗、模型调参），形成可复用技能库；ACC将上下文管理视为学习控制问题，通过策略决定保留或压缩哪些历史信息，而非被动截断。整体采用两阶段多智能体训练：第一阶段用监督微调赋予智体基础任务执行能力；第二阶段以任务成功率为奖励，通过强化学习联合优化技能选择与上下文压缩，使智体自我进化。理论上，EvoDS的层次化设计降低了工具选择错误率，并满足信息瓶颈原则。

**结果**：在四个数据科学基准（MLAgentBench、DSBench等）上，EvoDS平均性能超越最佳开源智能体28.9%，且完全消除因token超限导致的失败。消融实验验证了ASA和ACC各自的贡献，技能复用缩短了任务解决时间。
