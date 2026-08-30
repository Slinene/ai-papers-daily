---
title: 'Learning to Prefer Reliably: Error-Augmented Emotion Preference Optimization
  with Calibrated Fusion'
title_zh: 可靠偏好学习：错误增强的情感偏好优化与校准融合
authors:
- Zilong Huang
- Junyi Peng
- Junjie Li
- Kai Li
- Wenze Ren
- Kong Aik Lee
- Man-Wai Mak
- Tatsuya Kawahara
affiliations:
- The Hong Kong Polytechnic University
- Brno University of Technology
- Tsinghua University
- National Taiwan University
- Kyoto University
arxiv_id: '2608.24730'
url: https://arxiv.org/abs/2608.24730
pdf_url: https://arxiv.org/pdf/2608.24730
published: '2026-08-25'
collected: '2026-08-30'
category: Training
direction: 多模态情感偏好优化与裁判校准
tags:
- Preference Optimization
- Multimodal LLM
- Emotion Recognition
- Error Augmentation
- Model Calibration
- Reward Model
one_liner: 通过错误增强负样本与多裁判边缘校准融合，提升多模态情感偏好判断的鲁棒性
practical_value: '- 负样本构造策略可迁移：在训练推荐/广告文案生成或排序模型时，不只是随机采样负样本，而是从正样本出发生成多类受控负样本（如语义流畅但违背用户真实意图的商品描述、评论），显著提升模型对困难负样本的区分度。

  - 多裁判融合的校准思路：当用多个 LLM 作为标注器/打分器（如商品质量评估、广告文案评分）时，不同模型输出打分分布差异大，先做 margin calibration（映射到统一尺度）再融合，比直接平均更稳定，可减少单一模型偏差。

  - 偏好优化数据增强：用错误增强方式扩充偏好对，能缓解稀疏监督问题，在电商 UGC 情感分析、客服对话语气判断等场景可以低成本生成更多高质量训练对。

  - 工程上可复用 soft fusion 思想：对于多个异构模型的预测结果，不采用 hard voting 或简单平均，而是保留偏好 margin 并做校准后加权，适合集成多个微调裁判模型，提升线上评估一致性。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**
情感偏好学习通常用成对比较数据训练 MLLM 裁判或奖励模型，但现有监督稀疏：每个正样本只配一个负样本，无法覆盖多样错误模式，尤其缺少“语义流畅但情绪不一致”的困难负样本。同时单一 MLLM 裁判存在模型特定偏差，影响细粒度多模态情绪判断可靠性。

**方法关键点**
提出 Error-Augmented Preference Optimization (EAPO)，分数据与模型两层：
1. 错误增强数据集：从每个偏好描述生成多个受控、情绪感知的负描述，覆盖不同错误类型，强化对流畅但违反视频多模态情绪证据的描述的暴露。
2. 多裁判训练：将多个独立 MLLM 适配到增强后的监督，各自学习情绪偏好判断。
3. 边缘校准软融合：将不同裁判输出的偏好 margin 通过校准映射到公共尺度后再聚合，降低异构打分尺度不一致导致的融合偏差。

**关键结果**
在 MER2026-EmoPrefer Challenge 官方数据集及自建错误增强数据集上，EAPO 提升了情感偏好预测精度，并在评估语义流畅但与视频多模态情绪证据冲突的描述时表现出更高鲁棒性。代码已开源。
