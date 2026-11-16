---
title: Smart Home Agents Make Capable but Unpredictable Grid Operators
title_zh: 智能家居智能体成为电网调度员：能干但难预测
authors:
- Christopher Terrazas
- Eduardo Cotilla-Sanchez
affiliations:
- Oregon State University
arxiv_id: '2611.18395'
url: https://arxiv.org/abs/2611.18395
pdf_url: https://arxiv.org/pdf/2611.18395
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: Agent 韧性与故障响应评测
tags:
- Smart Home Agents
- Resilience
- Power Outage
- LLM Agents
- Failure Analysis
one_liner: 首次在停电全流程中评估智能家居智能体韧性，发现其能充当电网调度但存在多种新失效模式。
practical_value: '- 在电商/推荐 Agent 上线前，构建故障注入环境模拟停电、服务超时、状态丢失等极端异常，记录 Agent 的恢复轨迹与误操作类型，而不是只测正常流程。

  - 针对 LLM Agent 的不可预测性，在关键操作（如库存修改、价格调整、广告投放）前增加确定性的规则校验与人工审批兜底，避免自主决策造成级联失败。

  - 借鉴电网调度员的标准化故障响应流程，为推荐/广告 Agent 定义明确的故障状态机（如降级、重试、人工接管），将非结构化 LLM 输出映射到受控动作空间。

  - 评估时除最终成功率外，增加“恢复时间”“错误操作数”“级联影响”等韧性指标，量化 Agent 在压力场景下的稳定性。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**  
智能家居设备大量接入电网边缘，但现有研究极少关注故障响应；停电后用户需手动排查负载均衡和设备恢复，缺乏自动化。电力系统运营商有标准化故障处理流程，能否将这些韧性能力映射到智能家居 agent 是待探索问题。

**方法**  
该工作构建一套面向完整停电过程的故障响应仿真套件，在 live environment 中注入停电事件，评测多个智能家居 agent 在停电前、中、后的表现，记录其决策与失败模式。将电网调度员的响应流程作为参照，分析 agent 是否具备电网调度能力。

**结果**  
实验显示智能家居 agent 能执行部分电网调度任务，如负载管理和设备恢复；但发现若干新的失败类别，所有被测模型均存在局限性，表现为行为不可预测。作者认为这为智能家居 agent 作为电网边缘调度者奠定了基础，但需进一步解决可靠性问题。
