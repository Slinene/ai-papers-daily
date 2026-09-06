---
title: Multi-Tool Image Editing Attribution in Facial Forgery
title_zh: 人脸伪造中的多工具图像编辑归因
authors:
- Sheng Liu
- Qiang Sheng
- Danding Wang
- Yu Li
- Chenming Zhou
- Juan Cao
affiliations:
- 中国科学院计算技术研究所
- 中国科学院大学
arxiv_id: '2609.02751'
url: https://arxiv.org/abs/2609.02751
pdf_url: https://arxiv.org/pdf/2609.02751
published: '2026-09-02'
collected: '2026-09-06'
category: Other
direction: 多工具图像编辑归因与伪造检测
tags:
- Image Forensics
- Multi-Tool Attribution
- Deepfake
- Frequency Domain
- Curriculum Learning
one_liner: 面向多工具编辑人脸图像，提出DPEC方法结合空间-频域特征与课程学习，实现多工具归因
practical_value: '- 多工具痕迹解耦：在处理多行为叠加信号（如搜索、点击、收藏、购买）时，可借鉴空间与频率双分支设计，用局部感知特征分离不同来源的模式。

  - error-based curriculum learning：按预测难度渐进训练，可迁移到多任务学习或难易样本挖掘，例如广告转化率预估中先学简单样本再逐步加入难样本，稳定收敛。

  - 合成数据集构建：通过组合基本操作模拟真实多步编辑，可用于构建多行为归因评测集或用户行为序列模拟。

  - 频域线索：在电商商品图质量检测或主图篡改识别中，引入频域特征可增强对压缩/编辑痕迹的识别能力。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

## 动机
生成式AI工具普及使普通人可轻易编辑人脸图像，现有图像编辑归因方法假设单一工具，无法应对多工具复合编辑场景中不同工具伪影叠加的问题。

## 方法关键点
- 定义多工具图像编辑归因（MIEA）任务，目标是从给定编辑人脸图像中识别所有涉及的工具。
- 构建MultiEdit数据集，包含500k+编辑人脸图像，覆盖6类支持换脸与面部增强的工具，模拟最多5步的编辑流程。
- 数据分析表明编辑痕迹具有局部性和频率域可区分性，据此设计DPEC方法：在空间与频率双分支捕获局部可感知的工具痕迹，并采用基于错误的课程学习策略渐进训练。

## 关键结果
在最多5步编辑的设定下，DPEC优于9种现有方法，验证了多工具归因任务上双域特征与课程学习的有效性。
