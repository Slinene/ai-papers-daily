---
title: 'The Scheduler Is a Hidden Retriever: How Asynchrony Shapes Evidence Acquisition
  in Search Agents'
title_zh: 调度器是隐藏的检索器：异步如何塑造搜索 Agent 的证据获取
authors:
- Ruiyang Ren
- Yuhao Wang
- Yinan Zhang
- Chunyan Miao
affiliations:
- Nanyang Technological University
arxiv_id: '2610.26310'
url: https://arxiv.org/abs/2610.26310
pdf_url: https://arxiv.org/pdf/2610.26310
published: '2026-10-19'
collected: '2026-10-20'
category: Agent
direction: 搜索 Agent · 调度不变证据获取
tags:
- schedule invariance
- search agents
- asynchronous execution
- evidence acquisition
- CEA
- retrieval stability
one_liner: 证明送达顺序会改变搜索 Agent 的检索决策与证据获取，并提出 CEA 实现调度不变且免全局等待的稳定证据获取
practical_value: '- 电商搜索/Agent 中多个并行召回或商品信息调用返回顺序会改变 query 改写或目标 item 选择；要获得可复现的召回质量，应让子任务等自身证据域完整后再决策，而不是固定到达数量后
  early commit。

  - 共享搜索/召回预算时，不要用“先完成先执行”的竞争分配；即使本地 query 生成稳定，最终召回集合仍会随完成顺序漂移。可改为预先固定优先级，例如按 domain
  索引或 question-seeded hash 分配。

  - 将上下文按证据域/子任务隔离，不要把全部并行结果注入同一份共享 notes；文中私有历史减少 40.2% 输入 tokens，且能降低无关上下文对决策的干扰。

  - 工程上把等待全部结果的全局 barrier 改成每个证据域 complete 后立即局部推理，可提前首个决策与最终响应（约 3–8 秒），适合在线 Agent
  的延迟优化。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

语言模型 Agent 越来越多通过并行推理和异步信息获取解决复杂任务。同一批初始证据，送达顺序不同，可能改变 Agent 最终获取的附加证据；即使最终都拿到相同文档，检索路径也可能不可复现。这种“调度即隐藏检索器”的现象，对需要审计证据链的 Web/搜索 Agent 是可靠性问题。

**方法关键点**

论文用固定 evidence packet 和冻结 BM25 检索器，在不同 delivery order 下回放搜索 Agent 决策，分离调度效应与检索内容/延迟效应。核心概念是 schedule invariance：改变送达顺序，搜索决策、检索文档集、答案分布应保持不变。

为恢复稳定性和有用性，提出 Confluent Evidence Acquisition (CEA)：
- 按子问题将初始文档划分为 dependency domains，分支在其所有证据到齐后立即开始推理，不等待无关结果。
- 同一分支按 canonical order 处理证据，保持私有 notes，避免并发分支污染上下文。
- 共享搜索预算由 schedule-independent 分配规则决定，例如固定优先级或 question-seeded hash，而非 first-ready 竞争。
- 最终答案按 domain 索引合成，搜索反馈只进入选中分支，保证局部决策、执行检索与答案联合分布不受送达顺序影响。

**关键结果**

在 2Wiki、HotpotQA、MuSiQue 上，用 DeepSeek-V4-Flash 与 GPT-5.6 Luna 评估。early commitment（2/6 arrivals）的检索集合 disagreement 比 same-order repeat variation 高出 11.6–23.8 pp；输入完成后 probe 仍有 5.5–14.7 pp 差异，说明早期调度会持续影响后续搜索。CEA 在 question-only plans 下，acquisition disagreement 降至 0.6、-0.2、1.0 pp，接近 repeat variation；准确率与完整输入控制相当，较 early commitment 最多提升 12.6 pp（2Wiki）。高争用条件下，first-ready allocation 增加 21.6 pp acquisition disagreement，而固定优先级保持一致。CEA 还使首个子任务决策提前约 8 秒、最终响应加快 3.1–3.9%，并减少 40.2% 输入 tokens。

**最值得记住的一句话**

调度器是隐藏的检索器：送达顺序决定哪些已到证据能引导下一次查询；通过局部证据完整 + 调度无关分配，可以同时获得稳定、可复现的检索与异步进度。
