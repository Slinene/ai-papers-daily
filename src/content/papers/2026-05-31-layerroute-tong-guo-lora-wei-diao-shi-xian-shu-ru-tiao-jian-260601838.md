---
title: 'LayerRoute: Input-Conditioned Adaptive Layer Skipping via LoRA Fine-Tuning
  for Agentic Language Models'
title_zh: 'LayerRoute: 通过 LoRA 微调实现输入条件自适应层跳过'
authors:
- Prateek Kumar Sikdar
affiliations:
- Accenture
arxiv_id: '2606.01838'
url: https://arxiv.org/abs/2606.01838
pdf_url: https://arxiv.org/pdf/2606.01838
published: '2026-05-31'
collected: '2026-06-09'
category: Agent
direction: Agent 推理加速 · 自适应层跳过
tags:
- Layer Skipping
- LoRA
- Agentic LLM
- Inference Efficiency
- Straight-Through Estimator
one_liner: 用 1.1M 参数教会 0.5B 模型按步型跳层：工具调用省 15.2% FLOPs，规划几乎不跳，质量不降反升。
practical_value: '- **Agent 推理系统加速**：在工具调用占比高的场景（如电商客服中的查订单、查库存），可对 LLM 使用 LayerRoute
  适配，保持规划能力同时大幅降低工具步驟计算量，直接提升吞吐。

  - **不同请求类型动态深度分配**：推荐/Agent 场景中，简单确定性请求与复杂推理请求可复用本方法——用极少量参数为每层配路由器 + LoRA，按输入类型动态跳过若干层，实现“按需深度”。

  - **偏置初始化的工程技巧**：对分层路由任务，有意识将中间层初始化为“跳过”状态（bias 负值），可打破对称，让梯度信号快速区分层的重要性，避免所有门控全开。

  - **门正则化防止平凡解**：任何可学习门控机制（如多分支动态路由、MoE 专家选择）都应加入类似正则项，否则模型倾向于保持所有通路开启，丧失动态选择能力。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
Agentic LLM 系统中，工具调用（结构化、低困惑度）与规划/推理步骤（长、高困惑度）的计算需求截然不同，但现有推理系统对所有步骤分配相同计算量，造成明显浪费。工具调用的高置信度往往使深层 Transformer 贡献有限。本文希望让模型能按输入类型自适应跳过部分层，以节省推理成本。

**方法关键点**  
- 在 Qwen2.5-0.5B-Instruct 的 24 个块上，每块外加一个路由器（Linear(896,1) → sigmoid → 硬门控 0/1），与冻结的主干和额外的 LoRA 适配器（rank=8, Q/K/V/O 投影）联合训练。  
- 使用直通估计器（STE）实现前向硬门控、反向梯度经过 sigmoid，消除训练与推理的不一致。  
- 训练目标 = 语言建模交叉熵损失 + 门正则化（惩罚高门控值），强迫路由器找出可跳过的层。  
- 关键初始化：前 8 层和后 7 层偏置 +1.0（初始门控 ≈0.73，保持开放），中间 9 层偏置 −1.0（初始门控 ≈0.27，关闭），打破对称，使梯度立即反映层的必要性。  
- 在混合 Agent 数据（Hermes 函数调用、Glaive 函数调用、GSM8K 等）上训练 3000 步，batch size 16，单张 A100 约 6.4 分钟完成。

**关键结果**  
- 在 100 条测试样本上，工具调用跳过 15.25% FLOPs（平均运行 20.34 层），规划仅跳过 2.34%（23.44 层），跳过差异 12.91%。  
- 由于 LoRA 适配，困惑度反比全量基线下**降** 1.29（工具调用）和 1.30（规划），实现有损变增益。  
- 门控收敛为稳定的两簇：第 0–7 层与 17–23 层常开，第 8–16 层常闭，方差仅 0.05，完全区分任务类型。  
- 消融实验表明：去掉正则化则跳过率几乎为零；统一初始化导致规划跳过更多（-5.4%），反常用设计。

**一句话结论**  
用偏置初始化和门正则化，仅 0.22% 的可训参数就能让预训练 LLM 学会根据 Agent 步骤类型动态跳过中层，在零质量损失下获得确定性的推理加速。
