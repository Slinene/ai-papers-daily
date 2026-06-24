---
title: 'OpenThoughts-Agent: Data Recipes for Agentic Models'
title_zh: 训练通用智能体模型的数据配方：开放实验与消融研究
authors:
- Negin Raoof
- Richard Zhuang
- Marianna Nezhurina
- Etash Guha
- Atula Tejaswi
- Ryan Marten
- Charlie F. Ruan
- Tyler Griggs
- Alexander Glenn Shaw
- Hritik Bansal
affiliations:
- UC Berkeley
- Stanford University
- University of Texas at Austin
- UCLA
- Amazon
arxiv_id: '2606.24855'
url: https://arxiv.org/abs/2606.24855
pdf_url: https://arxiv.org/pdf/2606.24855
published: '2026-06-22'
collected: '2026-06-24'
category: Agent
direction: Agent训练数据配方的系统性消融与开放数据集
tags:
- Agentic Models
- Data Curation
- Fine-tuning
- Ablation Study
- Open Dataset
- Generalization
one_liner: 100+消融实验揭示智能体训练数据配方的关键要素，100K数据微调Qwen3-32B后在7个基准上平均准确率44.8%，超越最强开源基线3.9个百分点
practical_value: '- **数据多样性优于单一任务源**：消融显示混合多种任务源（如代码、交互、推理）对泛化至关重要，构建推荐/搜索Agent的微调数据时应避免只用单一场景的日志。

  - **指令格式与难度分布**：通过统一系统提示、调整任务难度比例可以稳定提升Agent鲁棒性；在电商Agent微调中可借鉴控制简单/困难样本比例的方法，防止模型过拟合简单对话。

  - **开放数据流水线复用**：论文公开了完整的数据处理管线（任务收集、格式标准化、难度过滤、质量筛选），可直接复用构建内部垂直领域Agent训练集，尤其适合客服、推荐解释等场景。

  - **消融方法论**：100+对照实验的设计思路可用于业务中快速诊断数据瓶颈，比如对比不同召回源、不同交互历史长度对Agent效果的影响，低成本找到最优数据配方。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前开源Agent训练数据多针对单一基准（如SWE-Smith、SERA），难以泛化到多样Agent任务。需要一套公开、可扩展的数据管理方案，训练通用智能体模型。

**方法关键点**：
- 构建端到端数据管线，涵盖任务来源选择、指令格式化、难度过滤、多源混合等阶段。
- 设计并执行超过100次受控消融实验，系统验证每个环节对模型性能的影响。
- 最终组装100K高质量样本，用其微调Qwen3-32B。

**关键结果**：
- 在7个Agent基准上平均准确率44.8%，比最强同类开源模型（Nemotron-Terminal-32B）的40.9%提高3.9个百分点。
- 数据表现出强扩展性：在任意相同训练量下，该数据集均优于其他开源Agent数据集。
- 消融揭示了任务来源多样性与难度分布的重要性。
