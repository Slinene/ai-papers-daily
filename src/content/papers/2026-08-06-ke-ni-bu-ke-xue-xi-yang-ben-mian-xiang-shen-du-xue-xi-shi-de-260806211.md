---
title: 'Reversible Unlearnable Examples: Towards the Copyright Protection in Deep
  Learning Era'
title_zh: 可逆不可学习样本：面向深度学习时代的版权保护
authors:
- Binze Wang
- Jinyu Tian
- Xingrun Wang
- Xiaochen Yuan
- Jianqing Li
arxiv_id: '2608.06211'
url: https://arxiv.org/abs/2608.06211
pdf_url: https://arxiv.org/pdf/2608.06211
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: 数据版权保护 · 不可学习扰动
tags:
- unlearnable examples
- copyright protection
- watermarking
- mutual information
- adversarial perturbations
one_liner: 通过互信息最小化生成不可学习扰动并解耦水印提取，同时防御非法模型训练与数据泄露
practical_value: '- 业务可借鉴点有限，主要学术贡献，但数据扰动思路可迁移：对用户行为序列或 embeddings 添加微弱扰动，防止黑盒提取模型做未授权训练

  - 双提取器解耦思想可应用于需要同时嵌入可逆水印与扰动防御的场景，如推荐结果中隐藏追踪标识且不影响正常服务

  - 互信息最小化技巧可作为防御模型窃取的备选方案：在输出 logits 或中间表示上注入最小化互信息的噪声，降低攻击者模拟能力'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：深度学习依赖大规模数据，版权保护至为关键。已有不可学习样本方法只能防止非法模型训练，忽视数据泄露风险，且防训练与技术水印简单结合会相互冲突。

**方法关键点**：提出可逆不可学习样本框架。一方面，通过最小化模型输入输出互信息，生成扰动迫使模型学习不相关特征，从而实现强大的不可学习性，防止未经授权的模型训练；另一方面，设计双水印提取策略，使用两个独立的水印提取器分别处理水印图像和不可学习扰动，消除扰动对水印提取的负面影响，确保数据泄露时可验证版权。

**关键结果**：在 ImageNet、CIFAR-10、Pets 三个标准图像数据集上实验，所提方法可同时提供有效的训练防御与可逆水印提取，实现了全面的图像版权保护。
