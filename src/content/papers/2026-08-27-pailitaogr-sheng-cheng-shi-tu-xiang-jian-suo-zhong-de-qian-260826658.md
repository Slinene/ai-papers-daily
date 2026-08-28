---
title: 'PailitaoGR: Latent Think-with-Images for Generative Image Retrieval'
title_zh: PailitaoGR：生成式图像检索中的潜在以图思考方法
authors:
- Xiaomeng Fan
- Yueran Liu
- Shengyu Zhou
- Chenghan Fu
- Wanxian Guan
- Feng Li
- Chuan Yu
- Jian Xu
- Bo Zheng
affiliations:
- Alibaba Group
arxiv_id: '2608.26658'
url: https://arxiv.org/abs/2608.26658
pdf_url: https://arxiv.org/pdf/2608.26658
published: '2026-08-27'
collected: '2026-08-28'
category: GenRec
direction: 生成式检索 · Semantic ID · 视觉商品搜索
tags:
- Generative Retrieval
- Semantic ID
- Image Search
- Knowledge Distillation
- E-commerce
- Attention Guidance
one_liner: 在原始查询图上内化目标聚焦与选择性辅助证据利用，实现不裁剪缩放与不 OCR 阅读，生成式检索平均提升 13.8%
practical_value: '- 在拍立淘类图像检索/生成式推荐中，可借鉴“能力内化”架构：用轻量 Target Token Scoring + Token-level
  Residual Modulation 对 visual token 做目标加权，不改变主干，推理零额外延迟；把显式 grounding/crop/OCR 能力蒸馏进单一模型，避免多步工具调用。

  - On-policy distillation 对自回归 SID 生成很有价值：教师和学生共享学生自己采样的 prefix，蒸馏 top-K 候选分布，比 ground-truth
  prefix 蒸馏更贴近推理时的错误前缀场景，能降低 train-inference mismatch。

  - 利用 SID 的 coarse-to-fine 结构设计 attention guidance：fine/medium token 用 ROT mask 惩罚目标框外注意力，coarse
  token 保持高熵广注意；这一思路可迁移到任何 hierarchical Semantic ID 的商品检索，提高解码对主体商品的判别性。

  - 辅助信息（如 OCR 文本、品牌标）引入要加 utility/accessibility 双门控：只有当 OCR 教师相对 Crop 教师有增益且学生自己也能利用该信号时才
  transfer，否则 suppress/skip；能避免无关水印或背景文字误导，适合电商 query 图中常见噪声。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
拍立淘式电商图像搜索中，真实 query 图同时包含目标商品、可用辅助证据（品牌、型号等 OCR 文字）和无关内容（水印、背景物体）。生成式检索直接生成商品 SID 有优势，但若不在推理时做裁剪/OCR，模型很难自动聚焦目标；显式工具调用又会增加多步推理延迟，且全量引入辅助信息可能有害。因此核心问题是如何把“目标聚焦”和“选择性利用辅助证据”两种能力内化进一个只用原始图的前向模型。

**方法关键点**  
- **目标聚焦机制**：Target Enhancer 通过 per-token scoring 估计视觉 token 与目标相关度，再用 residual modulation 增强目标 token；训练上结合 on-policy distillation（学生按自身采样 prefix，与 Crop Teacher 对齐 top-K 分布）和 granularity-aware attention guidance（ROT loss 把注意力拉向目标框，entropy loss 让 coarse SID token 保持广注意、fine token 收敛到判别区域）。  
- **选择性辅助证据机制**：Auxiliary Enhancer 以目标 anchor 为条件评估视觉 token 是否提供互补 OCR 类信息并增强；蒸馏时用 OCR Teacher 相对 Crop Teacher 的 logit 增益度量 utility，用学生带/不带 auxiliary 的 logit 差度量 accessibility，双 soft gate 决定 open、close 或 skip，只传递有益且可被学生利用的辅助能力。  
- **数据与推理**：训练/测试来自拍立淘线上日志，训练 1,159,746 张、测试 8,647 张 query 图，覆盖 7 个类目，测试集时序隔离并做人工与匹配模型校验；推理只用原始 query 图，教师全部移除。

**关键结果**  
在点击/购买行为的 H@K 和 R@K 上，该方法相比直接 SFT 的全图 baseline 平均提升 13.8%；只用原始图即超过 Crop Teacher 4.76%、OCR Teacher 2.76%。当目标区域占比 0–5% 时提升最大（click H@1 +18.52 pp），有 OCR 的 query 增益也更明显。消融显示目标聚焦和选择性辅助利用各自带来稳定提升。

**最值得记住的一句话**：把裁剪/OCR 工具能力蒸馏进一个单模型，推理零额外延迟，是生成式图像检索从学术走向线上检索的关键路径。
