---
title: Task-Efficient Agent Evaluation Using Cached Traces
title_zh: 基于缓存轨迹的任务高效 Agent 评估
authors:
- Ben Johnson
- Hayden Helm
affiliations:
- Jataware
- Helivan
arxiv_id: '2611.06803'
url: https://arxiv.org/abs/2611.06803
pdf_url: https://arxiv.org/pdf/2611.06803
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: Agent 高效评估 · 轨迹摘要表示
tags:
- Agent Evaluation
- Trace Embedding
- Item Response Model
- LLM Summarization
- Efficient Benchmarking
one_liner: 利用 LLM 摘要与嵌入构建轨迹表示，结合几何预测和 IRT 模型，仅需少量任务即可精准估计 Agent 基准分数
practical_value: '- 对电商导购 Agent、客服 Agent、推荐理由生成等系统做全量 benchmark 成本高，可缓存历史 trace，用
  LLM 提取结构化摘要并嵌入，结合 IRT 几何预测，用 1 个随机任务即可估计全量表现，误差可降低 30%~40%。

  - 设计 trace 摘要时需强制剥离系统身份、模型家族、harness 等无关信号，只保留任务步骤、错误类型、最终正确性等任务相关字段，否则嵌入会被系统特定模式污染，失去跨系统泛化能力。

  - 在模型灰度或 A/B 测试阶段，可用少量线上/离线任务对新模型打分，通过其相对于历史参考系统的几何位置做早期筛选，避免昂贵的全量评测。

  - 若团队已积累多个模型版本在同一评测集上的结果，可直接复用该框架构建低维系统空间，对新加入的系统用几何插值预测，省去重新训练评分模型。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：Agent 评测极其昂贵，单个任务执行需消耗数十万 token 和沙箱环境，完整 benchmark 成本可超 $2000。现有高效评测方法只用二值正确性，忽略了执行 trace 中的丰富信号。

**方法关键点**：
- 对每个参考系统在每项任务上的 trace，用 LLM 提取结构化摘要，再用标准文本编码器嵌入，得到轨迹表示。该表示保留正确性和任务难度信息，同时最小化系统身份、模型家族、harness 等无关信号。
- 基于所有参考系统的轨迹表示，为每个系统构建低维表示，并用新系统在参考系统空间中的几何位置预测其得分。
- 将几何预测与 item-response model（IRT）结合，实现对仅执行少量任务的新系统的分数估计。

**关键结果**：
- SWE-bench Verified 上，仅提供单个随机执行任务时，MAE 从 0.13 降至 0.08（Wilcoxon p<10⁻⁴）。
- Terminal-Bench 2.0 上，MAE 从 0.14 降至 0.12（Wilcoxon p<10⁻³）。
- 当能访问完整参考系统集时，在任意给定执行任务数下均显著优于基线。
