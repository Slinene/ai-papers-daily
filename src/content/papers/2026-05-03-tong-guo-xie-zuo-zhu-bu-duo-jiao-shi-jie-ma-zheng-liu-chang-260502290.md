---
title: Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher
  Decoding
title_zh: 通过协作逐步多教师解码蒸馏长链推理
authors:
- Taewon Yun
- Jisu Shin
- Jeonghwan Choi
- Seunghwan Bang
- Hwanjun Song
affiliations:
- KAIST
- UNIST
arxiv_id: '2605.02290'
url: https://arxiv.org/abs/2605.02290
pdf_url: https://arxiv.org/pdf/2605.02290
published: '2026-05-03'
collected: '2026-05-19'
category: Training
direction: 长链推理蒸馏 · 多教师协作解码
tags:
- Long-CoT Reasoning
- Knowledge Distillation
- Multi-Teacher Decoding
- Step-wise Collaboration
- Predictive Perplexity
- Beam Search
one_liner: 提出CoRD框架，通过逐步多教师协作解码和预测困惑度指导，高效生成高质量长链推理数据，显著提升学生模型性能。
practical_value: '- 逐步多教师协作生成数据：让多个异构模型按步骤共同构建推理链，用预测性指标动态选择最优步骤，避免后验选择完整响应的浪费，可用于生成高质量的训练数据，如商品推荐解释或Agent决策推理。

  - 预测困惑度作为步骤质量信号：利用元模型计算当前前缀下正确答案的概率来评估中间步骤，无需额外训练奖励模型，轻量且有效，适用于长序列生成中的中间步骤评估。

  - 束搜索保持多样性：用多个并行轨迹保留有潜力的推理分支，防止过早贪婪选择，允许自我纠正和策略转换，在多智体交互中可保留多个方案，提升最终结果质量。

  - 步骤分割一致性：通过提示工程（如“### Step”）强制不同模型输出结构统一的步骤，便于跨模型比较和组合，可迁移到生成式推荐中需要多模型协作生成推荐理由的场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：长链推理模型（LRM）计算成本高，蒸馏到小模型是关键。现有方法（如S1、LIMO）采用先整体生成后选优的“策展”模式，无法利用多个异构教师协同探索互补推理路径，浪费计算且缺乏动态调整。

**方法关键点**
- **提示引导的步骤分割**：在输入指令中嵌入“<think> ### Step”，引导不同教师生成结构统一、语义连贯的推理步骤，使跨模型比较可行。
- **预测困惑度评分**：在每一步，用元证明器（如最强教师模型）计算当前推理前缀下真实答案的条件概率，作为步骤质量的连续性评估，直接反映推理朝正确答案推进的自然程度。
- **束搜索解码**：维持多个高潜力部分推理轨迹，在每步扩展时从所有教师候选步骤中选择 top-B 更新，保留可自我纠正或策略转换的路径，兼顾局部质量和全局探索。

**关键实验与结果**
- 在 LIMO-v1 数据集上，用 QwQ-32B、R1-Qwen-32B、Phi4-Reasoning-Plus 为教师，CoRD 生成的推理数据答案准确率达93.1%，预测困惑度0.774，显著优于 Curation 和 Integration 基线。
- 蒸馏出的 R1-Qwen-32B 学生模型在 AIME24/25 上 Pass@1 分别为79.6%/70.2%，超过所有单一教师表现（如 QwQ-32B 的 77.9%/66.7%）。
- 在 MATH500、TaTQA、PubMedQA 等外推任务上也一致优于基线，显示了泛化性。

**关键结论**：逐步协作解码将推理蒸馏从一次性选择转变为增量构建，预测困惑度与束搜索结合能高效产出超越教师水平的训练信号，为长链推理迁移提供新范式。
