---
title: Towards Robustness against Typographic Attack with Training-free Concept Localization
title_zh: 无需训练的语义概念定位抵御排版攻击
authors:
- Bohan Liu
- Wenqian Ye
- Guangzhi Xiong
- Zhenghao He
- Sanchit Sinha
- Aidong Zhang
affiliations:
- University of Virginia
arxiv_id: '2607.02494'
url: https://arxiv.org/abs/2607.02494
pdf_url: https://arxiv.org/pdf/2607.02494
published: '2026-07-02'
collected: '2026-07-06'
category: Other
direction: 视觉语言模型鲁棒性 · 机制可解释性
tags:
- Typographic Attack
- CLIP
- Mechanistic Interpretability
- Adversarial Robustness
- Vision Transformer
one_liner: 通过无训练机制解释定位并干预CLIP中偏重文本的注意力头，显著提升视觉模型抗排版攻击鲁棒性
practical_value: '- 无训练的防御思路可直接复用到电商商品图片理解：商品图常叠加促销文字、logo 等，模型易被文字误导，借鉴本方法可通过定位并抑制视觉编码器中词汇偏置的注意力头，**不改变模型参数**提升对文字干扰的鲁棒性。

  - 机制可解释性管线可成为多模态推荐系统的诊断工具：当视觉特征提取器在场景文本上表现异常时，可使用论文的采样归因方法快速定位问题 Circuit，指导针对性干预或微调策略的设计。

  - 对 LVLM 的 VQA 抗攻击提升表明，该方法可增强对话式购物助手对用户上传含文字商品图的语义理解能力，避免因包装文字错误识别属性。

  - 干预操作简单（仅调整少数注意力头的权重），工程成本低，可作为在线推理阶段的免训练后处理模块，适用于对延迟敏感的推荐系统。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：CLIP 作为 LVLM 的视觉编码器，易受排版攻击——图像中的无关文字会覆盖真实视觉语义，使特征偏向词汇含义，威胁安全应用。现有防御需额外训练或效果有限。

**方法关键点**：
- 提出无训练机制可解释框架，通过采样分析隐藏状态，量化每个注意力头对语义（视觉）与词汇（文本）信息的关注程度。
- 基于概率分析与 Circuit Mining，定位出 ViT 中专门编码词汇信息的注意力头子集。
- 直接干预定位到的 Circuit：选择性调整注意力权重以抑制文字偏置，无需任何训练。

**关键结果**：
- 在物体分类上，干预方法超越有监督和无训练防御基线。
- 将干预应用于多个 SOTA LVLM 的视觉编码器，在 RIO-Bench 排版攻击下的 VQA 准确率显著提升，验证了通用性与有效性。
- 证实通过简单改动即可大幅提高鲁棒性，为该漏洞提供了一种可解释且易于部署的缓解方案。
