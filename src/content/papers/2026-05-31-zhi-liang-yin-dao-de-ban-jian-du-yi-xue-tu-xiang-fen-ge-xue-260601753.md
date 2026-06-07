---
title: Quality-Guided Semi-Supervised Learning for Medical Image Segmentation
title_zh: 质量引导的半监督医学图像分割学习
authors:
- Kumar Abhishek
- Ghassan Hamarneh
affiliations:
- School of Computing Science, Simon Fraser University, Canada
arxiv_id: '2606.01753'
url: https://arxiv.org/abs/2606.01753
pdf_url: https://arxiv.org/pdf/2606.01753
published: '2026-05-31'
collected: '2026-06-07'
category: Other
direction: 医学图像分割 · 半监督学习 · 质量评估
tags:
- semi-supervised learning
- image segmentation
- quality estimation
- medical imaging
- pseudo-label reweighting
one_liner: 用专用网络预测分割质量，通过合成腐败训练该预测器，并以质量感知正则化与伪标签重加权增强半监督分割
practical_value: '- 训练辅助网络评估生成结果质量并用于样本加权，该思路可迁移到电商弱监督学习，例如对用户行为序列生成的伪标签进行可靠性评分。

  - 通过合成腐败（噪声、掩盖、变形）构造低质量数据训练质量预测器，类似方法可用于构建电商图像或文本描述的质量评估器。

  - 质量感知正则化损失：对低置信度区域施加平滑，可类比于推荐模型中对不确定性高的预测施加正则，防止过拟合噪声标签。

  - 即插即用的设计降低了集成成本，该思想可直接应用于现有半监督Agent或生成式推荐框架，快速引入质量感知机制。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：医学图像分割依赖大量密集标注，成本高昂。半监督学习利用无标签数据缓解标注需求，但现有方法通常用模型自身置信度评估伪标签可靠性，缺乏对分割质量的直接衡量。

**方法**：提出质量引导的半监督框架，额外训练一个分割质量预测网络，输入图像和掩膜对，输出逐像素或图像级质量分数。该预测器用合成腐败（如随机腐蚀、膨胀、噪声）与部分训练的分割模型输出的不完美掩膜进行训练，使其学会识别真实训练中出现的错误模式。预测器集成到SSL的两个机制：(1) 质量感知正则化损失，根据质量图自适应平滑分割概率；(2) 基于质量的伪标签样本重加权，低质量伪标签降低权重。该方法可作为现有SSL方法的即插即用增强。

**结果**：在5个医学图像数据集（包括MRI、CT、内窥镜等）和多种分割架构上实验，相比基准SSL方法（Mean Teacher、UA-MT等）在Dice系数上取得一致提升，验证了质量引导的有效性与通用性。
