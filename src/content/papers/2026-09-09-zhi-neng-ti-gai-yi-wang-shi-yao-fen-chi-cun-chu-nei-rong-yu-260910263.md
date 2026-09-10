---
title: What Should an Agent Forget? Separating What Is Stored from What Is Used
title_zh: 智能体该遗忘什么？分离存储内容与使用内容
authors:
- Yuhang Li
- Yuchen Li
affiliations:
- Beihang University
- East China Normal University
arxiv_id: '2609.10263'
url: https://arxiv.org/abs/2609.10263
pdf_url: https://arxiv.org/pdf/2609.10263
published: '2026-09-09'
collected: '2026-09-10'
category: Agent
direction: Agent 长期记忆的查询条件选择性遗忘
tags:
- selective forgetting
- query-conditioned retrieval
- semantic slots
- memory management
- LLM agents
- rate-distortion
one_liner: 提出 RD-Forget，训练无关地把智能体记忆的存储与查询时使用解耦，通过语义槽替换和意图感知检索实现可逆选择性遗忘
practical_value: '- 用户/商品画像采用 append-only source archive + query-conditioned view：不物理覆盖旧事实，按
  `subject|relation|scope` 槽位管理同槽新值替换旧值；当前推荐/客服回答只注入最新值，历史分析或矛盾处理时可 rescue 旧值，避免过时信息污染当前结果，同时保留时间旅行能力。

  - 对商品动态属性（价格、库存、类目、适用人群）建立 same-slot replacement links；例如价格更新后旧价格对当前意图应被压制，但历史比价/价格走势查询可恢复。这个机制适合电商中的事实变更、用户偏好漂移和冲突消解。

  - 工程实现可复用：固定 token 预算（如 2048）下，用 frozen LLM curator 提取证据、greedy pack 选证据；排序用 lexical
  overlap + active entry 加分 0.4，训练无关、易上线。成本函数 `c(m)=tok(m.text)+8` 直接作为记忆预算约束。

  - 消融结论：不进行遗忘（-FORGET）和不依赖查询的通用记忆（-QC）损害最大，因此优先做 query-conditioned curation 和 supersession；slot
  grouping 和 historical rescue 是次要但一致的增益，可后续迭代。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**

持久化语言智能体面临两个决策：存储什么、用什么影响当前回答。一个过时事实可能误导当前状态查询，却又对历史查询仍有价值。传统记忆管理要么删除/覆盖旧事实，破坏历史访问；要么不遗忘，让过时信息污染当前回答。因此需要把“存储”与“使用”分离，让遗忘成为一个查询局部决策，而非全局删除。

**方法关键点**

RD-Forget 保留一个 source archive 全量观察，同时构建 query-conditioned memory view 控制证据对答案的影响。冻结 LLM curator 从历史中提取原子证据，按语义槽 `subject|relation|scope` 分组；同槽 replacement links 标记 superseded，当前状态查询可抑制旧值，但保留 archive 供历史意图重新召回。retrieval 按 active/deprecated/superseded 状态决定 eligibility，并结合历史意图 rescue。构造 answer-time view 采用 rate-distortion：在 memory budget B=2048 下，成本 `c(m)=tok(m.text)+8`，greedy pack 选择证据；排序用 lexical overlap，active entry 加分 0.4。curator 同时被要求保留多跳推理所需的互补关系链，避免只取直接匹配证据。

**关键结果数字**

主评估覆盖 AMB-Text、LME-KU、MAB-FC 共 264 个任务，四个 backbone Qwen3.5-flash、GPT-5.6-Luna、MiniMax-M2.5、Kimi-K2.5。相比 ACE 和 ReasoningBank，RD-Forget 在 AMB-Text 上领先 1.16–19.77 个百分点，LME-KU 上领先 6.41–25.64 个百分点，事实整合上领先 11–26 个百分点。Luna 消融中，-FORGET 相比 matched Full 分数下降最多：AMB-Text 91.86→68.60，LME-KU 93.59→60.26，MAB-FC 74.00→51.00；-QC 其次；-CLOSURE、-RESCUE、-SLOT 也有一致但较小的下降。query-intent 扩展中，RD-Forget 在 BEAM 和 PersonaMem 全部 8 个模型/基准组合上领先，BEAM 优势 8.47–15.67 点，PersonaMem 优势 10.88–20.72 点。

**最值得记住的一句话**

把“遗忘”从存储删除变成回答时的使用控制，配合语义槽替换和可恢复历史访问，是应对变化事实和未来问题的实用方式。
