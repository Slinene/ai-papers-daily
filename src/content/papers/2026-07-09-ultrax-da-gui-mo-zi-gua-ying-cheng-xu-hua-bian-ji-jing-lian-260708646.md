---
title: 'UltraX: Refining Pre-Training Data at Scale with Adaptive Programmatic Editing'
title_zh: 'UltraX: 大规模自适应程序化编辑精炼预训练数据'
authors:
- Xinlong Zhao
- Dongsheng Liu
- Hengyu Zhao
- Zixuan Fu
- Zheng Wang
- Jie Cai
- Jie Zhou
- Qiang Ma
- Xuanhe Zhou
- Xu Han
affiliations:
- Peking University
- ModelBest Inc.
- Tsinghua University
- Shanghai Jiao Tong University
arxiv_id: '2607.08646'
url: https://arxiv.org/abs/2607.08646
pdf_url: https://arxiv.org/pdf/2607.08646
published: '2026-07-09'
collected: '2026-07-10'
category: Training
direction: 预训练数据精炼 · 程序化编辑
tags:
- Data Refinement
- Programmatic Editing
- Pre-training
- Function Calling
- Data Quality
one_liner: 提出函数调用式程序编辑框架，以插入/删除/修改实现细粒度数据精炼，提升预训练数据效率与质量
practical_value: '- 可将数据清洗定义为插入、删除、修改的程序操作，用小型模型（0.6B）学习执行，在推荐系统的大规模预训练语料上实现快速、高质量的精炼，比纯规则或LLM方法更平衡效率与效果。

  - 构造监督数据的方法（专家LLM生成精炼文本 → 行对齐 → 编辑操作序列）可直接迁移到商品描述优化、搜索词纠错等业务场景，低成本获取结构化编辑信号。

  - 滑动窗口预测与全局操作聚合的推理策略增强了长序列编辑的稳定性，可用于推荐系统中超长行为序列的规范化处理。

  - 低置信度过滤与基于操作组合的比例采样，可借鉴用于提升推荐模型微调的数据质量与训练分布稳定性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：遵循Scaling Law的语言模型正面临数据枯竭，单纯增加数据量带来的收益递减，提升数据质量成为关键。现有精炼方法中，规则方法无法适应实例级变化，LLM方法质量高但效率与可靠性不足。需要一种可大规模、细粒度编辑预训练数据的方法。

**方法**：UltraX将数据精炼建模为函数调用，引入插入、删除、修改三种编辑操作，构造完整的程序编辑空间。首先，使用专家LLM在自适应提示下生成高质量的端到端精炼文本；然后通过行对齐映射和动态上下文替换，把原始-精炼文本对转化为结构化的编辑操作序列（程序监督）。为稳定训练，采用低置信度样本过滤和按操作组合比例采样的策略。训练一个0.6B的编辑模型来预测编辑操作。推理时，通过滑动窗口预测、全局操作聚合与系统后处理对输出进行校验，保证大规模执行的可靠性。

**关键结果**：在多个语料上从零预训练1B模型，UltraX在所有语料上平均性能最高，且仅需更少的训练token即可匹配或超越未精炼基线，验证了其数据效率与精炼可靠性。
