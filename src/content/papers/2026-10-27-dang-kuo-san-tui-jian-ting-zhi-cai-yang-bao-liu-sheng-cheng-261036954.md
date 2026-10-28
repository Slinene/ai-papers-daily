---
title: 'When Diffusion Recommenders Stop Sampling: Preserving Generative Diversity'
title_zh: 当扩散推荐停止采样：保留生成多样性
authors:
- Louis Castres Saint Martin
- Alain Rakotomamonjy
- Patrick Gallinari
affiliations:
- Criteo AI Lab
- Sorbonne Université
- CNRS
- ISIR
arxiv_id: '2610.36954'
url: https://arxiv.org/abs/2610.36954
pdf_url: https://arxiv.org/pdf/2610.36954
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 潜在扩散与采样多样性
tags:
- Diffusion Recommender
- Latent Diffusion
- Sequential Recommendation
- Generative Diversity
- Posterior-Predictive Aggregation
- Diversity-Accuracy Trade-off
one_liner: DARTS 用三阶段潜在扩散解耦表示学习、生成与排序，缓解采样坍缩并提升排序精度
practical_value: '- **业务上可直接复用三阶段解耦**：先用 masked item modeling 冻结 item latent space，再在固定
  latent space 里训练 diffusion，最后只 fine-tune decoder 做排序。不要在图里一边训扩散一边让 representation
  漂移。

  - **不要在 diffusion 轨迹上加 catalog cross-entropy/ranking loss**：实验表明哪怕 α=0.1 的 CE 也会把采样方差比
  R 从 0.30 打到 0.14、PR 从 4.7 打到 1.5，且 NDCG 不升反降。生成阶段就只做 latent regression，排序监督延迟到 decoder。

  - **推理时用 posterior-predictive aggregation**：同一 context 采样 M 个 latent，decoder 输出的
  catalog softmax 做算术平均再排序，固定 slate size 下能稳定提升 NDCG。注意吞吐会降，但单样本已经比 DiffuRec 快 3.6
  倍且指标更好。

  - **采样多样性要有独立诊断指标**：只报 Jaccard 会误读低质量乱序；建议同时看 latent 空间的方差比 R 和 participation ratio
  PR，区分“量级小”与“方向坍缩”，避免把 decoder 敏感性当生成多样性。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
序列推荐通常只输出一个确定性排序，但用户历史可能对应多个合理下一步。扩散模型理论上可以多次采样保留多条未来路径，然而论文发现现有 target-item diffusion recommender 普遍出现采样坍缩：同一 context 多次采样得到几乎相同的排序列表。根因被定位为两个常见设计：latent space 与 denoiser 联合训练，以及 denoise 轨迹中加入 catalog cross-entropy/ranking loss。这会造成 diversity-accuracy 两难。

**方法关键点**
- DARTS 采用三阶段 latent diffusion：Stage 1 用 masked item modeling 预训练序列 autoencoder，mask 率 0.4 并强制 mask 最后一项，冻结 latent space；item representation 混合 frozen sentence-t5 语义向量与可学习 id 向量。
- Stage 2 冻结 encoder/decoder/item embeddings，只训练 conditional denoiser。目标是 contextualized next-item latent z0（完整序列中最后位置的 encoder 输出），条件来自 mask 最后 item 的前缀 latent；损失只有 latent RMSE，不含任何 catalog 损失。
- Stage 3 冻结 encoder/denoiser，仅 fine-tune decoder，用 temperature-scaled BPR 和 self-mined hard negatives 校准推理时的 distribution shift。
- 采样诊断：解码后 Jaccard 差异 J、latent 方差比 R、participation ratio PR。

**关键结果**
在 Amazon Reviews 2023 的 Instrument、Scientific、Game 三个数据集上，DARTS 相对最强 baseline 提升 6.8%–12.0% Recall/NDCG；相比 SASRec+T5，NDCG@10 分别提升 11.9%、16.4%、19.5%。Scientific 上 DARTS 的 J=0.30、R=0.30、PR=4.7，DiffuRec 为 J=0.019、R=4.8e-5，ADRec 几乎完全坍缩。消融显示，加 0.1 权重 CE 就把 R 减半、PR 降到 1.5，NDCG@5 下降；联合更新 item representation 会把 R 从 0.300 打到 0.024、NDCG@5 下降 42%。对 M=4 次采样做 posterior-predictive 概率平均，DARTS NDCG@5/10 再提升 3.2%，DiffuRec 几乎无变化。

值得记住的一句话：**把表示空间冻结、把离散排序监督从 diffusion 轨迹中拿掉，才能同时保住生成多样性与推荐精度。**
