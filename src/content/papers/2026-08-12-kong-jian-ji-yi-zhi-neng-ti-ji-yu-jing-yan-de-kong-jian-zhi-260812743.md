---
title: 'Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence'
title_zh: 空间记忆智能体：基于经验的空间智能程序性记忆
authors:
- Haokai Zhang
- Yuhang Ding
- Yunshu Zhou
- Xinze Du
- Shengtao Zhang
- Zhiyue Zhao
- Yuling Xi
- Hao Chen
affiliations:
- Zhejiang University
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
arxiv_id: '2608.12743'
url: https://arxiv.org/abs/2608.12743
pdf_url: https://arxiv.org/pdf/2608.12743
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: Agent 外部记忆自进化 · 空间推理
tags:
- Agent Memory
- Spatial Intelligence
- Self-Evolving Agent
- VLM
- Transfer Reliability
- Procedure Memory
one_liner: 冻结 VLM 通过外部可验证经验蒸馏可迁移教训，并用访问证据校准迁移可靠性分数，实现无参数更新的空间推理自进化
practical_value: '- 借鉴 TRS 校准思路：把每条 prompt/memory/经验卡片的“可迁移性”用线上反馈（reward/转化）做贝叶斯式更新（先验
  + 访问证据），检索时 similarity 与 reliability 联合排序；避免纯 embedding 相似度召回高相似但低效的案例，适用于推荐解释、商品知识检索、Agent
  工具经验复用。

  - One-Pass Memory Writing：只在首轮经验采集时写入结构化卡片，后续仅更新卡片访问/奖励状态，能显著减少经验库冗余并提高更新覆盖率；对推荐
  Agent 的 few-shot 示例库、query 改写策略库维护有直接工程价值。

  - 冻结基座模型、只动外部记忆：在线服务无需做 LoRA/RL 更新，风险低、迭代快；适合电商搜索/推荐中基础 LLM 不常更新但策略需要快速试错的场景。

  - 反思时输出 pattern / trap / check 三段式可迁移教训，并禁止 restating answer；这个可复用到生成式推荐、搜索 query
  推荐中的经验卡片设计，增强可读性和跨任务迁移。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
空间智能是 embodied agents 和 multimodal assistants 的基础能力，现有提升 VLM 空间推理的路线主要有两条：后训练微调/RL 或推理时调用外部空间工具（深度估计、3D 重建）。二者要么改权重，要么依赖专家工具。这里探索第三条路：参数冻结的 VLM 智能体能否通过可验证经验自进化，把验证过的经验蒸馏成可迁移教训，不更新权重、推理时不依赖工具。

**方法关键点**
- SMA 在可验证空间环境中获取 rollouts：冻结 VLM 预测，verifier 给标量 reward。
- 反射模型根据 verified target 把每次 rollout 压缩成卡片：task、summary、transferable lesson；禁止 restating answer，避免记忆泄漏。
- 每条卡片有 Transfer Reliability Score（TRS），初始化为统一先验，后续用访问证据校准：v = (λv0 + c) / (λ + n)，其中 n 为访问次数、c 为累计 reward；该分数衡量“该程序在未来是否可靠迁移”，而非 source rollout 是否正确。
- 部署时两阶段检索：先语义相似度过滤，再用 normalized similarity 与 normalized TRS 加权排序，top-k 作为 guidance 注入 prompt。只读部署阶段不写新卡、不更新分值。

**关键实验结果**
- 五个空间基准（RoboSpatial, ERQA, Omni3D, SAT, EmbSpatial）× 四个冻结 VLM（Qwen3.5-9B 到 122B-A10B 等）共 20 个评测中，SMA 大多数最优；相对最强非 SMA baseline，平均提升 1.7–2.9 点。
- Qwen3.6-27B 上，RoboSpatial 从 54.1 升至 68.5，Omni3D 从 41.6 升至 47.6。
- 与训练式 SpatialEvo-7B 对比，平均 47.1 → 63.5，提升 16.4 点。
- 消融：删去 transferable lesson 掉 3.5 点，删去 semantic filter 掉 5.8 点，reward-only reflection 掉 5.5 点。
- 相似度分析：SMA 把平均检索相似度从 0.792 降到 0.698，准确率却从 66.8% 升到 69.8%。

**最值得记住的一句话**
最好的记忆并不总是最相似的记忆；transfer reliability 把检索从语义匹配变成证据加权的程序选择。
