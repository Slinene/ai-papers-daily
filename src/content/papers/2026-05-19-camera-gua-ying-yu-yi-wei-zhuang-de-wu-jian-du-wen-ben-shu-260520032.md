---
title: 'CAMERA: Adapting to Semantic Camouflage in Unsupervised Text-Attributed Graph
  Fraud Detection'
title_zh: CAMERA：适应语义伪装的无监督文本属性图欺诈检测
authors:
- Junjun Pan
- Yixin Liu
- Yu Zheng
- Lianhua Chi
- Alan Wee-Chung Liew
- Shirui Pan
affiliations:
- Griffith University
- La Trobe University
arxiv_id: '2605.20032'
url: https://arxiv.org/abs/2605.20032
pdf_url: https://arxiv.org/pdf/2605.20032
published: '2026-05-19'
collected: '2026-05-21'
category: RecSys
direction: 无监督图欺诈检测 · MoE自适应融合
tags:
- Graph Fraud Detection
- Semantic Camouflage
- Unsupervised Learning
- Mixture of Experts
- One-class Learning
- Text-Attributed Graph
one_liner: 提出CAMERA，通过解耦MoE专家与上下文感知门控自适应融合多源线索，实现无监督检测语义伪装欺诈者
practical_value: '- **LLM 文本编码替代浅层特征**：用预训练 LLM（如 OpenAI text-embedding-3-small）提取节点文本的高质量语义表示，比
  TF-IDF 或 SentenceBERT 更能保留细微恶意信号，适合电商评论/社交文本的欺诈检测。

  - **MoE 解耦多源欺诈线索**：将结构偏差（GCN 残差）、语义偏差（自编码器残差）和全局分布偏差（距平均原型的距离）分别交给独立专家建模，避免单一信号被伪装掩盖；推荐系统做内容/行为异常检测时可效仿此解耦设计。

  - **上下文感知门控自适应融合**：门控网络结合节点自身表征和邻居聚合上下文计算专家权重，使同一个数据集中不同子社区能灵活侧重不同线索；可迁移到多源信号融合的推荐排序或风险模型中，用局部上下文动态调整信号重要性。

  - **利用稀有性的一类无监督训练**：基于欺诈者稀少的先验，采用 BCE 损失将多数节点得分压缩至 0，让少数欺诈节点自然凸显，配合专家级重构损失迫使专家学习正常模式；无需标签的训练思路可降低业务标注成本。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

**动机**：在电商、社媒等文本属性图上，欺诈者已进化出语义伪装（semantic camouflage），即模仿正常用户的语言风格来隐藏恶意目的，使得依赖局部亲和力等假设的传统无监督检测方法失效。现有方法要么需要标注，要么仅处理结构伪装，无法应对语义层面的隐匿，亟需一种无需标签且能自适应融合多元欺诈线索的检测方案。

**方法关键点**：
- **文本编码**：使用预训练 LLM 将评论/帖子等文本属性编码为稠密向量，捕捉深层语义，保留细微恶意信号。
- **Ego-Decoupled MoE 架构**：三个专家分别捕获：
  - 图专家：计算节点表示与 GCN 聚合邻居表示的残差，突出结构偏差；
  - 语义专家：通过自编码器重构输入，取重构残差作为语义偏差；
  - 全局专家：计算节点与全图平均原型的差异，提供分布层异常视角。
  MoE 层通过加性残差跳接（skip connection）解耦共享信息，防止专家冗余。
- **上下文感知门控**：门控网络输入 Ego 表征拼接邻居聚合上下文，经 Softmax 输出三个专家的动态权重，使不同社区能自适应侧重不同线索（例如高端餐饮侧重结构声誉，休闲酒馆侧重语义）。
- **无监督训练**：利用欺诈者稀少的先验，采用一类（OC）损失迫使多数节点得分趋零，同时施加专家损失（最小化残差 L2 范数）让专家学习正常模式，使欺诈节点因更大偏差而被检出；加入熵正则化损失鼓励门控生成更确定的权重分布。

**关键实验**：在 Reddit、Instagram、AmazonVideo、YelpChi 四个真实数据集上对比 9 种 SOTA 方法，CAMERA 在 AUROC 上平均提升 2–14 个百分点，尤其在语义伪装严重的 Instagram 和 AmazonVideo 上分别达到 58.21 和 63.05，而最强基线仅 54.38 和 58.08；消融表明三专家协同与上下文门控均至关重要，LLM 编码效果远超 Bag-of-Words 和 SentenceBERT。

**一句话记住**：解耦的 MoE 专家加上基于局部上下文的自适应门控，使得无监督模型能自动捕捉不同社区中最有效的欺诈信号，有效对抗语义伪装欺诈者。
