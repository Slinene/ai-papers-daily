---
title: 'PaletteID: Prototype-Composed Semantic Identifiers for Multimodal CTR Prediction'
title_zh: PaletteID：基于原型组合的语义ID用于多模态CTR预测
authors:
- Huanyu Liu
- Baining Chen
- Hui Liu
- Zengyang Li
- Ziyi Huang
affiliations:
- 华中科技大学
- 华中师范大学
arxiv_id: '2607.29000'
url: https://arxiv.org/abs/2607.29000
pdf_url: https://arxiv.org/pdf/2607.29000
published: '2026-07-31'
collected: '2026-08-03'
category: RecSys
direction: 语义ID · 原型组合 · 多模态CTR
tags:
- Semantic ID
- Prototype-based
- CTR Prediction
- Multimodal
- Long-tail
- DPP
one_liner: 用原型选择替代量化编码，保留连续相似性信号，提升CTR预测和长尾表现
practical_value: '- **用真实物品作为语义锚点（原型）替代抽象码本**：PID 直接从物品池中选出代表物品构成原型调色板，每个 token 都有具体物品可追溯，增强了可解释性，也避免了码本分配中的语义损失。在电商场景中，可以直接将高曝光、多内容的优质商品作为原型，赋予更强的业务语义。

  - **软聚合保留连续相似性，避免硬量化**：通过 top-K 原型相似度加权聚合（sigmoid 门控），保留了多模态嵌入空间的细粒度相似性，比 RQ-VAE
  等硬分配方式对长尾物品更友好。可借鉴到已有的 Semantic ID 方案中，将硬编码改为软检索-聚合，尤其适合提升冷启动物品的表征质量。

  - **SQ-DPP 原型选择兼顾多样性和代表性**：使用质量感知的 DPP 从全量物品中选出一组既覆盖语义空间又避免过于孤立的原型，平衡了长尾覆盖和高频语义区域的准确度。在推荐系统的特征工程或表示学习阶段，可复用这种建库思路，构造更具泛化性的基础语义单元。

  - **离线原型检索，在线仅需查表聚合，极易部署**：PID 序列和相似度分数全部离线预计算并存入特征存储，在线推理只需 K 次 embedding 查表、一次线性变换和加权求和，计算开销极低，可直接插入现有
  CTR 模型（如 DeepFM、DCNv2、DIN）作为新特征。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有的 Semantic ID 方法（如 RQ-VAE、RQ-KMeans）通过量化多模态嵌入为离散 token，虽能共享语义知识，但存在两个核心局限：硬码本分配丢弃了向量空间的连续相似性，导致相近物品可能被分到不同 token，细粒度语义丢失；残差编码路径对前缀高度依赖，深层 token 在不同前缀下语义混杂，且扩展性差，有效信息增量随深度递减。此外，离散化过程对嵌入扰动敏感，抽象码本索引缺乏可解释性。为此，论文借鉴调色板混合颜色的思想，提出 PaletteID（PID），用一组代表物品（原型）作为语义锚点，通过软组合来表征每个物品。

**方法**  
- **原型选择**：设计 Semantic Quality-Aware DPP（SQ-DPP）从全量物品中选出一个紧凑的原型调色板。先利用余弦 RBF 核构建相似度矩阵，再增加局部内容密度作为质量分数，使高密度区域的原型获得更高权重，同时 DPP 的行列式最大化保证所选择原型的全局多样性。
- **PID 生成**：对每个目标物品，检索 top-K 相似原型（经过相似度阈值过滤），得到一组原型索引和原始相似度分数。将这些相似度通过可训练的线性层和 sigmoid 门控转化为独立权重，再对原型 embedding 加权求和，形成 PID 表征。通过单调正则项鼓励排名更靠前的原型获得更高置信度。
- **集成到 CTR 模型**：PID 作为额外的物品侧特征，可与现有 CTR 骨架（DCNv2、RankMixer、DIN）拼接使用，支持对历史行为序列和目标物品进行统一的语义增强。

**实验**  
在 TAOBAO-MM（淘宝广告点击，1M 物品，7.2M 用户）和 KuaiRec（快手短视频推荐）两大数据集上评估。与 VQ-VAE、RQ-VAE、RQ-KMeans 相比，PID 在 DCNV2+ 和 RankMixer+ 骨架上均取得一致的 AUC/GAUC 提升：TAOBAO-MM 上 DCNV2+ 的 AUC 从 0.6275（None）提升到 0.6314，RankMixer+ 从 0.6286 到 0.6318；KuaiRec 上 RankMixer+ AUC 提升尤为显著（0.8172→0.8201）。长尾物品分析显示，PID 在尾部 40% 物品上相对 None 提升 0.0128 AUC，远超整体提升，且比 RQ-VAE 多出 0.0042。消融验证了 sigmoid 门控优于 softmax 和平均池化，SQ-DPP 优于随机、KMeans 和纯 DPP，并揭示了原型数 K 和调色板大小 M 的最优区间。
