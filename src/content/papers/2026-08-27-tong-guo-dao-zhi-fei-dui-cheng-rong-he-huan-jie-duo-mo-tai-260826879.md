---
title: Mitigating Strong-Modality Collapse in Multimodal Learning via Inverted Asymmetric
  Fusion
title_zh: 通过倒置非对称融合缓解多模态学习中的强模态坍缩
authors:
- Mary Ogbuka Kenneth
- Foaad Khosmood
- Abbas Edalat
affiliations:
- Imperial College London
- California Polytechnic State University San Luis Obispo
arxiv_id: '2608.26879'
url: https://arxiv.org/abs/2608.26879
pdf_url: https://arxiv.org/pdf/2608.26879
published: '2026-08-27'
collected: '2026-08-30'
category: Multimodal
direction: 多模态融合中强模态坍缩抑制
tags:
- Multimodal Fusion
- Knowledge Distillation
- Modality Collapse
- Asymmetric Fusion
- Pathway Isolation
one_liner: 提出 Inverted Asymmetric Fusion，保留强模态通路并以弱模态蒸馏锚定融合，避免强模态退化
practical_value: '- 多模态推荐/搜索中常出现文本、图像、行为等信号不均衡，直接对称融合可能损害主模态表征。可设计非对称融合结构，让强模态（如商品标题、用户历史）保持自身通路，弱模态仅作为上下文信息辅助，而不是强制相互注意力。

  - 对图像、视频等弱模态先做模态感知知识蒸馏，使其在融合前尽可能逼近强模态或教师模型的语义空间，能减少融合时的噪声干扰，提高整体效果。

  - 引入路径隔离评估：在融合前后分别测试各单模态内部准确率，快速定位是否发生融合退化，这在推荐模型迭代中可作为调试工具，避免“融合后反而变差”的隐性故障。

  - 该思路可用于电商多模态排序、详情页理解等场景：文本描述通常是强模态，图片/视频是弱模态，可让视频/图片特征以文本特征为锚定，而非让文本特征被图像注意机制拉偏。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

## 动机
多模态融合通常期望超过最强单模态，但在 MultiHuSE 上，early、late、symmetric attention 融合常常未能超越文本单模态基线。路径隔离分析发现一个对称注意力融合模型中，文本通路准确率从融合前的 74.9% 下降到 56.4%，说明主导模态在融合过程中被损害，作者称之为 strong-modality collapse。这一现象解释了部分多模态模型无法优于单模态基线的原因。

## 方法关键点
提出 Inverted Asymmetric Fusion (IAF)：
- 不强制模态间相互注意力；
- 主导模态（如文本）通过融合层时保持不变，避免被弱模态干扰；
- 弱模态（如音频、视频）以主导模态为上下文锚点进行注意力计算；
- 融合前对弱模态使用 Modality-Aware Knowledge Distillation 增强其表征能力。

## 关键结果
在三个具有不同模态层次结构的 benchmark 上评估：文本主导的 MultiHuSE、UR-FUNNY，以及音视频主导的 MUStARD。
- 路径隔离显示，IAF 在所有测试配置下将主导模态的内部准确率保持在其单模态上限；对称融合在 MultiHuSE 上最多导致 18.5 个百分点下降。
- IAF 相比最强单模态基线最高提升 8.25%。
