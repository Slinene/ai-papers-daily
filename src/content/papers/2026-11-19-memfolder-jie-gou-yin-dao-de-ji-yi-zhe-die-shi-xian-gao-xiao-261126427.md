---
title: 'MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management'
title_zh: MemFolder：结构引导的记忆折叠实现高效 Agent 记忆管理
authors:
- Xuyang Liu
- Chenwen Lu
- Junxi Wang
- Siyu Ren
- Xinying Lin
- Siteng Huang
- Hongli Sun
- Linfeng Zhang
- Honggang Chen
affiliations:
- Sichuan University
- Fudan University
- Sun Yat-sen University
- Zhejiang University
- Shanghai Jiao Tong University
arxiv_id: '2611.26427'
url: https://arxiv.org/abs/2611.26427
pdf_url: https://arxiv.org/pdf/2611.26427
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: 长时 Agent 记忆双轴压缩
tags:
- Agent Memory
- Memory Compression
- Entity Grounding
- Temporal Chaining
- Verified Encoding
- LLM Agents
one_liner: 通过 RecordFolder 减记录数、ContextFolder 减每条 token，实现长时 Agent 记忆双轴无损压缩
practical_value: '- 记忆压缩可借鉴“先折叠条数、再折叠每条长度”的双轴思路：不只对 vector DB 做 pruning，还要同时控制 retrieved
  context token；电商导购/客服 Agent 压缩用户长期画像和对话历史，能直接降低召回延迟与 prefill 开销。

  - RecordFolder 的实体亲和 + 时间链链路可迁移到用户行为序列/订单事件压缩：用 IDF 加权稀有实体重合、Hungarian 匹配限制为非分支链，再按时间顺序让
  LLM summarization，比单纯语义相似聚类更保关键事实。

  - ContextFolder 的 planner–compressor–blind verifier 闭环可作为独立的 prompt/档案压缩质量门禁：盲测压缩结果是否仍能恢复关键事实，无法恢复才修订；适合生成式推荐中的用户
  profile、商品知识、广告素材压缩。

  - 工程上可用作 post-construction 存量记忆压缩，不动原有写入与检索链路；在 Mem0/MemOS 等系统上插入即可获得 30% retention
  下 1.88–5.34× 的检索加速。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：长时 Agent 会积累大量外部自然语言记忆记录，记录数增加会增大索引与检索空间，而多条短记录拼接在一起又会拉长上下文，提高 prefill 和逐 token 解码成本。现有 pruning 会丢证据，consolidation 又常导致单条记录变长，只解决一个维度。

**方法关键点**：MemFolder 用共享 memory groups 做两种折叠。
- RecordFolder：先做实体 grounding 得到 canonical entity 集合；用 density-peak + novelty 渐进选择代表性与互补性兼备的 anchor；再融合稀有实体 IDF 加权的 entity affinity 和 semantic cosine similarity；通过 gain-gated Hungarian matching 只保留正增益 temporal links，形成非分支链并按时间顺序 LLM consolidation，把 N 条记录折叠为 K 个 retrieval units。
- ContextFolder：沿用分组，用 planner 提取原子事实、标注重要性/可推断性并生成 QA checks；compressor 在 token budget 下生成 grammar-based compact encoding（@YYYY-MM-DD、A->B、E:x、~、?）；blind verifier 只看 encoding 和 legend 回答 QA，judge 核对关键事实恢复情况，最多 3 轮反馈修订，必要时 fallback 到原文。

**关键实验**：在 LoCoMo、LongMemEval、PersonaMem、M3-Bench-web/robot 上，对比随机/KMeans/DART pruning 和 ToMe/MemForest merging，以及 LLMLingua-2/BabelTele context compression。Mem0 上 50% record reduction 时，RecordFolder 保留原平均性能的 99.0%，高于 MemForest 的 97.1%；70% reduction 时仍保留 96.6%，MemForest 为 93.3%。再叠加 ContextFolder，LoCoMo/LongMemEval/M3-Bench-robot 每条 token 进一步减少 40.3%/37.9%/31%。30% retention 下检索 mean latency 加速 1.88–5.34×，LongMemEval 从 97.5ms 降至 15.5ms。

**最值得记住**：对长时记忆，可同时压缩“记录条数”和“每条长度”，并通过实体/时间结构与可验证编码控制关键事实丢失。
