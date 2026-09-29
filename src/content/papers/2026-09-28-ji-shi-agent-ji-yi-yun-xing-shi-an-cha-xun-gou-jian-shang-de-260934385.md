---
title: Just-In-Time Agent Memory with Runtime Agentic Research
title_zh: 即时 Agent 记忆：运行时按查询构建上下文的 JAM 框架
authors:
- Bingyu Yan
- Chaofan Li
- Hongjin Qian
- Shuqi Lu
- Chaozhuo Li
- Zheng Liu
affiliations:
- Beijing Academy of Artificial Intelligence
- Peking University
- Hong Kong Polytechnic University
arxiv_id: '2609.34385'
url: https://arxiv.org/abs/2609.34385
pdf_url: https://arxiv.org/pdf/2609.34385
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent 记忆 · 运行时上下文构建
tags:
- Agent Memory
- Runtime Context
- SFT
- GRPO
- Memory-Gym
- Hybrid Retrieval
one_liner: JAM 将 Agent 记忆从请求无关预压缩转为运行时按查询构建上下文，结合分层工作区与可训练研究员策略
practical_value: '- 对推荐 Agent 的用户长期行为/会话历史，不要只存预生成摘要；学 JAM 保留原始 session，并用轻量 memo/README
  做导航，在线时用小模型按 query 迭代 open/search/browse，保留跨 session 细粒度依赖。

  - 工程上采用 hybrid BM25 + dense retrieval 提供候选；离线建库一次性成本可接受，在线 13.81s/query 质量反超 58.08s
  的 MemAgent；测试期可增加 action budget 换取 F1，budget 是上限而非固定成本，多数 query 早停。

  - 训练研究员时用 verified-trajectory SFT 过滤“浅搜即答”的捷径行为，再用 GRPO 优化，奖励用 source recall（召回
  gold supporting sessions）；训练时注入 hint 稳定多步探索，推理时移除，业务可直接复用该奖励设计。

  - Memory-Gym 的四阶段合成 pipeline（anchor discovery → task-dependent expansion → instantiation
  → validation）可改造用于生成电商场景训练样本：单跳定位、多跳证据连接、多 session 聚合，覆盖用户行为轨迹与商品知识。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有 AOT 记忆系统在请求到达前预压缩历史，易丢失后续关键的细粒度/跨会话信息；而训练式记忆 agent 的监督数据常来自多跳 QA 或 benchmark，覆盖不足。JAM 针对长历史下按需构造上下文的问题，提出运行时按查询做 agentic research。

**方法关键点**  
- Memorizer 离线把原始 session 完整存入分层 workspace，为每个 session 生成 memo，按语义分组并维护目录 README，形成 page-store + 导航摘要。  
- Researcher 在线在 thinking–exploration–reflection 循环中调用 open/search/browse 三个工具，search 用 BM25 + dense 混合检索；满足充分性判定或达到 action budget 后 finalize 上下文，保留出处。  
- Memory-Gym 覆盖 6 个领域、9 类任务、三个任务族：单跳定位、多跳证据连接、多 session 概括；四阶段合成：anchor discovery → task-dependent expansion → instance instantiation → validation，28,276 候选保留 16,794（59.4%），200 条人工审计合格率 95%。  
- 训练采用 cascaded：verified-trajectory SFT（teacher 轨迹 + LLM judge 过滤低质/捷径）→ Hint-guided GRPO；奖励用源 session recall，hint 只在训练 rollouts 注入，推理移除。

**关键结果**  
- 用 Qwen3.5-4B 作为 backbone，在 LoCoMo / LongMemEval / NarrativeQA / HotpotQA 上对比训练无关 AOT（A-MEM、Mem0、MemoryOS、LightMem）与 trained（MEM1、MemAgent、Memory-R1）；JAM LoCoMo overall F1 52.09，优于 MemAgent 46.13、A-MEM 41.17 等。  
- 跨域迁移 LongCodeQA 未训练：54.08 → SFT 65.67 → SFT+RL 75.54。  
- 效率：离线构建 79.53s，在线 13.81s/query，相比 MemAgent 58.08s 降低 76.2%，同时 F1 更高；默认 20 轮 budget 下中位数仅 3–6 轮，budget 耗尽 <5%。

> 最值得记住的一句：Agent 记忆不应是请求无关的预压缩，而是保留原始记录 + 可训练的、按查询运行的证据研究过程。
