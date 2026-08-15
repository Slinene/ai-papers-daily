---
title: 'AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design'
title_zh: AutoDesign：面向长程智能体设计的元 Harness 优化
authors:
- Yaxin Luo
- Haobin Jiang
- Jialv Zou
- Xu Huang
- Wenhao Yan
- Haodong Li
- Zhengrong Yue
- Jing Li
- Xiaofu Chen
- Xiaohan Zhao
affiliations:
- Meituan
- MBZUAI
- Huazhong University of Science and Technology
- Peking University
- Tsinghua University
arxiv_id: '2608.13560'
url: https://arxiv.org/abs/2608.13560
pdf_url: https://arxiv.org/pdf/2608.13560
published: '2026-08-12'
collected: '2026-08-15'
category: Agent
direction: Agent 长程任务与元 Harness 优化
tags:
- Agentic Design
- Meta-Harness Optimization
- Long-Horizon
- Poster Generation
- Benchmark
one_liner: 提出元 harness 优化框架，让 code agent 基于 rollout 反馈递归改进设计 harness，在海报生成任务上超越商业系统
  7.45 分
practical_value: '- 借鉴 meta-harness 分离设计与执行：把 agent 的 prompt、工具调用、流程编排等封装成 harness（代码/配置文件），由一个上层
  optimizer 分析 rollout 反馈对 harness 做可版本化修改。业务中可对推荐对话 Agent、创意生成 Agent 做同样抽象，支持快速迭代和跨任务复用。

  - 用低成本长程探索 + 自动评估驱动自我改进：AutoDesign 40 分钟、$3 执行 253 次工具调用和 11 次编辑，说明 agentic 创意生成可以做到量产成本。可迁移到电商
  banner/商品主图/广告素材生成，先构建轻量自动评估指标（如图文匹配、布局密度）进行离线筛选，再人工验收。

  - 建立任务专用 benchmark 与 mini 子集：PosterBench 用 100 篇论文主赛道 + 10 篇 mini 控制评估，业务上可仿照建立自己的素材/设计质量基准，覆盖多类目、系统盲评，避免只调
  prompt 却没有可比较的离线指标。

  - 多模型配置下的一致性增益：在 7 种 code-agent-model 配置中引入学习到的 DesignHarness 平均提升 12.4 分，说明好的 harness
  具有跨模型迁移性；在选型 LLM 时可以把 harness 优化作为关键层，而不是只换模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：将多模态源转化为结构化媒体输出本质上是围绕 model-harness 系统的长程 agentic 过程。理想 harness 应对齐人类设计先验、通过经验积累递归自我改进，但现有范式多为静态，缺乏这种能力。

**方法关键点**：AutoDesign 框架采用 meta-harness optimizer 指导 code agent，基于 rollout 反馈对 harness 进行递归改进。以学术论文到海报生成为实例，定义 PosterBench：含 100 篇论文的 Main Track 覆盖五个学科，以及 PosterBench-mini（10 篇共享子集）用于受控评估。学习到的 DesignHarness 封装了设计流程、工具调用与反馈改进策略。

**关键结果**：PosterBench Main Track 上 AutoDesign 得分 78.32，超越闭源商业系统 Claude Design 7.45 分；在 7 种 code-agent-model 配置中，集成 DesignHarness 平均将 PosterBench Score 从 54.99 提升至 67.39（+12.4%）；全自动长程循环 40 分钟、$3 成本执行 253 次工具调用和 11 轮编辑，达到会议海报平均质量；系统盲评人类偏好最高。
