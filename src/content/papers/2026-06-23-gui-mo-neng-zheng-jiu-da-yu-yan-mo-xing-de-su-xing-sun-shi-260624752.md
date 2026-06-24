---
title: Can Scale Save Us From Plasticity Loss in Large Language Models?
title_zh: 规模能拯救大语言模型的塑性损失吗？
authors:
- J. Fernando Hernandez-Garcia
- Tomás Figliolia
- Beren Millidge
affiliations:
- Zyphra
arxiv_id: '2606.24752'
url: https://arxiv.org/abs/2606.24752
pdf_url: https://arxiv.org/pdf/2606.24752
published: '2026-06-23'
collected: '2026-06-24'
category: Training
direction: LLM持续学习的塑性损失标度律
tags:
- plasticity loss
- continual learning
- scaling laws
- LLM
- multilingual training
one_liner: 发现LLM塑性损失遵循可预测的亚线性标度律，增大模型仅能延缓而无法根除。
practical_value: '- 搜索推荐系统若需持续增量训练（在线学习），应监控模型在新任务/分布上的快速适应能力，警惕塑性损失导致更新失效。

  - 单纯增大模型规模（如从1B升到10B）只能把塑性损失出现时间向后推，无法彻底避免；对于长期运行的业务模型，需考虑周期性重置部分参数、采用弹性权重巩固或正则化策略。

  - 即使数据分布平稳（如电商流量自然漂移），长时间训练也会累积塑性损失；定期用固定预算在新数据上微调并评估性能下降，可作为预警指标。

  - 借鉴标度律思路，可在模型升级时预估塑性损失风险的延迟收益，辅助资源投入决策。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机：** 塑性损失（网络学习新信息的能力随训练推进而退化）长期被视为持续学习的核心挑战，但以往研究多基于小规模、非自然语言模型。本文检验该现象在现代GPT式Transformer LLM中是否仍存在，以及单纯扩大规模能否解决。

**方法：** 在5M到314M非嵌入参数规模的GPT模型上进行多语言持续学习实验——先训练英语，再切换至越南语，用越南语探针任务衡量适应新分布的能力。同时考察静态多语言混合训练下的塑性损失。

**关键结果：** 1) 各规模模型均显示明显塑性损失；2) 塑性损失的出现时间遵循亚线性标度律，模型增大可推迟损失显现，但无法根除；3) 在无任务切换的静态多语言训练中同样观测到塑性损失，说明该现象不只是剧变任务引起的。整体结论：增大模型规模只能延缓而无法解决LLM的塑性损失问题。
