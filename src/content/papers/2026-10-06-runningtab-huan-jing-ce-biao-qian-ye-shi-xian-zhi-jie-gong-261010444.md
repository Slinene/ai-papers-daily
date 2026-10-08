---
title: 'RunningTab: Direct Workspace Interaction with Environment-Side Tabs'
title_zh: RunningTab：环境侧标签页实现直接工作区交互
authors:
- Jinheon Baek
- Soyeong Jeong
- Yumin Choi
- Dongsu Han
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2610.10444'
url: https://arxiv.org/abs/2610.10444
pdf_url: https://arxiv.org/pdf/2610.10444
published: '2026-10-06'
collected: '2026-10-08'
category: Agent
direction: Agent 环境侧任务追踪
tags:
- LLM Agent
- Workspace Interaction
- Task Tracking
- Environment-Side Memory
- Long-Horizon
one_liner: 为 LLM agent 直接操作工作区文件引入环境侧任务台账，记录需求、已读摘录与未打开候选，防止交付遗漏
practical_value: '- 在多步文档/商品库 agent 任务中，把“需求跟踪”从 prompt/context 外置到环境侧。每个需求一个状态，记录证据来源（例如商品
  ID、文档 chunk、文件路径）和未打开的检索候选，避免生成时丢信息。

  - 借鉴 finish check：在 LLM agent 输出最终推荐/报告前加一个环境侧校验，若仍有 open requirements 未匹配到证据，强制回补或显式标记放弃，降低漏召回。

  - 对 listing 结果中未打开的文件/商品保留候选列表，按与需求的匹配度排序；这类似搜索/推荐中的“曝光未点击”信号，可辅助二次召回和解释。

  - 若用 DWI 模式做企业 workspace 的 RAG，可把每次 read 自动抽取 excerpt + provenance 存成环境侧条目，支持 agent
  多次引用和审计，不依赖长上下文。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM agent 在 workspace 中直接检索/读取文件生成交付物（DWI），但缺少任务级追踪：需求、已读内容、列出但未打开文件都滑出上下文窗口，导致信息遗漏。

方法：RunningTab 在环境侧维护 per-task tab，agent 添加需求；环境将每个已读文件记录为带出处的摘要（excerpt+provenance），将列出但未打开文件记作候选；agent 可查看每个需求匹配的最佳摘要和 top 未打开候选，对匹配内容解决或给出理由搁置；若结束时仍有未解决需求，finish check 会返回这些需求。

结果：在 3 个 benchmark 上搭配 3 个 LLM 验证，RunningTab 一致优于 plain DWI 和把记录放在模型内的 baseline，并且 tab 通常保留交付物所需的值。
