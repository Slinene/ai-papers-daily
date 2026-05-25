---
title: 'LLM-driven design of physics-constrained constitutive models: two agents are
  better than one'
title_zh: LLM驱动的物理约束本构模型生成：双智能体优于单智能体
authors:
- Marius Tacke
- Matthias Busch
- Kian Abdolazizi
- Jonas Eichinger
- Kevin Linka
- Roland Aydin
- Christian Cyron
affiliations:
- Helmholtz-Zentrum Hereon
- Hamburg University of Technology
- RWTH Aachen University
- Saarland University
- German Center for Artificial Intelligence
arxiv_id: '2605.23754'
url: https://arxiv.org/abs/2605.23754
pdf_url: https://arxiv.org/pdf/2605.23754
published: '2026-05-22'
collected: '2026-05-25'
category: MultiAgent
direction: 多智能体协作与物理约束审计
tags:
- Multi-agent
- LLM
- Physics-informed
- Constitutive modeling
- Automated model discovery
one_liner: Creator生成模型，Inspector审计物理约束，将LLM生成的本构模型物理合规率提升至100%且保持高精度。
practical_value: '- **生成-审计分离架构**：可复用到推荐策略或Agent输出的质量控制中，由独立审计Agent校验业务规则、合规性或公平性约束，提高系统可靠性。

  - **迭代细化闭环**：Inspector反馈不满足的约束，Creator重新生成直至通过，这种 refine-till-valid 模式可用于自动优化推荐文案、搜索策略或模型配置，确保输出始终满足预设标准。

  - **约束清单化**：将物理约束显式转化为检查列表，类似地，业务约束（多样性、利润底线、合规要求）可编码为审计规则，让LLM或专家系统自动验证生成结果。

  - **LLM驱动的自动化建模**：利用LLM生成模型代码并通过多Agent保证质量，可借鉴到AutoML或无代码平台，提升模型开发效率与可靠性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：单智能体LLM直接生成材料本构模型时缺乏物理合规性检查，导致模型可能违反热力学等定律，难以实际应用。  
**方法**：提出首个多智能体LLM本构建模框架，包含Creator（生成模型）和Inspector（审计9项物理约束）两个Agent。Creator根据数据生成代码，Inspector自动测试约束，若失败则反馈给Creator迭代优化，最多循环5次。框架与模型无关，测试了Claude Opus与Kimi两种LLM。  
**结果**：在脑组织、实验橡胶等数据集上，Inspector将Opus的物理合规率从91%提升至100%，Kimi从37%提升至56%，且预测精度与单次生成接近，并展现出强大的外延能力。双Agent生成的模型满足物理约束、高精度、可泛化，可直接用于工程实践。
