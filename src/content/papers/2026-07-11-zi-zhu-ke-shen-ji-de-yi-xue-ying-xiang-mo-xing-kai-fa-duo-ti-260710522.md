---
title: Towards Autonomous and Auditable Medical Imaging Model Development
title_zh: 自主可审计的医学影像模型开发多智能体框架
authors:
- Shengyuan Liu
- Jia-Xuan Jiang
- Boyun Zheng
- Cheng Wang
- Zipei Wang
- Wentao Pan
- Hongtao Wu
- Houwen Peng
- Yu Gu
- Lichao Sun
affiliations:
- The Chinese University of Hong Kong
- Institute of Automation, Chinese Academy of Sciences
- Microsoft Research
- Lehigh University
- Independent Researcher
arxiv_id: '2607.10522'
url: https://arxiv.org/abs/2607.10522
pdf_url: https://arxiv.org/pdf/2607.10522
published: '2026-07-11'
collected: '2026-07-17'
category: MultiAgent
direction: 多智能体协作驱动自动化模型开发
tags:
- MultiAgent
- Automated ML
- Medical Imaging
- Verification
- Optimization
- LLM Agent
one_liner: 提出 AMID 多智能体框架，通过数据条件方法规划与验证引导两阶段优化，实现医学影像模型开发自主化
practical_value: '- **数据条件的方法规划**：根据任务数据分析（特征分布、数据质量等）将粗粒度搜索空间细化为可执行的并行探索路径，可迁移至推荐系统的自动特征工程和模型架构搜索，避免盲目超参试探。

  - **验证引导的两阶段优化**：先广泛探索再聚焦高潜力候选，并在全流程强制校验验证协议、指标计算和输出物，适用于电商推荐模型的 AB 实验自动优化与合规检查，减少人工介入。

  - **多智能体协作流水线**：计划、执行、验证等 agent 分工协作，可参考搭建推荐模型开发的自主迭代闭环，从数据到上线全链路自动化。

  - **强调可审计性**：对预测产物和流程的强制验证思路，可借鉴用于生成式推荐中确保生成内容的安全性与一致性，或广告创意自动化审核。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：大型语言模型智能体已开始自动化机器学习工程，但医学影像领域因模态特异性实验需求和严格的验证协议，通用系统难以胜任。需要一种自主且可审计的模型开发方案。

**方法关键点**：
- **数据条件方法规划**：根据任务数据分析和可运行资源，将粗粒度搜索空间细化为可执行、可并行的方法车道，避免无效搜索。
- **验证引导两阶段优化**：第一阶段进行行为门控的广泛探索，并行评估多样方法组合；第二阶段聚焦有前途的候选进行选择性利用，并强制执行验证协议、指标计算和预测产物审计。
- **多智能体架构**：不同智能体负责规划、编码、调试、验证，形成协同开发流水线。

**关键结果**：在20个医学影像挑战任务（不同模态和预测类型）上，AMID 全面优于通用 MLE 系统，并在多个任务上接近或达到人类专家设计的解决方案水平，验证了将手动工程转化为可审计的代理工作流的可行性。
