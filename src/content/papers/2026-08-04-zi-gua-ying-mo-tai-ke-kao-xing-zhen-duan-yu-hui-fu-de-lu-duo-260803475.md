---
title: Adaptive Modality Reliability Diagnosis and Restoration for Robust Multimodal
  Intent Recognition
title_zh: 自适应模态可靠性诊断与恢复的鲁棒多模态意图识别
authors:
- Suraj Kumar
- Mohnish Raj
- Soumi Chattopadhayay
- Chandranath Adak
- Ayan Dutta
arxiv_id: '2608.03475'
url: https://arxiv.org/abs/2608.03475
pdf_url: https://arxiv.org/pdf/2608.03475
published: '2026-08-04'
collected: '2026-08-09'
category: Multimodal
direction: 多模态融合可靠性诊断与修复
tags:
- multimodal fusion
- reliability diagnosis
- heteroscedastic uncertainty
- modality restoration
- inverse-variance fusion
- intent recognition
one_liner: 提出闭环诊断-修复-重评估框架PRIME，用异方差不确定性估计模态弱项并修复，提升多模态融合鲁棒性
practical_value: '- **多模态特征可靠性诊断机制可复用**：利用预测置信度、认知分歧、跨模态一致性、特征退化等作为诊断证据，估计各模态的对数方差，可用于电商推荐中文本、图像、行为序列等模态的质量评估，动态决定融合权重。

  - **受控损坏训练思路**：在无真实可靠性标注时，通过人为注入已知严重程度的模态损坏（如Mask、噪声）并配合异方差损失，直接学习可靠性估计器。这种训练范式可迁移到推荐模型的鲁棒性训练中，低成本获得模态不确定性感知能力。

  - **原型条件变分修复模块**：对于低质量模态，不是简单丢弃或降权，而是用其他高可靠模态的信息驱动变分自编码器进行重建，并根据修复后的可靠性重新评估是否参与融合。这一思路可应用于特征缺失或噪声场景下的特征补全与二次判断。

  - **逆方差融合实现自适应集成**：以后修复的可靠性精度为权重进行多模态融合，自动削弱不可靠模态的贡献。在广告、搜索的多信号融合（如CTR预估中内容与行为特征融合）中可直接套用，提升对噪声输入和模态缺失的鲁棒性。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：多模态意图识别中，各模态可能存在噪声、缺失、语义冲突或主导性过强。现有方法通常隐式推断重要性，对不可靠模态直接降权或丢弃，未判断是否可以修复后再利用。

**方法**：提出PRIME框架，形成闭环诊断-修复-重评估。
1. **可靠性诊断**：通过预测置信度、认知分歧、跨模态一致性和特征退化等证据，估计每个模态的上下文对数方差（即弱项），代表不确定性。因无真实标注，训练时引入受控模态损坏并采用异方差不确定性目标，使方差能反映退化严重程度。
2. **模态修复**：利用估计的弱项控制原型条件变分修复模块，从互补模态中重建退化表征，恢复有用信息。
3. **重评估与融合**：修复后再次估计可靠性，仅当修复后的表征足够可信时才参与最终逆方差融合预测。

**关键结果**：在多模态意图识别基准上，PRIME在干净数据上保持有竞争力性能，同时在模态缺失、噪声、冲突和不平衡条件下鲁棒性显著提升，验证了闭环可靠性感知融合的有效性。
