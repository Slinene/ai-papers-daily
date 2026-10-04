---
title: 'RLE-Bench: A Qualifying Exam for Coding Agents as Robot Learning Engineers'
title_zh: RLE-Bench：编码智能体作为机器人学习工程师的资格考试基准
authors:
- Haitong Ma
- Chenxiao Gao
- Rushi Qiang
- Bo Dai
- Na Li
affiliations:
- Harvard University
- Georgia Institute of Technology
arxiv_id: '2609.34210'
url: https://arxiv.org/abs/2609.34210
pdf_url: https://arxiv.org/pdf/2609.34210
published: '2026-09-28'
collected: '2026-10-04'
category: Eval
direction: 编码智能体 · 机器人工程能力评测
tags:
- Coding Agent
- Benchmark
- Robotics
- Agent Evaluation
- Workflow Evaluation
one_liner: 提出覆盖四类机器人开发工作流的编码智能体评测基准，用 RLE Index 聚合多维工件指标并给出排行榜
practical_value: '- 借鉴“工作流拆解 + 工件级评估”范式：将电商推荐 Agent 的能力按 query 理解/候选召回/排序策略/诊断优化等
  workflow 拆分，分别评估 Agent 产出的代码、配置或策略，避免只测对话文本。

  - 借鉴 RLE Index 的异构指标归一化聚合方法：在 Agent 综合能力排名中，对不同任务的成功率、策略收益、结构指标等做标准化后加权，可用来比较不同
  LLM 驱动的推荐 Agent。

  - 引入资源约束与多模态反馈的评估条件：电商 Agent 常面临延迟、成本、多样性约束，评测时可加入相应限制，考察 Agent 在受限环境下生成可部署 artifact
  的能力。

  - 案例研究定位 failure mode：对 Agent 在复杂搜索推荐任务中的行为做细粒度分析，可发现 LLM 在集成异构组件、处理多模态信号时的具体短板，指导后续微调或
  prompt 设计。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有机器人基准主要评估单个策略或控制器，忽略编码智能体在实际机器人开发中需要构建、集成、诊断和改进异构工件的能力。为了填补这一空白，论文提出 RLE-Bench。

**方法关键点**：RLE-Bench 覆盖四个代表性机器人开发工作流：交互控制、策略学习、感知与估计、机械设计。评估对象是编码智能体提交的各类工件（work products），包括成功控制率、训练的策略、构建的 harness、设计的机械结构等。采用多样任务特定指标，聚合成整体 RLE Index 和 workflow-specific capability profiles，实现多维能力系统比较。此外还进行深度案例研究，分析智能体在代表性任务上的行为。

**关键结果**：排行榜显示 GPT-6 Astra 以 73.4 的 RLE Index 领先，其次是 Claude Fable 64.0、Claude Opus 53.4；DeepSeek-V4.1-Flash 38.9，Gemini 3.7 Flash 26.8 等。案例研究指出了当前编码智能体在机器人工程任务中的能力边界和局限，以及未来智能体训练可挖掘的机会。
