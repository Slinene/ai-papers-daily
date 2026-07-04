---
title: Multimodal Continuous Reasoning via Asymmetric Mutual Variational Learning
title_zh: 非对称互变分学习实现多模态连续推理
authors:
- Shijie Li
- Yilin Gao
- Siyuan Yang
- Tieyuan Chen
- Chaofan Gan
- Zhihao He
- Zicheng Zhao
- Yuyu Guo
- Weiyao Lin
- Hang Yu
affiliations:
- Shanghai Jiao Tong University
- Ant Group
arxiv_id: '2607.00461'
url: https://arxiv.org/abs/2607.00461
pdf_url: https://arxiv.org/pdf/2607.00461
published: '2026-06-30'
collected: '2026-07-04'
category: Reasoning
direction: 连续潜变量推理 · 训练-推理校准
tags:
- Multimodal Reasoning
- Continuous Latent Reasoning
- Variational Learning
- KL Divergence
- Train-Inference Mismatch
- MLLM
one_liner: 提出AMVL框架，通过双向KL散度校准缓解训练-推理不匹配，提升连续潜变量推理稳定性
practical_value: '- 电商推荐中，生成式item编码（如Semantic ID）常依赖答案信息（下一item）进行连续潜变量建模，AMVL的双向KL正则可防止后验泄漏未来信息，提升在线推理质量。

  - 多模态Agent决策时，若使用连续潜变量规划动作，逆KL惩罚后验可避免利用未来信息，使规划模型更贴近真实推理环境。

  - 工程上，双向KL仅增加一个正则项，可简便集成到现有VAE推荐框架，适用于对话式推荐、动态创意生成等交互生成任务。

  - 论文对“先验污染”的理论分析以及训练-推理不匹配的量化，为推荐系统中teacher-forcing训练策略的改进提供了新视角。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机：** 多模态大模型被迫将连续视觉概念离散化成语言token，丢失感知细节。连续潜变量推理可绕过语言瓶颈，但存在严重训练-推理不匹配：训练时后验网络利用真值答案产生捷径，标准变分训练迫使推理时的先验模仿这种含有答案泄漏信息的后验，导致测试性能骤降。

**方法：** 提出非对称互变分学习(AMVL)，引入双向校准目标。正向KL项训练先验逼近后验，同时创新性地加入逆向KL散度正则化后验，阻止其坍塌到与推理不兼容的区域，从而缓解“答案泄漏”。理论分析将泄漏形式化为“先验污染”，并证明双KL目标能有效减小污染。

**关键结果：** 在多模态大模型中实例化AMVL，在复杂视觉推理基准BLINK上，平均得分提升+10.83，个别任务提升高达+32.00，潜空间稳定性明显增强，一致优于强离散及潜变量推理基线。
