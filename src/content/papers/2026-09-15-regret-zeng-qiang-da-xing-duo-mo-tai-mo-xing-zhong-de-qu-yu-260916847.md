---
title: 'RegRet: Enhancing Region-Level Retrieval in Large Multimodal Models'
title_zh: RegRet：增强大型多模态模型中的区域级检索
authors:
- Xun Liang
- Honghui Yang
- Weihang Pan
- Ruisi Zhao
- Boyuan Pan
- Yao Hu
- Wenxiao Wang
- Binbin Lin
- Deng Cai
affiliations:
- Zhejiang University
- Xiaohongshu Inc.
arxiv_id: '2609.16847'
url: https://arxiv.org/abs/2609.16847
pdf_url: https://arxiv.org/pdf/2609.16847
published: '2026-09-15'
collected: '2026-09-16'
category: Multimodal
direction: 多模态区域级检索 · 对比学习
tags:
- Region-Level Retrieval
- Large Multimodal Models
- Contrastive Learning
- E-commerce Search
- Region-Aware Encoder
- Benchmark
one_liner: 通过 Region-Aware Encoder 与多阶段对比学习，在不牺牲全局检索性能下大幅提升区域级检索
practical_value: '- 电商以图搜图/相似商品推荐场景中，用户常指定 ROI（如局部图案、纹理），全局检索易被背景干扰误召。可借鉴 Region-Aware
  Encoder 思路：在现有多模态编码器上增加区域特征分支，与全局特征做加权或注意力融合，输出联合表示，提升区域查询召回精度。

  - 训练流程采用“局部字幕生成→区域对比学习”两阶段设计：先利用图文对自动生成区域描述构造正负样本，再对区域表示做对比微调。业务中可直接复用该 pipeline，用少量人工标注或伪标注构建区域级训练数据。

  - 论文表明仅零样本推理的区域级检索能力就超过强基线，说明预训练 LMM 已隐含区域理解；若业务受限于标注，可先直接使用 LMM 区域裁剪+文本匹配做召回，再逐步用对比学习微调。

  - 引入 REGMB 基准，覆盖区域-区域/区域-文本等四类任务，评估体系可参考扩展；尤其对电商搜索，可建立内部 ROI 检索评测集，量化不同模型对细粒度意图的满足度。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机

区域级检索要求对齐用户指定的图像区域与相关区域或文本描述，在电商商品搜索、RAG 等真实场景中非常关键。但现有大型多模态模型（LMM）主要聚焦全局级检索，难以捕获有效的细粒度区域表示，导致在 ROI 查询时容易被背景干扰而误召。

## 方法关键点

- **Region-Aware Encoder**：在保持全局背景上下文的同时，专门捕捉详细区域特征，平衡区域与全局表示，避免牺牲全局检索性能。
- **多阶段训练流程**：先进行详细局部字幕生成，增强区域理解；再进行区域对比学习，提升表示的判别性。
- **REGMB 基准**：构建包含 225k 对比对、覆盖四种多模态检索任务的评测集，弥补区域级对比训练数据和评测多样性的缺失。

## 关键结果

- 零样本设定下，RegRet 超越多个强基线。
- 加入对比学习训练后，在 REGMB 和公开基准上平均提升超过 20%。
- 全局级检索任务上取得与基线相当或更好的结果，验证了区域增强不损害全局能力。
