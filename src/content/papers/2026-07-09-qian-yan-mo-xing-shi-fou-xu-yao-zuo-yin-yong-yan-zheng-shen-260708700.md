---
title: Do You Need a Frontier Model as a Citation Verifier? Benchmarking Rubric LLMs
  for Deep-Research Source Attribution
title_zh: 前沿模型是否需要做引用验证？深度研究来源归属的评判模型基准测试
authors:
- Ethan Leung
- Elias Lumer
- Corey Feld
- Austin Huber
- Vamse Kumar Subbiah
- Kevin Paul
affiliations:
- Commercial Technology and Innovation Office, PricewaterhouseCoopers, U.S.
arxiv_id: '2607.08700'
url: https://arxiv.org/abs/2607.08700
pdf_url: https://arxiv.org/pdf/2607.08700
published: '2026-07-09'
collected: '2026-07-11'
category: Eval
direction: LLM裁判校准·评估偏差分析
tags:
- LLM Judge
- Citation Verification
- Rubric Evaluation
- Reward Model
- Model Calibration
- Deep Research
one_liner: 对比8个LLM裁判在引用质量评估中的表现，发现便宜模型即可胜任，且标量F1掩盖的方向性偏差会误导RL训练
practical_value: '- **选裁判不必选最贵**：在结构化评估任务（如推荐理由真实性、搜索结果相关性）中，GPT-4o-mini等小模型即可获得与大模型相当的F1，可大幅降低离线评估和RL奖励信号的计算成本。

  - **单看F1会踩坑**：即使各裁判F1相近，其通过率漂移、假阳性/假阴性率可能差异巨大，这会直接扭曲RL训练的优化方向。评估裁判时必须同时报告方向性偏差指标。

  - **校准裁判是使用LLM作为奖励模型的前提**：在将LLM用于生成式推荐、对话Agent的自动评分时，应先进行类似的人工标注一致性实验，量化裁判的偏差，并选择与业务目标一致的错误偏好（例如宁愿假阴性还是假阳性）。

  - **对抗样本测试很重要**：论文采用对抗生成的长文本评估集，并人工仲裁困难案例。类似地，在电商搜索中应构建覆盖歧义、多义等难例的评估集，确保裁判鲁棒性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：RLVR训练中普遍使用LLM裁判作为奖励模型，但裁判自身的能力和偏差缺乏校准研究。针对深度研究中的引用质量评估（每个声明需附来源验证），需要明确裁判模型的选择标准。

**方法**：设计一个结构化的评判任务，从来源相关性和事实支持两个维度评估引用-来源对。收集对抗生成的长文本基准，包含1,248个评判项，全部经人工复核，其中378个困难案例由裁判分歧结果仲裁得到。测试了3个模型系列、8种现成的LLM裁判，以人工金标签为准，计算F1、Kappa、通过率漂移、假阳性/假阴性率等指标。

**关键结果**：
- 便宜模型表现不逊于前沿模型：GPT-5-mini在来源相关性上获得最高通过类F1（0.908，κ=0.636），在事实支持维度上各裁判统计不可区分。
- 单纯的F1掩盖了方向性偏差：裁判间的假阳性率、假阴性率差异显著，这种偏差若进入RL下游循环会被放大。
- 校准裁判是必要步骤，且不一定要使用最昂贵的模型。
