---
title: 'TRIAGE: Three-level Routing and Intelligent Agent Guidance for Efficient Execution'
title_zh: TRIAGE：三级路由与轨迹复用实现高效 Agent 执行
authors:
- Ruocan Wei
affiliations:
- China Telecom Cloud, Beijing, China
arxiv_id: '2609.01428'
url: https://arxiv.org/abs/2609.01428
pdf_url: https://arxiv.org/pdf/2609.01428
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: LLM Agent 轨迹复用与三级路由降本
tags:
- LLM Agent
- Token Efficiency
- Trajectory Reuse
- Semantic Routing
- Skill Extraction
- TaaS
one_liner: 用历史执行轨迹做语义路由与技能化复用，在 1007 条查询上降低 62.3% token 消耗
practical_value: '- **把高频参数化查询做成 0 token 的 Skill 复用**：对电商 BI、客服诊断、广告投放 Agent 里反复出现的“改参数不换结构”查询，可以用
  embedding 阈值 + 参数抽取 + 模板替换，绕过 LLM 生成 SQL/工具调用；本质是带参数替换的语义 cache，比 GPTCache 更细粒度。

  - **路由策略要看 overhead / execution cost 比值**：文中 ablation 很直接：LLM router 每条约 224 token
  的路由开销，导致整体反而 -37.3% savings；在单条 SQL 生成成本约 197 token 时，zero-cost 阈值路由完胜。迁移到业务时，若单次
  Agent 任务成本很高（长上下文、多步工具编排），才值得上 LLM router；低成本的 query 类场景千万不要用 LLM 做路由。

  - **用 LLM feedback 自举参数抽取规则**：L2 参数替换时，遇到轻量归一化无法解释的差异，再调一次 LLM 判定是否是参数变化，并把结果注册成正则规则；后续同类参数可以
  0 token 处理。这个机制很适合商品名、类目、时间窗口等高频可变参数的电商 query。

  - **在线冷启动路径可以直接抄**：无预训练、无人工标注，前 100 条 query 内 L2 命中从 0 到 57%；适合内部 dashboard、监控告警、运营取数
  Agent 上线。但要注意文中提到的 error propagation，自动提取的 Skill 需要加正确性校验或执行后验证，不能直接推全量。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
ReAct 类 LLM Agent 每次 query 都从零推理，相似 query 的 schema 推理、SQL 生成、执行、格式化被反复重算。本文用 1007 条安全监控查询实测，单条 ReAct 平均 198 token，总 199,782 token；大量 query 只是参数不同却付出完全相同成本。现有 prompt compression、speculative decoding、GPTCache 都无法消除重复推理循环。

**方法关键点**
- **三级路由**：用 all-MiniLM-L6-v2 384 维 embedding 做 cosine similarity 检索，L1≥0.98 direct reuse，L2≥0.90 Skill substitution，L3<0.90 full ReAct；L1/L2 均为 0 token 执行。
- **TaaS（Trajectory-as-a-Skill）**：成功执行的轨迹持久化为可检索经验库，生命周期 store → retrieve → reuse → distill；高频轨迹自动抽象成带类型参数的 deterministic Skill。
- **Skill 自动提取**：对工具调用做 pattern normalization（值替换为 typed wildcard）→frequency accumulation→pairwise diff 参数归纳→注册为 0 token 模板；SQL 场景下将 string literal/日期/数字替换为占位符，保留表名列名结构。
- **LLM 辅助参数抽取**：轻量归一化无法解释差异时，调 LLM 判定是否参数变化，并把新参数模式注册为正则规则，后续 0 token 处理，形成自改进参数抽取。
- **在线学习**：query 顺序到达，混合分布包含 6.1% 每日固定查询、57.2% 参数变化查询、36.7% 全新查询；系统从 cold-start 到 mature 逐步提升效率。

**关键实验**
在 1007 条 security monitoring queries 上对比完整 ReAct baseline：总 token 199,782 → 75,238，节省 62.3%；API calls 1007 → 421；路由分布 L1 5.5%、L2 56.0%、L3 38.5%，即 61.5% query 走零 token 路径。Ablation 中移除 L2 后节省降至 55.0%；用 LLM router 替换阈值路由导致负节省 -37.3%，主因路由 overhead 225,628 token 超过总执行成本。跨领域 ToolBench 15 domains/345 queries 达到 76.3% token reduction，其中 L1+L2 覆盖 96.2%。

**最值得记住的一句话**：效率是经验的函数——Agent 用得越多、轨迹库越丰富，自动提取的 Skill 越多，单 query 成本越低，而不是静态优化的一次性收益。
