---
title: User-Centric Modeling of Transactional Sequences with Explainable State Space
  Models
title_zh: 结合对比学习与状态空间模型的用户交易序列建模
authors:
- Ivan Palagin
affiliations:
- HSE University
arxiv_id: '2607.20228'
url: https://arxiv.org/abs/2607.20228
pdf_url: https://arxiv.org/pdf/2607.20228
published: '2026-07-22'
collected: '2026-07-23'
category: RecSys
direction: 用户序列表示学习 · 状态空间模型
tags:
- State Space Models
- Mamba
- Contrastive Learning
- User Embeddings
- Transactional Sequences
- Explainability
one_liner: 用 CoLES 预训练用户向量初始化 Mamba 隐藏态或作为前缀 token，加速收敛并提升序列建模效果
practical_value: '- **CoLES 用户先验注入方式可复用**：在电商行为序列建模中，可将预训练好的用户 Embedding 作为 Mamba
  的初始隐藏状态或序列前缀 token，相比从头训练更快收敛（2-3倍），且无需改变模型主体。

  - **Mamba 替代 Transformer 处理长序列**：交易序列往往极长，Mamba 的线性复杂度优势明显，适合落地到点击、购买等长历史行为建模，性能优于
  RNN 且效率高于 Transformer。

  - **解释性分析指导特征选择**：利用离散化步数映射（discretization-step maps）和 Integrated Gradients 可识别最具信息量的交易特征，直接指导特征工程和业务规则制定，如突出高价值行为节点。

  - **多任务共用的用户表示**：CoLES 预训练得到的压缩用户向量可复用于年龄预测、多标签产品获取、购买预测等多个下游任务，降低在线推理成本。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：基于用户交易序列的建模面临两难——RNN 有梯度消失，Transformer 面对长序列有二次复杂度，而新兴的选择性状态空间模型 Mamba 虽高效但尚未在个性化用户分析中充分探索。同时，对比表示学习（CoLES）能生成高质量用户向量，但缺乏对序列动态的建模。

**方法关键点**：提出两种无侵入的混合策略，在 Mamba 中注入预训练的 CoLES 用户嵌入作为强先验：1) 将 CoLES 嵌入投影后作为 Mamba 隐藏状态的初始值；2) 将嵌入作为前缀 token 追加到输入序列。两种方式均使模型从第一步起就拥有用户画像信息。

**结果**：在 Age（年龄组预测）、MBD（多标签产品获取）和 Taobao（购买预测）三个公开数据集上，混合模型一致优于单独的 Mamba 和 CoLES+线性分类器，收敛速度提升 2-3 倍。解释性分析显示，在行为丰富的数据集上模型自动过滤无用事件，并能定位到最有决策影响力的交易特征。
