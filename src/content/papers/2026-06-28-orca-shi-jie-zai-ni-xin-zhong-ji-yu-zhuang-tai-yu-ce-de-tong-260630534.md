---
title: 'Orca: The World is in Your Mind'
title_zh: Orca：世界在你心中——基于状态预测的通用世界基础模型
authors:
- Yihao Wang
- Yuheng Ji
- Mingyu Cao
- Yanqing Shen
- Runze Xiao
- Huaihai Lyu
- Senwei Xie
- Euan Liu
- Klara Tian
- Tianfeng Long
affiliations:
- Beijing Academy of Artificial Intelligence
arxiv_id: '2606.30534'
url: https://arxiv.org/abs/2606.30534
pdf_url: https://arxiv.org/pdf/2606.30534
published: '2026-06-28'
collected: '2026-07-01'
category: Multimodal
direction: 世界模型 · 多模态预训练
tags:
- world model
- next-state prediction
- multimodal learning
- representation learning
- foundation model
- video understanding
one_liner: 以Next-State-Prediction为核心，通过无意识与有意识学习统一世界潜在空间，在下游多模态任务中展现强迁移能力
practical_value: '- **状态转移建模借鉴**：用户行为序列可类比世界状态转移，用无意识学习处理大量未标注浏览序列，有意识学习聚焦稀疏但关键的转化事件（如点击、购买），提升对用户长期兴趣的建模。

  - **多模态统一表示**：将商品图文、用户行为等多模态信号对齐到同一潜在空间，冻结预训练主干，仅在下游训练轻量解码器，降低推荐/搜索系统的多任务开发成本。

  - **数据飞轮构建**：参考“密集状态转移（视频帧）+ 稀疏事件标注”的混合预训练数据设计，构建高密度交互日志与人工标注反馈相结合的训练流水线。

  - **工程轻量化**：冻结世界模型主干、只微调解码器的范式，可直接迁移到已有大模型部署场景，快速适配新业务目标如内容生成、问答、动作推荐。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前多模态模型孤立优化下一token、帧或动作预测，缺乏对世界状态转移的统一表征。为此，提出Orca，一个以Next-State-Prediction为核心的通用世界基础模型，旨在学习可复用的世界潜在空间。

**方法关键点**：
- 编码器-解码器架构，编码器通过两种互补范式学习世界潜在表示：无意识学习从连续视频捕获密集的自然状态转移；有意识学习利用语言描述的事件和VQA监督，建模稀疏但有意义的状态变迁。
- 预训练使用125K小时视频和160M事件标注，构建大规模世界学习数据集。
- 下游评估时冻结骨干网络，仅训练轻量的模态特定解码器（文本生成、图像预测、具身动作生成），验证潜在空间迁移能力。

**关键结果**：
- 扩大模型规模与数据量能持续提升下游性能，验证范式可扩展性。
- 在相同模型规模下，Orca超越各任务专用基线，更强的世界潜在表示带来更强的下游表现。
- 结果初步证明，以状态预测为中心的统一世界模型是理解、预测和作用于世界的有效路径。
