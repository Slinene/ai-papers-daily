---
title: 'Computed, not Memorized: Bit-Factorized Identifiers for Efficient Generative
  Retrieval'
title_zh: 计算而非记忆：面向高效生成式检索的位分解标识符
authors:
- I-Fan Lin
- Zhen Zhang
- Faegheh Hasibi
- Suzan Verberne
affiliations:
- Leiden University
- Shandong University
- Radboud University
arxiv_id: '2610.17467'
url: https://arxiv.org/abs/2610.17467
pdf_url: https://arxiv.org/pdf/2610.17467
published: '2026-10-12'
collected: '2026-10-14'
category: GenRec
direction: 生成式检索 · 数值 DocID 零样本适配
tags:
- Generative Retrieval
- DocID
- Bit-Factorized
- Zero-shot Adaptation
- Multi-tree Beam Search
- Semantic Hashing
one_liner: 将文档向量符号位作为 DocID，结合多树束搜索，实现零训练新文档适配与最低推理延迟
practical_value: '- 新物品/新文档冷启动：可用预训练编码器对物品标题、属性、描述做 tanh 后取符号位，直接生成可打分的二进制 DocID，无需为新
  ID 训练 embedding；通过 weight interpolation（α=0.5）融合通用编码器与任务调优编码器，能在 seen/unseen 间取得平衡。

  - 推理工程：采用 flat token 评分，所有候选 token 在一次 encoder 前向中完成打分，不需要 autoregressive decoder；再用多棵不同
  bit 排列的前缀树做 constrained beam search（h=8），可比单纯增大 beam 更有效地减少早剪枝，提升未见文档召回。

  - 资源与延迟：120-bit DocID 仅需 15 bytes/doc，单 query 延迟 24 ms（A100），显著低于现有生成式检索方法；适合商品库频繁更新、需要低延迟检索的场景，可作为生成式推荐索引层。

  - 局限与改进：平坦 ID 缺少层级先验，高召回略弱；若业务需要 Hit@100 更优，可尝试将 bit-factorized 与 RQ-VAE 等残差量化层级结构结合。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式检索通常需要在训练中记忆 DocID token embedding，导致新文档加入后数值 DocID 几乎无法泛化，而增量训练或模型编辑成本高。需要一种无需重训即可对新文档打分、同时保持推理高效的 DocID 设计。

**方法关键点**：
- 用编码器得到文档 embedding，经 LN + tanh 得到 k 维连续向量，取 sign 作为 k-bit 二进制 DocID；用 InfoNCE 对齐 query/document 表示，得到 DocID 编码器 M1。
- 查询经 M1 初始化编码器输出 zq，再乘以可学习位权重 w 得 uq；文档得分 s(q,d)=bd^T uq。在 seen 文档上训练 retriever M2。
- 对 M1 和 M2 做 WiSE-FT 权重插值：θ'2=0.5θ1+0.5θ2，平衡 seen/unseen 泛化。
- 推理时把 k bits 分成 T tokens，token score 只依赖当前 query 段，无需 autoregressive decoder；用 h=8 棵不同 bit 排列的 prefix tree 做 constrained beam search，合并候选。

**关键实验**：在 NQ320K/TriviaQA 60/40 split 上，unseen 文档 Hit@10 达到 77.74/77.15，比 NCI、DSI、MEVI 等数值 DocID 高 40-60 个百分点；seen 文档 Hit@1 最高。在 MS MARCO 90/10 split 上，零训练 Hit@10 74.5，仅比 DSI++/DOME 低约 3 点。单 query 延迟 24 ms，比 NCI/DSI/MEVI 快 7×，比 SEAL 快 397×，存储 15 bytes/doc。

**最值得记住**：把 DocID 从“训练出的 ID embedding”改为“从文档内容计算得到的符号位”，结合多树束搜索，使生成式检索能对任意新文档零样本打分，同时保持低延迟。
