---
title: From Large Language Models to Efficient System One Models via Adaptive Computation
title_zh: 从大语言模型到高效系统一模型的自适应计算转换
authors:
- Minh-Anh Nguyen
affiliations:
- Nanyang Technological University, Singapore
arxiv_id: '2611.16321'
url: https://arxiv.org/abs/2611.16321
pdf_url: https://arxiv.org/pdf/2611.16321
published: '2026-11-11'
collected: '2026-11-14'
category: LLM
direction: 自适应计算 · System One 决策
tags:
- adaptive computation
- early exit
- self-distillation
- LLM fine-tuning
- system one
one_liner: 提出 NESTONE，用共享末层与决策头的前缀子模型加门控自适应深度，在决策任务上实现更优精度效率权衡
practical_value: '- 在电商/Agent 的高频轻量决策场景（意图识别、工具选择、路由、安全过滤）中，可借鉴嵌套子模型训练：多个深度共享末层与决策头，通过自蒸馏对齐，单模型服务多档延迟/精度，避免维护多个独立小模型。

  - 用轻量门控读隐状态判断是否继续计算，能实现“简单样本早退、难样本深算”，适合推荐系统中的实时打分或 query 理解等对 p99 延迟敏感的服务。

  - 论文结论提示决策信息集中在中间层，末 6 层可移除，说明精调此类决策模型不必保留完整 LLM backbone；在召回/粗排等轻量模型中可尝试裁剪深层并自蒸馏复用主模型表示。

  - 独立训练的小模型主要模仿全模型而非发展专门决策能力，建议业务中优先复用主模型底层特征或做知识蒸馏，而不是单独训练小模型。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM 智能体需要大量 System One 快速决策，如路由请求、选择工具、识别意图等，但目前的做法是在完整 LLM backbone 上替换决策头，每个决策都要跑全部层，延迟高且低效。作者先探究这类决策到底需要多深。

方法关键点：发现决策信息集中在中间层，早期层构建基础特征，末 6 层可直接移除而不损失精度；而独立训练的小模型只是模仿全模型，没有发展出专门决策能力。基于此，提出 NESTONE：联合训练完整模型与多个前缀子模型，所有子模型共享末层和决策头，通过自蒸馏对齐；每个 exit 放置一个轻量门控，读取当前隐状态决定是否需要继续深层计算，让一个模型在多个深度自适应运行。

关键结果：在 7 个决策基准上，NESTONE 在每个深度都匹配或优于独立训练的模型；自适应门控在四个最大基准上保持精度与固定 24 层出口相差不超过 0.1 个百分点，同时将平均计算层数从固定出口的约 20.7 层降至约 17-19 层，实现更好的精度-效率权衡。
