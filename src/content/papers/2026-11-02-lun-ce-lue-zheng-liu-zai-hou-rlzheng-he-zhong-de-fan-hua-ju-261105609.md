---
title: On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation
title_zh: 论策略蒸馏在后RL整合中的泛化局限
authors:
- Yichen Wang
- Yufa Zhou
- Siqi Zhu
- Haozheng Luo
- Jingzhi Bao
- Zhichao Liu
- Zijun Wei
affiliations:
- University of Chicago
- Duke University
- UIUC
- Northwestern University
- ByteDance
arxiv_id: '2611.05609'
url: https://arxiv.org/abs/2611.05609
pdf_url: https://arxiv.org/pdf/2611.05609
published: '2026-11-02'
collected: '2026-11-05'
category: Training
direction: 多教师在线蒸馏的OOD泛化分析与改进
tags:
- On-policy distillation
- Multi-teacher distillation
- OOD generalization
- Post-RL consolidation
- Replay
- Geometry-based patching
one_liner: 发现OPD/MOPD的IND近完美掩盖了OOD遗忘，提出几何修补与基座保留回放提升泛化
practical_value: '- 在电商/Agent场景用蒸馏整合多个专家模型或策略时，评估不能只看分布内指标，需增加OOD、长尾、组合场景测试集，否则上线后可能发生静默泛化退化。

  - 蒸馏后OOD掉点可从两个方向排查：教师能力是否覆盖目标分布、蒸馏数据是否包含边界/组合样本；联合增强两者可消除OOD遗忘。

  - 引入 base-preserving replay（保留基座模型的高质量响应或混合原始数据）能有效缓解能力遗忘，类似持续学习中的经验回放，适合在不停迭代的推荐/Agent策略模型中使用。

  - 监控蒸馏过程的参数更新几何：更新矩阵谱过度集中或共享结构异常时，可能预示泛化受限，可作为训练健康度预警指标。'
score: 7
source: huggingface-daily
depth: abstract
---

多教师在线蒸馏（MOPD）常用于整合多个RL后教师模型的能力，但之前近完美的分布内（IND）蒸馏分数掩盖了泛化层面的盲点。

在合成推理与真实任务（数学推理、编码、Agent、长上下文）上评估发现：OPD/MOPD在IND上可达教师的96.04-102.73%，但OOD分数比基座模型低2.45-16.25%；三个组合场景中MOPD虽提升IND，但组合任务OOD比最佳教师低18.19-24.34%。

进一步把教师能力和数据覆盖识别为两个关键瓶颈，联合缓解可消除OOD遗忘，甚至可能超越教师泛化。相比RL基线，（M）OPD平均减少OOD遗忘，更新几何分析显示其更新更小、谱更集中，MOPD下共享结构更强。

基于此提出几何修补与基座保留回放，在保持IND的同时改善OOD，揭示了能力整合中需要显式支持OOD保留与泛化的必要性。
