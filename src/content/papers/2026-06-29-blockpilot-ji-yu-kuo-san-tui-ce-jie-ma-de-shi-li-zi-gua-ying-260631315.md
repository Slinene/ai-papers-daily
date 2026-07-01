---
title: 'BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative
  Decoding'
title_zh: BlockPilot：基于扩散推测解码的实例自适应块大小策略学习
authors:
- Hao Zhang
- Yiming Hu
- Yong Wang
- Mingqiao Mo
- Xin Xiao
- Xiangxiang Chu
affiliations:
- AMAP, Alibaba Group
arxiv_id: '2606.31315'
url: https://arxiv.org/abs/2606.31315
pdf_url: https://arxiv.org/pdf/2606.31315
published: '2026-06-29'
collected: '2026-07-01'
category: LLM
direction: 推测解码 · 实例自适应块大小
tags:
- speculative decoding
- diffusion model
- block size
- adaptive policy
- inference acceleration
- dLLM
one_liner: 提出从预填充表示学习预测最优块大小的策略，突破固定块限制，提升扩散推测解码效率
practical_value: '- 在大模型在线推理（如对话式推荐、搜索 Agent）中，可集成该自适应策略，根据 prompt 的预填充特征动态选择最优块大小，无痛提升加速比，且预测开销极小。

  - 方法即插即用，无需修改原扩散推测解码框架，适合在已有推理管道中快速部署，降低工程改动成本。

  - 揭示了最优块大小的局部结构——集中在训练块尺寸附近，可据此设定搜索范围或剪枝预测类别数，简化策略学习。

  - 对于需要低延迟响应的业务场景（如实时广告文案生成、个性化推送），该技术能有效减少端到端延迟，提升用户体验。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：扩散推测解码通过并行生成 token 块大幅提升 LLM 推理速度，但现有方法固定块大小，忽略了不同输入样本的差异，导致效率次优。作者发现最优块大小因样本而异且呈局部结构（集中在训练块尺寸附近），从而将问题转化为低维结构化决策。

**方法**：提出 BlockPilot，一种样本自适应策略。在预填充阶段后，利用轻量级模块从输入表示预测当前样本的最优块大小，仅需一次前向计算。该策略通过离线模拟生成标签并优化交叉熵损失学习，无缝嵌入现有框架，不改变 diffusion draft model 与 target LM 的交互方式。

**结果**：在 Qwen3-4B 上，temperature T=1 时，BlockPilot 实现 5.92 的接受长度和 4.20× 加速比，超越固定块方案且开销微小。消融实验表明预测准确率与效率增益正相关，验证了自适应块大小的关键作用。
