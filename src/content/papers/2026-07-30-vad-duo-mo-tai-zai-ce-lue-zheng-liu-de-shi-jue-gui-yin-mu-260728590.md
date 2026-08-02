---
title: 'VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal On-Policy
  Distillation'
title_zh: VAD：多模态在策略蒸馏的视觉归因目标重构
authors:
- Kangning Zhang
- Yixing Li
- Shuai Shao
- Qingyao Li
- Zhengxi Lu
- Zhiyuan Yao
- Jianghao Lin
- Wenxiang Jiao
- Yuan Lu
- Weiwen Liu
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Inc.
- The Chinese University of Hong Kong
- Zhejiang University
- Southeast University
arxiv_id: '2607.28590'
url: https://arxiv.org/abs/2607.28590
pdf_url: https://arxiv.org/pdf/2607.28590
published: '2026-07-30'
collected: '2026-08-02'
category: Multimodal
direction: 多模态在策略蒸馏 · 反事实视觉归因
tags:
- Multimodal Distillation
- Visual Attribution
- Counterfactual Reasoning
- On-Policy Learning
- Target Reconstruction
one_liner: 通过反事实目标重构分离教师修正中的视觉可归因部分，提升多模态细粒度蒸馏效果
practical_value: '- 电商多模态场景（商品图片理解、视觉问答）中，若存在特权教师（如高分辨率图），可用反事实方法计算视觉证据方向，重构更纯的监督信号，避免语言先验污染，提升学生模型细粒度识别能力。

  - 在蒸馏训练时，将监督信号分解为视觉可解释部分和残差，仅用视觉部分作为主要目标，可借鉴到多模态搜索/推荐模型的特征对齐，抑制无关文本偏差。

  - 反事实目标重构可作为一种通用原则，用于多模态Agent的决策归因，识别哪些视觉线索驱动了正确行为，从而指导针对性蒸馏。

  - 分布式训练中，教师模型冻结评估两次（证据存在/移除）来计算代理方向，该方法可工程化实现，用于在线知识蒸馏以提升多模态模型鲁棒性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：多模态在策略蒸馏（OPD）中，教师模型提供的下一token修正通常混合了视觉信号、语言先验及模型特定偏置，导致学生难以习得纯净的视觉知识。如何估计修正中真正由视觉证据支持的部分成为关键挑战。

**方法**：VAD采用反事实目标重构。对每个学生生成的前缀，首先在完整视觉证据下和移除相关视觉证据下分别使用冻结的教师模型计算每token的对数概率，两场景差别中心化后得到视觉证据方向代理$u_t$。$u_t$为有符号向量，表示揭示证据如何支持或反对候选token。将教师原始修正投影到$u_t$方向，得到干预对齐分量（视觉可归因部分），剩余为代理未解释残差。从对齐分量重构目标分布，并依据学生当前策略进行锚定。训练时，该重构目标作为主要监督信号，教师原始分布仅作为弱正则项。

**结果**：在4B和9B规模六个细粒度视觉任务上，VAD显著优于直接特权教师蒸馏和基于视觉优势加权的蒸馏。Token级分析显示代理对齐分量富含任务相关视觉修正，尤其在证据反驳错误答案时目标偏移更强，验证了反事实目标重构的有效性。
