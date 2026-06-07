---
title: 'Before Fusion, Ask What to Keep: Contextual Calibration of Multimodal Signals'
title_zh: 融合前，先问保留什么：多模态信号的上下文校准
authors:
- Jiyuan Liu
- Liangwei Nathan Zheng
- Wei Emma Zhang
- Xinpei Wang
- Weitong Chen
affiliations:
- Adelaide University
- Shandong University
arxiv_id: '2606.02679'
url: https://arxiv.org/abs/2606.02679
pdf_url: https://arxiv.org/pdf/2606.02679
published: '2026-06-01'
collected: '2026-06-07'
category: Multimodal
direction: 多模态融合 · 预融合校准模块
tags:
- Multimodal Fusion
- Pre-fusion Calibration
- Cross-modal Comparison
- Modality Reliability
- Plug-in Module
one_liner: 在融合前通过跨模态比较生成实例级与维度级校准信号，抑制干扰、保留弱但有用证据，提升多模态融合鲁棒性。
practical_value: '- 在电商多模态推荐（商品图、文、视频）中，可借鉴此预融合校准模块，动态评估各模态当前样本的可靠性，抑制噪声模态（如低质图片或误导性描述），提升推荐特征鲁棒性。

  - 模块为即插即用设计，能与现有融合结构（如注意力、门控）无缝集成，无需改变下游预测头，便于在已有推荐模型上快速试验和迭代。

  - 跨模态交互方式（summary-level 比较 + 实例/维度调制）为处理用户评论中图文不一致、恶意文本等场景提供了简洁有效的校准思路。

  - 该方法在多种模态缺失和噪声注入下表现稳定，可推广到用户行为序列、社交关系等多源信息的融合预校准，增强推荐系统对缺失或低质量数据的容错性。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

多模态学习中，不同模态对最终预测的贡献并不稳定，某些模态可能成为干扰。现有方法多在融合后处理，忽视了融合前对模态可靠性的主动校准。本文提出一种紧凑的预融合校准模块，在融合前为每个模态生成实例级和维度级的调制信号：首先将各模态压缩为 summary 向量，通过跨模态比较提取支持与冲突线索，再据此调制原始特征，从而抑制误导成分、保留弱但有用的证据，增强跨模态一致性。模块即插即用，可附加于序列化或卷积融合架构。在情感理解、动作识别、音视频事件检测与情感分类等五个基准上，预融合校准在多种融合设置下均带来一致的性能提升。消融实验和噪声注入分析表明，该方法显著降低不可靠模态的干扰，使多模态训练过程更加稳定，并在模态缺失或合成破坏下表现出更好的鲁棒性。
