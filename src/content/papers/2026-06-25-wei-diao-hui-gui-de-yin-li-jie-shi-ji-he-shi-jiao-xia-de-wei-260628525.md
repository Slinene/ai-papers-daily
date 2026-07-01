---
title: A Gravitational Interpretation of Fine-Tuning Reversion
title_zh: 微调回归的引力解释：几何视角下的行为恢复与干预
authors:
- Samuele Poppi
- Nils Lukas
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), UAE
arxiv_id: '2606.28525'
url: https://arxiv.org/abs/2606.28525
pdf_url: https://arxiv.org/pdf/2606.28525
published: '2026-06-25'
collected: '2026-07-01'
category: Training
direction: 微调行为退化的几何机制与方向干预
tags:
- Fine-Tuning Reversion
- Geometry
- Safety Alignment
- Representation Drift
- Intervention
- Training Dynamics
one_liner: 用历史训练流形的“引力”解释微调后行为回归，通过阻断回归方向有效抑制有害性恢复
practical_value: '- 持续微调或在线学习场景中，可监控表征漂移与历史回归方向(v_rev)的对齐程度，预警行为退化风险。

  - 计算v_rev只需保存初始化检查点与当前模型的激活差异，工程开销低，适合嵌入增量训练流水线。

  - 若需保留特定能力（如去偏见推荐），可在更新时投影梯度以阻断v_rev方向上的位移，实验证明能以极小任务代价大幅降低有害性。

  - 方法不依赖特定安全向量，利用训练历史本身定义回归方向，对搜索推荐模型的偏好保持与灾难性遗忘缓解具有启发意义。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：微调无害数据可能逆转对齐效果、恢复不安全行为或遗忘能力，现有解释散乱。作者提出几何假说：大规模预训练形成主导行为流形，后续对齐或专精微调只是浅层位移，因此后续微调易继承指向该流形的“回归分量”。

方法：在激活空间中，利用早期训练阶段模型与对齐后模型的差值定义回归方向 v_rev。跟踪微调过程中参数或激活沿 v_rev 的对齐程度，并设计干预实验：每次更新时投影梯度以阻止沿 v_rev 的运动。

关键结果：微调第一步后对齐即达 cos=0.429，20步后升至0.647，所有观测值均显著高于各向同性零分布。阻断 v_rev 方向运动使最终对齐反转为-0.211，有害率从19.0%降至8.5%，而任务性能几乎无损。结果支持 v_rev 是早期微调回归的因果中介，但不宣称它是唯一安全方向。
