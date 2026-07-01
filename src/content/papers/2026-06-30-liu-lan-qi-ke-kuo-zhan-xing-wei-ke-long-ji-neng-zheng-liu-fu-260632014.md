---
title: Scalable Behaviour Cloning on Browser Using via Skill Distillation
title_zh: 浏览器可扩展行为克隆：技能蒸馏复用用户轨迹
authors:
- Kaisen Yang
- Zheng Jiang
- Yuzhao Peng
- Houde Qian
- Boshi Zhang
- Youjie Zheng
- Shijin Hong
- Qingle Liu
- Ruoyu Han
- Bohan Lyu
arxiv_id: '2606.32014'
url: https://arxiv.org/abs/2606.32014
pdf_url: https://arxiv.org/pdf/2606.32014
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: 智能体 · 技能蒸馏与行为克隆
tags:
- Behavior Cloning
- Skill Distillation
- Browser Agent
- Natural Language Skills
- Skill Graph
one_liner: 将用户浏览器交互轨迹蒸馏为自然语言技能并组织成技能图，让Agent直接复用决策先验
practical_value: '- 从用户搜索/点击日志中蒸馏出紧凑的自然语言意图模板，供推荐或导购Agent直接检索复用，避免重复学习底层操作。

  - 构建意图技能图谱，合并相似技能控制规模膨胀，可迁移到电商Query推荐中的意图归类或标签系统去冗余。

  - 将行为克隆焦点从低层动作序列提升到高层决策先验，用于自动化运营Agent的策略初始化，减少冷启动探索。

  - 利用互联网用户集体行为提炼常见任务流程（如比价、下单），作为生成式推荐的上下文背景或对话策略分支。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：当前浏览器智能体在真实网页上效率低下，瓶颈并非解析与执行动作，而是信息不完全下的决策——人类浏览中隐含大量可复用的先验知识，但未被有效利用。

**方法**：提出**技能蒸馏（Skill Distillation）**，将用户交互轨迹转换为紧凑的自然语言技能描述，Agent可直接读取、检索与组合。为避免技能无限膨胀，进一步构建**技能图谱（Skill Graph）**，通过合并相似技能实现增长时有序合并，而非简单堆积。

**关键结果**：论文为一个框架性工作，未给出具体数值实验，但通过原型论证了浏览器智能体的可扩展性来源于互联网用户已表达的集体技能，而非仅靠手工设计任务，为从大规模用户轨迹中抽取行为克隆技能提供了新范式。
