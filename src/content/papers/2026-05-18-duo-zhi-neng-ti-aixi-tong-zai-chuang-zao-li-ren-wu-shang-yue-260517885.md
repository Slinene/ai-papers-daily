---
title: Multi-agent AI systems outperform human teams in creativity
title_zh: 多智能体AI系统在创造力任务上超越人类团队
authors:
- Tiancheng Hu
- Yixuan Jiang
- Haotian Li
- José Hernández-Orallo
- Xing Xie
- Nigel Collier
- David Stillwell
- Luning Sun
affiliations:
- University of Cambridge
- Zhejiang University
- Microsoft Research Asia
- Universitat Politècnica de València
arxiv_id: '2605.17885'
url: https://arxiv.org/abs/2605.17885
pdf_url: https://arxiv.org/pdf/2605.17885
published: '2026-05-18'
collected: '2026-05-19'
category: MultiAgent
direction: 多智能体创意生成与轨迹分析
tags:
- multi-agent systems
- creativity
- semantic trajectories
- LLM
- discussion structure
- human-AI comparison
one_liner: 多智能体LLM团队创造力显著优于人类团队(d=1.50)，新颖性驱动且轨迹分析揭示可设计杠杆
practical_value: '- **多智能体讨论结构可调节创意质量**：迭代细化（Iterative Refinement）等结构化流程能让GPT-4.1类模型的新颖性显著提升而不过度损失有用性；在电商文案生成、推荐理由创意等场景，可设计类似“提出-比较-选择”的对话模板来优化生成内容的新颖性。

  - **语义轨迹框架可作为诊断与优化工具**：通过计算对话的全局相干性、语义覆盖广度等指标，可量化评估多智能体系统的探索效率，避免产出过度集中在单一主题；在Agent协作系统中，可据此监控并自动调整讨论策略。

  - **推理模型对讨论结构依赖较低**：o3-high等强推理模型在无结构讨论下同样高产，设计系统时可减少外部流程控制，节约token消耗；而普通模型需外部脚手架，这为不同成本的模型选型提供了依据。

  - **团队规模不是越大越好**：3人与6人LLM团队创意无显著差异，实际部署中采用3智能体即可，能节约计算资源且不损害创意效果，对构建成本敏感的Agent系统有直接指导意义。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
创造力长期被视为人类智能的最后堡垒。虽然大型语言模型（LLM）在诸多认知任务中已比肩或超越人类，但在开放式创意问题解决中，LLM多智能体团队能否超越人类团队尚无系统验证。本研究旨在填补这一空白，并揭示背后的交互机制。

**方法关键点**  
- **实验设置**：比较了114个人类团队（3或6人，共341个创意）与多智能体LLM团队（3或6个智能体，共4,541个创意）在6个创意问题解决任务上的表现；另收集179个单智能体想法作为基线。  
- **模型与讨论结构**：LLM涵盖GPT-4.1、o3-high、o3-low及多模型混合；设计5种讨论结构（开放讨论、指令讨论、迭代细化、渐进优化、无讨论），系统操控模型类型、团队大小、人格设定等。  
- **评估方式**：所有想法经GPT-4.1标准化改写后，由5位人类评委采用共识评估技术盲审新颖性与有用性，创造力定义为两者乘积。  
- **语义轨迹分析**：将对话序列映射到Qwen3-Embedding空间中，计算路径长度、语义散布、全局/局部相干性、曲率等9维轨迹特征，用于预测创造力并比较LLM与人类的探索模式。

**关键结果**  
- LLM多智能体团队创造力均值0.297，显著高于人类团队的0.151（Cohen's d=1.50），优势由新颖性驱动（d=1.29）而有用性持平（d=0.08）。  
- 在分布上尾，LLM的95分位（0.47）比人类高53%，最佳创意高出58%。  
- 语义轨迹分析显示两者共同受益于宽泛的语义探索（低全局相干性），但LLM额外依赖高效探索（高语义散布、短路径），人类则依赖平滑的局部连贯与频繁转向。  
- 模型类型与讨论结构是两大设计杠杆，合计解释对话动态26.8%的方差；推理模型对结构敏感度低，标准模型可通过迭代细化提升创意表现。

**结论一句话**  
多智能体LLM系统在创造力上全面超越人类团队，其探索模式可被轨迹特征量化，且通过选择模型与讨论结构能够系统性地优化创意输出。
