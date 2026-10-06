---
title: 'SCOUT: Supply-Aware Cold-Start Proactive Query Suggestion for Travel Search'
title_zh: 供给感知的旅行搜索冷启动主动查询建议框架 SCOUT
authors:
- Hao Li
- Shashank Reddy
- Kedar Bellare
- Ashish Jain
- Stephanie Moyerman
affiliations:
- Airbnb, Inc.
arxiv_id: '2610.05619'
url: https://arxiv.org/abs/2610.05619
pdf_url: https://arxiv.org/pdf/2610.05619
published: '2026-10-04'
collected: '2026-10-06'
category: QueryRec
direction: 生成式 Query 建议 · 供给感知 RL
tags:
- Query Suggestion
- RL
- GRPO
- Cold Start
- Supply-Aware
- LLM
one_liner: 用搜索重排分作免费 RL 奖励，GRPO 把供给感知压进 LLM，零推理成本追平 best-of-8
practical_value: '- 可直接复用「用生产重排器 query-listing 匹配分作为 RL 奖励」：相比在线跑 best-of-N 或 LLM
  judge，重排分在 serving 路径本来就会算，奖励零额外推理；电商搜索/推荐可把现有 ranking model 的 relevance score 拆出来当密集奖励，降低训练成本。

  - 冷启动无点击日志时，可用历史结构化请求（目的地/日期/人群等筛选条件）作为 context 主动生成 query，并用当前 catalog 检索 top K
  后做离线 inventory/diversity 评估；这对新入口、新场景的无样本 bootstrapping 很实用。

  - 若用 DPO 做生成式 query 对齐，注意 diversity collapse 风险；本文中 DPO 的 distinct%@0.9 掉到 11.07，RPO
  加辅助 SFT loss 能恢复，GRPO 则天然更稳。业务里偏好优化建议优先 GRPO 或 RPO，而不是裸 DPO。

  - 把 serve-time best-of-N 的验证成本「一次性摊销进模型权重」可成为部署架构：训练时用 search engine 做 environment
  在线 rollout，线上不再多次检索；对 latency 敏感、库存/广告供给受限的搜索推荐链路很有借鉴意义。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
旅行搜索长期依赖结构化 picker（目的地、日期、人数），没有用户自由文本 query 日志，因此标准 SFT/RLHF 所需的 demand-side 数据缺失；同时旅行库存强物理约束，生成「浪漫海滨别墅」在东京可能无结果，supply-unaware 模型会主动 hallucinate demand。团队需要从结构化 context 直接生成供给可履约的 proactive query suggestion，且不能靠 serve-time best-of-N 带来的高检索成本。

**方法关键点**
- 任务定义：context c=(destination, date range, guest count)，policy 生成 slate S={s1,...,s|S|}，每个 suggestion 无 seed query。
- 无标签评估：用历史参数化搜索作 context；IMR@18 对每个 suggestion 检索 top 18 listings，用人工校准过的 LLM judge 算语义匹配均值；diversity 用 MiniLM embedding 在 cosine 0.9 下 greedy leader-cluster 得到 distinct%@0.9。
- 奖励设计：不直接用昂贵 IMR@18，改用生产 reranker 的 query-listing semantic match score m∈[0,1] 对 top 18 取均值得到 R18；该分数在 serving path 免费产出，rank correlation 与 IMR@18 为 Spearman 0.45。
- 优化：把 live search engine 当 RL environment，LLM 生成 query 后检索返回 supply reward；用 GRPO，group G=8，组内标准化 advantage，clip + KL penalty β=0.06；Qwen3-8B + LoRA rank 32、alpha 64，全 linear layers。

**关键实验**
按 destination 切分 train/eval，|S|=2、K=18，三 seed 均值。SCOUT 相比 Few-shot：R18 +37.63%，IMR@18 +12.30%，diversity 基本持平（83.72 vs 84.03）。RSFT 只 +1.75% IMR@18；DPO 出现严重 diversity collapse（distinct%@0.9 仅 11.07），RPO 用辅助 SFT loss 恢复到 84.04 并获得部分收益；SCOUT 在 zero marginal serve-time cost 下达到 best-of-8 的 inventory 水平，处于 best-of-1 到 best-of-16 的 81% 位置。

**最值得记住的一句话**
把供给验证成本在训练时一次性摊销进模型权重，用搜索系统既有重排分作免费奖励，比 serve-time best-of-N 更可实时部署。
