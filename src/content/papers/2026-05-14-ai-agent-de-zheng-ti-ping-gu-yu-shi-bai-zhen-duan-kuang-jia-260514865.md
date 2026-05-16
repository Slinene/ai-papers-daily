---
title: Holistic Evaluation and Failure Diagnosis of AI Agents
title_zh: AI Agent 的整体评估与失败诊断框架
authors:
- Netta Madvil
- Gilad Dym
- Alon Mecilati
- Edo Dekel
- Jonatan Liberman
- Rotem Brazilay
- Liron Schliesser
- Max Svidlo
- Shai Nir
- Orel Shalom
affiliations:
- Deepchecks
arxiv_id: '2605.14865'
url: https://arxiv.org/abs/2605.14865
pdf_url: https://arxiv.org/pdf/2605.14865
published: '2026-05-14'
collected: '2026-05-16'
category: Eval
tags:
- Agent
- Evaluation
- Tracing
- Failure Diagnosis
- Span-level
- TRAIL benchmark
one_liner: 结合自顶向下与自底向上的跨度级评估，在 TRAIL 基准上实现最优错误定位与分类，证明评估方法论是瓶颈而非模型能力
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有 AI Agent 评估主要关注端到端任务的最终成功率，无法回答“在哪里失败、为什么失败”。流程级方法在长 trace 中难以可靠地将错误类型定位到具体 span，且统一 LLM 评判器（monolithic judge）受限于上下文窗口和“丢失中间”偏差。更细粒度的错误归因对 agent 的可信部署与迭代至关重要。

### 方法关键点
- **整体评估框架**：结合**自顶向下**（agent 级指标如规划效率、工具覆盖、工具滥用、完整性）和**自底向上**（span 级指标如指令遵循、推理完整性、工具完备性）两层分析。
- **跨度分解**：将评估拆解为独立的 per‑span 评判，每个 span 产生 pass/fail 判定、分类评分和自然语言依据，天然可扩展至任意长度 trace 且无上下文溢出。
- **分层传播**：叶子 span 判定向上汇聚，支持存在性、阈值、类型过滤等多种传播策略；错误定位给出从根到叶的完整因果链。
- **Top‑down 捕获跨度间模式**：仅在全 trace 视角下才能发现的冗余调用、计划偏离、覆盖不全等行为，由 agent 级指标捕获。
- **标签映射**：框架输出通用指标评分，经 LLM 映射器转换至 TRAIL 错误分类体系，保证与基准可比。

### 关键结果
- 在 **TRAIL 基准**（148 条 OpenTelemetry trace，841 个 span 级错误标注，含 GAIA 和 SWE‑bench 两数据集）上：
  - **加权类别 F1**：较最强基线提升 26%（GAIA）／38%（SWE‑bench）。
  - **定位准确率**：0.823（GAIA）／0.860（SWE‑bench），相对提升 1.25×／3.5×。
  - **联合准确率**：0.616（GAIA）／0.638（SWE‑bench），相对提升 2.58×／12.5×。
- 同类模型（GPT‑5.4）在框架内定位准确率是统一评判器的 **2.8×（GAIA）至 12×（SWE‑bench）**，说明评估方法论才是瓶颈。
- 随 trace 变长，其他所有方法的定位准确率急剧下降或失败，而本框架保持稳定，且无任何 trace 因长度被排除。

### 最值得记住的一句话
**评估方法论而非模型能力才是 agent 失败诊断的瓶颈——同一 frontier 模型在跨度分解框架中的定位准确率可高达单次全 trace 评判的 12 倍。**
