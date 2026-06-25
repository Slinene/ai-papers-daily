---
title: Extreme Meta-Classification for Large-Scale Zero-Shot Retrieval
title_zh: 大规模零样本检索的极端元分类框架
authors:
- Sachin Yadav
- Deepak Saini
- Anirudh Buvanesh
- Bhawna Paliwal
- Kunal Dahiya
- Siddarth Asokan
- Yashoteja Prabhu
- Jian Jiao
- Manik Varma
affiliations:
- Microsoft Research, Bengaluru, India
- Microsoft, Redmond, USA
- Indian Institute of Technology Delhi, India
arxiv_id: '2606.25237'
url: https://arxiv.org/abs/2606.25237
pdf_url: https://arxiv.org/pdf/2606.25237
published: '2026-06-23'
collected: '2026-06-25'
category: RecSys
direction: 极端分类 · 零样本检索元分类
tags:
- extreme classification
- zero-shot retrieval
- meta-classification
- large-scale retrieval
- sponsored search
- Rademacher complexity
one_liner: 提出 EMMETT 元分类框架，为未见过的物品动态合成分类器，实现零样本检索精度最高 15% 提升，线上 CTR 增益 4.2%
practical_value: '- **冷启动物品快速向量化**：借鉴 IRENE 的“选择已有分类器→元分类器生成”流水线，新商品无需重训模型，只需用 ANNS
  检索少量相似商品的分类器（如 K=3），经单层 Transformer 融合即可上线，延迟仅毫秒级。

  - **训练策略冻结基座**：冻结预训练的编码器和已知物品分类器，仅训练轻量生成器，避免过拟合，使新零样本泛化更鲁棒；业务中可将商品 embedding 和分类器视为固定模块，新增物品只更新生成器。

  - **损失函数设计**：训练时用邻居分类器替代物品自身分类器模拟零样本，加权二元交叉熵强调正样本，该思路可直接迁移到推荐召回或广告匹配的冷启动物品表示学习。

  - **工程化推理解耦**：分类器选择（ANNS）与元分类器生成（单层 Transformer）分离，新物品入池仅需一次生成器前向和索引插入，适合大规模、频繁更新的广告或商品推荐系统。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大规模检索（如赞助搜索广告）中，双塔编码器为实时性必须使用小型模型，缺乏充分世界知识；极端分类方法为每个已知物品学习单独的分类器，精度高但无法处理零样本（新）物品。急需一种既能利用已有分类器知识、又能为未见物品高效生成高质量表示的方法。

### 方法
- **EMMETT 框架**：包含两个核心模块——**分类器选择器 S** 从已知物品分类器中快速选出最相关的少量分类器；**元分类器生成器 G** 融合选出的分类器与物品编码器表示，动态合成新物品的分类器。
- **IRENE 实例**：S 使用最大内积搜索（ANNS）选出 K 个最近邻物品的分类器；G 为单层 Transformer，输入该物品的编码器向量与选中的 K 个分类器向量（配合可学习的类型嵌入），输出元分类器。
- **训练与推理**：冻结预训练编码器 E 和已知物品分类器 W；训练时对每个观察物品，用其邻居分类器（而非自身分类器）生成元分类器，以加权二元交叉熵联合所有查询-物品对，模拟零样本场景；推理时仅需为查询计算编码器向量，从已构建的 ANNS 索引中检索相关物品，新物品的元分类器可即时生成并插入索引。
- **理论保障**：将零样本检索视为二元分类问题，证明 1-vs-all 损失降低方差，冻结分类器避免过拟合，泛化能力与数据规模、生成器复杂度相关。

### 关键实验结果
- **离线指标**：在文档标注、产品推荐、赞助搜索等 6 个不同规模数据集上，IRENE 加到多种基线编码器（DPR、ANCE、MACLR、NGAME）之上，零样本 Recall@10 最大提升 15%，且额外推理开销极小（毫秒级）。
- **在线 A/B 测试**：在大型搜索引擎的赞助搜索广告检索任务中，IRENE 使广告点击率提升 4.2%，验证了真实业务价值。
- **消融实验**：K=3 时效果与效率最佳；Transformer 生成器显著优于简单加权和；冻结原有模块有效防止过拟合并提升泛化。

**核心洞见**：百万量级的已学习分类器包含着几乎全部所需世界知识，将它们智能组合即可为零样本物品“元合成”出高精度表示。
