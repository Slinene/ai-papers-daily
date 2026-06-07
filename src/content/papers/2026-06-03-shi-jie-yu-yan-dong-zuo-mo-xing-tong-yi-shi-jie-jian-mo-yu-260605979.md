---
title: World-Language-Action Model for Unified World Modeling, Language Reasoning,
  and Action Synthesis
title_zh: 世界-语言-动作模型：统一世界建模、语言推理与动作合成
authors:
- Yi Yang
- Zhihong Liu
- Siqi Kou
- Yiyang Chen
- Yanzhe Hu
- Jianbo Zhou
- Boyuan Zhao
- Zhijie Wei
- Xiao Xia
- Xueqi Li
affiliations:
- SJTU
- SII
- HUST
- SCUT
- ECUST
arxiv_id: '2606.05979'
url: https://arxiv.org/abs/2606.05979
pdf_url: https://arxiv.org/pdf/2606.05979
published: '2026-06-03'
collected: '2026-06-07'
category: Other
direction: 具身AI · 世界-动作模型
tags:
- embodied AI
- world model
- vision-language-action
- autoregressive transformer
- robot control
one_liner: 提出WLA模型，基于自回归Transformer联合预测文本子任务、子目标图像和动作，统一世界建模与语言推理
practical_value: '- **世界预测辅助动作生成的分工设计**：可借鉴世界专家与动作专家的解耦思路，在推荐/Agent中引入辅助世界建模任务（如用户状态或环境变化预测），为决策提供额外信号，训练时利用世界预测的归纳偏置，推理时可关闭以降低延迟。

  - **自回归联合预测语义意图与物理动作**：用户行为序列建模可扩展为同时预测下一步的语义意图（如查询词）和具体动作（如点击），提升推荐策略的长程一致性。

  - **Test-time scaling机制**：世界预测在推理时可按需激活，通过多步前瞻提升动作准确性。在推荐场景中，类似地可在关键决策点（如重排序）冗余计算未来用户状态，以计算换性能。

  - **从无标注视频学习新任务**：论文展示了仅利用无动作标注视频预训练的潜力，对电商中从无强监督行为日志学习策略有启发，但需注意领域差异。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
现有具身模型通常割裂世界建模与语言推理：世界动作模型（WAM）擅长从视频预训练中学习物理动态，但缺乏长程任务所需的语言推理能力；视觉语言动作模型（VLA）具备推理却未充分利用世界模型。为统一两者，提出世界-语言-动作（WLA）模型，旨在让机器人同时理解语言指令、预测环境变化并生成动作。  

**方法**  
WLA采用自回归Transformer骨干，输入文本指令、图像和机器人状态，输出下一状态的语义级文本子任务、子目标图像和动作。关键点：1）世界专家负责预测细粒度物理动态，其输出被动作专家利用，强化状态-动作关联学习；2）通过meta-query机制使世界预测隐式影响动作生成，推理时可禁用世界支路以提速，亦可激活进行test-time scaling提升控制精度；3）支持从跨形态机器人视频中无动作标注地学习新任务。  

**结果**  
WLA-0（2B参数）在RTX 5090上每步推理仅40ms。多任务和长程实验效果显著：RoboTwin2.0 Clean任务成功率92.94%，复杂基准RMBench达56.5%，均领先先前方法。
