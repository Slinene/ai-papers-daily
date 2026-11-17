---
title: 'Jetriever: Shifting Agent Memory Retrieval from Similarity to Utility'
title_zh: Jetriever：将智能体记忆检索从相似度转向效用打分
authors:
- Ruizhe Li
- Licheng Zhang
- Mingxuan Du
- Zhendong Mao
affiliations:
- University of Science and Technology of China (USTC)
arxiv_id: '2611.21478'
url: https://arxiv.org/abs/2611.21478
pdf_url: https://arxiv.org/pdf/2611.21478
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: Agent 记忆检索 · 效用打分
tags:
- Agent Memory
- Utility Retrieval
- Decision Model
- RLCD
- InMind
one_liner: 用 LLM 决策模型 Jev 对每个候选记忆做效用打分并全量重排，在 InMind 隐含关联任务上 R@1 84.8%，远超 BM25 的 1.6%
practical_value: '- 在 RAG/记忆检索中不要只依赖 BM25 或 embedding 相似度：对隐式偏好、跨域关联场景（如用户过敏史→商品成分禁忌、营养需求→食谱推荐），可用
  LLM 决策模型对候选记忆做 utility 打分，判断每条记忆是否对当前 query 的回答有贡献。

  - 全量重排可行：当候选池在几百到几千规模时，用结构化决策模型（如 Jev 这类 System One 模型）逐条打分，并配合 50-100 并发，6k+ pairs
  可在约 90 秒完成，单 query 成本仅 0.8-3 美分；适合做精排或作为高召回后的 reranker。

  - 普通 LLM 直接给概率容易“端水”，排序区分度差：Jev 通过 RLCD 训练输出 calibrated 决策分数，比 Qwen3.5 9B 的 answer-token
  概率更擅长把决定性证据排到第一；在需要排序的场景，可优先选择结构化决策输出而非自由文本生成。

  - 候选粒度影响效用排序：在 InMind 上，用完整 exchange 比用整段 session 的 R@1 从 49.6% 提升到 84.8%。做记忆/会话索引时，建议按语义单元或短片段切分，避免长上下文淹没关键信息。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**

传统 Agent 记忆检索沿用搜索引擎的相似度逻辑：BM25 或 embedding 找与 query 文本相近的记忆。但当有用记忆与 query 无词面重叠时，这种检索失效。InMind benchmark 暴露了这一点：用户说过坚果过敏，之后问“马卡龙食谱怎么做”，马卡龙含杏仁粉，但 query 里没有 nuts；BM25/MiniLM 几乎找不回这条过敏记忆。Jetriever 把目标从“相似”换成“有用”：对每一条已存记忆打分，判断它对当前 query 的回答是否有帮助。

**方法关键点**

- 使用 Jev，一个 LLM-derived System One decision model，用 RLCD 训练输出结构化决策和概率，而非自由文本；Jev 接收 (query, memory) 对，输出 usefulness 分数。
- 全量重排：对每个候选记忆独立打分 s(q, mi)，按负分数排序取 top-k；答案生成器只看到 top-k 记忆，不看分数或理由。
- 避免 query expansion：不要求 agent 在检索前猜出所有潜在关联，而是直接检查已有记忆。
- 候选粒度：完整 exchange 比 session 更优；短 exchange 利于判断。

**关键实验**

InMind-125：相同 241 candidates per query，Jetriever R@1=84.8% vs BM25 user-turn 1.6%、MiniLM 0.0%；R@5=92.0%。端到端 Application 76.0%，对比最强 baseline 14.4%，backbone target-in-context 84.0%。20-question Jev vs Qwen3.5 9B vs Laya：Jev 和 Qwen3.5 9B 都能找到 90% gold（rank 50），Laya 只有 30%；但 rank 1 Jev 85% vs Qwen 40%，说明 Jev 的分数更有区分度。MAB 60 题样本：Jetriever 55.4% vs ReFind 44.3%。成本 $0.00834/InMind query，$0.03103/MAB query；批处理 6,446 pairs 90.16s @100 并发。

**最值得记住的一句话**：找对答案有用的记忆，而不是找听起来像 query 的记忆。
