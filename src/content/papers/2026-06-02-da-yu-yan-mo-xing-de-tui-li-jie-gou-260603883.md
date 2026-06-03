---
title: Reasoning Structure of Large Language Models
title_zh: 大语言模型的推理结构
authors:
- Frédéric Berdoz
- Luca A. Lanzendörfer
- Fabian Farestam
- Roger Wattenhofer
affiliations:
- ETH Zurich
arxiv_id: '2606.03883'
url: https://arxiv.org/abs/2606.03883
pdf_url: https://arxiv.org/pdf/2606.03883
published: '2026-06-02'
collected: '2026-06-03'
category: Reasoning
direction: 推理结构分析 · 逻辑谜题 · 推理效率度量
tags:
- reasoning efficiency
- graph extraction
- logic puzzles
- LLM evaluation
- structural analysis
one_liner: 将推理轨迹转化为可验证图并提出效率指标 η，区分聚焦推理与发散探索，揭示 token 量无法衡量推理质量。
practical_value: '- 推理图提取方法可复用到复杂诊断场景：将模型自由文本输出转为原子声明与依赖图，对多步决策 Agent 的推理路径进行结构化审计。

  - 效率指标 η 能暴露推理中的“冗余膨胀”与“验证开销”，可用于指导 Test-time Compute 的分配策略，避免盲目增加 token 预算。

  - 框架中的声明验证依赖可执行环境，在电商/推荐场景中可结合知识库或规则引擎，对推理中间步骤做事实性校验，提升可解释性。

  - 对于需要链式推理的生成式推荐（如 Semantic ID 序列推导），可借助图结构分析推理是否收敛到解所需的最小信息集，优化推理效率。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
当前大推理模型（LRM）评估通常只看最终答案准确率和生成 token 数量，但这些一维指标掩盖了推理过程的本质差异。同一正确的解法可能来自高度聚焦的演绎，也可能来自大量发散探索。因此需要一种能捕捉推理结构的方法，区分推理效率高低。

**方法关键点**
- 构建可扩展的逻辑谜题基准（21 种二维网格谜题，4 个难度等级），配有可执行环境，能对中间声明进行确定性验证。
- 设计两阶段混合提取流水线：先用确定规则+LLM 辅助从推理轨迹中抽取原子声明，再用 LLM 结合谜题规则提取声明间的推演边，构建有向无环推理图 G。
- 将推理流建模为吸收马尔可夫链：将源声明作为初始逻辑质量均匀分布，行归一化邻接矩阵得转移矩阵，计算瞬态节点上的逻辑质量分布 m，并定义结构熵 Hstr。
- 提出推理流效率 η = (log|V| − Hstr(G)) / (log|V| − log|C*|)，衡量逻辑流相对于解所需最小声明集的集中程度。η 越高表示推理越聚焦，越低表示发散或验证冗余多。

**关键实验**
- 在 GPT-5、Qwen3 235B、DeepSeek V3.2、Kimi K2 上评测。难度从 Trivial 到 Human hard，准确率普遍断崖下跌（GPT-5 从 83.8% 降至 5.7%），但 token 数却大幅上升。
- η 与完成 token 数几乎无关（r=−0.05, p=0.64），表明令牌量不是推理质量的代理。
- η 与图中解支撑部分占比正相关（r=0.55），与图总大小负相关（r=−0.33）；额外 token 主要转化为验证开销（|Vver|/|Vsol| 与 token 数 r=0.53）。
- 对比图 1 中同一模型同一实例的两个解，η 低（0.059）对应大量游离推论，η 高（0.362）对应紧凑推演，准确率和 token 数无法区分两者。

**最值得记住的一句话**
推理流效率 η 通过吸收马尔可夫链刻画逻辑质量的流集中度，在 token 数失效时仍能揭示推理结构的本质差异。
