---
title: 'AutoTrainess: Teaching Language Models to Improve Language Models Autonomously'
title_zh: AutoTrainess：通过训练专用接口实现语言模型自主后训练
authors:
- Zhaojian Yu
- Penghao Yin
- Shuzheng Gao
- Shilin He
- Kai Cai
- Xiao-Ping Zhang
affiliations:
- Tsinghua University
- The Chinese University of Hong Kong
- Simple Agent Lab
arxiv_id: '2606.31551'
url: https://arxiv.org/abs/2606.31551
pdf_url: https://arxiv.org/pdf/2606.31551
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: Agent 自动化模型训练流程
tags:
- Agent-Computer Interface
- Post-Training
- Autonomous Training
- LLM Agent
- Benchmark
one_liner: 提出训练专用智能体-计算机接口（AutoTrainHub），将人类后训练经验编码为工作流，使LLM agent在PostTrainBench上显著超越CLI-only基线
practical_value: '- 在自动化模型迭代任务中，将人类最佳实践抽象为固定接口（数据选择、清洗、格式验证），可大幅降低agent在训练pipeline中的失败率，尤其适合需持续优化的推荐模型再训练。

  - 采用分阶段工作流（诊断→基础对齐→困难样本增强）引导agent逐步优化，避免过早陷入局部改进，可迁移至推荐系统的特征工程或数据诊断自动化。

  - 通过结构化实验日志保留长期记忆，使agent在多轮迭代中保持连贯决策，对需要长期A/B测试和增量学习的搜推广系统有参考价值。

  - 使用受约束的动作空间（固定训练框架、评估脚本）确保可复现性，这一设计原则可应用于搭建可靠的自动化模型上线与监控流程。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：即使前沿LLM agent已能完成复杂软件工程任务，后训练流程仍高度依赖人工。核心挑战在于训练不只是写代码，还需反复规划迭代、构建与基准对齐的数据、运行稳定的训练、评估检查点并在数小时内维护实验状态。现有agent在无约束的CLI环境中容易引入数据格式错误、模板错配等低级问题，导致训练失败。因此，将人类积累的训练经验显式化为可复用的计算机接口，是提升agent自主训练效率的关键。

**方法关键点**：
- **AutoTrainHub接口**：将自主训练分解为规划、数据处理、训练、评估和日志五个模块化技能，每个技能封装了人类专家的约束与最佳实践。
- **数据处理三阶段**：强制agent执行数据选择、构建、验证，要求数据格式与基准评估接口严格对齐，验证不通过则回退修正，有效减少训练时的输入错误。
- **训练标准化**：固定使用LlamaFactory后端，要求全参数微调与小规模预验证，禁止随意切换框架，保证实验可复现。
- **评估驱动诊断**：用基准官方脚本运行评估，自动提取15个案例并总结失败模式（数据/训练/模板），为下一轮规划提供结构化证据。
- **持久化日志与规划**：每轮迭代记录完整上下文，形成跨迭代的长时记忆；规划接口需基于前序证据明确目标、干预和成功标准，维持探索的连贯性。

**关键结果**：在PostTrainBench上，GPT-5.4 (Codex) 驱动的AutoTrainess取得26.94的平均分数，相对于CLI-only基线（23.21）提升3.73分（+16.1%）。消融实验证实各模块独立贡献：移除数据处理使训练动作失败率上升5.5个百分点，移除评估使评估失败率飙升15.2个百分点；完整的接口在探索数（111次训练到评估的交接）和保留提升（7个）上均最优。行为分析揭示agent的迭代模式：早期对齐基准格式，中期转向数据合成与困难样本构造，后期聚焦剩余失败案例，且偏好从最优检查点继续训练而非重训。

**一句话**：将人类训练经验编码为显式的Agent-Computer Interface，能大幅提升自主后训练在有限时间内的探索有效性与迭代稳定性。
