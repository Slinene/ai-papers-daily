---
title: 'Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit
  Feedback from Users'
title_zh: 你的鼠标和眼睛悄悄泄露偏好：基于隐式反馈的LLM对齐
authors:
- Haw-Shiuan Chang
- Jeffrey Gomez
- Mehul Patwari
- Aryan Sajith
- Hamed Zamani
affiliations:
- University of Massachusetts, Amherst
- York University
arxiv_id: '2606.20482'
url: https://arxiv.org/abs/2606.20482
pdf_url: https://arxiv.org/pdf/2606.20482
published: '2026-06-18'
collected: '2026-06-20'
category: Training
direction: 隐式反馈LLM对齐 · 多模态行为信号
tags:
- implicit feedback
- LLM alignment
- reward modeling
- eye tracking
- mouse trajectory
- DPO
one_liner: 利用鼠标轨迹与眼动追踪等隐式用户信号，显著提升LLM对齐的奖励模型准确率与DPO优化效果
practical_value: '- **对话式推荐/Agent交互中植入隐式信号收集**：在电商导购Agent或搜索推荐对话界面中，可低成本采集鼠标悬停、停留时长、滚动行为、甚至眼动数据（如用户授权），作为比显式点击/购买更稠密的偏好信号，用于细粒度reward建模。

  - **奖励模型融合trick**：使用随机森林等非线性模型融合隐式行为特征与文本特征，比纯文本reward模型提升9个百分点，可直接迁移到推荐系统中的用户意向打分或排序融合。

  - **DPO训练中注入隐式反馈权重**：将基于鼠标/眼动的偏好得分作为DPO优化中的似然权重或对比对的选择依据，类似rDPO with NLL，可让生成结果更贴合真实用户关注模式。

  - **数据收集与隐私平衡**：论文所用Mechanical Turk的webcam眼动方案成本较低，电商搜索/Agent产品可考虑在用户知情同意下进行小规模采集，用于对齐模型的持续优化。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM对齐严重依赖显式人类反馈，但用户极少主动提供偏好标注，高质量数据昂贵；互联网巨头常用隐式行为信号构建经济护城河，而LLM对齐尚未有效利用。本文旨在量化鼠标轨迹、眼动注视等隐式反馈对LLM对齐的价值。

**方法关键点**：
- 构建新数据集 **IFLLM**，包含59名众包工人在多轮对话中的1336个问题、完整鼠标轨迹和通过Webcam采集的眼动注视点序列，揭示用户行为多样性。
- 设计基于**隐式反馈的奖励模型**：从鼠标坐标序列、眼动扫视路径中提取统计特征（如停留时长、扫视长度），用随机森林融合文本特征与现代BERT的隐层输出，预测用户偏好。
- 将隐式奖励得分融入DPO对齐流程，以**rDPO with NLL**形式增强多个LLM的响应质量。

**关键结果**：
- 隐式奖励模型将纯文本奖励模型的偏好预测准确率从**55%提升至64%**。
- 在对8个LLM进行DPO对齐后，响应质量的相对提升**接近原来的三倍**。
