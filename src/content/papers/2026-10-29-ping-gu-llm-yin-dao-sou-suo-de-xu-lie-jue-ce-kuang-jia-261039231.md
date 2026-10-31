---
title: A Sequential Decision Framework for Evaluating LLM-Guided Search
title_zh: 评估 LLM 引导搜索的序列决策框架
authors:
- Siqing Huo
- Andrew Parry
- Debasis Ganguly
- Mark Smucker
- Charles L. A. Clarke
affiliations:
- University of Waterloo
- University of Glasgow
arxiv_id: '2610.39231'
url: https://arxiv.org/abs/2610.39231
pdf_url: https://arxiv.org/pdf/2610.39231
published: '2026-10-29'
collected: '2026-10-31'
category: Eval
direction: LLM 搜索策略的统一评估框架
tags:
- LLM-guided search
- sequential decision
- high-recall IR
- evaluation
- query reformulation
- multi-armed bandit
one_liner: 将 LLM 引导搜索抽象为 select/spawn 序列决策，统一评估高召回检索与 deep research 策略
practical_value: '- 做 Agentic Search / RAG 搜索策略时，把每次决策拆成 `select`（继续看当前召回 list）和 `spawn`（重新生成
  query 或换召回通道），可以统一 A/B 不同策略，避免只按最终答案做黑盒评估。

  - 电商搜索改写长尾 query 时，可借鉴「批量 query reformulation + Move-to-Front」：一次性生成多路 candidate
  queries / 召回 lists，再动态把近期能出相关结果的 list 调到前面轮转；这比固定只走单路或仅前向探索召回更高，但要显式设置 spawn quota
  或连续无效结果阈值，否则 LLM 判断成本会显著上升。

  - 检索底座和策略同等重要：SPLADE 与 hybrid reranker 在所有策略下都比 BM25 更高效。业务上先把底层召回/精排做扎实，再叠加搜索策略，不要只优化
  policy。

  - 评测指标可以按预算场景重构：高召回或商品覆盖场景用 recall@R 或有效 nugget 覆盖率，而不是只看 DCG@K；同时可以把停止规则设成全局连续无关结果数，衡量单位
  LLM 判断成本下的收益。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 驱动的 RAG 和 deep research 系统会迭代生成 query、检索文档、阅读内容并用结果指导下一步搜索。系统自主搜索时，必须显式决定探索哪些 search trajectory、优化什么目标。现有端到端基准只看最终答案，无法刻画搜索策略本身。因此需要一个统一框架描述、比较和评估不同搜索策略。

## 方法关键点
- 将搜索环境建模为有状态 ranked lists 集合；每步执行两种原语动作之一：`select` 从现有 list 继续向下判断文档，`spawn` 通过 query 生成/改写/rerank 创建新 list，并立即观察其第一个文档。
- 每次动作产生一次文档 observation，更新 search state，并获得 task-specific reward；目标为加权累计奖励 ∑ w(t) r_t，可覆盖 DCG、RBP 及高召回预算目标。
- 在高召回检索 HRIR 场景下，w(t)=1(t≤J)、r_t 为二元相关性，等价于在预算 J 内最大化命中相关文档数；J 可按已知相关文档数 R 归一化为 recall@R。
- 现有策略如 adhoc、Move-to-Front、Thompson sampling、Interactive Search and Judging、Continuous Active Learning 都可表达为 select/spawn policy；query reformulation 只定义如何生成新 list，何时 spawn 仍由 policy 决定。
- 实验用 TREC Deep Learning 2019，GPT-4o-mini 做相关性判断，GPT-5 负责 spawn，DSPy 做 query reformulation；对比 BM25、SPLADE-v3、TCT-ColBERT-v2 与 hybrid MonoT5/DuoT5 四种检索管道。

## 关键实验
- 共 16 个 run = 4 种策略 × 4 种检索管道，按 recall@R 评估。
- Query Reformulation + MTF 在所有检索管道和预算下召回最高；SPLADE + 该策略整体最佳，且与所有 BM25 策略的 95% bootstrap 置信区间无重叠。
- 固定全局预算下，QR+MTF 召回高但会消耗更多 LLM 判断；Adhoc 判断效率最低；检索管道与搜索策略对性能影响同样重要。

## 一句话
LLM 引导搜索不应只看最终答案，而应显式评估“继续看哪个已有排序”和“何时生成新 query”这两类搜索决策。
