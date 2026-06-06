---
title: Benchmark Everything Everywhere All at Once
title_zh: 全自主代理系统按需构建多模态评测基准
authors:
- Shiyun Xiong
- Dongming Wu
- Peiwen Sun
- Yuang Ai
- Bokang Yang
- Wencheng Han
- Xiao-Hui Li
- Xiangyu Yue
affiliations:
- The Chinese University of Hong Kong
- The Chinese University of Hong Kong, Shenzhen
- Shandong University
- Huawei Technologies
- Shenzhen Loop Area Institute
arxiv_id: '2606.06462'
url: https://arxiv.org/abs/2606.06462
pdf_url: https://arxiv.org/pdf/2606.06462
published: '2026-06-03'
collected: '2026-06-06'
category: Agent
direction: Agent 系统自主构建评测基准
tags:
- Benchmark Agent
- Autonomous Benchmarking
- LLM Evaluation
- Multi-Agent System
- Data Synthesis
one_liner: 首个全自主代理系统，将评测基准构建从人力驱动转变为自动规划、执行与刷新的可定制化流程
practical_value: '- **长周期任务的分层规划**：Benchmark Planner（设计-接地-分配）与 Executor（样本规划-执行-校验）的解耦设计，直接适用于电商
  Agent 中的多步推荐流程编排，例如将“生成个性化推荐理由”拆解为子任务并分配数据源与转换工具。

  - **闭环质量保障机制**：Verification 与配额补充（Verification-guided replenishment）可迁移到自动标注 pipeline，对生成式推荐的样本实施语义校验、格式合规检查，不合格样本回炉重造，保证产出质量。

  - **用户意图到任务规格的自动转化**：Design Agent 将模糊需求分解为结构化 subtask 的思路，可用于根据运营目标（如提升点击率）自动生成
  A/B 测试的评估方案或推荐模型评测集。

  - **低成本持续刷新能力**：Benchmark Agent 的快速迭代特性（人类标注 5-6 min/样本 vs. Agent 0.2-0.3 min）提示，电商推荐中的离线评估集可以随模型升级和业务变化自动更新，维持区分度，避免饱和。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有 LLM/MLLM 评测基准依赖大量人力设计、标注与偏好对齐，构建周期长、难以复用，且发布后模型性能迅速饱和（如 Qwen 系列在多个基准上数月内突破 80%），导致区分度不足。为应对可扩展性与可持续性挑战，需一种能根据用户需求自动化生成及动态更新基准的方法。

**方法关键点**：
- 提出 **Benchmark Agent**，首个全自主代理框架，将基准构建转化为可控的自动化流程。
- 采用 **脑–小脑分层架构**：**Benchmark Planner**（高层决策）将用户评价需求分解为 subtask 集，通过 Design Agent（提议/修订/丢弃）、Grounding Agent（数据集搜索与变换合规性校验）、Allocation Agent（配额与资源可行性闭环分配）生成可行的基准规格。
- **Benchmark Executor**（操作执行）对每个 subtask 进行样本级规划，调用工具（OCR、TTS、图像处理、网络搜索等）执行变换，并通过验证与配额补充确保质量合标。
- 系统可兼容多种 LLM 骨干，产出的基准覆盖文本、音频、图像、全模态理解及领域推理。

**关键实验与结果**：
- 基于 GPT-5.1 及 General-Bench 数据集池，按 15 个代表性的用户需求自动构建基准，涵盖多视角文本、多语种音频、医疗影像推理等。
- 人工评估：样本接受率达 **96–98%**；LLM-as-Judge 评估：用户意图对齐（UIA）得分 **68.54–81.48**，格式与问题答案一致性较高。
- 一致性检验：同一模型家族的性能随规模增长单调提升（如 Qwen3.5 2B→27B 在 Multi-Perspective 上 **71.06→87.23**），验证基准的区分力。
- 消融实验：去掉 Design Agent、变换合规性校验或样本级规划均导致整体质量下降，尤其对复杂多模态基准影响显著；直接让 LLM 一次性生成基准的 UIA 仅 20-43%，证明代理流程的必要性。
- 成本对比：人工标注 5-6 分钟/样本，Benchmark Agent 仅需 0.2-0.3 分钟。

**一句话价值**：该工作展示了一个端到端的基准自动构建系统，其规划-执行-验证架构与闭环质量控制可直接启发推荐系统评估集的自动生成与持续迭代。
