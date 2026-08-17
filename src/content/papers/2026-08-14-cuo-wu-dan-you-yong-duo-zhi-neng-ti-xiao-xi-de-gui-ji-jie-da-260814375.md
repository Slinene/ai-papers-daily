---
title: 'Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent
  Messages'
title_zh: 错误但有用：多智能体消息的轨迹价值超越答案正确性
authors:
- Chih-Hsuan Yang
- Anjir Ahmed Chowdhury
- Cheng-Hau Yang
- Weijian Zheng
- Fernando Llorente
- Xiaolong Ma
- Xinyang Li
- Eliu A. Huerta
- Ian T. Foster
- Rajeev Thakur
affiliations:
- Argonne National Laboratory
- University of Houston
- Brookhaven National Laboratory
- University of Chicago
arxiv_id: '2608.14375'
url: https://arxiv.org/abs/2608.14375
pdf_url: https://arxiv.org/pdf/2608.14375
published: '2026-08-14'
collected: '2026-08-17'
category: MultiAgent
direction: 多智能体轨迹价值评估与消息筛选
tags:
- Trajectory Value
- Multi-Agent
- Message Filtering
- LLM Reasoning
- DHD
- Wrong-but-Useful
one_liner: 提出 DHD 重放协议，证明错误答案消息在多智能体推理中仍可能帮助后续集成，且可重复测量轨迹价值
practical_value: '- 在推荐/搜索的 Agent 工作流中，不要仅用最终答案正确性或 auto-scorer 过滤中间候选消息（如商品理由、query
  改写、约束提取）。可复用 DHD 的“缓存+重放”方法，离线评估每条消息对最终决策的因果贡献（trajectory value），筛选出“错误但有用”的消息用于训练或在线保留。

  - 构建多 Agent 集成器时，可对同一组候选消息重复运行 integrator，统计每个消息出现/隐藏对最终结果的影响，识别可重复的 help/harm 消息；此类标签可用于训练一个轻量级
  selector/滤波器，判断哪些中间输出值得传给下游。

  - 工程实现上，DHD 缓存多个独立生成消息并重放，成本可控；可在业务中先对少量 query/问题做离线 replay，得到消息级轨迹价值标注，再逐步替换基于
  confidence/agreement 的过滤规则。

  - 注意完整消息（含推理过程）往往比仅保留答案更有效，因此中间消息的 reasoning trace 不应过早丢弃；在商品解释、推荐理由生成等场景中保留结构化推理片段可能提升最终聚合质量。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：多智能体推理系统通常依赖 agreement、confidence 或自动分数筛选消息，默认“可能正确”的消息才值得保留。但错误答案可能包含有用的分解、约束或科学原理。

**方法关键点**：设计 Diverse Hypothesis Deliberation (DHD) 受控测量协议：缓存五个独立生成的消息，对同一 integrator 分别重放每个消息可用/隐藏，通过对比最终答案变化测量该消息的轨迹价值（trajectory value）。在五个数学与科学基准、两个开放模型家族（gpt-oss-120b 与 gemma-4-31B-it）上实验。

**关键结果**：错误但有用的消息出现在所有 benchmark-model 组合；在改变最终正确性的错误答案消息中，每个模型超过四成变化是有帮助的；控制重复下可重复消息效应显著（p=0.0002）；聚焦干预发现完整消息效果最好，保留推理比仅保留答案保留更多成功；在同一问题内，基于轨迹价值证据的保留/删除选择优于仅凭答案正确性。
