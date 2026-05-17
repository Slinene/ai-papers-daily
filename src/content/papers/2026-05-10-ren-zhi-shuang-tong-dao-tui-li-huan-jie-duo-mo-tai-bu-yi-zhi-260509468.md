---
title: Mitigating Multimodal Inconsistency via Cognitive Dual-Pathway Reasoning for
  Intent Recognition
title_zh: 认知双通道推理缓解多模态不一致性用于意图识别
authors:
- Yifan Wang
- Peiwu Wang
- Yunxian Chi
- Zhinan Gou
- Kai Gao
affiliations:
- Hebei University of Science and Technology
- Hebei University of Economics and Business
arxiv_id: '2605.09468'
url: https://arxiv.org/abs/2605.09468
pdf_url: https://arxiv.org/pdf/2605.09468
published: '2026-05-10'
collected: '2026-05-17'
category: Multimodal
direction: 多模态意图识别 · 冲突消解与双通道推理
tags:
- Multimodal
- Intent Recognition
- Inconsistency
- Dual-Pathway
- Disentanglement
- Prototype Matching
one_liner: 用直觉与推理双通道动态融合，量化并消解多模态冲突，实现鲁棒意图识别
practical_value: '- **多模态冲突鲁棒处理**：当文本、图像、语音等模态信号不一致时，CDPR 的双通道设计（直觉路径聚合共识，推理路径显式量化冲突并动态加权）可直接迁移到电商多模态对话或商品理解中，避免错误模态主导决策。

  - **语义原型匹配校准**：利用原型向量与统计概率校准来量化冲突严重度，可借鉴到推荐系统中有噪声的多模态内容（如用户评论图文不符），提升意图/偏好识别的可靠性。

  - **多视角损失防模态懒惰**：防止训练中某模态被忽略，适用于电商多模态特征融合（如商品标题、图片、视频），保障各模态信息充分挖掘。

  - **表示解耦提供模块化接口**：将模态不变与特定特征分离，便于在 Agent 系统中对不同模态组件进行独立优化或故障排查，增强可解释性。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：多模态意图识别（MIR）常遇跨模态信号不一致，现有方法难以有效区分一致与冲突线索，导致语义抵消，最终影响意图理解的鲁棒性。

**方法**：提出认知双通道推理框架 CDPR。先通过表示解耦分离模态不变与特定特征；直觉通道利用共享特征聚合跨模态共识，构建稳定语义基础；推理通道引入不一致感知机制，结合语义原型匹配与统计概率校准，精准量化冲突严重程度，并动态调节双通道权重。额外设计多视角损失函数，分阶段学习结构化特征，缓解模态懒惰。

**结果**：在两个 MIR 基准数据集上达到 SOTA，并在不一致数据上表现出显著鲁棒性提升，验证了双通道协同解决多模态冲突的有效性。
