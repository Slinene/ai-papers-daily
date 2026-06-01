---
title: 'LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis'
title_zh: LongDS-Bench：长程智能体数据分析评测基准
authors:
- Kewei Xu
- Xiaoben Lu
- Shuofei Qiao
- Zihan Ding
- Haoming Xu
- Lei Liang
- Ningyu Zhang
affiliations:
- Zhejiang University
- Ant Group
- Zhejiang University - Ant Group Joint Laboratory of Knowledge Graph
arxiv_id: '2605.30434'
url: https://arxiv.org/abs/2605.30434
pdf_url: https://arxiv.org/pdf/2605.30434
published: '2026-05-27'
collected: '2026-06-01'
category: Eval
direction: 长时程智能体数据分析评测
tags:
- long-horizon
- data analysis
- agent benchmark
- state tracking
- LLM agents
one_liner: 长时程数据分析任务中揭示状态维护（而非交互步数）是智能体核心瓶颈的评测基准
practical_value: '- 电商智能体长会话建模：借鉴 LongDS 的状态演化任务设计（回滚、反事实扰动），评估和优化多轮会话中的状态长期记忆与追索能力。

  - 状态维持优先：实验表明增加额外步骤不必然提升准确率，提示在工程实现中应优先投资显式状态管理（结构化缓存、中间结果索引）而非盲目提高交互预算。

  - 错误恢复机制：长程错误占比 52-69%，可在智能体 pipeline 中引入检查点备份与状态回滚策略，提升长任务鲁棒性。

  - 推荐 Agent 评测：对于多轮对话推荐或自动化分析 Agent，可参考依赖跨度指标和状态组合模式，构建更贴近真实长期交互的离线评测。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 智能体数据分析评测多为孤立短任务，无法反映真实场景中多轮次、状态持续演化的长程分析需求。  
**方法**：构建 LongDS 基准，包含 68 个来自 Kaggle 真实项目的长程任务，共 2,225 个交互回合，覆盖地球科学、商业、教育等六领域。任务设计围绕状态演化模式：反事实扰动、回滚、多状态组合等，平均依赖跨度 11.3 轮，要求智能体在多轮中维持、更新、恢复并组合分析状态。  
**结果**：评估五个先进模型，最高平均准确率仅 48.45%，从初期到后期回合准确率下降近 47 个百分点，长程错误占整体失败的 52%–69%。进一步分析表明，增加额外交互步数并不一定提升性能，核心瓶颈在于维护正确的分析状态，而非提升交互预算。
