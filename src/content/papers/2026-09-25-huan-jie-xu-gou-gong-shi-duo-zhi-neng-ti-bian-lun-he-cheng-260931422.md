---
title: 'Towards Mitigating Fabricated Consensus: The Active Provenance Gate for Multi-Agent
  Debate Synthesis'
title_zh: 缓解虚构共识：多智能体辩论合成的主动来源门控
authors:
- Jakub Masłowski
- Jarosław A. Chudziak
affiliations:
- Institute of Computer Science, Warsaw University of Technology
arxiv_id: '2609.31422'
url: https://arxiv.org/abs/2609.31422
pdf_url: https://arxiv.org/pdf/2609.31422
published: '2026-09-25'
collected: '2026-09-28'
category: MultiAgent
direction: 多智能体辩论的主动来源验证与分歧处理
tags:
- Multi-agent debate
- Provenance fidelity
- NLI auditing
- Consensus synthesis
- LLM safety
- Self-correction
one_liner: 在MAD合成阶段引入主动来源验证与条件阻断，显著提升来源保真度并抑制虚构共识
practical_value: '- 在多Agent决策或推荐解释生成流程中，增加「来源审计」层：对最终输出逐条验证是否被上游日志/数据支持，防止模型生成流畅但无据的结论。

  - 采用「自修复→硬阻断」策略：先尝试修正无支持的声明；若无法修正，则直接阻断并输出分歧报告，而非强行发布。在电商推荐理由生成、代理协商结果等场景可显著降低事实幻觉风险。

  - 设置发布前质量门（gate）：当证据不足或置信度低时，主动降级为明确的不确定性提示（如“无法给出可靠推荐”），而不是给一个看似合理的错误答案。

  - 用户研究表明，在关键场景下，用户更偏好明确的失败信号而非虚假的流畅共识。在产品设计中应优先保证可信度与透明度，而非一味追求文本流畅性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：多智能体辩论（MAD）系统被用作复杂决策管道，但其最终合成阶段缺乏控制。即使有详细辩论日志，摘要模型也倾向于生成流畅但无根据的共识，带来安全风险。

**方法关键点**：提出 Active Provenance Gate (APG) 作为后验验证层，将来源视为硬约束。APG 分析辩论日志，对摘要中的每个声明进行审计（基于NLI），并先尝试自修复；若无法修复，则阻断该声明并生成分歧报告，而不是输出虚假共识。

**关键结果数字**：在危机模拟的困难场景下，自修复机制将平均数据来源保真度（Provenance Fidelity）提升了一倍以上；严格门控后，所有无支持声明被阻断。人类研究中，超过 75% 的用户更偏好明确报告失败的分歧报告，尽管他们认为基准系统生成的虚构共识更流畅。主要贡献是将数据来源跟踪从被动记录转变为发布前的主动条件阻断。
