---
title: 'Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human
  Design'
title_zh: 代理系统中的协同进化：走向超越人类设计的自引导进化
authors:
- Qing Zong
- Jiayu Liu
- Junhao Shen
- Zecong Tang
- Linsi Wu
- Yuxuan Liu
- Rui Wang
- Zhaowei Wang
- Weiqi Wang
- Cheng Qian
affiliations:
- Hong Kong University of Science and Technology
- University of Illinois Urbana-Champaign
- The Chinese University of Hong Kong
- The University of Hong Kong
- Peking University
arxiv_id: '2608.10299'
url: https://arxiv.org/abs/2608.10299
pdf_url: https://arxiv.org/pdf/2608.10299
published: '2026-08-09'
collected: '2026-08-12'
category: MultiAgent
direction: 多智能体协同进化框架与分类
tags:
- Agentic Systems
- Co-Evolution
- Multi-Agent
- Self-Evolution
- Taxonomy
- Survey
one_liner: 提出三阶段分类法，梳理多智能体与环境协同进化逐步摆脱人工设计约束的研究
practical_value: '- 设计多智能体推荐系统时，可借鉴 Agent-Agent 协同进化中的对抗、协作与组织适应机制，使各策略 agent 在动态博弈中自动优化分工与交互协议，而非依赖人工静态编排。

  - Agent-Environment 协同进化的思想可用于构建自适应的搜索推荐框架：将用户反馈、上下文环境作为演化压力，在线调整召回、排序、重排模块的参数或模型结构，应对数据分布漂移。

  - 元协同进化为“可演化的 Agent 架构”提供思路，例如在电商 chatbot 或 query 生成 agent 中，使 prompt 模板、工具选择逻辑甚至内部思维链结构具备自我调优能力，减少人工迭代成本。

  - 该综述强调的安全与可控性挑战，提醒我们在实际部署自动演化系统时需设计监控、回滚与约束机制，防止 agent 策略在长期演化中偏离业务目标。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有单智能体自进化受限于固定的任务、反馈与环境，难以突破设计上限。该综述系统梳理了多组件协同进化的前沿工作，旨在构建能够逐步摆脱人类静态设计的开放式代理系统。

**方法**：提出三阶段渐进分类法：
- **Agent-Agent 协同进化**：多智能体通过动态同伴施加适应压力，涵盖对抗（如博弈论框架）、协作（角色分配与通信拓扑自适应）与组织（层级结构自发涌现）三类范式。
- **Agent-Environment 协同进化**：环境不再固定，任务、反馈与交互空间随 agent 行为共同演化，形成双向塑造闭环。
- **元协同进化**：进化机制本身（如损失函数、搜索算子、评估准则）也可演化，使系统具备自指升级能力。

**关键发现**：综述覆盖大量近期论文，分析了各阶段代表性工作在性能突破与局限性，并指出评估基准缺失、多组件扩展时的复杂性爆炸、自主演化的安全可控性三大开放挑战，为后续研究提供统一参照。
