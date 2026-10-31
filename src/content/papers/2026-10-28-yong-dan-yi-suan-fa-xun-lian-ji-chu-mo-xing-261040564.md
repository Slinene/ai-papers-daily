---
title: Training Foundation Models with a Single Algorithm
title_zh: 用单一算法训练基础模型
authors:
- Yuda Song
- Alvin Zhang
- Fahim Tajwar
- Daman Arora
- Jeff Schneider
- Daniel Khashabi
- Ruslan Salakhutdinov
- J. Andrew Bagnell
- Aarti Singh
- Andrea Zanette
affiliations:
- Carnegie Mellon University
- Johns Hopkins University
- Aurora Innovation
arxiv_id: '2610.40564'
url: https://arxiv.org/abs/2610.40564
pdf_url: https://arxiv.org/pdf/2610.40564
published: '2026-10-28'
collected: '2026-10-31'
category: Training
direction: 基础模型统一训练范式
tags:
- Unified Training
- RL as Likelihood
- Foundation Models
- Data Mixture
- Training Pipeline
one_liner: 将预训练、SFT、RL 统一为单一似然训练目标，把 RL 视作对模型生成分布的最大似然拟合
practical_value: '- 在业务 LLM 迭代中，可放弃严格分阶段 SFT→RLHF 流水线，用统一似然目标直接混合静态标注与模型生成样本，减少多阶段维护成本和切换误差，尤其适合电商文案生成、对话策略等需要快速试错的场景。

  - 把 RL 步骤改写为在模型自身生成分布上的最大似然拟合，可降低 reward hacking 风险并稳定训练；在推荐系统用用户行为反馈作为偏好信号时，可借鉴该视角设计更平滑的在线学习目标。

  - 将数据选择、配比和训练时机作为核心调参对象，而不是算法切换；可在电商推荐中用行为日志、人工标注、模型生成样本做动态配比，统一训练提升覆盖率和准确率。

  - 统一训练提供更强持续学习起点：上新品类、适配新用户群体或增量更新推荐模型时，可沿用同一训练器而不必重启多阶段流程。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：传统基础模型训练被拆成预训练、中期训练、SFT、RL 多个阶段，数据和算法目标各自独立，造成流水线复杂、切换成本高。论文认为这种分离并非本质，训练生命周期应简化为单一学习问题。

方法关键点：核心是把合适的 RL 目标推导为对模型生成目标分布的最大似然拟合，从而所有阶段都能放在同一个基于似然的训练算法下。统一训练系统在单一 trainer 中混合静态数据和 RL 生成样本；设计重心从阶段算法选择转移为选择训练哪些数据、以什么比例、在什么时机训练，传统分阶段训练只是其特例。

关键结果：在受控与真实实验中，统一训练改善了准确率-计算权衡和任务覆盖，同时保持通用能力，并为持续学习提供更强起点。论文未公开具体数值，但奠定了基础模型训练统一科学的框架。
