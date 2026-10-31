---
title: Proving and Improving the Platonic Representation Hypothesis with JEPAs
title_zh: 用 JEPA 证明并改进柏拉图表征假说
authors:
- Randall Balestriero
- Yann LeCun
affiliations:
- Brown University
- New York University
- AMI Labs
arxiv_id: '2610.39302'
url: https://arxiv.org/abs/2610.39302
pdf_url: https://arxiv.org/pdf/2610.39302
published: '2026-10-28'
collected: '2026-10-31'
category: Multimodal
direction: 多模态表示对齐 · JEPA 理论
tags:
- JEPA
- Platonic Representation
- multimodal alignment
- self-supervised learning
- scaling laws
- image-text alignment
one_liner: 证明基于“好视图”的 JEPA 可跨模态对齐表征，且比 next-token 高效 42 倍
practical_value: '- 多模态商品/内容塔可尝试用 JEPA 式“同一商品/场景的两个视图”构造正对，替代或辅助 CLIP 式图文对比，降低对大规模成对数据的依赖。

  - 正对质量优先于数据规模：在电商语料中构造标题 vs 属性描述、原图 vs 增强视图等 good views，可能以远小于 next-token 预训练的样本量获得跨模态对齐，节省训练成本。

  - 文本塔单独自监督训练后仅需学习一个旋转矩阵即可实现图像-文本检索/文案生成，适合为商品图生成短描述或跨模态召回。

  - 若业务中有不成对的图文/视频/行为数据，可借鉴其 pair-free 零样本评测思路，验证表征对齐是否足够支撑下游任务。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：Platonic Representation Hypothesis 猜想不同模态的大模型会收敛到共享世界表征，但此前既无证明也无可操作 recipe。

方法关键点：
- 将 PRH 转化为定理：Joint-Embedding Predictive Architectures (JEPAs) 在任意多模态上分别训练，只要正对是同一场景的两个观测（good views），且误对齐有界，则各模态表征仅相差一个旋转。
- 揭示 next-token prediction 本质是 JEPA 的 bad views：其正对来自同一文档的不同片段，因此语言模型只能靠规模才与视觉表征对齐。
- 实验覆盖 145k captions 到 940M web images，并发现 alignment scaling law，可在 seed noise 内预测 unseen runs。

关键结果：
- good views 达到同样对齐所需训练样本比 next-token 少 42 倍。
- 109M 参数 text JEPA 与 DINOv2 和 CLIP 图像编码器的对齐，超过所有评估的 LLM（最高 72B）以及 CLIP 文本编码器。
- 一个旋转即可将独立训练的编码器变为图像 captioner，COCO CIDEr 0.838。
- 在 pair-free 零样本 benchmark 上，text JEPA 的 ImageNet-100 top-5 为 64%，而 8B 以下 LLM 最高 56%。

结论：positive views 而非单纯 scale 才是构建柏拉图表征的关键杠杆。
