---
title: When is Your LLM Steerable?
title_zh: LLM激活引导何时可行？基于早期隐藏状态预测的可控性
authors:
- Chenrui Fan
- Yize Cheng
- Ming Li
- Soheil Feizi
- Tianyi Zhou
affiliations:
- University of Maryland, College Park
- MBZUAI
arxiv_id: '2606.11599'
url: https://arxiv.org/abs/2606.11599
pdf_url: https://arxiv.org/pdf/2606.11599
published: '2026-06-09'
collected: '2026-06-15'
category: LLM
direction: LLM激活引导 · 早期状态预测引导效果
tags:
- activation_steering
- steerability_prediction
- GBDT
- inference_time_control
- early_decoding
one_liner: 用生成前几步的隐藏状态差异训练GBDT，预测激活引导是欠调、成功还是过调，预测器可指导强度搜索，大幅降低解码成本
practical_value: '- **激活引导的行为预测可用于Agent/对话系统**：在电商客服、推荐解释生成等场景，若需控制输出风格（如语气、说服力），可在生成前几步后即判断引导是否有效，避免了完整生成后评估，节省推理成本。

  - **特征工程思路可复用**：提取引导前后隐藏状态的差异，对比不同层和初始token位置的激活偏移，这类特征能结构化编码引导传播路径，类似做法可用于业务中判断模型是否遵循特定指令。

  - **轻量预测器做在线决策**：用GBDT对早期状态做三分类（欠调/成功/过调），预测速度快，可嵌入推理管线，实时调整引导强度或决定是否重试，无需耗时的网格搜索。

  - **引导强度动态搜索**：利用预测器作为指导，在小部分解码步骤后预测效果，快速逼近最优强度，这种思路适用于任何需要调参的控制方法（如LoRA权重、prompt权重）。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：激活引导是一种轻量级推理时控制LLM行为的方法，但成功与否高度依赖提示、概念、模型和引导强度，传统上需通过昂贵的网格搜索和完整生成来评估。本文探索能否从生成最初几步的隐藏状态中预测最终引导效果，并用预测器改进引导成功率。

**方法**：首先构建ASTEER测试集，包含150个概念、1.4M次引导生成，每次标注为欠调、成功或过调。然后提取特征：在引导前后，对每个层和每个初始解码步骤，计算隐藏状态的差异（如余弦距离、L2范数变化等），以此捕捉引导效应的传播模式。基于这些特征训练一个GBDT分类器，在仅看到前几个token后即可预测最终状态，无需完整序列。

**结果**：在未见概念上，预测器达到约0.7的宏F1分数，表明早期隐藏状态编码了丰富的结局信息。进一步用预测器指导引导强度的搜索，仅使用少量解码成本（约10%）即可接近通过完整评估才能达到的最优性能。
