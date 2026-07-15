---
title: Tracing Agentic Failure from the Flow of Success
title_zh: 从成功流中追溯代理失败：无监督失败归因方法
authors:
- Samuel Yeh
- Yiwen Zhu
- Shaleen Deep
- Sharon Li
arxiv_id: '2607.12747'
url: https://arxiv.org/abs/2607.12747
pdf_url: https://arxiv.org/pdf/2607.12747
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: Agent 失败归因 · 无监督异常检测
tags:
- Failure Attribution
- Agentic Systems
- One-Class Learning
- Neural CDE
- Unsupervised Learning
- Debugging
one_liner: 仅用成功轨迹训练，通过神经控制微分方程建模动态，高效定位代理失败步骤。
practical_value: '- 对于电商搜索推荐Agent系统调试：可借鉴仅用少量成功轨迹（如100条）训练失败识别模型，避免人工标注错误步骤，大幅降低成本。

  - 在A/B实验或在线诊断时，快速定位Agent链中哪一步引入错误（如query改写、召回、排序等子模块），提高迭代效率。

  - 方法基于动态建模（神经CDE），能捕捉步骤间时序依赖，适合多步Agent链路（如多轮对话推荐、多阶段广告竞价）。

  - 推理速度极快（比基于LLM的提示方法快200-5000倍），适合实时在线异常报警和批量离线分析。'
score: 8
source: arxiv-cs.CL
depth: abstract
---

动机：LLM驱动的Agent系统失败归因对调试至关重要，但现有方法要么依赖昂贵的大模型提示，要么需要错误步骤标注。实际要求轻量且无需失败轨迹监督。

方法：提出OAT，视失败归因为单类学习问题——仅在成功轨迹上训练，用神经控制微分方程（Neural CDE）学习成功轨迹在隐空间的动态模式。推理时，计算失败轨迹每一步相对于成功动态的异常分数，据此定位错误步骤。模型仅需100条成功轨迹训练，无监督地识别失败步骤。

结果：OAT推理速度比基于提示的基线快200-5000倍；在域内和分布外数据集上，F1分数分别高出+20%和+7%，表明该方法高效且有前景。
