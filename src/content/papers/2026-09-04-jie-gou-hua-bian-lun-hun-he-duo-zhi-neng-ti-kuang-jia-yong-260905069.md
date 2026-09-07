---
title: A Structured Debate-Mixture-of-Agents Framework for Complex Clinical Diagnostic
  Decision Support
title_zh: 结构化辩论混合多智能体框架用于复杂临床诊断决策支持
authors:
- Chang Xia
- Leilei Ouyang
- Huimin Wang
- Yong Zhao
- Kang Li
affiliations:
- College of Computer Science, Sichuan University
- West China Hospital, Sichuan University
arxiv_id: '2609.05069'
url: https://arxiv.org/abs/2609.05069
pdf_url: https://arxiv.org/pdf/2609.05069
published: '2026-09-04'
collected: '2026-09-07'
category: MultiAgent
direction: 多智能体结构化辩论诊断
tags:
- Multi-Agent
- Debate
- LLM
- Clinical Diagnosis
- Diagnostic Safety
- Mixture-of-Agents
one_liner: 提出DMoA结构化辩论混合多智能体框架，提升复杂诊断准确率与安全率超10个百分点
practical_value: '- 结构化角色分工和辩论流程比单纯堆模型或拼接输出更有效，可用于电商搜索/推荐的 query 改写、商品推荐理由生成等场景，设计“生成-质疑-汇总”的
  agent 链提升输出质量。

  - 借鉴 4×2 的 MoA 结构：4 个提案 agent + 2 个评审/聚合 agent，在 token 预算允许时能稳定提升最终结果；业务落地时可先用小规模消融找到性价比最优的结构。

  - 在最终输出前加入安全/合规评审 agent 进行辩论，可显著降低风险输出，适用于广告审核、违禁词过滤、客服应答等敏感场景。

  - 提升并非来自更长输出或更多模型，说明结构化流程比增加推理长度更划算，Agent 系统设计应优先优化辩论/聚合逻辑而非盲目增加 token。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 单轮问答与真实临床诊断的迭代推理流程脱节，在复杂诊断场景中表现受限。

方法：提出 DMoA（Debate-Mixture-of-Agents），通过角色化多智能体结构化辩论实现迭代诊断推理；不同基座模型按角色参与辩论，聚合多模型观点形成最终诊断。

结果：在 297 例罕见病和 1719 例高难度病例上，DMoA 相对 GPT-4o 将最可能诊断准确率提升 10.21 个百分点、安全率提升 11.36 个百分点。消融显示提升并非仅来自更多模型或更长输出，结构化工作流有独立贡献；进一步分析发现 4×2 结构、更强基座模型和更大 token 预算能带来更好性能。
