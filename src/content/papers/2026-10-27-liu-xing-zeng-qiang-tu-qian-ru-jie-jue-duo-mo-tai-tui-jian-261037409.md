---
title: Can Complementary Signals Bridge Similarity Islands? Manifold-Augmented Graph
  Embedding for Multimodal Recommendation
title_zh: 流形增强图嵌入解决多模态推荐互补信号孤岛问题
authors:
- Zhenye Yang
- Jinpeng Chen
- Wenbo Fu
- Jun Ma
- Huan Li
- Qimin Zhou
- Tao Wang
- Li Sun
- Senzhang Wang
affiliations:
- Beijing University of Posts and Telecommunications
- Key Laboratory of Trustworthy Distributed Computing and Service (BUPT), Ministry
  of Education
- Zhejiang University
- Central South University
arxiv_id: '2610.37409'
url: https://arxiv.org/abs/2610.37409
pdf_url: https://arxiv.org/pdf/2610.37409
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: 多模态推荐 · 互补信号流形增强
tags:
- Multimodal Recommendation
- Complementary Recommendation
- Graph Neural Networks
- Manifold Learning
- Soft Conceptor
- Heterophily
one_liner: MAGE框架结合离线流形增强与在线非对称双流GNN，缓解多模态推荐中互补品语义漂移问题
practical_value: '- 离线流形增强（Phase I）可作为 plug-and-play 特征变换，直接替换现有多模态推荐模型的 item 文本 embedding，不改架构即可在
  Sports/Clothing 等数据上稳定提升 GUME/MGCN/MENTOR（论文表7），适合在召回或粗排阶段低成本引入。

  - 采用非对称双流设计：视觉特征作为 stable anchor 只走同配相似性图，增强后的文本特征作为 flexible probe 走混合互补边图，可解耦“替代品相似”和“互补品功能关联”两类信号，避免互补边污染视觉表示。电商推荐中可分别维护视觉图和文本图，按模态特性选择传播拓扑。

  - 互补信号注入用 per-seed 相对强弱邻居划分 + Soft Conceptor 软子空间投影，提取与替代品子空间正交的残差方向，并施加局部 gap-preserving
  约束和归一化后回溯，控制语义漂移。工程实现时，可参考用 SVD 子空间和自适应步长，而非固定全局融合权重。

  - LLM 文本预处理（Qwen3-32B-AWQ）仅做证据约束提取，冻结特征，训练/推理不调用 LLM，避免在线成本。但论文显示仅替换 LLM 文本特征收益不一致，真正增益来自几何增强+拓扑传播组合，提示业务中别只靠
  LLM 清理文本，需配套图侧设计。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：
多模态推荐系统依赖相似性构图和传播，但互补商品（如 iPhone 充电器）与种子 item 在视觉/文本上差异大，形成“Similarity Islands”，导致同配传播带来语义漂移，损害互补推荐。现有方法要么仅添加行为边，要么采用通用异配 GNN，未解决特征几何与行为拓扑之间的根本失配。

方法关键点：
- 离线流形增强（Phase I）：利用 co-purchase 邻居，按局部相似性分为 strong/weak 集合，通过局部 SVD 构建替代品主导子空间，使用 Soft Conceptor 软投影提取弱邻居中与子空间正交的残差方向，并在 gap-preserving 约束下自适应注入文本 embedding。
- 在线非对称双流 GNN（Phase II）：视觉流仅走相似性 kNN 图作为稳定 anchor；文本流走相似性+互补边混合图，传播增强后的文本表示作为灵活 probe。Self-Calibrated Gate 融合共享语义和模态残差，ID 协同表示作为行为 backbone。
- 辅助正则：moment-matching、NCE 对齐 fused 与 ID 表示、用户视图一致性。
- 数据：LLM 预处理提取功能属性，原始文本控制实验。

关键结果数字：
四个 Amazon 数据集（Baby/Sports/Clothing/Electronics）上全指标最优，Recall@20 相对最强基线提升 2.77%-6.53%；hard complement 子集平均相对提升 9.87%。消融显示 Phase I 和互补拓扑均有效。离线增强可迁移到 GUME/MGCN/MENTOR，Sports/Clothing 一致提升，但 Baby 涨跌不一。

最值得记住的一句话：几何变换优于单纯拓扑加边；先对文本特征做局部流形整形，再配合非对称传播，能缓解互补商品语义漂移。
