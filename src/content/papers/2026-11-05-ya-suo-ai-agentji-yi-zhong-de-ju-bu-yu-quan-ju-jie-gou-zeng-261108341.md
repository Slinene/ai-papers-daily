---
title: Enhancing Local and Global Structure in Compressed AI Agent Memory
title_zh: 压缩AI Agent记忆中的局部与全局结构增强
authors:
- Henry Han
arxiv_id: '2611.08341'
url: https://arxiv.org/abs/2611.08341
pdf_url: https://arxiv.org/pdf/2611.08341
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: Agent记忆向量压缩优化
tags:
- Vector Quantization
- Product Quantization
- Agent Memory
- Embedding Compression
- Local Fidelity
- Global Fidelity
one_liner: 提出局部感知量化LAQ，在保持字节与搜索开销不变下首次用全局保真度界驱动OPQ码本优化
practical_value: '- 在电商/推荐向量召回中，对物品/用户 embedding 做 PQ 压缩时不能只盯 top-k 召回率，还需检查全局结构是否被破坏：可复用论文的局部保真度
  L 和全局保真度 G 作为无标签评估指标，快速发现类目漂移或主题错乱。

  - 借鉴 LAQ 思路：在训练 PQ/OPQ 码本时增加 far-hinge 正则项，显式约束远距离对之间的序关系，避免“高分局部召回但全局混乱”的隐性风险，无需增加字节或改动线上检索。

  - 若线上已使用 rescored binary codes 或 PCA 压缩，注意 rescoring 只提升局部邻居但会改变远距离结构，易造成主题漂移（如实验中
  10.1% 段落跳变）；建议改用 LAQ 这类联合优化，或至少监控全局保真度。

  - 对于 Agent 记忆系统，压缩记忆前应同时考虑后续的 consolidate/delete/compare 操作依赖全局关系，仅用 recall@k 评估会漏掉大量错误；可引入
  G 指标作为上线门禁。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：AI Agent 将文本存储为 embedding 并压缩以节省成本，但现有压缩评估只看最近邻是否存活（局部保真度 L），而 Agent 还需执行记忆整合、删除、比较等依赖远距离结构的操作，全局结构被忽视会引发主题漂移。

**方法关键点**：
- 定义无标签局部保真度 L（10 邻居）和全局保真度 G（30%~50% 记忆占比）。
- 发现 rescored binary codes 在 96 字节下 L=0.97 但将 10.1% 段落移动到另一主题，PCA 8-bit L=0.77 只移动 1.7%。
- 证明全局保真度 G 的损失（1-ν_k）受限于近-远 rank-violation rate 的平方根（2~2.18 倍），该率与压缩距离噪声高度相关（0.979）。
- 提出 locality-aware quantization (LAQ)：将该界转化为 OPQ 码本上的 hinge 目标，保持字节数、旋转和搜索方式不变，是首个由远距离保真度证明驱动的量化器。

**关键结果**：
- 仅用 reconstruction 在 52 个 held-out runs 中提升 G 的次数为 0；far hinge 在全部 52 次中提升 G。
- LAQ 在全部 52 次中提升 G（p=8.5×10⁻⁴），包括外部 FinDER memory。
- 在 12 个 Multi-Doc-2025 runs 中，LAQ 在七种等大小量化器中 G 最高，扩展到百万级段落，并保持证据召回。
