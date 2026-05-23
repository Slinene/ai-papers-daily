---
title: Forecasting Scientific Progress with Artificial Intelligence
title_zh: 用AI预测科学进展：评估前沿模型的局限性
authors:
- Sean Wu
- Pan Lu
- Yupeng Chen
- Jonathan Bragg
- Yutaro Yamada
- Peter Clark
- David Clifton
- Philip Torr
- James Zou
- Junchi Yu
affiliations:
- University of Oxford
- Stanford University
- Allen Institute for AI
- Sakana AI
arxiv_id: '2605.22681'
url: https://arxiv.org/abs/2605.22681
pdf_url: https://arxiv.org/pdf/2605.22681
published: '2026-05-20'
collected: '2026-05-23'
category: Eval
direction: 科学预测评估 · 时序知识截止
tags:
- benchmark
- scientific forecasting
- evaluation
- frontier models
- uncertainty estimation
- temporal prediction
one_liner: 提出CUSP基准评估AI预测科学进展的能力，发现当前模型无法可靠预测科学发现的实现与时机，且存在过度自信。
practical_value: '- **评估框架可迁移**：CUSP的时序知识截止、多维度评估（可行性、机制推理、解决方案设计、时间预测）设计可迁移到电商销量预测或趋势预测的模型评测中，通过控制训练数据时间窗并引入机制判断，更细粒度诊断预测能力的短板。

  - **不确定性校准至关重要**：模型在预测任务中表现出系统性过度自信和偏差，提示在推荐系统或Agent推理中，应引入类似的信心评估与校准分析，避免盲目信任模型预测，尤其是在时序前置信息有限时。

  - **领域异质性的警示**：AI领域预测准确率高于生物、化学、物理，提醒跨领域预测模型（如不同品类、不同市场）可能存在严重域偏置，需要针对性校准，不可直接复用。

  - **历史知识增益有限**：额外训练前知识能提升但无法弥补到全信息水平，表明单纯堆料不能解决预测问题；在电商长期策略（如大促影响预测）中，可借鉴该实验设计，用受控信息增量测试模型上限。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：AI已广泛应用于科学发现过程，但它能否提前预测科学进展仍未知。现有评估缺乏对时序知识和预测能力的系统性检验。

**方法**：引入CUSP基准，包含4760个跨学科（AI、生物、化学、物理）科学事件，每个事件设有截止日期。任务包含四维度：可行性判断、机制推理、生成解决方案设计、以及时间预测（是否发生、何时发生）。通过控制模型训练数据截止前后信息，分析知识暴露的影响。

**关键结果**：
- 前沿模型能识别合理方向，但无法可靠预测事件是否实现，时间预测误差大；
- 表现对训练截止前后事件不敏感，主要限制不在知识暴露本身；
- 额外提供截止前知识可提升但远未达到全信息水平，高引工作提升更有限；
- 模型普遍过度自信，校准失败，出现固定响应偏置。

结论：现有AI远非可靠的科学预测工具，预测能力更依赖事后信息而非前向推理。
