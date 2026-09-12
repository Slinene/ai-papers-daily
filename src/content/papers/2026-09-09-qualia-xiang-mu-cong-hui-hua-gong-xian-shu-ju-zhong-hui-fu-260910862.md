---
title: 'Project Qualia: Recovering Experiential Music Structure from Session Co-occurrence
  Data'
title_zh: Qualia 项目：从会话共现数据中恢复体验式音乐结构
authors:
- Nizam Mohammed
- Abu B. S. Rahman
- Dimuthu D. K. Arachchige
affiliations:
- Independent Researcher
- Hampton University, USA
arxiv_id: '2609.10862'
url: https://arxiv.org/abs/2609.10862
pdf_url: https://arxiv.org/pdf/2609.10862
published: '2026-09-09'
collected: '2026-09-12'
category: RecSys
direction: 音乐推荐 · 会话共现嵌入
tags:
- session co-occurrence
- word2vec
- song embeddings
- artist-residual
- self-supervised learning
- music recommendation
one_liner: 在大规模听歌会话上训练 Song2Vec，通过 artist-residual 去除艺术家主导信号，揭示跨艺术家的体验相似性结构
practical_value: '- **去除主 ID 主导信号的 residual 方法可迁移**：电商/内容推荐中，店铺、品牌、作者、热门品类等主 ID 往往会主导物品
  embedding 空间，掩盖跨主 ID 的隐性语义（如风格、场景、话题）。可以借鉴论文的 artist-residual 做法：计算每个主 ID 的 embedding
  质心，从物品向量中减去，再评估剩余空间的结构。例如在电商中，减去店铺或品牌质心后，可能发现跨店铺的品类风格、价格带或适用场景相似性，用于召回或标签生成。

  - **简单 skip-gram 在大规模会话数据上依然高效**：论文用 Word2Vec 处理 28.6M sessions / 531.6M scrobbles，工程成本低。可作为序列推荐模型的
  item embedding 初始化或冷启动特征，尤其适合只有隐式行为、缺少内容特征的场景（如新 SKU、低频类目）。

  - **用高相似 item pairs 聚类做 embedding 质量评估**：设置 cosine 阈值筛选 cross-ID 高相似对并人工检查聚类主题，可快速验证
  embedding 是否学到有意义的结构，而不需要下游任务指标。业务上可以定期对推荐召回 embedding 做类似审计，发现跨类目/跨店铺的隐性关联。

  - **为 residual 表示作为后续架构输入提供实证基础**：论文后续计划用 JEPA 直接学习体验层；从业者可以尝试把 residual embedding
  作为辅助特征加入排序或召回模型，或作为自监督预训练目标的一部分。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现代音乐推荐系统在工程上很成熟，但主要基于流派、元数据或协同过滤，只能近似预测用户下一首想听什么，无法捕捉歌曲之间独立于艺术家标签的“体验相似性”。

**方法关键点**：
- 构建大规模听歌会话数据集：采集 9,396 名 Last.fm 用户的 1.29B scrobbles，预处理后得到 28.6M sessions / 531.6M 训练 scrobbles。
- 用 skip-gram Word2Vec 训练 Song2Vec：session 当句子，track 当 token，得到歌曲 embedding。
- 观察到 embedding 空间被 artist identity 主导，原因与会话中同一艺术家的连续播放有关。
- 提出 artist-residual 方法：对每个艺术家计算其所有 track embedding 的质心，从 track embedding 中减去质心，得到残差表示，再进行跨艺术家结构分析。

**关键结果数字**：
- 原始空间平均跨艺术家 cosine similarity 为 0.2487，残差空间降至 0.0005，证明减去的质心捕获了艺术家主导信号。
- 残差空间中仍有 4,577 组跨艺术家 track pairs 的 cosine similarity ≥ 0.70，形成连贯的流派/年代聚类：trip-hop、1990s grunge、2020 mainstream pop、跨作曲家古典钢琴对（最高达 0.95）。
- 结果表明训练数据中存在独立于艺术家的体验结构，为后续 joint-embedding predictive architecture 直接学习该层提供实证依据。
