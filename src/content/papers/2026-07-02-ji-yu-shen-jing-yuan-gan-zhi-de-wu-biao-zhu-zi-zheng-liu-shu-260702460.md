---
title: Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation
title_zh: 基于神经元感知的无标注自蒸馏数据选择方法
authors:
- Zhuowei Chen
- Xiang Lorraine Li
affiliations:
- University of Pittsburgh
arxiv_id: '2607.02460'
url: https://arxiv.org/abs/2607.02460
pdf_url: https://arxiv.org/pdf/2607.02460
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: 无标注LLM自蒸馏与数据选择
tags:
- Neuron-Aware
- Self-Distillation
- Annotation-Free
- On-Policy
- Calibration
- LLM
one_liner: 通过神经元激活筛选无标注数据和构造上下文，实现无监督LLM自蒸馏，提升领域性能且保持泛化
practical_value: '- 可利用**神经元激活计数**筛选模型易答对的未标注样本进行自训练，降低电商/推荐领域高质量标注依赖。

  - **通过神经元激活重叠度检索少样本上下文**构造教师提示，提升伪标签质量，可借鉴到LLM生成式推荐的教师模型构建。

  - 采用**逆向KL蒸馏 + EMA教师**稳定训练，避免校准崩塌，适合需校准概率的推荐场景（如CTR预估）。

  - 纯**离线、无奖励信号**的迭代框架，适合无在线交互的广告/搜索系统日志后训练。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：专业领域LLM后训练缺乏交互反馈或人工标注，现有无标注自进化方法（SFT/GRPO、RL）存在域外性能下降或校准误差增大的问题。

**方法关键点**：提出Neuron-OPSD，一个基于数据选择的无标注自蒸馏框架。核心在于利用LLM内部神经元激活指导训练数据筛选与教师上下文构建：（1）对未标注数据执行零样本滚动，收集神经元激活，用激活神经元数量近似答案正确性，选择最低20%干净样本作为训练集；（2）通过神经元激活重叠度检索top-K滚动近邻样本，组成少样本上下文，构造教师分布；（3）学生模型通过逆向KL损失拟合教师分布，教师由EMA更新。全过程无需真实标签。

**结果**：在多个专业领域基准上，Neuron-OPSD相比基线提升了域内性能，同时保持跨域泛化，显著缓解校准崩塌。
