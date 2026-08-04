---
title: Douyin Multimodal Embedding Model Technical Report
title_zh: 抖音多模态嵌入：兼顾效率与细粒度的语义充分性学习
authors:
- Haonan Chen
- Chu Li
- Zhicheng Wang
- Yuanwei Liu
- Yuanjiang Wang
- Shaohua Jiang
- Zhicheng Dou
affiliations:
- ByteDance Douyin Search Multimodal Team
- Renmin University of China GSAI
arxiv_id: '2608.02148'
url: https://arxiv.org/abs/2608.02148
pdf_url: https://arxiv.org/pdf/2608.02148
published: '2026-08-03'
collected: '2026-08-04'
category: Multimodal
direction: 多模态检索 · 语义充分性
tags:
- Multimodal Embedding
- Semantic Sufficiency
- Latent Reasoning
- Cross-Conditional Reconstruction
- Bi-Encoder
- Industrial Search
one_liner: 通过隐证据推理与跨条件重构，使 bi-encoder 嵌入兼具细粒度语义充分性，在 MMEB-v2 和抖音搜索中取得显著增益
practical_value: '- **两阶段训练范式**：第一阶段大规模异构对比学习建立统一多模态空间，第二阶段用高质量数据 + 教师监督做语义充分性微调，可直接迁移到电商多模态搜索（商品图文视频检索）的模型升级路径。

  - **隐式证据推理**：通过少量 anchor tokens 定位证据区域、类型化隐状态（localize/align/ reject）组织推理，完全在隐藏空间完成，不产生显式
  CoT 文本，保持在线召回低延迟，可用于电商 query 理解中的隐式意图定位与证据提取。

  - **跨条件重构监督**：利用 NTP/MTP 让 query 嵌入解码商品文本，反之亦然，提供 token 级细粒度监督，可强化搜索相关性建模，尤其适合电商场景中
  query 与商品详情之间语义细节的精确匹配。

  - **语义充分性度量**：通过 teacher forcing 的 Top‑K 准确率量化嵌入的信息完整性，可替代或补充传统召回指标，作为模型优化和迭代的可靠中间信号。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
工业级多模态检索需要同时满足亿级索引效率和细粒度语义判别，但现有对比学习嵌入效率高却缺乏对检索证据和对侧语义的建模，而显式 CoT 增强模型虽提升准确性却引入高延迟。为此，文中提出一种保留 bi‑encoder 极速推理、同时嵌入具备证据感知与语义充分性的多模态嵌入训练方案。

**方法**  
- **两阶段训练**：S1 在 25M 异构多模态对上进行大规模对比预训练，建立统一嵌入空间；S2 在 5M 高质量数据上通过教师模型生成的监督信号提升语义充分性。  
- **证据锚定与类型化隐推理（S2‑A）**：用模态感知的 anchor tokens 定位文本、图像区域、视频帧等证据，类型化隐状态（localize, align_pos, reject_neg, summarize）组织检索推理，无需显式生成 CoT。  
- **跨条件重构（S2‑B）**：以 query 嵌入为前缀条件，通过 NTP 和 MTP 解码文档文本（双向对称），强制嵌入保留对侧细粒度语义；仅训练时使用，推理无额外开销。  
- **语义充分性度量**：通过 teacher forcing 的 token 恢复准确率（acc@K）量化嵌入可恢复性，提供可解释的优化信号。

**结果**  
- MMEB‑v2：DME‑2B 和 DME‑9B 分别取得 74.8 和 78.4 整体分数，视频和视觉文档检索增益突出。  
- 抖音工业评测：离线相对提升 2.92%，在线 A/B 测试带来 0.1% Lifetime 增益。  
- 消融：Stage 1 提升视频/VisDoc 对齐，Stage 2‑A 对视频检索贡献最大（+4.4），Stage 2‑B 带来全面稳步提升。

**核心贡献**  
DME 证明，通过隐式证据组织与跨条件生成监督，bi‑encoder 可以在不牺牲效率的前提下显著提升细粒度语义建模能力，为工业级多模态检索提供了一套可落地的强语义充分性学习框架。
