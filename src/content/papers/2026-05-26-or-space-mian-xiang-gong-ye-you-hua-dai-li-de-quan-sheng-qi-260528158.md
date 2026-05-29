---
title: 'OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization
  Agents'
title_zh: OR-Space：面向工业优化代理的全生命周期工作空间基准
authors:
- Chenyu Zhou
- Xinyun Lu
- Jiangyue Zhao
- Jianghao Lin
- Dongdong Ge
- Yinyu Ye
affiliations:
- Shanghai Jiao Tong University
- Shanghai University of Finance and Economics
- Stanford University
arxiv_id: '2605.28158'
url: https://arxiv.org/abs/2605.28158
pdf_url: https://arxiv.org/pdf/2605.28158
published: '2026-05-26'
collected: '2026-05-29'
category: Eval
direction: 工业优化Agent · 全生命周期基准
tags:
- benchmark
- operations research
- LLM agents
- workspace
- evaluation
one_liner: 提出持久多工件工作空间基准OR-Space，评测LLM代理在OR建模的构建、修订与解释全任务上的可靠性
practical_value: '- 工作空间设计可迁移：在电商供应链、库存优化等Agent系统中，可借鉴其持续多文件工作空间结构，将业务文档、数据、代码和求解反馈整合，使Agent能维护状态与连贯操作。

  - 生命周期任务引入：不仅评测一次性建模，还模拟需求变更（如促销约束）和求解反馈，可设计Revise任务来提升电商优化Agent对动态场景的适应力。

  - 多维评估协议：其自动评估与纠错框架可用于检验电商优化Agent在解释方案时的准确性和可靠性，降低业务风险。

  - 失败模式洞察：通过基准暴露的常见错误（如约束遗漏、逻辑刚度）可为电商优化Agent的微调或提示工程提供针对性导向。'
score: 7
source: huggingface-daily
depth: abstract
---

现有运筹学（OR）LLM代理基准通常简化为从独立文本一次性生成数学公式或求解程序，忽视了真实工业工作流的两大特征：持续多工件工作空间和多阶段任务生命周期。OR-Space提出一个全生命周期工作空间基准，每个实例是可执行工作空间，包含业务文档、结构化数据、代码工件、求解器输出和评估器，这些散布在多个相互依赖的文件中。基准定义了三种任务模式：Build——从异构工件构建可直接求解的优化模型；Revise——在需求变更或求解反馈下修改现有模型，保留先前有效逻辑；Explain——基于工作空间证据回答关于解、约束和业务影响的问题。通过结合持久工作空间与生命周期任务，OR-Space能评估代理在OR工作流中的可靠性，而不仅限于端到端文本生成。论文详述了基准设计、自动与人工结合的评估协议及质量控制流程，为研究LLM代理在工业OR场景下的失败模式和实用准备提供了标准测试平台。
