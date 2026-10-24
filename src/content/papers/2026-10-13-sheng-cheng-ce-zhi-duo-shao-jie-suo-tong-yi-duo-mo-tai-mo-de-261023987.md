---
title: 'What Generation Knows: Unlocking Fine-Grained Understanding in Unified Multimodal
  Models'
title_zh: 生成侧知多少：解锁统一多模态模型中的细粒度理解
authors:
- Tengju Ru
- Weitong Lian
- Zecong Tang
- Zhiheng Liu
- Lingyi Meng
- Haoran Li
- Kaixuan Wang
- Bohao Li
- Xihui Liu
affiliations:
- Zhejiang University
- The University of Hong Kong
- The Chinese University of Hong Kong, Shenzhen
- Shenzhen Loop Area Institute
arxiv_id: '2610.23987'
url: https://arxiv.org/abs/2610.23987
pdf_url: https://arxiv.org/pdf/2610.23987
published: '2026-10-13'
collected: '2026-10-24'
category: Multimodal
direction: 多模态生成与理解协同
tags:
- Multimodal
- Fine-grained Visual Understanding
- Generation-side Representation
- GAFU
- Post-training
- Vision-Language Models
one_liner: 揭示统一多模态模型中生成侧表示对细粒度视觉理解的互补价值，提出 GAFU 框架压缩生成侧表示为 G tokens 供理解通路检索，显著提升细粒度任务性能
practical_value: '- 在电商多模态商品理解中，可尝试提取统一多模态模型生成侧（如扩散前向或自回归解码中间层）的视觉表示，与理解侧表示融合或作为额外特征，改善商品颜色、材质、局部属性等细粒度识别；尤其适合对图像细微差异敏感的场景。

  - GAFU 将生成侧视觉表示压缩为少量 G tokens 再供理解通路做 task-conditioned retrieval，这一思路可借鉴到多模态特征工程：用可学习压缩
  token 保留关键细节，降低计算开销，并支持按任务动态选取相关特征。

  - 实验表明生成侧表示对细粒度语义变化更敏感且能捕获理解侧遗漏的变化，说明在搜索/推荐的多模态相关性排序中，可引入生成侧表示作为辅助信号，尤其在 title/图片差异、spatial
  relation 等需要精细匹配的任务上可能带来增益。

  - 该工作采用后训练（post-training）方式而非重新预训练，适合在已有模型基础上低成本注入细粒度理解能力，对业务中多模态模型升级有一定参考。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有视觉语言模型在高层次语义理解上较强，但细粒度视觉理解（局部属性、空间关系）仍有挑战。统一多模态模型（UMM）的生成通路保留了丰富的视觉信息，与理解通路互补，但已有工作未系统探索直接利用原生生成侧表示。

方法关键点：作者系统性分析生成侧表示特性，发现其对细粒度语义变化更敏感、能捕获理解侧遗漏的任务相关变化、且依赖正确空间组织。基于此设计 GAFU 后训练框架：将生成侧视觉表示压缩为紧凑的 G tokens，保留细粒度视觉细节，并支持理解通路按任务条件检索。该方法无需重新预训练，在相同训练数据下优于 SFT 基线。

关键结果：在 VStar-Bench、OmniSpatial、VSR-Bench 上最大相对提升分别为 20.00%、17.94%、8.62%，跨多个 UMM 架构一致改善。
