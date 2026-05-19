---
title: Scalable Environments Drive Generalizable Agents
title_zh: 可扩展环境驱动可泛化智能体
authors:
- Jiayi Zhang
- Fanqi Kong
- Guibin Zhang
- Maojia Song
- Zhaoyang Yu
- Jianhao Ruan
- Jinyu Xiang
- Bang Liu
- Chenglin Wu
- Yuyu Luo
affiliations:
- HKUST(GZ)
- DeepWisdom
- PKU
- NUS
- SUTD
- UdeM & Mila
arxiv_id: '2605.18181'
url: https://arxiv.org/abs/2605.18181
pdf_url: https://arxiv.org/pdf/2605.18181
published: '2026-05-18'
collected: '2026-05-19'
category: Agent
direction: 环境扩展与跨环境泛化
tags:
- Environment Scaling
- Agent Generalization
- Programmatic Generators
- World Models
- Cross-Environment Adaptation
- Taxonomy
one_liner: 区分轨迹、任务、环境三类扩展，提出程序化生成与生成式世界模型两种环境扩展范式，量化跨环境适应
practical_value: '- 明确区分轨迹、任务、环境三类扩展，在构建评测或训练管线时可据此定位瓶颈：若只需提升固定规则下的能力，用任务扩展；若要训练跨规则适应，必须做环境扩展。

  - 程序化环境生成器（如 EnvScaler、AutoEnv）通过参数化规则集，提供可复现、可验证的环境，适合为电商搜索、推荐对话等场景构建可控的 Agent
  压力测试套件。

  - 生成式世界模型（如 Genie 3）可与程序化规则支架结合，在保持交互规则可控的同时注入语义多样性，丰富训练分布。

  - 部署时，即使环境固定，也可利用局部环境扰动（ploc）生成邻域变体（修改布局、实体、观察等），使 Agent 训练更鲁棒，减少上线后的 brittle failure。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
当前智能体训练主要依赖固定规则集下的轨迹或任务扩展，导致智能体在面对接口、动态、观察或反馈信号变化时表现脆弱。本文认为，**真正的泛化需要环境扩展**——系统性地生成具有不同可执行规则集的世界，而非仅在同一世界内增加数据。

## 方法关键点
1. **统一分类体系**：将扩展实践分为三类——轨迹扩展（增加交互痕迹）、任务扩展（扩大目标分布）、环境扩展（生成新规则集），并通过主要产出物和规则集变更程度进行区分。
2. **环境扩展范式**：
   - **程序化生成器**：用代码定义规则支架（¯E）并嵌入语义内容（c），实现可控制、可验证的环境扩张，支持模块化扰动和复杂度度量。
   - **生成式世界模型**：从自然语言提示直接生成可交互世界，依靠学习到的动态模型提供高覆盖度和开放性，但需额外验证机制。
3. **跨环境学习目标**：将智能体训练表述为在环境分布上的期望回报最大化，并强调通过内部状态更新（L）来降低跨环境适应后悔值，衡量规则偏移不匹配度。
4. **评价准则**：提出可执行性、信号质量、覆盖度、复杂度（行为指标如解路径长度、分支因子）和效率五维评估体系。

## 关键结果
本文为立场性论文，未开展新实验。附录中总结了现有代表性环境扩展套件的统计指标（LoC、动作空间、信号类型等），用以示范评价框架。文章的核心结论是：**环境应被视为同等重要的“一等工件”进行扩展、验证和度量**，而非仅是训练数据的附属品。
