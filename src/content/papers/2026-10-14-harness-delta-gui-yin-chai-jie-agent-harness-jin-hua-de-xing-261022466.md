---
title: 'Harness-Delta Attribution: Dissecting Gains From Harness Evolution'
title_zh: Harness-Delta 归因：拆解 Agent Harness 进化的性能增益来源
authors:
- Wenxuan Ding
- Qin Lu
- Changlong Yu
- Sha Li
- Shuowei Jin
- Xin Liu
- Zhenyu Shi
- Greg Durrett
affiliations:
- Amazon
- New York University
arxiv_id: '2610.22466'
url: https://arxiv.org/abs/2610.22466
pdf_url: https://arxiv.org/pdf/2610.22466
published: '2026-10-14'
collected: '2026-10-21'
category: Eval
direction: Agent 评测与进化增益归因
tags:
- Harness Evolution
- Agent Evaluation
- Overfitting
- Test-time Scaling
- Benchmark Overfitting
- Attribution
one_liner: 提出 HDA 协议，将 harness 进化增益归因为 overfitting、test-time scaling 与 residual 三类
practical_value: '- 在做 Agent 搜索结果页策略、推荐链路 prompt/tool 搜索时，引入 HDA 式分解：对 search set
  的 lift 拆成 artifact overfitting、inference compute scaling 与 residual；只报验证集不够。

  - 必须设置 held-out tasks/跨类目流量做泛化验证；电商 query 推荐、广告文案生成等场景，benchmark 相似 query 的增益常不迁移到真实分布。

  - 对加入多采样、投票、更多推理步数的方案，单独量化 test-time scaling 贡献，避免把“多算力带来的提升”误判为 harness 设计有效。

  - 用 artifact-driven probes（如检测规则式捷径、重复输出短路）暴露过拟合；可在推荐 Agent 中设计反事实或干扰样例来检查泛化。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：agent harness 进化在固定权重模型上调 prompts/tools/orchestration，常见 search set 提升，但多少是过拟合或额外推理算力？需要拆解收益来源。

**方法关键点**：提出 Harness-Delta Attribution (HDA)，把进化增益分为 artifact-driven overfitting、由 test-time scaling 解释的增益、以及 residual（可泛化改进的上界）。在 11 个 executor 模型、3 个 harness 进化框架、math/coding/creativity/agentic 任务上应用。

**关键结果**：21 个有显著 search set 收益的设置中，overfitting 占增益平均 54%，test-time scaling 占 14%；14/21 设置两者合计超 50%。search set 增益往往不能迁移到 held-out tasks，难以在分布漂移下持续；validation-based 信号不足以阻止过拟合。建议未来 harness 进化研究采用 attribution-aware 评估。
