---
title: 'The Tell-Tale Norm: $\ell_2$ Magnitude as a Signal for Reasoning Dynamics
  in Large Language Models'
title_zh: ℓ2 范数：大语言模型推理动态的内在信号
authors:
- Jinyang Zhang
- Hongxin Ding
- Yue Fang
- Weibin Liao
- Muyang Ye
- Junfeng Zhao
- Yasha Wang
affiliations:
- Peking University
- Zhejiang University
arxiv_id: '2606.06188'
url: https://arxiv.org/abs/2606.06188
pdf_url: https://arxiv.org/pdf/2606.06188
published: '2026-06-04'
collected: '2026-06-05'
category: LLM
direction: LLM 推理内在信号与测试时控制
tags:
- ℓ2 norm
- reasoning dynamics
- sparse autoencoders
- test-time scaling
- hidden state
one_liner: 发现隐藏状态 ℓ2 范数是无需训练的模型内在推理强度指标，并基于此提出三种推理增强技术。
practical_value: '- 在 LLM Agent 推理链中，可实时监控各层 ℓ2 范数，检测推理峰值以自适应分配计算资源（如递归计算或提前退出），在电商复杂查询解析、多步决策等场景提升效率。

  - 对生成式推荐，ℓ2 范数可作为一种无监督的候选序列质量度量，替代外部打分或规则，用于生成式 item 推荐中的响应重排或生成路径选择。

  - 三种推理增强技术（层递归、隐藏状态引导、响应选择）无需额外训练，可直接嵌入现有的推理引擎，为推理时 Agent 缩放提供轻量、数据无关的工具。

  - 发现 ℓ2 范数与 SAE 推理特征激活高度正相关且具有因果性，提示在训练推荐/Agent 模型时，可加入 ℓ2 正则或约束来激励中间推理表征，提升模型对复杂任务的泛化。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：大语言模型（LLM）在复杂推理上的表现日益突出，但其内部层间推理动态仍不透明。现有方法依赖稀疏自编码器（SAE）等外部探针，或从输出层分析，训练成本高、模型特定性强，难以通用。亟需一种模型内在、无需训练的推理强度信号，以便感知和控制推理过程。

**方法关键点**：
- 利用 SAE 分析 Qwen-3 等模型的逐层隐藏状态，发现推理特征激活在后期层急剧升高，揭示层间推理动态。
- 理论证明在 SAE 重建保真和特征正交假设下，隐藏状态 ℓ2 范数可上下界 SAE 推理特征激活强度，从而成为推理强度的内生指标。
- 大规模相关与因果分析：ℓ2 范数与 SAE 推理激活 Spearman 相关系数达 0.84–0.87，与输出熵正相关；抑制高范数隐藏状态导致性能大幅下降，证明其因果重要性。
- 提出三种测试时推理增强技术：自适应逐层推理递归（ALRR）在 ℓ2 峰值层内迭代加深计算；内生推理状态引导（ERSS）利用历史高范数状态增强当前表征；ℓ2 引导的响应选择（LRS）用中间-后层范数累积分拣候选输出。所有技术无需额外训练或数据。

**关键结果**：在 Qwen3 系列和 DeepSeek-R1-Distill-Llama 上，覆盖数学与通用推理基准，平均相对提升 4.51%，挑战性任务 AIME 提升达 9.13%。跨基准 ℓ2 分布显示任务难度影响明显，验证了自适应阈值机制的必要性。

**核心启示**：隐藏状态 ℓ2 范数是一个简单、可靠的内在推理强度信号，可低成本地监控和放大 LLM 的推理计算，为推理增强和机制解释性提供了新视角。
