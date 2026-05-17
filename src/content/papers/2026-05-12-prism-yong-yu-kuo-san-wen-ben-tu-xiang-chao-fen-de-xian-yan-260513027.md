---
title: 'PRISM: Prior Rectification and Uncertainty-Aware Structure Modeling for Diffusion-Based
  Text Image Super-Resolution'
title_zh: PRISM：用于扩散文本图像超分的先验校正与不确定性结构建模
authors:
- Zihang Xu
- Xiaoyang Liu
- Zheng Chen
- Yulun Zhang
- Xiaokang Yang
arxiv_id: '2605.13027'
url: https://arxiv.org/abs/2605.13027
pdf_url: https://arxiv.org/pdf/2605.13027
published: '2026-05-12'
collected: '2026-05-17'
category: Other
direction: 文本图像超分辨率 · 扩散模型
tags:
- Diffusion Models
- Image Super-Resolution
- Text Image
- Flow Matching
- Uncertainty Modeling
- Single-Step Diffusion
one_liner: 通过流匹配先验校正和不确定性感知残差编码，实现单步扩散的文本图像超分辨率
practical_value: '- 扩散模型中利用流匹配对隐空间先验进行校正的思路，可迁移到序列生成任务（如用户行为序列还原），通过构建高低质量隐变量对学习修正映射，提升生成可靠性。

  - 不确定性引导的残差学习可用于多模态特征融合，对置信度低的模态特征进行抑制，避免噪声扩散，适合电商场景中不完整商品描述等。

  - 单步扩散的加速技巧（如蒸馏、流匹配一步生成）可应用于实时推荐系统中的内容生成（如标题、摘要），降低推理延迟。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：文本图像超分辨率（Text-SR）在严重退化下常因文本条件不可靠和先验不精细导致字符错误。现有方法虽引入识别或生成先验，但仍未解决这两个问题。  
**方法**：提出PRISM，单步扩散框架，包含两个核心组件。Flow-Matching Prior Rectification (FMPR) 在训练时利用配对的高低质潜变量，学习一个流匹配过程，将退化特征传输至恢复导向的先验空间，提供更可靠的全局文本引导。Structure-guided Uncertainty-aware Residual Encoder (SURE) 则预测不确定性感知的结构残差，根据局部边界证据的可靠性自适应地吸收清晰笔画而抑制模糊区域，从而细化局部结构。二者结合在一次扩散前向中完成全局先验修正与局部结构精炼。  
**结果**：在合成和真实文本图像基准上取得SOTA，推理速度达毫秒级，大幅超越之前的多步扩散方法。
