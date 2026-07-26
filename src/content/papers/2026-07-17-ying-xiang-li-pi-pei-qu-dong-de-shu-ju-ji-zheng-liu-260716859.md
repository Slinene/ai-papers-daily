---
title: Dataset Distillation by Influence Matching
title_zh: 影响力匹配驱动的数据集蒸馏
authors:
- Haoru Tan
- Wang Wang
- Sitong Wu
- Xiuzhe Wu
- Yangtian Sun
- Chirui Chang
- Shaofeng Zhang
- Xiaojuan Qi
affiliations:
- HKU
- CUHK
- Stanford
arxiv_id: '2607.16859'
url: https://arxiv.org/abs/2607.16859
pdf_url: https://arxiv.org/pdf/2607.16859
published: '2026-07-17'
collected: '2026-07-26'
category: Other
direction: 数据集蒸馏 · 影响力匹配
tags:
- Dataset Distillation
- Influence Matching
- Outcome Alignment
- Sample-Level Influence
- Synthetic Data
- Vision-Language Distillation
one_liner: 通过结果对齐合成数据的影响力，替换传统的梯度或轨迹匹配，性能显著提升
practical_value: '- 影响力评估可用于识别用户交互数据中最重要的样本，实现训练集压缩或噪声过滤，降低存储和训练成本。

  - 合成数据集蒸馏思想可构建紧凑的用户行为摘要，在在线推荐服务中减少上下文长度或 KV cache 占用，提升推理效率。

  - 可微影响力估计器可集成到推荐模型训练中，实时评估样本梯度贡献，实现动态课程学习或难例挖掘。

  - 联邦推荐场景下，客户端上传蒸馏后的合成数据而非原始隐私数据，兼顾隐私保护与模型效用。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有数据集蒸馏方法多依赖过程代理（如匹配梯度或训练轨迹），启发式且不保证最终模型收敛结果一致，限制了合成数据的泛化性。

方法：提出影响力匹配（Inf-Match），从结果中心视角出发，学习一个紧凑合成集，使其对模型收敛参数的影响与完整数据集一致。核心创新是一个全可微的样本级影响力估计器，无需计算逆 Hessian 积，而是展开优化动态并应用一阶泰勒近似，实现线性时间复杂度。训练时，最小化合成集与真实数据集的影响力差异，从而直接对齐最终训练结果，而非模仿中间过程。

结果：在标准分类基准上取得最优精度，如 Tiny-ImageNet（IPC=10）达到 31.5%，比 NCFM 高 4.7%。在视觉语言蒸馏任务 Flickr30K 上，用 200-1000 个合成样本训练，图像/文本检索平均性能超越强过程匹配基线 NCFM 2.5%，证明方法可扩展至大规模多模态场景。
