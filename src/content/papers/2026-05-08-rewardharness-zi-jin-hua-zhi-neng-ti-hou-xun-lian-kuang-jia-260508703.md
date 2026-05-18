---
title: 'RewardHarness: Self-Evolving Agentic Post-Training'
title_zh: RewardHarness：自进化智能体后训练框架
authors:
- Yuxuan Zhang
- Penghui Du
- Bo Li
- Cong Wei
- Junwen Miao
- Huaisong Zhang
- Songcheng Cai
- Yubo Wang
- Dongfu Jiang
- Yuyu Zhang
affiliations:
- University of British Columbia
- Vector Institute
- Kuaishou Technology
- Carnegie Mellon University
- University of Waterloo
arxiv_id: '2605.08703'
url: https://arxiv.org/abs/2605.08703
pdf_url: https://arxiv.org/pdf/2605.08703
published: '2026-05-08'
collected: '2026-05-18'
category: Agent
direction: Agent 自进化奖励建模
tags:
- self-evolving
- agentic
- reward model
- preference alignment
- tool generation
one_liner: 将奖励建模从权重优化转为上下文进化，用少量样本自动演变工具技能库，实现高数据效率评估
practical_value: '- 用少量人工标注（100 条）即可引导 Agent 自主迭代进化评估标准，大幅降低构建评价模型的成本，可借鉴到电商多模态内容（商品图/视频）的
  automated evaluation 或 RLHF reward signal。

  - Orchestrator + Sub-Agent 的推理链架构，通过选择工具和技能来构建判断逻辑，类似可应用于推荐系统中排序策略的评判或解释生成，提升可解释性与可干预性。

  - 自进化工具库的维护方式（分析成功/失败案例后增删改工具）提供了 Agent 持续学习的工程范式，可以迁移到多智体协作场景，让评估 Agent 随着业务迭代自动适配新准则。

  - 冻结子模型配合技能库的思路，让 API-only 模型也能参与 reward modeling 的迭代，对使用闭源大模型做判断的业务有参考意义。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有图像编辑奖励模型依赖海量偏好标注和模型训练，数据效率远低于人类（人类能从少量示例中推断标准）。为弥补这一差距，需要一种数据高效、免训练、可自进化的奖励建模方法。

方法：提出 RewardHarness，将奖励建模重构为上下文进化而非权重优化。仅需约 100 条偏好演示即可启动。框架由三部分组成：(1) 维护一个动态的工具和技能库，最初可空或手工注入少量 seed；(2) Orchestrator 根据输入（源图、候选编辑图、指令）从库中挑选最相关的工具和技能子集；(3) 冻结的 Sub-Agent 用这些工具技能构建推理链，输出偏好判断。通过比对预测与 ground-truth，Orchestrator 自动分析推理过程的成功/失败，从而增删改库中的工具和技能，循环迭代，无需额外人工标注。

结果：仅用 EditReward 0.05% 的数据，RewardHarness 在图像编辑评估基准上平均准确率 47.4%，超出 GPT-5 5.3 个百分点。将其作为 GRPO 微调的奖励信号，RL 调优后的模型在 ImgEdit-Bench 达到 3.52 分。该框架实现了极低标注依赖下的高效偏好对齐。
