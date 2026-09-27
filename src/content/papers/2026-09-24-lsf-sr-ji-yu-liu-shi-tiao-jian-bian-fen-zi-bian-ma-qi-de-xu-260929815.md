---
title: 'LSF-SR: Latent Semantic Fusion for Sequential Recommendation via Flow-based
  Conditional Variational Autoencoders'
title_zh: LSF-SR：基于流式条件变分自编码器的序列推荐潜在语义融合
authors:
- Shih-Hong Chen
- Josh Jia-Ching Ying
- Vincent S. Tseng
affiliations:
- National Yang Ming Chiao Tung University
- National Chung Hsing University
arxiv_id: '2609.29815'
url: https://arxiv.org/abs/2609.29815
pdf_url: https://arxiv.org/pdf/2609.29815
published: '2026-09-24'
collected: '2026-09-27'
category: RecSys
direction: 序列推荐 · LLM 语义融合
tags:
- Sequential Recommendation
- LLM
- CVAE
- Normalizing Flows
- Semantic Fusion
- KL Annealing
one_liner: 用流式 CVAE 融合协同 ID 与 LLM 语义，缓解分布错位并提升长尾推荐
practical_value: '- 语义信号只做 item-level 离线 profile：用 LLaMA 生成 item 描述 + SimCSE 抽取语义向量，避免用户级实时
  LLM 调用；电商场景可离线批量构建 item 语义库，推理时只查表。

  - 不要简单 concat 或 late fusion：LLM 语义 embedding 呈现高相似度聚类，协同 embedding 近似高斯，直接用会错位。可借鉴
  CVAE 条件融合 + planar/radial flow 学习非高斯后验，把 item ID 映射到语义条件约束的潜在空间。

  - 训练细节：推荐 loss 用全 catalog softmax，KL 只在序列 item 的随机路径上计算，全 catalog 推理走确定性路径；VAE 融合模块需要
  cyclical KL annealing，避免 posterior collapse，比固定/线性/sigmoid 更稳。

  - 冷启动/长尾收益明显：论文在 tail items 上相对最强 LLM baseline 的 NDCG@20 提升 22.88%/18.50%，说明语义条件能按语义相关度而非流行度放置尾部
  item；适合商品目录长尾、新品冷启动。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Sequential recommendation 只用 ID embedding，稀疏与冷启动问题严重。LLM 语义 embedding 与协同 embedding 分布错位（LLM 聚类、协同近似高斯），直接 late fusion 或独立检索无法对齐；用户级 LLM profiling 推理开销大。

### 方法关键点
- LSF-SR = CVAE + Normalizing Flows：以 LLM 语义 embedding 为条件，把 item ID embedding 变换到共享潜在空间。
- 离线 item 语义获取：LLaMA 3.1-8B-Instruct 生成 item 描述，SimCSE RoBERTa-large 提取语义并线性投影。
- 条件融合：encoder MLP 输出 mu/sigma，reparam 得到 z0；经 planar/radial normalizing flows 变换为 z_K；decoder 以 z_K 和 semantic condition 生成 enhanced item embedding，再进 Transformer backbone。
- 训练：推荐 loss 为全 catalog softmax 的负对数似然；KL 项约束后验；全 catalog logits 用确定性 path，序列 item 用随机 path；采用 cyclical KL annealing。

### 关键实验
五个数据集：Amazon Beauty/Office/Sports/Toys、Yelp；对比 SASRec、DuoRec、FMLP-Rec、SRA-CL 等。LSF-SR 在 R@20 最高提升 12.98%（Sports），NDCG@20 最高提升 14.13%（Sports）；tail item NDCG@20 相对 SRA-CL 提升 22.88%（Beauty）和 18.50%（Yelp）。消融显示 w/o LLM、w/o Flows、w/o KL loss 均下降，cyclical annealing 最优。

### 最值得记住的一句话
用概率生成模型替代确定性融合，配合 flow 提升后验表达力，是协同行为与 LLM 语义空间对齐、显著改善长尾的关键。
