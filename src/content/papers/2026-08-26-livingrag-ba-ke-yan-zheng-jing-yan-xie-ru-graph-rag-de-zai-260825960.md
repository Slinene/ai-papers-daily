---
title: 'LivingRAG: Augmenting Graph RAG with Experience'
title_zh: LivingRAG：把可验证经验写入 Graph RAG 的在线复用框架
authors:
- Yuzhuo Cui
- Zongye Zhang
- Qingjie Liu
affiliations:
- State Key Laboratory of Virtual Reality Technology and Systems, Beihang University
- Hangzhou Innovation Institute, Beihang University
arxiv_id: '2608.25960'
url: https://arxiv.org/abs/2608.25960
pdf_url: https://arxiv.org/pdf/2608.25960
published: '2026-08-26'
collected: '2026-08-27'
category: RAG
direction: Graph RAG 在线经验复用
tags:
- Graph RAG
- Experience Reuse
- Multi-hop QA
- Activation Map
- Reasoning Scaffold
- NLI Grounding
one_liner: 提出可写经验存储的 Graph RAG 框架，复用激活图和推理摘要，在多跳 QA 上提精度并降生成 token
practical_value: '- 在线搜索/推荐会遇到大量『同模板不同实体』的 query，如『A 和 B 哪个更省电/更快』。可借鉴 masked template
  相似度匹配历史问题的推理脚手架，只把摘要交给生成模型，不把历史实体直接注入召回，避免污染当前结果。

  - 把历史 query 在图上的实体激活向量作为可复用先验：用当前 query 语义相似度 + 当前 base activation 与历史稀疏 activation
  的 cos 相似度选 top-K，再融合到初始实体激活。电商知识图谱检索里可用它做 query 级 warm start，避免新 query 冷启动重新探索图邻域。

  - 经验写入一定要有质量门：先 novelty 去重，再对答案提取原子 claims 用 NLI 做证据支撑检查。业务 Agent 记忆/知识库写入可参考这种『先廉价
  novelty、后昂贵 NLI』的顺序，既省推理成本又避免错误经验被放大。

  - 成本收益要区分 prompt/completion：经验复用会增加约 3.5% prompt tokens，但能减少 22.7% completion tokens、总
  API cost 降约 12.1%。在生成成本远高于输入成本的 LLM 应用中，这种 trade-off 更划算；同时要注意经验增长，需设计过期、剪枝或 time-decay，动态商品/价格/库存场景更关键。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
在线 QA 流中，Graph RAG 仍逐 query 独立处理，回答后丢弃大部分推理信号。实际流中大量相关查询共享实体、图邻域或问题模板；逐次从零检索和推理既浪费又容易不稳定。因此需要一种可写、可复用的经验机制，让后续相关查询受益。

**方法关键点**
- 基于 LinearRAG（passage-sentence-entity 图 + PPR）增加经验存储；每条经验含 query embedding、稀疏激活图、简短推理摘要、答案、时间戳、grounding confidence。
- 检索增强：用语义相似度 + 当前 base activation 与历史稀疏 activation 的 cos 相似度选 top-K；将激活图加权融合进初始实体激活，再走原图检索，实现图邻域 warm start。
- 生成增强：用 masked template 相似度选择合适经验作为 reasoning scaffold 加入 prompt，不把历史实体直接注入检索。
- 写入门控：先 novelty 去重，再对候选答案提取原子 claims，用 NLI 判断是否被检索证据支持；双门槛都过才写入。存储稀疏激活图和摘要，不存原始 trace。

**关键结果**
在 2WikiMultiHopQA、HotpotQA、MuSiQue(-full)、WixQA 上，LivingRAG 的 LLM-Acc 均超过 LinearRAG 等 strong baselines：MuSiQue-full 58.42 vs 52.71，WixQA 70.25 vs 66.00。在线流 token：加权 prompt +3.5%，completion -22.7%，总 API cost -12.1%（$51.05→$44.87）。写入门控最终只写 27.4% 候选经验；消融显示去掉激活融合、scaffold 或质量门都会掉点。

**最值得记住的一句话**
在线 Graph RAG 复用经验时，最有价值的不是缓存答案，而是复用验证过的图邻域激活与推理模板；用 NLI+novelty 双门控写入，才能让记忆越用越可靠。
