---
title: 'AdShot: Benchmarking Multimodal Large Language Models for Video Advertisement
  Clipping'
title_zh: AdShot：面向视频广告剪辑的多模态大模型评测基准
authors:
- Wen Xie
- Om Rastogi
- Sai Siddhartha Vivek Dhir Rangoju
- Gijs Overgoor
- Yakov Bart
- Sarah Ostadabbas
affiliations:
- Northeastern University
- Southern Methodist University
arxiv_id: '2610.33377'
url: https://arxiv.org/abs/2610.33377
pdf_url: https://arxiv.org/pdf/2610.33377
published: '2026-10-24'
collected: '2026-10-31'
category: Eval
direction: 多模态大模型评测 · 广告剪辑
tags:
- MLLM
- Benchmark
- Video Advertisement
- Shot Selection
- Computational Advertising
- Multimodal
one_liner: 推出 AdShot 基准：823 对广告镜头选择评测，发现架构优先于规模且模型有内容偏好
practical_value: '- 在电商商品视频多时长自动剪辑中，把镜头选择建模为受时长预算约束的子集选择，而非让 MLLM 直接输出完整 15s 连续片；AdShot
  显示模型原始输出平均时长误差 5.39s，工程上必须加显式约束（DP/贪心 + 镜头时长表）。

  - 选型时不要迷信 72B 大模型；该基准中架构比规模更关键，小模型常追平或超过大模型。业务落地可优先评测 7B–13B 视频 MLLM，成本更低且可私有化部署。

  - 评估/微调需要显式覆盖 action、emotion、information、imagery 四类内容；模型系统性偏好 information/emotion
  镜头，会漏掉 action 和 imagery，电商广告中动作展示、产品外观镜头可能需要通过 prompt、奖励或后处理加权校正。

  - 若构建类似自动剪辑系统，建议加入音频声道：音频消融提示纯视频模型缺乏口播/音乐信息，商品口播、卖点音频对剪辑相关性高，评测时应纳入音频模态。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：广告主常需为 30s 源片制作 15s 版本，人工选镜头成本高；现有 MLLM 通用视频理解强，但专用剪辑能力缺少评估。

**方法**：AdShot 构建 823 对专业剪辑的 30s/15s 广告对，覆盖 194 品牌、17 行业，标注镜头边界和内容特征（action、emotion、information、imagery）。评测 13 个纯视频 MLLM 和 2 个音视频 MLLM（7B–72B），指标为镜头选择 Precision/Recall/F1、15s 时长约束、内容保留，并做音频消融。

**结果**：架构比参数规模更关键，小模型常追平或超过大模型；6–10 个镜头的目标广告表现最好。平均绝对时长误差 5.39s，多数模型超过 15s，但仍可大幅减少人工剪辑工作量。所有模型有系统内容偏好：倾向信息丰富、情绪向镜头，低估动作和画面镜头。
