---
title: 'UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks'
title_zh: UniClawBench：面向真实世界任务的主动式智能体通用基准
authors:
- Zhekai Chen
- Chengqi Duan
- Kaiyue Sun
- Bohao Li
- Yuqing Wang
- Manyuan Zhang
- Xihui Liu
affiliations:
- HKU MMLab
- Meituan
arxiv_id: '2607.08768'
url: https://arxiv.org/abs/2607.08768
pdf_url: https://arxiv.org/pdf/2607.08768
published: '2026-07-08'
collected: '2026-07-10'
category: Eval
direction: Agent 评估基准与能力分析
tags:
- Agent Evaluation
- Proactive Agent
- Benchmark
- Capability-Driven
- Closed-Loop Evaluation
- Real-World Tasks
one_liner: 首个能力驱动、在动态 Docker 环境中闭环评估主动智能体的基准，揭示框架比模型更影响性能
practical_value: '- 能力解耦设计：将任务按 Skill Usage、Exploration、Long-Context Reasoning、Multimodal
  Understanding、Cross-Platform Coordination 五个维度划分，可启发我们在构建电商搜索/推荐 Agent 时按能力模块进行独立评估与优化

  - 闭环评估策略：采用执行器-监督器-用户模拟器三角色闭环，隐藏真值、模拟多轮人类反馈，可用于内部 Agent 迭代，避免静态评测过拟合

  - 框架选择比模型更重要：实验结论提示我们在实际系统中应优先优化 Agent 框架（工具编排、上下文管理）而非盲目升级基础模型

  - 实时环境执行（Docker 容器+步骤检查点）：可借鉴将 Agent 丢入真实可操作环境（如浏览器、终端）并设计细粒度完成度打分，弥补传统离线评测的不足'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
现有 Agent 基准多依赖沙盒环境和单轮评估，任务分类混杂多种能力，难以定位失败根源。需要一个能力驱动、实时交互、闭环反馈的基准来可靠评估主动智能体。

**方法**
- 构建 UniClawBench，围绕五大基础能力（工具使用、探索、长上下文推理、多模态理解、跨平台协调）设计 400 个双语真实任务。
- 评估在动态 Docker 容器中实时进行，使用细粒度步骤检查点替代预录答案。
- 设计三角色闭环策略：执行器 Agent 操作工具生成轨迹与产物；隐藏监督器依据隐秘真值和规则判定通过/失败/继续；用户模拟器提供自然多轮反馈但不泄露评分标准。
- 在多种主流 Agent 框架（OpenClaw、EDICT、Nanobot）上比较多个 SOTA 模型，解耦基础能力与框架影响。

**关键结果**
- 框架选择对能力表现的影响一致性大于模型选择，即合适框架更能释放模型潜力。
- 长上下文与多模态任务是主要瓶颈，大部分模型在这些维度通过率较低。
- 公开代码与基准数据，促进可复现的 Agent 研究。
