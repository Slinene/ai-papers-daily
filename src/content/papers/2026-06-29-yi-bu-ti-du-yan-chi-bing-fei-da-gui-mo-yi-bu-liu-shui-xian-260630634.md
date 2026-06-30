---
title: One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline
  Parallel LLM Pretraining
title_zh: 一步梯度延迟并非大规模异步流水线并行LLM预训练障碍
authors:
- Philip Zmushko
- Egor Petrov
- Nursultan Abdullaev
- Mikhail Khrushchev
- Samuel Horváth
affiliations:
- Institute of Science and Technology Austria (ISTA)
- Yandex
- Basic Research of Artificial Intelligence Laboratory (BRAIn Lab)
- Innopolis University
- Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)
arxiv_id: '2606.30634'
url: https://arxiv.org/abs/2606.30634
pdf_url: https://arxiv.org/pdf/2606.30634
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: 异步流水线并行训练与优化器鲁棒性
tags:
- asynchronous pipeline parallelism
- gradient delay
- optimizer robustness
- Muon
- Error Feedback
- LLM pretraining
one_liner: 证明异步流水线并行中的一步延迟下优化器选择决定稳定性，Muon比AdamW鲁棒，结合误差反馈校正可匹敌同步训练
practical_value: '- 训练LLM时可采用 PipeDream-2BW 异步流水线并行消除GPU空闲，大幅提升吞吐；配合 Muon 优化器可避免一步延迟导致的严峻性能下降，无需担心稳定性。

  - 若必须使用 AdamW 等对延迟敏感的优化器，可引入论文提出的 Error Feedback 校正模块，作为一种轻量级的、优化器无关的延迟补偿机制，抑制梯度陈旧影响。

  - 在搜索推荐领域自研大规模模型（如生成式推荐模型）时，可借鉴该结论：分布式流水线并行不必局限于同步方案，异步+Muon 组合可能成为资源利用率和模型质量的更好解。

  - 对于需要快速迭代实验的团队，异步并行带来的高吞吐可直接加速模型训练，结合 Muon 的鲁棒性，有望在保持模型效果的同时缩短研发周期。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：异步流水线并行能消除同步流水线中的GPU空闲（bubble），极大提升吞吐，但引入的一步梯度延迟（PipeDream-2BW 方案保证固定一步延迟）被普遍认为会导致训练不稳定，限制了其在LLM预训练中的实际应用。

**方法与关键点**：
- 首次大规模实证分析显示，一步延迟下的性能退化并非异步并行的固有缺陷，而是强烈依赖于优化器选择：当年 PipeDream-2BW 提出时主流的 AdamW 确实会严重退化，但新近的优化器 Muon 对一步延迟表现出强鲁棒性。
- 提出一种受 Error Feedback 启发的、优化器无关的校正技术，进一步缓解延迟效应，并可灵活插入任意优化器。
- 为 Muon 在延迟设置下提供收敛理论分析，覆盖无校正与带校正两种情况。

**关键结果**：在高达10B参数的模型上评测，采用 Muon + Error Feedback 校正的异步流水线并行训练损失与同步训练差距几乎消失（例如在某个规模下同步与异步的困惑度差异从不可接受降至可忽略），证实异步流水线并行可达到与同步方案同等的模型质量，同时收获显著吞吐收益。
