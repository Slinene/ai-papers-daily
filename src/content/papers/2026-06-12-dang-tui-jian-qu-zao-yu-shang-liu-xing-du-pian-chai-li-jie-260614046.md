---
title: 'When Recommendation Denoising Meets Popularity Bias: Understanding and Mitigating
  Their Interaction'
title_zh: 当推荐去噪遇上流行度偏差：理解与缓解其交互
authors:
- Guohang Zeng
- Jie Lu
- Guangquan Zhang
affiliations:
- Australian Artificial Intelligence Institute, University of Technology Sydney
arxiv_id: '2606.14046'
url: https://arxiv.org/abs/2606.14046
pdf_url: https://arxiv.org/pdf/2606.14046
published: '2026-06-12'
collected: '2026-06-15'
category: RecSys
direction: 去噪推荐 · 流行度偏差
tags:
- Denoising Recommendation
- Popularity Bias
- Implicit Feedback
- Long-tail
- Small-loss Heuristic
- PAD
one_liner: 损失去噪可能抑制长尾信号，提出流行度感知门控PAD，在多个基准上取得更优准确-多样性权衡。
practical_value: '- 在工业协同过滤中，若使用损失重加权去噪（如 RCE），可叠加流行度门控：对高曝光商品保持强去噪，对长尾商品减弱去噪，避免误删稀疏但真实的交互信号，公式简单、非侵入式。

  - 评估去噪方法时，除 Recall/NDCG 外应关注 Coverage、Gini 等多样性指标，以发现去噪对头部偏差的放大效应。

  - GMF/NeuMF 等 MF 类模型上 PAD 增益显著；LightGCN 等图模型可能通过邻居传播隐式平滑噪声，此时直接 ERM 可能已足够强，去噪需谨慎引入。

  - PAD 的超参 α（去噪强度）和 η（流行度补偿强度）解耦良好：增大 η 可恢复长尾覆盖，对准确率影响不大，便于业务中灵活调整准确-多样性权衡。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
隐式反馈中存在大量假阳性噪声，去噪推荐常用“小损失启发式”（small‑loss criterion）——损失小的交互更可靠，高损失交互被降权或剔除。但长尾物品因交互稀疏、表示学习困难，其正样本损失常偏高，可能被错误抑制，导致有效监督向头部偏移，加剧流行度偏差。本文针对这一盲区，系统分析了损失去噪与流行度偏差的交互机制。

**方法关键点**
- **条件分析**：定义有效头尾信号比 \(B\)，证明当尾部正样本损失分布相对于头部右移时，单调降权函数会使 \(B\) 增大，即头部信号占比升高，尾部信号被压制。
- **Popularity‑Aware Denoising (PAD)**：提出一个轻量插件框架，对基础去噪权重 \(w\) 进行流行度调制：\(w_{\mathrm{PAD}} = (1-s_i) + s_i \cdot w\)，其中 \(s_i = (\mathrm{pop}(i)/\max\_\mathrm{pop})^{\eta}\)。头部物品 \(s_i\!\approx\!1\) 保留原有去噪能力，尾部物品 \(s_i\!\approx\!0\) 则弱化去噪，避免压制清洁但难学的长尾信号。基础去噪器采用 RCE‑style 重加权 \(w = \hat{y}^\alpha\)。
- 验证时选用低损失验证样本集，以缓解分布偏移。

**关键实验结果**
- 数据集：MovieLens‑100k、Amazon‑Book、Yelp，均保留假阳性噪声。
- 模型：GMF、NeuMF、LightGCN，对比 ERM、RCE、TCE、DeCA、DCF、PLD、UDT 等去噪 baseline。
- 在 GMF 和 NeuMF 上 PAD 几乎全面最优，如 MovieLens 上 GMF‑PAD 的 NDCG@50 较最佳 baseline 提升 8.0%，Recall@50 提升 1.0%；Amazon‑Book 上 NeuMF‑PAD 的 Recall@50 提升 7.3%。多样性指标（Coverage、Gini‑Div）亦明显优于均匀去噪。
- LightGCN 上 ERM 有时更强，表明图传播已具备隐式去噪能力，PAD 仍优于其他去噪 baseline。
- 超参分析：α 控制去噪强度，η 控制流行度补偿，增大 η 可恢复覆盖度而轻微影响 NDCG。BPR 目标下 PAD 同样有效。

**关键结论**
去噪推荐应视流行度而调节：对头部强去噪，对尾部弱去噪，方可保留长尾真信号。
