---
title: 'AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation
  Learning'
title_zh: AlphaWiSE：面向持续多模态表征学习的自适应权重插值
authors:
- Sarthak Jain
- Qiran Hu
- Zhen Zhu
- Yaoyao Liu
affiliations:
- University of Illinois Urbana-Champaign
- Google DeepMind
arxiv_id: '2607.15094'
url: https://arxiv.org/abs/2607.15094
pdf_url: https://arxiv.org/pdf/2607.15094
published: '2026-07-16'
collected: '2026-07-17'
category: Multimodal
direction: 多模态持续学习·权重插值
tags:
- continual learning
- weight interpolation
- multimodal retrieval
- CLIP
- exemplar memory
- audio-image-text
one_liner: 提出后处理权重插值方法 AlphaWiSE，为每个参数张量学习一个标量系数组合新旧检查点，实现多模态持续学习的灵活稳定性-可塑性权衡
practical_value: '- 多模态推荐系统持续新增领域数据时，可直接使用 AlphaWiSE 在旧任务稳定检查点和新任务适应检查点间插值，无需重新训练，避免全方向遗忘

  - 利用小样本记忆（exemplar memory）自适应学习每个参数张量的插值系数（单个标量），参数量极小，可快速部署，适合线上频繁更新的场景

  - 插值后的模型与原检查点架构完全一致，推理零额外开销，适合对延迟敏感的电商搜索/推荐服务

  - 该方法解耦了不同检索方向（如文搜图、图搜文、音搜图）的稳定性需求，可针对不同方向定制插值系数，提升整体多模态搜索质量'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：多模态表征模型（如 CLIP、AudioCLIP）在持续适应新领域数据时，会破坏已学到的跨模态对齐，导致在旧任务上检索性能下降。传统持续学习方法只产出单一检查点，强行对所有检索方向（文本→图像、图像→文本等）施加相同的稳定性-可塑性权衡，忽略方向间的差异性。

**方法**：AlphaWiSE 是一种后处理权重空间插值策略。它维护两个冻结的源检查点——一个专注旧任务稳定性，另一个专注新任务可塑性。对于模型中的每个参数张量（由检查点 key 标识），在张量级别学习一个共享的标量插值系数 α，由所有张量条目共同使用。系数通过在小型样本记忆上最小化检索损失拟合，最终合成一个插值后的部署模型。该模型架构和参数量与源检查点一致，推理零额外开销。

**结果**：在音频-图像-文本三模态持续学习基准上，AlphaWiSE 在多个检索方向和联合评估指标（Recall@K）上一致超越强基线（如 LwF、EWC、DER），且仅需少量样本记忆即可获得显著增益。消融实验表明张量级别自适应系数优于全局共享系数或逐层固定插值。
