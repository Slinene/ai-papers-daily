---
title: 'Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories,
  and Reads'
title_zh: Agentic RAG 评估预算：问题数、轨迹数与读取次数的分配
authors:
- Jingjie Ning
- Xueqi Li
- Yibo Kong
affiliations:
- Carnegie Mellon University
arxiv_id: '2610.05034'
url: https://arxiv.org/abs/2610.05034
pdf_url: https://arxiv.org/pdf/2610.05034
published: '2026-10-03'
collected: '2026-10-08'
category: Eval
direction: Agentic RAG 评估预算采样优化
tags:
- Agentic RAG
- Evaluation budget
- Generalizability theory
- Repeated sampling
- Retrieval-feedback comparison
one_liner: 同 token 预算下，扩展问题覆盖比增加读取或轨迹数更有效降低评估标准误
practical_value: '- 评估 agentic RAG / LLM 排序系统时，预算层级可分解为 query/问题数、轨迹/rollout 数、每次
  rollout 的读取/答案重复数；在总 token 预算固定时优先扩 query 覆盖（多问题）而不是多 trajectory 或多 read，尤其在搜索请求费用低（<
  $1/1k requests）时，可显著降低标准误。

  - 用嵌套（nested）或仅问题（Q-only）的 archived forecast 做审计，预测不同预算分配的 SE，误差可在 4% 内；可以在正式大规模评估前用小
  audit 校准预算，避免盲目采样。

  - 温度设为 0 可将答案不一致从 ~14% 降到 ~3.4%，同时比较精度变化不大；对于策略对比评估、离线评测，应默认 temperature=0 减少重复读数需求。

  - 如果系统涉及 search API 费用，要把每千次搜索价格纳入预算分配：搜索费用在 $0–1/1k 时更多问题优先于更多轨迹；但 question vs
  read 的费用排序在当前数据下不确定，需按自身模型/搜索价格重估。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：Agentic RAG 评估预算需在问题数、搜索轨迹数、最终答案重复次数三层分配，不同分配影响策略对比的方差与成本。

方法：基于 HotpotQA 和 MuSiQue 做 retrieval-feedback 比较，用 Generalizability theory 和 repeated sampling 测量 allocation precision、reading efficiency、cost boundaries；构建 nested 与 Q-only 两种归档预测。

结果：在 34.14–34.39M model tokens 预算下，扩展问题覆盖的标准误比 5 次读取低 33%，比 3 条轨迹低 12.6%；nested 和 Q-only 预测误差分别为 4.0% 和 3.5%；depth subsets 未显示超越 two-trajectory audit 的预测优势。单次读取相对同 token 最优分配的方差惩罚为 0–9.9%，Pro 模型不确定性大。费用上，搜索价格 $0–1/1k requests 时更多问题优于更多轨迹；问题 vs 读取的费用排序未解决。temperature=0 将答案不一致从 14.3% 降至 3.4%，比较精度相近。
