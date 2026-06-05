---
title: 'CollabSim: A CSCW-Grounded Methodology for Investigating Collaborative Competence
  of LLM Agents through Controlled Multi-Agent Experiments'
title_zh: CollabSim：基于CSCW理论的多智能体协作能力受控评估框架
authors:
- Jiaju Chen
- Bo Sun
- Yuxuan Lu
- Yun Wang
- Dakuo Wang
- Bingsheng Yao
affiliations:
- Northeastern University
- Microsoft
arxiv_id: '2606.06399'
url: https://arxiv.org/abs/2606.06399
pdf_url: https://arxiv.org/pdf/2606.06399
published: '2026-06-04'
collected: '2026-06-05'
category: MultiAgent
direction: 多智能体协作能力评估 · CSCW理论指导
tags:
- MultiAgent
- Collaborative Competence
- LLM Evaluation
- Simulation
- CSCW
one_liner: 将CSCW协作需求引入LLM多智能体评估，通过受控实验分离条件、模型和设计的影响。
practical_value: '- 评估多智能体系统不应只看任务完成度，需借鉴CSCW理论诊断协作能力（共同基础、任务理解对齐等），用于优化电商Agent间的协调机制。

  - 可通过受控操纵通信带宽、角色不对称等条件，在模拟环境中快速发现协作瓶颈，避免直接上线后暴露问题。

  - 框架支持行动级探测智能体内部状态，可复用到推荐对话Agent或供应链协作Agent的行为归因分析，帮助定位模型或设计缺陷。

  - 揭示了智能体设计效应依赖任务类型，提示业务中应针对不同协作场景（如实时竞价、联合推理）定制角色与通信协议，而非通用设计。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有多智能体系统（MAS）评估多聚焦任务结果或单智能体能力，但实际协作失败往往源于协作能力不足——建立共同基础、维持共享任务理解、平衡个体与集体激励、修复对齐偏差。计算机支持的协同工作（CSCW）领域数十年的研究已刻画了人类团队的这些需求，但MAS评估尚未系统引入。

**方法**：提出CollabSim，一个可配置的模拟框架，将理论驱动的协作能力定义、交互条件的受控操纵（如通信约束、角色非对称性）与智能体内部状态的行动级探测相结合。框架实例化四类经典CSCW实验任务（Shape Factory、DayTrader等），通过控制实验分离条件效应。

**结果**：在四个LLM上的实验表明，CollabSim能有效捕捉不同交互条件的影响，区分模型性能模式，并揭示智能体设计的效果高度依赖任务类型。该框架为MAS协作能力的系统诊断和优化提供了理论扎实的评估工具。
