---
title: Can Agents Win the Video Browser Showdown?
title_zh: 智能体能否赢得视频浏览器挑战赛
authors:
- Bastian Jäckl
- Zuzana Vopálková
- Daniel A. Keim
- Jakub Lokoč
affiliations:
- University of Konstanz
- Charles University
arxiv_id: '2609.07311'
url: https://arxiv.org/abs/2609.07311
pdf_url: https://arxiv.org/pdf/2609.07311
published: '2026-09-07'
collected: '2026-09-10'
category: Agent
direction: Agent 自主交互式视频检索
tags:
- VLM
- interactive video retrieval
- autonomous agents
- video browser showdown
one_liner: 用VLM智能体自主操控交互式视频检索系统，从初始意图描述出发完成多轮搜索，性能比肩历史专家操作水平
practical_value: '- 把现有检索/推荐系统包装成工具接口，让 LLM/VLM 智能体通过 API 控制查询、翻页、过滤等操作，能快速构建自主搜索或评估流程，无需让模型预知全量候选集。

  - 智能体只分析 top-k 结果（如图像/视频关键帧）并决策下一步动作，避免对全库做昂贵推理，在电商图片/视频商品检索中可直接复用这种「索引+小窗口 VLM
  判断」模式。

  - 用模糊初始意图描述驱动多轮交互式检索，可作为电商搜索中长尾 query 或图片找同款场景的自动化补充，降低用户反复试错成本。

  - 评估方式可借鉴 VBS 的任务完成率与交互轮数指标，用于量化推荐/搜索系统在智能体操作下的实际可用性，而不仅是离线排序指标。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：交互式视频检索高度依赖用户同时理解搜索意图和系统功能，认知负担重、容易出错，且结果受操作者经验影响。作者探索能否让现代 VLM 智能体从初始意图描述出发，全自动地操作现有交互式视频检索系统完成搜索任务。

**方法关键点**：
- 不要求 VLM 预先了解整个视频数据集，而是把已有检索系统作为索引和高效查询工具。
- VLM 智能体分析 top-ranked 候选项（关键帧）并决定后续动作，形成「查询-浏览-决策」闭环。
- 对比多种 VLM 和 agentic 策略在 Video Browser Showdown 任务上的表现。

**关键结果**：
- 现代智能体能自主解决大量交互式搜索任务，仅凭初始意图描述即可运行。
- 在多个设置下，性能与历史强专家操作系统的结果具有竞争力。
