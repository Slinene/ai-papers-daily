---
title: 'A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and
  Realization in CUGA FLO'
title_zh: '将遗留工作流提升为智能体化BPM的流程支架: CUGA FLO设计与实现'
authors:
- Fabiana Fournier
- Lior Limonad
affiliations:
- IBM SIL, Israel
- University of Haifa
arxiv_id: '2606.27188'
url: https://arxiv.org/abs/2606.27188
pdf_url: https://arxiv.org/pdf/2606.27188
published: '2026-06-25'
collected: '2026-06-28'
category: Agent
direction: 智能体化流程管理 · 策略治理的自主性
tags:
- agentic BPM
- process harness
- policy-governed agents
- LLM
- workflow automation
- TDF model
one_liner: 提出流程支架在确定性工作流引擎上附加策略治理的智能体层, 实现推理与适应而不替换引擎
practical_value: '- 在现有确定性推荐/搜索排序引擎上叠加LLM智能体支架, 对关键控制点进行拦截, 实现动态决策路由与流程调整, 无需重建引擎

  - 采用TaskAgent/DecisionAgent/FlowAgent分工, 可将电商Agent系统中的知识密集型任务、案例级路由、流程自适应解耦, 降低耦合与Token成本

  - 利用process FRAME统一管理所有LLM调用的策略, 确保合规性与可控性, 适用于广告审核、价格调整等需严格治理的环节

  - Hook机制允许在异常或监管需求时插入人工干预或规则覆盖, 适用于高灵敏度场景如异常流量处置、活动熔断'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**: 传统BPM系统提供确定性执行保障, 但缺乏开放式推理与自适应能力, 应对例外需人工处理; 引入LLM智能体可增强灵活性, 但可能破坏结构合规性。

**方法**: 提出流程支架(process harness), 在保留原工作流引擎的基础上, 围绕其建立策略管控的智能体层, 在指定控制点拦截并进行推理、适应和监督。核心模型TDF将LLM推理分解为三种策略治理的Agent：**TaskAgent**执行知识密集型任务, **DecisionAgent**进行案例级网关路由, **FlowAgent**通过Hook机制在运行时调整流程。所有Agent在显式策略集process FRAME内推理。实现为CUGA FLO系统, 在贷款审批工作流中验证, 展示了三种Agent协作及Hook驱动的合规覆盖。

**关键结果**: 该方法统一了命令式需求(确定性执行保证结构合规)与规范性需求(策略框架下的自主性在所需控制点提供适应), 无需替换底层引擎即可实现智能体化BPM。
