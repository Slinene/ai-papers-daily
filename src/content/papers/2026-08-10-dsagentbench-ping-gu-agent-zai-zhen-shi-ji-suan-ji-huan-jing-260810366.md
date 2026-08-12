---
title: 'DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real
  Computer Environments?'
title_zh: DSAgentBench：评估 Agent 在真实计算机环境中自动执行端到端数据科学工作流的能力
authors:
- Mizanur Rahman
- Mohammed Saidul Islam
- Ridwan Mahbub
- Md Tahmid Rahman Laskar
- Shafiq Joty
- Enamul Hoque Prince
affiliations:
- York University
- Nanyang Technological University
- Salesforce AI Research
arxiv_id: '2608.10366'
url: https://arxiv.org/abs/2608.10366
pdf_url: https://arxiv.org/pdf/2608.10366
published: '2026-08-10'
collected: '2026-08-12'
category: Agent
direction: Agent 能力评估与基准构建
tags:
- Agent
- Benchmark
- Data Science
- End-to-end
- Real-OS
- Multi-step Reasoning
one_liner: 首个在真实 OS 中评估 agent 完成全流程数据科学任务的基准，揭示当前模型巨大能力鸿沟
practical_value: '- 为电商推荐场景中自动化数据分析（清洗、特征工程、模型评估）的 Agent 提供评估框架，可借鉴其任务设计和评测方法。

  - 强调真实 OS 环境下的多工具协同（终端、浏览器、数据库），提示业务 Agent 需要具备文件系统操作、数据库连接等底层能力，而非仅代码生成。

  - 确定性 evaluator 不仅检查代码执行，还验证分析结果正确性、可视化和模型性能，该思路可直接用于业务 Agent 的效果验收。

  - 当前开源 Agent 成功率几乎为 0，闭源最高仅 56.7%，说明复杂长链路自动化仍不成熟，现阶段业务中应谨慎引入端到端全自动 Agent，更适合人机协同模式。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：真实数据科学工作流涉及数据清洗、探索、建模、可视化和验证的长时间多阶段过程，需要跨笔记本、终端、浏览器、数据库等工具协调，但现有基准缺乏真实计算机交互，无法评估 agent 端到端完成此类任务的能力。

**方法**：构建 DSAGENTBENCH，包含 275 个多样化任务，完整覆盖数据科学生命周期，每个任务要求 agent 在真实 OS 环境中基于中间输出做出决策并协同使用多种工具。评估器采用确定性规则，不仅验证代码执行，还检查分析准确性、可视化 outputs 和模型性能。实验测试了 15 个闭源与开源模型。

**关键结果**：最强模型 Claude-4.6-Sonnet 成功率仅 56.70%，所有开源 agents 均低于 1%；主要失败模式包括工具编排错误、OS 环境理解不足和多步推理断裂。这表明当前 agent 与真实数据科学实践间存在显著能力缺口。
