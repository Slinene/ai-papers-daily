---
title: 'UniSteer: Text-Guided Flow Matching in Activation Space for Versatile LLM
  Steering'
title_zh: UniSteer：文本引导的激活空间流匹配实现通用LLM控制
authors:
- Yingdong Shi
- Ruiming Zhang
- Changming Li
- Zhiyu Yang
- Kaixing Zhang
- Jingyi Yu
- Kan Ren
affiliations:
- ShanghaiTech University
arxiv_id: '2605.30076'
url: https://arxiv.org/abs/2605.30076
pdf_url: https://arxiv.org/pdf/2605.30076
published: '2026-05-27'
collected: '2026-05-30'
category: LLM
direction: LLM激活导向控制
tags:
- Flow Matching
- Activation Steering
- LLM
- Text-Guided
- Conditional Generation
one_liner: 用文本条件统一控制LLM行为的激活流匹配框架，支持细粒度概念和多约束组合。
practical_value: '- **Agent 行为风格控制**：在电商多智能体对话系统中，可利用 UniSteer 的文本条件流匹配对单个 Agent 的回复风格（如亲切客服、专业导购）进行细粒度激活干预，而无需微调模型。

  - **推荐理由多样性生成**：将“个性化”“幽默”“极简”等文本条件注入激活空间，可引导 LLM 在生成推荐理由时呈现不同风格，提升内容吸引力，无需为每种风格训练独立控制模块。

  - **多约束指令遵循**：当业务需要同时满足合规性、品牌调性、敏感词规避等多个约束时，UniSteer 的组合式条件能力可一次性应用多条文本规则，比顺序推理或多次干预更高效。

  - **激活空间分类用于质量筛选**：利用重构能量进行分类的方式，可作为轻量级线上过滤器，对 LLM 生成的候选文案或对话回复进行快速一致性或真实度评分，降低人工审核成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 激活控制方法依赖固定方向或任务特定模块，难以泛化到细粒度概念和组合约束。

**方法**：UniSteer 学习一个通用的条件速度场，通过流匹配建模从自然语言条件到残差流激活的条件分布。推理时执行流反演：将源激活部分传输至隐状态，在目标文本条件下再生激活，再注入冻结的 LLM。同一模型还支持基于最低重构能量的激活空间分类。

**关键结果**：在三个不同规模的 LLM 上，UniSteer 统一实现了行为控制、真实性引导、细粒度概念控制、多约束指令遵循和激活空间分类五项任务，无需为每种行为单独设计干预模块。
