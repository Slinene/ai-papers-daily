---
title: Thinking with Looped Flows
title_zh: 用循环流思考
authors:
- Ayhan Suleymanzade
- Chanhyuk Lee
- Floor Eijkelboom
- Nicholas M. Boffi
- İsmail İlkan Ceylan
- Jinwoo Kim
affiliations:
- EPFL
- KAIST
- University of Amsterdam
- Carnegie Mellon University
- TU Wien
arxiv_id: '2609.11801'
url: https://arxiv.org/abs/2609.11801
pdf_url: https://arxiv.org/pdf/2609.11801
published: '2026-09-10'
collected: '2026-09-11'
category: Reasoning
direction: 循环神经网络与概率流推理
tags:
- Looped Models
- Flow Matching
- Denoising
- Inference-time Compute
- Test-time Scaling
one_liner: 提出循环流模型，用局部去噪目标训练循环网络，推理时积分概率流实现计算扩展，在ARC-AGI等基准上超越先前的循环模型
practical_value: '- 循环生成模型训练中，若梯度只截断少数步（如在线生成式推荐的多步解码），可借鉴局部去噪目标：每一步只做当前噪声水平的去噪，不要求整个循环链端到端可微，缓解早期步骤无法支持后续步骤的问题。

  - 推理时通过更细的时间网格积分概率流，用更多计算换取更好预测，适合对延迟敏感的业务按负载动态调整解码步数，实现在线算力弹性伸缩。

  - 从不同初始噪声采样可获得多个有效预测，可用于生成式推荐中产出多样化候选 item，后续用排序模型筛选或做多样性打散，兼顾覆盖与准确。

  - 循环状态与流状态解耦（先运行去噪器更新循环状态，再执行 ODE/SDE 步），工程上易于模块化，可分别优化状态传递逻辑和数值积分器。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：深度学习模型在推理时计算量固定，难以处理需要更多步骤的难题。循环模型通过循环更新隐藏状态实现计算扩展，但训练时 BPTT 通常只截断少数步，导致早期更新难以支持后续迭代。

**方法关键点**：
- 提出 **looped flows**：训练循环网络时使用局部去噪目标，每一步预测被噪声污染的解，并更新循环状态。
- 关键 trick：噪声水平随时间逐步降低，且不同样本共享噪声，从而强制循环状态传递对后续步骤有用的计算，无需完整梯度回传。
- 推理时将学到的去噪器参数化为概率流的速度场，循环状态与流状态耦合，通过 ODE/SDE 积分求解；用更细的时间网格增加计算量，从不同初始噪声采样得到多个有效预测。

**关键结果**：在六个推理基准（含两个多解基准）上超越先前 SOTA 循环模型，ARC-AGI-1 测试准确率 58.8%，ARC-AGI-2 为 12.2%。
