---
title: 'CausalMix: Data Mixture as Causal Inference for Language Model Training'
title_zh: CausalMix：通过因果推断优化语言模型训练数据混合
authors:
- Zinan Tang
- Yukun Zhang
- Shaomian Zheng
- Zhuoshi Pan
- Qizhi Pei
- Dingnan Jin
- Jun Zhou
- Yujun Wang
- Biqing Huang
affiliations:
- Tsinghua University
- Ant Group
- Renmin University of China
arxiv_id: '2607.01104'
url: https://arxiv.org/abs/2607.01104
pdf_url: https://arxiv.org/pdf/2607.01104
published: '2026-06-30'
collected: '2026-07-02'
category: Training
direction: 数据混合优化 · 因果推断
tags:
- Data Mixture
- Causal Inference
- LLM Training
- CATE
- Extrapolation
one_liner: 将数据混合优化转化为因果推断问题，利用CATE从小规模实验外推到大规模模型与数据
practical_value: '- **推荐模型多域数据配比**：电商推荐中常需融合搜索、推荐、广告等多域数据，可借鉴CausalMix用小规模代理实验+因果模型推断最优配比，避免大规模重训。

  - **混杂因子控制**：将数据域特征（如长度、难度）作为协变量，显式建模以剔除伪相关，提升配比泛化性，适用于动态数据池下的训练策略调整。

  - **外推能力**：方法支持从0.5B模型外推到7B模型，从512次运行外推至800K数据池，可降低推荐模型在不同规模、不同时段数据上的配比试错成本。

  - **可解释性工具**：CATE Interpreter提供可视化的混合策略分析，可帮助理解不同数据域对下游任务的影响，指导人工调参。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM训练中数据混合决定性能，但现有方法假设数据分布固定，数据池变化时需从头重训，无法低成本从小规模实验扩展到大规模模型与数据。

**方法关键点**：
- 将数据混合优化形式化为因果推断：以数据池统计特征（如领域难度、平均长度、质量得分）为协变量，领域混合比例为处理变量，下游任务表现为结局。
- 在Qwen2.5-0.5B上运行512次不同混合实验，拟合因果模型估计**条件平均处理效应（CATE）**。
- 训练一个CATE预测器，输入新数据池的协变量，直接输出该池每个任务的最优混合权重，实现外推。
- 将外推得到的混合方案应用于800K数据池训练7B模型，并成功扩展到Chain-of-Thought数据。
- 提供**CATE Interpreter**可视化学习到的混合策略，解释不同数据域如何影响性能。

**关键结果**：CausalMix在多个下游任务上一致提升，优于RegMix等基线；成功从512次小模型实验外推到7B模型的大规模训练，且泛化到新的数据域和模型系列。
