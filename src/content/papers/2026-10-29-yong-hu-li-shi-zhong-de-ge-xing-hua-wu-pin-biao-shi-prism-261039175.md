---
title: 'PRISM: Personalized Item Representations in User History'
title_zh: 用户历史中的个性化物品表示 PRISM
authors:
- Renzhi Wu
- Zikun Cui
- Junjie Yang
- Li Sheng
- Yongjun Xie
- Jerry Fu
- Nipun Mathur
- Sri Reddy
- Hong Li
affiliations:
- Meta MRS
- Facebook Discovery
arxiv_id: '2610.39175'
url: https://arxiv.org/abs/2610.39175
pdf_url: https://arxiv.org/pdf/2610.39175
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 序列推荐 · 个性化历史表示
tags:
- Sequential Recommendation
- Personalized Embeddings
- Autoencoder
- Scaling Law
- Industrial RecSys
one_liner: 复用上游排序计算，为每个用户-物品对生成个性化历史嵌入，提升下游序列推荐质量
practical_value: '- **复用上游排序器中间状态**：不需要为历史序列单独训练一个 user-item 模型，而是从现成的 ranker 中提取
  user tower、user-item tower 和 session mixing 的隐藏层，用 autoencoder 压缩成一个固定维度的 event
  embedding。这样可以把昂贵的个性化计算摊销到上游推理，下游只读取轻量向量。

  - **多层状态联合压缩**：将 user 状态、pair 状态、同请求候选混合状态的所有层 concatenate 后做归一化，再用一个带重构损失的 autoencoder
  压缩到 128 维。注意对每一部分做 per-part normalization 控制尺度，并用 softsign 限制输出范围；重构损失只更新 encoder/decoder，不干扰主任务。这比只取最后一层或简单
  pooling 信息更丰富。

  - **个性化历史长度存在幂律收益**：实验测得 NE 提升随历史长度 L 呈 ~L^0.468 增长，说明保留更多个性化事件是有持续收益的，但边际递减。业务上可以据此做
  ROI 分析，选择合适的历史长度与存储成本。

  - **工程落地细节**：导出的 embedding 采用 INT8 量化，附带时间戳和生成器版本，下游通过版本化投影矩阵读取，兼容模型迭代。这种版本管理对线上推荐系统很实用，避免旧
  embedding 失效。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：传统序列推荐中，历史物品的初始 embedding 由共享的 item embedding 表得到，同一物品在不同用户历史中完全相同，无法表达用户与物品的个性化关系（如一个烹饪视频对普通观众和美食创作者意义不同）。本文提出个性化物品表示：每个历史条目应该表达“该物品与该用户在该时刻的关系”，从而为后续序列建模提供更丰富的输入。但直接为每个历史事件训练一个 user-item 模型成本过高，因此考虑复用推荐系统中已有的上游 ranker 计算。

**方法关键点**：
- PRISM 是一个上游 ranker，在正常打分的同时，为每个用户-物品对生成一个固定宽度的个性化 embedding（event code）。
- 该 ranker 包含三个组件：user tower（用户状态）、user-item tower（用户与物品交互）、same-request candidate mixing（同请求候选间的上下文混合），三者共同刻画用户-物品关系。
- 导出 embedding 时，将三个组件**所有层**的隐藏状态（user 状态、pair 状态、候选特定 session 状态和请求级 summary）拼接，先对每部分做归一化和 stop-gradient，再用一个带重构损失的 autoencoder 压缩到 128 维。重构损失只更新 encoder/decoder，不反向传播到主模型，保证主任务不受影响。
- 压缩后的 event code 与时间戳、生成器版本一起存储；下游使用时通过版本化投影矩阵还原为 token，与普通特征一起进入序列编码器和候选注意力。

**关键实验**：在 Meta 十亿级推荐场景 Surface 1 上离线评估。PRISM 相比 baseline 在 positive engagement 任务上 NE 降低 0.17%，negative 任务降低 0.11%，综合 -0.15%；对比 VISTA 的 -0.07% 提升更明显。在历史长度 26 到 240 事件范围内，NE 增益随长度呈幂律增长（指数 0.468），从 0.06% 增至 0.17%，说明个性化历史长度是一个新的扩展维度。

**最值得记住的一句话**：个性化物品表示把“用户与物品的关系”前置到历史输入中，并通过复用上游排序计算和联合压缩所有层状态，为下游序列模型提供了更丰富的证据，且其收益随历史长度呈幂律扩展。
