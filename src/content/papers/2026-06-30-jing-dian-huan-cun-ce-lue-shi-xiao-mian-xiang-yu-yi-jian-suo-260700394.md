---
title: 'When Classic Cache Policies Fail: Learning-Augmented Replacement for Semantic
  Retrieval Buffers'
title_zh: 经典缓存策略失效：面向语义检索缓冲区的学习增强替换
authors:
- Yushi Sun
- Bowen Cao
- Wai Lam
affiliations:
- LIGHTSPEED, Tencent
- The Chinese University of Hong Kong
arxiv_id: '2607.00394'
url: https://arxiv.org/abs/2607.00394
pdf_url: https://arxiv.org/pdf/2607.00394
published: '2026-06-30'
collected: '2026-07-09'
category: Agent
direction: Agent记忆缓存 · 学习增强替换
tags:
- Semantic Cache
- Agent Memory
- Online Learning
- Competitive Ratio
- Retrieval Buffer
- Regret
one_liner: 提出学习增强框架 SOLAR，通过遗憾驱动更新和贝叶斯在线选择，在语义缓存中取得恒定竞争比和 5–75% 的相对提升
practical_value: '- **不要盲信 LRU/LFU**：在语义检索缓存场景（如 Agent 记忆、会话推荐上下文）中，由于缺乏时间/频率局部性，简单的
  FIFO 往往优于经典策略，可作为安全基线。

  - **遗憾驱动的阈值触发**：借鉴 SOLAR 的修改时机决策，仅当累积遗憾超过阈值时才淘汰/插入内容，可大幅降低缓存刷新开销（修改率～17%），适合高吞吐在线服务。

  - **从隐式反馈中学习选择内容**：使用贝叶斯在线学习基于检索命中质量（连续打分）动态选取缓存条目，可迁移到推荐系统中的曝光缓存、实时兴趣表征缓存，提升长尾覆盖与及时性。

  - **缓存容量不是越大越好**：实验发现的倒 U 型关系表明，过大的缓存可能引入噪声，可尝试将容量视为噪声控制开关，关注“工作集”而非全量存储，避免无效检索干扰。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM Agent 普遍依赖检索缓冲区复用历史经验，但缓存替换策略多凭经验，经典算法（LRU、LFU）在语义检索下因缺少时间局部性和频率集中而表现不佳，甚至不如简单的 FIFO。需要一种针对语义命中质量连续、匹配靠嵌入相似度的缓存管理方法。

**方法关键点**：将问题形式化为带切换代价的在线语义缓存替换。提出 SOLAR 框架：修改时机由**遗憾累积**驱动——仅当累积遗憾超过阈值才触发替换，修改率可低至 17%；内容选择采用**贝叶斯在线学习**，从每一次检索是否命中及命中质量（连续值）中学习，动态决定应保留哪些经验条目。理论上证明了 SOLAR 的竞争比 ≤3，与缓存大小 K 和序列长度无关（对比 FIFO 为 Ω(K)）；驱逐遗憾为 O(√(KT log T))，匹配下界至对数因子。

**关键结果**：在 MemoryBench 两个对话数据集上，缓存紧张时相对 FIFO 提升 5–75%；在缓存容量接近工作集大小时出现性能相变。合成实验发现池大小与检索质量呈**倒 U 型**，说明容量限制是检索噪声控制手段，而非单纯的存储约束。
