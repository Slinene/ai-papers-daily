---
title: A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network
  Models
title_zh: 面向专用神经网络自动调参的多智能体 LLM 系统
authors:
- Ivan Moloshnikov
- Dmitry Kunitsyn
- Alexander Sboev
- Maksim Skorokhodov
- Roman Rybka
- Yuanchao Liu
affiliations:
- National Research Centre “Kurchatov Institute”, Moscow, Russia
- National Research Nuclear University MEPhI, Moscow, Russia
- Moscow Institute of Physics and Technology, Dolgoprudny, Russia
- Harbin Institute of Technology, Harbin, China
arxiv_id: '2610.13663'
url: https://arxiv.org/abs/2610.13663
pdf_url: https://arxiv.org/pdf/2610.13663
published: '2026-10-09'
collected: '2026-10-13'
category: Training
direction: 多智能体 LLM · 自动调参
tags:
- Multi-Agent LLM
- AutoML
- Spiking Neural Networks
- Physics-Informed Neural Networks
- Automated Tuning
- LLM Code Generation
one_liner: 多智能体 LLM 框架用分析师/编码员/记录员三角色在受限语义空间内调优专用神经网络组件，在 SNN 和 PINN 任务上大幅超越基线
practical_value: '- 组件级代码生成：不优化整个 ML 脚本，只让 LLM 改指定的功能组件（如个性化模块、损失权重、特征交叉），保持主网络结构不变，可降低线上模型迭代风险，适合电商推荐模型的快速调优。

  - 多角色 + 沙箱 + 实验日志：分析师、编码员、记录员分工明确，配合 sandbox 执行和完整日志，能构建可信的自动实验流水线；可用于超参数搜索、训练策略调优或模型结构微调。

  - 弱模型对详细提示更敏感：在成本受限无法用顶级 LLM 时，可优先投资详细的 prompt 设计，而非盲目换更大模型。

  - 跨任务通用性：同一框架在分类和 PDE 求解上都有效，提示多智能体自动调参有潜力迁移到推荐系统多任务学习权重、损失平衡等场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：机器学习常采用两级流程：专家先选定方法类别，类内关键组件（如损失形式、学习规则、网络模块）仍需人工试错，专业性强且耗时。

**方法**：构建三智能体 LLM 框架——分析师、编码员、记录员，配合实验日志与沙箱执行环境。该框架在开放但语义受限的空间中运行：只生成指定组件的代码，不改变整体网络结构；与优化完整脚本或离散架构搜索形成差异。

**结果**：在五类任务上验证：SNN 分类 MNIST 与 Digits，PINN 求解 GNLSE 与 KS 边值问题。结果：MNIST 准确率提升 13 个百分点，Digits 提升 6 个百分点；对解析单孤子解的误差降低约 2491 倍；GNLSE 高斯扰动下不变保持误差降低约 325 倍，多次初始化平均降低超过 100 倍；KS 高斯扰动质量漂移降低 14 倍。同一框架无需结构调整即可跨模型迁移。另外，详细提示可显著提升弱 LLM 性能。
