---
title: 'Occamy-1.0: Open Pareto-frontier 35B Intelligence for Co-work'
title_zh: Occamy-1.0：面向协同工作的开源帕累托前沿35B智能模型
authors:
- Wenhui Chen
- Shiwen Cheng
- Hao Dong
- Chenda Duan
- Ruixiang Feng
- Zhong Guan
- Boqiang Guo
- Xueyuan Han
- Haojie Hao
- Liangmeng Huang
affiliations:
- Accio Team
arxiv_id: '2609.11977'
url: https://arxiv.org/abs/2609.11977
pdf_url: https://arxiv.org/pdf/2609.11977
published: '2026-09-03'
collected: '2026-09-15'
category: Agent
direction: 协同工作Agent模型后训练
tags:
- Agent
- Post-training
- Pareto frontier
- Tool use
- Co-work
- LLM
one_liner: 开源35B协同工作模型，通过执行接地数据和分阶段后训练实现成本效率帕累托最优
practical_value: '- **成本效率优先的模型选型**：在业务中构建Agent时，可采用低参数MoE架构（如35B-A3B）替代超大模型，在保持工具调用、编码等能力的同时显著降低单次调用成本，适合电商场景中大量并发的商品信息查询、订单处理等任务。

  - **执行接地数据构建**：借鉴其采集真实执行轨迹并重放的方法，在电商Agent训练中记录用户与Agent的完整交互序列（包括工具调用、状态变更、错误恢复），作为后训练数据，可提升模型在长流程任务中的状态跟踪与协调能力。

  - **分阶段后训练**：将能力拆分为信息收集、工具使用、编码、文件操作等模块，分阶段注入训练数据，逐步巩固，避免灾难性遗忘，适合在现有基座模型上迭代增强特定Agent技能。

  - **全流程成本评估**：在评估Agent模型时，除accuracy外，应统计整个episode的累计token成本与延迟，绘制成本-性能帕累托曲线，选择位于低拐点的模型部署，而非仅看单点benchmark分数。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：协同工作Agent执行复杂工作流时，成本与延迟在完整episode中累积，实际价值取决于能力与效率的综合表现。日常工作步骤更强调状态跟踪、协调、恢复和后续执行，而非前沿推理，因此需要成本高效的专用模型。

**方法关键点**：基于Qwen3.6-35B-A3B后训练，构建执行接地数据和环境，捕获可重放的长时程轨迹，通过分阶段后训练逐步开发和巩固互补执行能力。

**关键结果**：在多个协同工作基准上，Occamy-1.0在同等规模模型中保持最强，并与更大前沿系统竞争。例如Claw-Eval Average得69.50（GPT-5.6 Sol为82.20），Terminal-Bench 2.1得1004（GPT-5.6 Sol为1128），CommerceAgentBench成本$44,751（GPT-5.6 Sol为$79,868），在成本-性能帕累托前沿中处于低拐点。工具调用、编码和指令遵循评估显示保留了广泛Agentic能力。模型权重和部分训练数据已开源。
