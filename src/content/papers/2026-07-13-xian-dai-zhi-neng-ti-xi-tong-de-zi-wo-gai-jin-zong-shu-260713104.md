---
title: 'Self-Improvements in Modern Agentic Systems: A Survey'
title_zh: 现代智能体系统的自我改进综述
authors:
- Zhe Ren
- Yimeng Chen
- Dandan Guo
- Guowei Rong
- Tonghui Li
- R. B. Xiong
- Qingfeng Lan
- Wenyi Wang
- Li Nanbo
- Yibo Yang
affiliations:
- Jilin University
- King Abdullah University of Science and Technology
- Independent Researcher
- University of Alberta
- The Swiss AI Lab IDSIA/USI/SUPSI
arxiv_id: '2607.13104'
url: https://arxiv.org/abs/2607.13104
pdf_url: https://arxiv.org/pdf/2607.13104
published: '2026-07-13'
collected: '2026-07-17'
category: Agent
direction: Agent 自我改进的系统化综述
tags:
- self-improving agents
- foundation model
- scaffolding
- survey
- LLM agents
one_liner: 提出系统级框架，将自改进Agent形式化为对模型参数或脚手架的自诱导更新，并整理论坛。
practical_value: '- **在线持续优化推荐策略**：在电商推荐中，可借鉴自改进闭环，利用用户交互反馈（点击、转化）自动更新模型参数或提示，实现推荐效果的持续提升，减少人工干预。

  - **动态工具与策略脚手架**：类似文中的 Scaffolding Improvement，可将推荐系统的召回、排序、过滤等组件视为可动态调整的“工具”，根据实时效果自动调整路由或组合策略，例如动态选择推荐模型、调整混排规则。

  - **利用弱反馈信号驱动自适应**：论文中总结了多种反馈信号（标量、定性、群体等），实际业务中可利用隐式反馈（停留时长、滑动行为）甚至用户投诉作为改进信号，通过生成-验证-修正循环提升推荐质量。

  - **Agent 形式的推荐生成**：若采用生成式推荐（GenRec），可将推荐生成视为一个自改进 Agent，通过自我反思和多轮交互优化最终推荐结果，特别适用于对话式推荐或搜索结果排序。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现代自主智能体正从研究原型走向部署，核心需求是可控的自我进化——从经验中持续提升能力，最小化人工干预。本综述旨在提供一个系统化框架，梳理现有自改进 Agent 方法。

**方法关键点**：
- **系统级框架**：将现代 Agent 视为基础模型（FM）与操作脚手架（提示、记忆、工具、控制逻辑）的耦合。自改进被定义为自诱导更新算子，可选择性地更新模型参数 θ 或脚手架组件 Σ。
- **两大改进路径**：① **基础模型改进**：利用内在生成的演示、评估反馈或外在探索经验，通过 SFT/RL 更新模型参数；② **脚手架改进**：不改变模型参数，而是非参数地优化提示、工具路由、记忆结构或控制逻辑，例如通过迭代提示优化、动态工具路由、自主工具创建等。
- **驱动信号**：总结了标量反馈、定性反馈、群体反馈等多种信号来源，以及生成策略、数据格式、应用域。
- **应用与评估**：覆盖软件工程、网页导航、游戏、科学发现、具身智能等，讨论了评估标准与开放性挑战。

**关键结果**：作为综述，无实证数字，但通过系统梳理，呈现了自改进 Agent 的完整图景，并指出了未来方向，如整合模型与脚手架改进、世界模型辅助、安全性等。
