---
title: Can Search Agents Correct Their Own Errors? Evaluating Retrieval, Evidence
  Delivery, and Answer Completion
title_zh: 搜索 Agent 能否自我纠错：检索、证据传递与答案完成评测
authors:
- Venkata Pagadala
- K. Rajasekhara Rao
- Pratyay Ganguly
affiliations:
- KL University
- Indian Institute of Technology Kharagpur
arxiv_id: '2611.30243'
url: https://arxiv.org/abs/2611.30243
pdf_url: https://arxiv.org/pdf/2611.30243
published: '2026-11-23'
collected: '2026-11-24'
category: Eval
direction: 搜索 Agent 错误恢复的分段诊断评测
tags:
- search agents
- RAG
- evaluation
- knowledge conflict
- abstention
- evidence delivery
one_liner: 回放模型自身错误答案并干预证据，分段诊断搜索 Agent 在检索、证据传递和作答完成上的失效
practical_value: '- 在对话式购物助手/企业搜索中，把“错误恢复”拆成检索召回、证据进上下文、证据使用、最终作答四段分别埋点评测；不要只看最终答案，否则无法定位是
  ranking 还是生成问题。

  - 对于“用户坚持错误答案”的场景，不要只优化模型不盲从；观察 abstention 与重复错误的比例，像 gpt-oss 一样可能以“无法确认”代替复述，这会影响体验但风险不同，需要分别监控。

  - 直接注入权威证据（如商品政策、活动规则）比仅把相关文档置顶更有效：本文中 direct passage delivery 提升 Qwen3.5 51 pp，而
  gold page rank 1 仍常不被打开；工程上可对高置信权威内容做 snippet 注入/强制上下文。

  - 评估时要使用所有 episode 作为分母，分别报告正确、复述错误、其他错误、abstain、无答案/超预算；特别关注“模型烧完搜索预算但无答案”的 completion
  failure。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
搜索 Agent 已经给出错误答案后，用户追问或要求确认，系统能否借助后续搜索纠正？常见失败可能来自没检索到、检索到没打开、证据在上下文也没用、或最后没作答。需要分段诊断，才能决定改哪个组件。

**方法关键点**
- 使用 BrowseComp-Plus：830 个多跳问题、约 10 万文档、人工标注 evidence/gold documents。
- 先对每个模型做 closed-book 采样，取模型自己的错误答案作为 prior/candidate，回放到对话中，配 hedged / confident / user insists 三种话术。
- 两个实验：supplied-evidence 无工具，交叉 evidence arm（none/neutral/partial/complete）与 hint arm；search-agent 干预，控制 gold page 排名、direct passage delivery。
- 结果评分：correct、adopts candidate、other wrong、abstain、failure/no single answer，所有 episode 为分母。
- 模型：Qwen3.5-35B-A3B、Nemotron-3-Nano-30B-A3B、Gemma-4-31B-it、gpt-oss-120b；vLLM/H100。

**关键结果**
- supplied evidence 覆盖 709 题、26,665 条件：complete evidence 下多数模型几乎不 adopt hints，但 Nemotron 在 confident hint 下 adopt 27.5%，insist 49.1%；准确率从 73.2% 降至 57.2% 和 40.3%，净 -16.1pp 和 -32.9pp。
- gpt-oss 在 insist 下准确率降 12.6pp，但正确答案更多转为 abstention（8.3%）而非重复。
- 搜索干预：gold page rank 1 后 Nemotron 仅 38%/46% episodes 打开 decisive source，Qwen3.5 40%/36%；direct passage delivery 比 neutral 提升 Qwen3.5 +51.0pp、Nemotron +22.4pp。
- 即使证据在上下文，Nemotron 在 19/51 decisive-delivery episodes 耗尽 20 轮预算无答案。
- 检索深度 5→20 提升 gold recall 8.6pp，但准确率基本不变 +0.5pp。

**最值得记住的一句话**
错误会以不同方式“活下来”：检索失败、打开失败、证据使用失败和作答完成失败，必须分段配对测试才能决定改哪个组件。
