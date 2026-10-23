---
title: 'Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep
  Research Reports'
title_zh: 面向视频深度研究报告的 Agent 基准与评测框架
authors:
- Jiahao Meng
- Qize Yang
- Yuxuan Wang
- Yunfei Chu
- Wensi Dai
- Jin Xu
- Yunhai Tong
affiliations:
- Peking University
- Alibaba Token Hub, Alibaba Group
arxiv_id: '2610.31158'
url: https://arxiv.org/abs/2610.31158
pdf_url: https://arxiv.org/pdf/2610.31158
published: '2026-10-21'
collected: '2026-10-23'
category: Eval
direction: Agent 评测 · 视频深度研究报告
tags:
- Deep Research Agent
- Video Understanding
- Benchmark
- Rubric Tree
- Multimodal Evidence
- Agent Evaluation
one_liner: 构建首个以源视频为中心的深度研究 Agent 基准 OmniDR-Bench，并提出原子化 Rubric 树评测方法
practical_value: '- 可将 Omni-ARTs 的原子化 rubric 树和 ARC 构建流程复用到电商视频内容评测（如商品讲解、直播回放、教程视频），对
  Agent 生成的卖点摘要做逐条可验证打分，替代模糊的 LLM-as-judge。

  - skill-based workflow 提供可插拔结构，适合在商品视频导购/答疑 Agent 中按“问题拆解 → 多模态证据检索 → 交互式报告/回答卡片”组织
  pipeline，尤其要求输出带时间戳引用，直接匹配短视频带货场景的卖点溯源。

  - 当前 Agent 在跨模态因果推理和引用准确性上仍是明显短板，业务上做视频问答或报告生成时，应增加对引用证据的强校验层（检索片段强制回挂时间戳并二次校验），避免
  LLM 幻觉影响用户决策。

  - 中英文双语任务与 19 个真实子类别设计可参考，用于构建电商垂直领域的视频 Agent 回归集，覆盖不同品类和问题类型。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 deep research agent 评测集中于文本网页证据，缺少以源视频为核心的研究场景。视频天然携带丰富的情景、实体、空间关系和动作线索，用户需要定位相关片段、核验声明、复现演示或做决策，但当前 agent 难以系统完成这类任务。

方法关键点：定义 Video-Centered Deep Research Report Generation——给定视频和用户请求，Agent 识别研究问题、检索外部多模态证据、生成可交互报告并链接到相关视频时刻。实现上采用 skill-based workflow，可插拔地组合视频理解、检索、报告生成等技能。评测方面提出 Omni Atomic Rubric Trees（Omni-ARTs），每棵树包含 3 个维度、23 个共享方向及任务特定的原子二元标准，覆盖视听定位、多模态证据使用、交互呈现。构建流程 Audited Rubric Construction（ARC）通过独立证据收集、自动检查、行为校准和迭代人工审核来保证 rubric 质量。OmniDR-Bench 包含 50 个中英文任务、19 个真实子类别、6414 条标准。

关键结果：在 18 个 agent 配置中最佳系统仅得 63.3/100，主要短板是内容覆盖不足、跨模态因果与逻辑分析弱、引用支持不准确。分析还揭示不同模型、harness、技能配置、视频类别和研究轨迹对性能的影响。
