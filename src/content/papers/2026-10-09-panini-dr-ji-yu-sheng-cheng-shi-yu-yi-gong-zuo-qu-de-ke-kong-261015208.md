---
title: 'PANINI-DR: Controlled Deep Research through Generative Semantic Workspaces'
title_zh: PANINI-DR：基于生成式语义工作区的可控深度研究多智能体框架
authors:
- M. Yigit Turali
- Shreyas Rajesh
- M. Efe Lorasdagi
- Chenda Duan
- Kartik Sharma
- Vwani Roychowdhury
affiliations:
- University of California, Los Angeles
arxiv_id: '2610.15208'
url: https://arxiv.org/abs/2610.15208
pdf_url: https://arxiv.org/pdf/2610.15208
published: '2026-10-09'
collected: '2026-10-14'
category: MultiAgent
direction: 多智能体深度研究 · 结构化验证工作区
tags:
- deep research
- multi-agent
- verification
- semantic workspace
- evidence support
- generative workspace
one_liner: 用共享生成式语义工作区记录子问题依赖与证据，并分离研究/验证，深度研究性能与答案可溯源均领先
practical_value: '- 将复杂用户问题/购物任务拆成显式 DAG，每个节点带 retrieval hint + answer type + verification
  claim。对商品属性、价格、库存、政策等事实节点先做 deterministic type 与证据检查，再进入 LLM claim 判断，可显著降低错误传播到推荐/导购决策。

  - 共享 workspace 替代无限增长 dialogue history：把已确认的子问题、证据、review status 存为结构化状态，新子任务只注入相关已确认发现，缓解长上下文中间信息丢失；适合多轮导购/售后
  Agent 的状态管理。

  - 增加 observed support 作为上线指标：不只评估最终答案/推荐是否对，还要求可推荐信息能从已保存证据恢复。电商/广告中尤其要区分模型参数记忆与实时检索证据，避免凭“记忆”给出库存/价格/活动文案。

  - 工程上为每个 Researcher 配一个 Reader agent 抽取引用/quote，减少全文档入 context；评估计算成本要按 uncached
  input/generated tokens，而不是 submitted tokens，因为 vLLM prefix cache 下重复上下文成本被高估。调大
  turn allowance 前先测边际收益（20→80 turns 仅 +2.7 点却 2.8× prompt tokens）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
Deep research 需要多步搜索、推理与计算，中间发现会引导后续调查。随着历史增长，隐式把状态放在对话历史里会让模型难以利用中间信息，且中间错误会沿依赖传播。例如把 Camp David Accords 时的总统错认成 Reagan，即使后续检索正确也会得到错误答案。

**方法关键点**
- 用 Generative Semantic Workspace 把查询拆成 DAG：节点是子问题/answer target，边表示依赖；每个 blank 带 retrieval hint、expected answer type、verification claim。
- Orchestrator 维护 workspace W=(P,S)，选择 ready nodes 并行派发 Researcher；Researcher 先做一次 typed retrieval，成功则交验证，失败转 ReAct；阅读工具用单独 LLM 提取相关 quotes，避免长 context。
- Verifier 先做 deterministic 的 type/evidence 检查，再判断 cited evidence 是否支持候选且能否区分 plausible alternatives；失败反馈可重试最多 5 次。
- Findings 被 admit 后填入 blank、记录证据和 review status；计算节点在输入齐后由 code 执行；发现缺失中间事实可让 Planner 修订 plan。

**关键实验**
在 BCP CF-150、FRAMES、MoNaCo 上对比 7 个 SOTA harness，共享 gpt-oss-120b 和检索服务。BCP overall 73.3%，比最强 baseline SLEUTH 57.3% 高 16.0 个百分点；BCP hard 52%，近两倍 SLEUTH 的 28%；FRAMES 79.1%，平均第一。Observed support 三个基准均最优：BCP 70.7 vs 54.0，FRAMES 66.1 vs 55.2，MoNaCo 0.458。Ablation：structured planning/state 将 BCP 从 41.3% 提到 58.0%；verification 加 16.0 点。估算计算约 7.3× SLEUTH，66.5% 输入 token 命中 prefix cache。

**最值得记住的一句话**：把中间结论显式化并进行子问题级验证，正确且可溯源比单纯答对更重要。
