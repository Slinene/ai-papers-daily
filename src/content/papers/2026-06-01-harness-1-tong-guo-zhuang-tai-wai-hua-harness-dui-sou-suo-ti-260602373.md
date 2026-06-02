---
title: 'Harness-1: Reinforcement Learning for Search Agents with State-Externalizing
  Harnesses'
title_zh: Harness-1：通过状态外化 harness 对搜索智能体进行强化学习
authors:
- Pengcheng Jiang
- Zhiyi Shi
- Kelly Hong
- Xueqiang Xu
- Jiashuo Sun
- Jimeng Sun
- Hammad Bashir
- Jiawei Han
affiliations:
- University of Illinois at Urbana-Champaign
- UC Berkeley
- Chroma
arxiv_id: '2606.02373'
url: https://arxiv.org/abs/2606.02373
pdf_url: https://arxiv.org/pdf/2606.02373
published: '2026-06-01'
collected: '2026-06-02'
category: Agent
direction: 搜索智能体 · 状态外化 harness
tags:
- RL
- Search Agent
- Stateful Harness
- Cognitive Offloading
- Retrieval
one_liner: 将搜索中的机械簿记卸载到环境端状态，使 20B 策略 RL 后平均召回达 0.730，比最佳开源 subagent 高 +11.4 点
practical_value: '- 电商搜索/推荐的多步检索中，可设计类似的**工作记忆状态机**（候选池、重要性标记、证据图、验证记录），将“记住已看文档、过滤重复、跟踪约束”等记账任务由环境维护，让策略模型聚焦语义决策，降低小模型
  RL 的优化难度。

  - **Warm-start curation**（自动从第一次成功搜索结果中 seed top-8 为 `fair` 重要性）解决了空 curated set
  带来的早期奖励无区分度问题，可迁移到对话式的商品搜索、主动推荐场景，避免 RL 探索时的全零 reward。

  - **多样性奖励**（tool diversity bonus）防止策略坍缩到反复搜索的捷径，强制 agent 使用验证、阅读、curate 等多种行动，提升最终精排质量。这在电商
  Agent 做多轮“搜索-浏览-比较-加购”决策时特别有用。

  - **紧凑的派生状态渲染**（BM25 句子压缩、证据图、重要性分级）和**两级去重**（chunk-ID + MinHash 指纹）有效控制上下文预算，让策略在长序列多轮交互中保持对关键证据的可见性，适合需要融合多篇商品评论、比价等长上下文场景。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有搜索智能体训练通常要求策略模型在生成下一个查询的同时记住已检索的文档、哪些是候选、哪些约束条件尚未满足——这种将语义搜索与琐碎状态维护混合优化的方式对 RL 极为不利：奖励信号难以区分搜索失败与状态遗漏，且上下文不断增长的 transcript 增大了学习难度。作者提出**状态外化卸载**原则：将可恢复的簿记工作交给环境侧的状态机（harness），让策略仅做语义决策（搜什么、保留/丢弃哪篇、验证哪个声明、何时停止）。

**方法**
- **状态机 harness**：维护候选池、重要性标记的 curated set（上限 30 篇）、证据图（实体→文档映射）、验证记录、压缩去重的观察和预算标记。策略通过 `curate`(add/remove/import-tag)、`verify`、`review_docs` 等结构化 action 编辑状态。
- **关键设计**：① 首次搜索成功自动 seed top-8 文档提供 warm-start curation，避免 blank slate；② 句子级 BM25 压缩 + chunk-ID / MinHash 内容去重，控制上下文；③ 证据图提取实体共现，显示桥接文档和单例实体，辅助跨文档推理。
- **训练**：SFT 用 GPT-5.4 在 harness 内生成 899 条轨迹，教模型工具调用节奏与验证-提升规范；RL 在 SEC 数据上用 CISPO 优化，奖励融合 curated recall (Fβ)、trajectory recall、final-answer recall、tool diversity bonus 等，并包含 answer-miss penalty 促使发现证据后必须提升为最终推荐。

**关键结果**
在 8 个跨领域检索基准（BC+, Web, Patents, SEC, LongSealQA, Seal0QA, FRAMES, HotpotQA）上，Harness-1 (20B) 平均 curated recall 达 0.730，超越最强开源 subagent Tongyi DeepResearch 30B 的 0.616，且与 Opus-4.6 等 frontier 模型相当。在完全未见过训练数据的 4 个传递基准上，召回增益平均 +17.0 点（vs 源域 +7.9），表明策略学到了通用搜索操作。组件消融显示每种 harness 机制均贡献重要，证据图、重要性标签、压缩等分别导致 ΔFA recall -3.9%~-7.9%。同时，多样性奖励被证实为 RL 训练的关键防坍缩手段。

**最值得记住的一句话**
*“将搜索中机械性的记账卸载到环境状态，让 RL 专注于语义决策，可以产生超越训练域泛化的检索行为。”*
