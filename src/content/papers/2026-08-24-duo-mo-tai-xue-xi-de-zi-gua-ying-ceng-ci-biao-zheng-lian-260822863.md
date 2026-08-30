---
title: Adaptive Hierarchical Representation Alliance for Multimodal Learning
title_zh: 多模态学习的自适应层次表征联盟
authors:
- Chunlei Meng
- Pengbin Feng
- Jacqueline J. Pang
- Chih-Ting Liao
- Rong Fu
- Zhaolu Kang
- Zhongxue Gan
- Chun Ouyang
affiliations:
- Fudan University
- University of Southern California
- Cornell University
- University of New South Wales
- Peking University
arxiv_id: '2608.22863'
url: https://arxiv.org/abs/2608.22863
pdf_url: https://arxiv.org/pdf/2608.22863
published: '2026-08-24'
collected: '2026-08-30'
category: Multimodal
direction: 多模态分层共享-私有专家框架
tags:
- Multimodal Learning
- Mixture-of-Experts
- Representation Learning
- Robustness
- CKA
one_liner: 提出AHRA分层共享-私有专家框架，缓解跨模态语义粒度错配并提升噪音与缺失鲁棒性
practical_value: '- 多模态商品理解中，不要默认各模态在最终层对齐；用 layer-wise CKA 识别语义深度差异：商品文本/标题往往需深层抽象，商品图/短视频帧的视觉证据在浅中层就可判别，可在对应层级做
  shared 对齐，减少浅层视觉信息被 flatten。

  - 共享/私有专家分解 + private decorrelation 可迁移到多通道用户/物品表示：跨场景共享专家建模共性，场景或模态专属专家保留细粒度信号，避免搜索/推荐/广告多域数据互相干扰。

  - sparsity-controlled soft-gating（foreground exam）适合多模态 item tower 的 token/feature
  选择：对缺失或噪声模态自动降权，增强 task-relevant private token，提升线上缺图/缺描述时的鲁棒性。

  - 层次 co-fusion 的 intra-level coordination + inter-level semantic selection 可用于多尺度融合商品图文与用户行为序列，动态选择最有利的语义层级，而非固定
  concat/attention。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有多模态模型通常在最终层统一对齐语言、视觉和音频，隐含假设各模态任务证据在同一语义深度出现。通过 layer-wise CKA 分析发现存在语义粒度错配：文本需要更深上下文抽象，视觉/声学线索常在浅中层即可判别，导致细粒度模态私有信息被压平，噪声、不平衡或缺失输入下鲁棒性下降。

**方法**：提出 AHRA，一个分层共享-私有专家框架。将每个模态分解为跨语义层的 shared 与 private 流，shared 流做对齐、private 流做去相关；共享信息经 cross-modal expert 路由，任务相关 private token 由模态专属专家与 sparsity-controlled soft-gating 增强；hierarchical co-fusion 先做 intra-level 专家协调，再做 inter-level 语义选择。

**结果**：在图像-文本分类、多模态意图识别、三模态情感分析共 6 个 benchmark 上，AHRA 一致优于强 baseline，并在噪声与缺失模态设置下保持鲁棒。
