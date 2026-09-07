---
title: Inventory-Grounded Policy-Level Optimization for Training-Free AI Search
title_zh: 基于库存证据的策略级优化：面向动态库存 AI 搜索的训练无关方法
authors:
- Wei Zhou
- Tiandeng Wu
- Jiandong Ding
- Zhufeng Fan
- Yi Cao
affiliations:
- Huawei Technologies Co., Ltd., China
arxiv_id: '2609.04813'
url: https://arxiv.org/abs/2609.04813
pdf_url: https://arxiv.org/pdf/2609.04813
published: '2026-09-04'
collected: '2026-09-07'
category: LLM
direction: AI 搜索 · 训练无关策略优化
tags:
- Training-Free Optimization
- Inventory-Grounded
- AI Search
- Policy Guidelines
- LLM Judge
- A-B Test
one_liner: 训练无关地把动态库存证据与可复用决策指南解耦，提升 AI 搜索 CTR 并减少坏例
practical_value: '- 把策略规则与库存事实分离：不要往 prompt 里写具体 item/类目是否存在，而是写成条件化、可执行的 Guideline，运行时注入
  inventory portrait；库存变动时不必频繁改 prompt 或重训。

  - 用离线 stochastic rollouts + LLM Judge 分组：同 query 同时有成功/失败轨迹才形成对比样本；全失败组用 inventory-guided
  exploration 主动回查漏召回路由，避免把“无库存”误判为“策略差”。可迁移到电商搜索 bad case 聚类与策略补丁生成。

  - 上线前做回放回归门控：每个候选 Patch 必须在 Target queries 和 Background/fixed regression set 上通过胜率、Precision/Recall/F1
  drop 阈值；组合时逐个加入并全量回放，可控制 prompt/规则更新的回归风险。

  - 轻量服务化：Guideline store ≤100，每阶段最多注入 3 条、平均 1.7 条，prompt 增量平均 247 tokens，latency
  p50 仅 +49ms；适合作为电商 AI 搜索/导购 Agent 的策略层。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：早期 AI 搜索/导购面对频繁变动的商品库存，item 上下架、属性缺失、运营规则变化快，不能把当前 catalog 写死进 prompt 或策略；微调/RL 需要标注与稳定 reward，静态 prompt patch 很快过时。核心难点是区分“检索/排序策略失败”与“当前库存确实无匹配”，否则 trace 优化会把瞬时库存事实编码进策略。

**方法关键点**：
- 在线：对每个 query 先 probing inventory，构建 inventory portrait：probe confidence、per-category density/field stats、scene profile（coverage gaps、recent changes）；再按 scene+stage 检索并注入 Policy Guidelines 到 Retrieval/Selection prompt。
- Policy Guideline 只写条件化决策规则（如何利用库存证据），不写具体 item/类目存在性；用 scene tag + stage tag 索引。
- 离线：固定 inventory snapshot 下做 N=5 stochastic rollouts，LLM Judge 标注 success/failure/uncertain；同 query 有成功/失败才形成 contrastive。全失败 query 进入 inventory-guided exploration，最多 K=10 轮主动找漏召回路径。
- Patch proposal 用 DeepSeek-V3 671B 生成 add/revise/merge/delete，候选必须通过 Target/Background/fixed regression gates 回放才可上线。

**关键结果**：
- 离线 native：Candidate Recall@30 0.691→0.847，F1@8 0.643→0.816，false no-inventory 30.6%→4.8%，false match 60.8%→15.2%。
- 14 天线上 A/B：全流量相对 CTR +3.17%（95% CI 1.9–4.5%），audited bad case 减少 38.9%；Composite 查询 CTR +7.19%，inventory-absence bad case 从 45/128 降到 14/125。
- 开销：prompt 平均 +247 tokens / p95 568，latency p50 +49ms / p95 +186ms；Guideline store ≤100，每阶段最多注入 3 条。

最值得记住的一句话：不要让策略记住当前有哪些 item，而是教它在运行时读库存证据并执行条件化决策。
