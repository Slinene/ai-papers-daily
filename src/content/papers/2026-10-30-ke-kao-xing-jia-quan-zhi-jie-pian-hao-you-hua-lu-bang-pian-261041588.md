---
title: 'Reliability-Weighted Direct Preference Optimization: Penalized Weights for
  Robust Preference Learning'
title_zh: 可靠性加权直接偏好优化：鲁棒偏好学习的惩罚权重方法
authors:
- Bin Luo
- Param Venkat Vivek Kesireddy
- Anil Vallepu
affiliations:
- School of Data Science and Analytics, Kennesaw State University
arxiv_id: '2610.41588'
url: https://arxiv.org/abs/2610.41588
pdf_url: https://arxiv.org/pdf/2610.41588
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: 偏好学习 · 鲁棒 DPO
tags:
- DPO
- robust-preference-learning
- noise-correction
- RLHF
- LLM-fine-tuning
one_liner: 在 DPO 中为每个比较样本引入可学习可靠性权重，自动降权翻转/噪声偏好，几乎无额外计算成本
practical_value: '- **直接用于 LLM 推荐/排序模型的偏好微调**：电商场景的用户行为（点击、点赞、下单）常含噪声甚至反转，RW-DPO 的权重估计与策略联合优化可自动降权可疑样本，工程实现只需在
  DPO loss 中加一个惩罚项和闭式权重更新，几乎不增加训练成本。

  - **容忍标注噪声，减少人工清洗**：实验显示在 10-30% 翻转标签下，RW-DPO 的 win rate 不随翻转率上升而下降，甚至超过干净标签 DPO，说明面对隐式反馈数据不必先花大量资源清洗，可直接训练。

  - **利用 margin 阈值识别翻转样本**：理论证明恢复所有翻转比较需要 margins 约 log n，可据此设计样本检查策略：优先审查模型与其高置信度预测矛盾且
  margin 较大的比较对，辅助数据质检。

  - **与其他噪声校正方法对比的启示**：RW-DPO 的误报标志更少、估计误差更低，可作为 RLHF 训练中鲁棒偏好建模的基线方案，适合需要快速验证鲁棒性的团队。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：DPO 假设所有偏好标注都正确，但真实数据常含翻转、平局或噪声，导致对齐质量随噪声比例下降。现有基于全局翻转率的方法无法区分错误样本，逐样本校正方法又各有局限。

**方法关键点**：RW-DPO 为每个比较样本引入未知可靠性权重 w_i∈[0,1]，以线性方式进入似然（DPO 相当于 w≡1，完全翻转样本 w_i=0）。权重与策略联合估计，并在 -log w_i 上施加 minimax-concave 惩罚，使模型同意的样本权重保持为 1，只对模型矛盾的样本降权。权重更新具有闭式解，相对 DPO 额外计算开销可忽略。理论证明：仅凭单次标注恢复所有翻转比较需要 margins 达到 log n 量级；在线性指数模型下，从方向正确的初始拟合出发，即使固定比例比较被翻转，估计器也能一致恢复偏好方向和权重，并识别超过该 margin 尺度的翻转样本。

**关键结果**：仿真中 RW-DPO 平均估计误差在 DPO、噪声率校正和近期鲁棒方法中最低，翻转标志远更精确；在 10-30% 标签翻转的 LM DPO 微调中，RW-DPO 的 win rate 不随翻转率增长而下降，甚至超过用干净标签训练的 DPO，与最强的近期方法持平，且校正集中在翻转标签上。
