---
title: 'SquidAgent: Parallelize Wisely, Coordinate Efficiently'
title_zh: SquidAgent：明智并行、高效协调的多智能体调度框架
authors:
- Yexiong Lin
- Shanshan Ye
- Yu Yao
- Zhen Fang
- Bo Han
- Tongliang Liu
affiliations:
- The University of Sydney
- Mohamed bin Zayed University of Artificial Intelligence
- University of Technology Sydney
- Hong Kong Baptist University
arxiv_id: '2610.08647'
url: https://arxiv.org/abs/2610.08647
pdf_url: https://arxiv.org/pdf/2610.08647
published: '2026-10-06'
collected: '2026-10-07'
category: MultiAgent
direction: 多智能体并行调度与成本建模
tags:
- multi-agent
- parallelization
- token-cost
- scheduling
- LLM agents
- orchestration
one_liner: 提出用预测输出 token 成本决定每层串并行，通过上下文继承和前置约定降低协调开销，吞吐提升 2.2 倍
practical_value: '- 在电商内容生成 Agent 工作流（商品详情页、营销落地页、多语言 Listing）中，不要默认全并行；先让 LLM 估算每个模块的
  output token 作为成本，按层比较 sum vs max + alignment，设置安全边际 α≈1.9，只对收益明确的层并行。

  - 让 worker 从 orchestrator 的 session fork 继承上下文，显著减少每个并行 agent 重复理解需求和约束的成本；工程上可复用“共享上下文快照
  + 只追加任务专属指令”的模式。

  - 用前置 convention block（统一命名、接口、格式、埋点口径）替代事后合并修正，尤其适合多 agent 生成商品标题/卖点/参数表时的一致性控制，降低返工。

  - LLM 对 wall-clock 时间估计不可靠（Spearman 0.16），但对 output token 估计可靠（0.77）；做 Agent 成本预估和调度时，优先用
  token 数量作为代理指标，不要问模型“要多久”。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：LLM-based multi-agent 系统理论上能通过并行加速复杂多步任务，但现有并行系统常比单 agent 串行还慢。论文指出原因不是并行本身，而是并行引入两类隐藏成本：re-exploration cost（worker 重复重建 orchestrator 已有的规划上下文）和 alignment cost（独立输出需要事后统一命名、接口、格式等）。因此需要显式准则判断何时并行真正有利。

方法关键点：
- 将任务 DAG 按拓扑分层，逐层选择串行/并行。串行成本 Tser=Στi；并行成本 Tpar=max τi + Cexp + Calg。仅当预测串行成本显著高于有效并行成本（bρk>α，α=1.9）才并行。
- 成本单位从 wall-clock time 改为 predicted output tokens：LLM 对自身时长估计校准差（Spearman 0.16），但对输出 token 估计可靠（Spearman 0.77），且 token 与生成时间近似线性。
- SquidAgent 实现：orchestrator 单次规划同时输出 DAG、每个 subtask 的 output token 预算、每层 alignment token；worker 从 orchestrator session fork 继承上下文，使 Cexp≈0；并行前写 shared convention block，将事后对齐成本前置并显式估计；deterministic scheduler 无需额外 LLM 调用。

关键实验：在 9 个任务（代码生成、文档写作、结构化规划，含 8-27 文件的大任务）上对比 Claude Code、SeqCV、MetaGPT、AFlow、Flow、MacNet、AgentConductor。SquidAgent 平均吞吐 38.1 words/s，是 Claude Code 的 2.2×，是最强多智能体 baseline AgentConductor 的 2.0×；质量得分 98.2%，高于 Claude Code 97.1%。消融显示去掉调度策略吞吐下降 32.1%，去掉 session fork 或 convention planning 也明显下降。进一步敏感性分析展示 α=1.9 能正确对紧耦合层选串行，避免对齐开销。

最值得记住的一句话：并行化不是默认选项，只有当预测串行成本与（关键路径 + 对齐成本）之比超过安全边际时并行才划算；用输出 token 而非 wall-clock 做成本代理。
