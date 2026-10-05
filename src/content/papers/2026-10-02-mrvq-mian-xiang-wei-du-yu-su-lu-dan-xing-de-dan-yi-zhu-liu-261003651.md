---
title: 'MRVQ: One Resident Index for Dimension- and Rate-Elastic Vector Search'
title_zh: MRVQ：面向维度与速率弹性的单一驻留向量索引
authors:
- Sean Culatana
- Shang-En Huang
- Kang Li
affiliations:
- Atlassian
- National Taiwan University
arxiv_id: '2610.03651'
url: https://arxiv.org/abs/2610.03651
pdf_url: https://arxiv.org/pdf/2610.03651
published: '2026-10-02'
collected: '2026-10-05'
category: RecSys
direction: 向量检索 · 弹性量化索引
tags:
- MRVQ
- Residual Vector Quantization
- Matryoshka
- Dense Retrieval
- Vector Compression
one_liner: 用一个残差量化索引通过残差阶段和坐标前缀两种截断，同时服务多种维度与码率，大幅节省驻留内存
practical_value: '- 在需要同时支持多 embedding 维度（Matryoshka prefix）和多压缩率（4/8/16 B/vector）的召回/检索场景，可用单个残差量化器替代每个配置存一套索引：训练时对多个前缀维度加权重建误差，服务时用
  stage 前缀控制码率、坐标前缀控制维度，大幅减少内存和部署复杂度。

  - 工程实现上，残差量化 stage 天然提供嵌套码长：只存最大码（本文为 16 B/vector），解码时截断前 b stages 即可得到低码率版本；query
  保持 floating point 不对称打分，容易接入 Faiss 等现有 PQ/OPQ 检索链路。

  - 对商品库更新快、需要频繁重建索引的电商/多租户场景，PCA-scalar 方案（PCA 旋转 + 按方差分配标量位 + 逐坐标量化）质量与 RaBitQ 相当，但拟合速度中位数快
  420 倍，适合近实时构建。

  - 注意两个负面结论：高 rate 下 QINCo2 可能训练 collapse，若复现需做稳定性处理；基于 residual energy 的 ranking
  bound 预测未达标，不能用于质量保证。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
Dense retrieval 在 RAG 和 agent 系统中，文档 embedding 与索引状态常主导驻留内存。部署需要同时支持维度弹性（Matryoshka prefix）和速率弹性（不同字节码），但按速率单独训练量化器会保留多套 code streams 和量化器状态，内存开销大。

**方法关键点**
- 对一个预先冻结的 embedding 集合训练 L=16 阶段的残差向量量化器（RVQ），每阶段 256 个 codeword，每个 stage index 占 1 字节；解码前 b 个阶段即得到 b-byte 码，实现速率弹性。
- 训练损失对多个 embedding prefix 维度加权重建误差（本文均匀覆盖 prefix menu），使同一 codebook 在坐标前缀截断时仍保持质量，实现维度弹性。
- 服务时选择 (m,b)：只解码前 b stages 并取前 m 维坐标，不需要额外重编码或存储低 rate 版本。驻留内存公式：R_MRVQ = 4LKD + 16n bytes（fp32 codebooks + 16 B/vector）。
- 另评估低成本 PCA-scalar 设计：PCA 旋转，按坐标方差分配标量位，逐坐标量化；无迭代训练。

**关键实验**
- 数据集：BEIR FiQA（57,638 docs）与 NFCorpus（3,633 docs）；四个 embedding 家族：MPNet、Mxbai、Nomic、BGE；指标 nDCG@10。
- 对比：按 rate 单独训练的 QINCo2、共享模型的 QINCo2、PQ、OPQ、AdANNS-OPQ、RaBitQ 等。
- 内存：MRVQ 在全部数据集/家族上为最低 RAM 配置，占 12.06–16.88 MiB；比三个单独 QINCo2 少 17.8–22.0 倍，比最精简共享模型少 1.89–2.02 倍。
- 质量：单独 QINCo2 比 MRVQ 高 0.026–0.107 nDCG@10（FiQA），构成两个 Pareto 角；但 MRVQ 在匹配码长下超过 PQ、OPQ、AdANNS-OPQ。
- PCA-scalar 与 RaBitQ 质量差异 <0.008 nDCG@10，拟合速度中位数快 420 倍。负结果：高 rate QINCo2 在部分种子/家族上训练 collapse；基于残差能量的 ranking bound 未达预设标准。

**最值得记住的一句话**：MRVQ 用 stage 前缀和坐标前缀两级截断，把一个最大速率残差码同时转换成多档速率和维度的索引，以小幅质量代价换取 17.8–22 倍内存节省，适合内存敏感、需要弹性检索的部署。
