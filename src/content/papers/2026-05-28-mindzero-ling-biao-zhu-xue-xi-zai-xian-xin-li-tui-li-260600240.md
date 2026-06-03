---
title: 'MindZero: Learning Online Mental Reasoning With Zero Annotations'
title_zh: MindZero：零标注学习在线心理推理
authors:
- Shunchi Zhang
- Jin Lu
- Chuanyang Jin
- Yichao Zhou
- Zhining Zhang
- Tianmin Shu
affiliations:
- Johns Hopkins University
- Peking University
arxiv_id: '2606.00240'
url: https://arxiv.org/abs/2606.00240
pdf_url: https://arxiv.org/pdf/2606.00240
published: '2026-05-28'
collected: '2026-06-03'
category: Reasoning
direction: 多模态LLM · 自监督RL · 心理推理
tags:
- Theory of Mind
- Self-supervised RL
- Multimodal LLM
- Online Inference
- Agent ToM
one_liner: 自监督强化学习训练多模态大模型进行在线心理推理，无需真实心理状态标注
practical_value: '- 电商客服/导购Agent可借鉴：从用户行为序列（点击、停留、加购）自监督学习推断意图（如购买动机、偏好），无需人工标注心理状态，利用行动似然估计（如购买概率模型）提供训练信号。

  - 多步推理压缩为单步前向：将需要多轮模拟或规划的意图推理内化到单次MLLM前向，显著降低延迟，适合实时交互场景。

  - 多假设信念更新机制：让LLM生成并维持多个用户意图假设，根据新观察行为更新概率，可用于动态用户建模（如推荐中的兴趣漂移）。

  - 利用环境动力学（planner）作为评判：在缺乏真实用户意图标签时，通过可观测的结果（如下单、跳出）反推用户心理状态，构建自监督奖励，适用于推荐系统对用户心智模型的隐式学习。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：AI助手需具备心智理论（ToM），从行为推断人类心理状态。现有方法面临在线多假设不确定性更新、实时推理效率、以及真实心理状态标注缺失三大挑战。

**方法**：提出MindZero，一个自监督强化学习框架，训练多模态大语言模型（MLLM）进行在线心理推理。训练时，模型生成多个心理状态假设，以最大化观察动作的似然为奖励信号（由基于模型的planner估计），无需显式标注。推理时，将原本缓慢的模型式推理内化为单次前向，实现高效实时的心理状态推断。

**实验结果**：在gridworld和居家场景的心理推理与AI协助任务中，MindZero显著提升MLLM的内在ToM能力，准确率和效率均优于基于模型的方法。单独的LLM推理准确率不足；模型式方法虽提高准确率但成本高、速度慢；MindZero则实现了快速且高精度的在线心理推理。
