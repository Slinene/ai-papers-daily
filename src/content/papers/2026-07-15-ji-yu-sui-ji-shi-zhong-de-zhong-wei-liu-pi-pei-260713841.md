---
title: Heavy-Tailed Flow Matching via Random Clocks
title_zh: 基于随机时钟的重尾流匹配
authors:
- Zhouhao Yang
- Yezhen Wang
- Kenji Kawaguchi
- Vladimir Braverman
- Haoyang Cao
affiliations:
- Johns Hopkins University
- National University of Singapore
arxiv_id: '2607.13841'
url: https://arxiv.org/abs/2607.13841
pdf_url: https://arxiv.org/pdf/2607.13841
published: '2026-07-15'
collected: '2026-07-18'
category: Other
direction: 重尾生成建模 · 流匹配
tags:
- heavy-tailed
- flow matching
- random clock
- generative model
- logsignature
- tail control
one_liner: 将重尾源分布分解为时钟条件高斯混合，使流匹配适配稀有事件生成并支持尾部校准。
practical_value: '- 推荐系统中长尾物品和极端用户行为的生成：可将长尾分布视为重尾，利用 HTFM 的条件高斯混合机制生成更真实的尾部样本，缓解冷启动和多样性问题。

  - 低采样步骤特性：HTFM 保留了流匹配的低 NFE（如 5 步）快速生成，适合在线推理场景，降低工程延迟。

  - 尾部程度可调控：通过改变时钟律或尾部参数即可校准生成样本的重尾程度，可用于广告投放中的风险控制，例如调节收益分布尾部厚度以匹配业务目标。

  - 条件编码思路：truncated logsignature 编码路径特征，轻量高效，可推广至其他需要将连续条件路径嵌入的条件生成任务，如用户行为序列建模。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：现实数据常呈重尾分布，稀有事件影响巨大（如长尾类别、金融风险、极端天气），但标准扩散/流匹配使用高斯源分布，与重尾数据不匹配，导致尾部生成质量差。

**方法**：提出重尾流匹配（HTFM），将重尾源分布建模为时钟条件高斯源的混合。对每个随机时钟路径（如 gamma 或 α-稳定过程），条件源为高斯，边缘化后得到高斯尺度混合族（覆盖高斯、α-稳定、Student-t）。训练时学习时钟条件矢量场，用 truncated logsignature 编码时钟路径特征以控制计算开销；采样时随机生成时钟并求解条件 ODE。

**结果**：在二维不平衡 α-稳定混合、CIFAR10-LT 长尾图像和 HRRR 天气场三个任务上，HTFM 相比高斯流匹配和重尾基线，显著改善模式覆盖率、生成质量（FID）及尾部统计量恢复，同时保持 5~10 NFE 的快速采样。额外提供尾部控制接口：仅调整时钟律或尾部参数，同一架构即可控制生成尾部的“重度”。
