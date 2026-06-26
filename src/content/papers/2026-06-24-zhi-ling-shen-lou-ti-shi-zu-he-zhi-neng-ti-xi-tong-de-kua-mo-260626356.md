---
title: 'Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems'
title_zh: 指令渗漏：提示组合智能体系统的跨模块干扰
authors:
- Ching-Yu Lin
- Yifan Liu
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2606.26356'
url: https://arxiv.org/abs/2606.26356
pdf_url: https://arxiv.org/pdf/2606.26356
published: '2026-06-24'
collected: '2026-06-26'
category: Agent
direction: Agent 提示组合干扰评估
tags:
- Prompt Composition
- Agent Evaluation
- Cross-Module Interference
- Behavioral Leakage
- LLM Safety
one_liner: 形式化提示组合Agent中的行为泄漏(CBL)，提出三通道探测协议并确认内容通道产生显著干扰效应
practical_value: '- 构建多模块提示组成的搜索/推荐 Agent 时，需评估模块间干扰：无共享变量也可能通过上下文窗口的自注意力产生行为泄漏，建议在部署前对模块组合进行联合测试。

  - 可直接复用三通道探测协议（volume、content、form）来量化生产 Agent 的 CBL，其中 content 通道最易触发干扰，可作为最小可行测试集。

  - 效应虽未引起单次推荐翻转（Cohen’s d=0.63），但在高吞吐场景下微小偏移会随决策次数积累，评估时不能只看 QA 准确率，必须监控分布级偏移。

  - 工程上可在提示编排中引入明确的分隔标记或模块隔离策略（如约束注意力范围），以减少非预期的跨模块信息混合。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：从业者发现，在提示组合式 Agent（如 OpenClaw）中编辑一个提示模块会悄然改变其他模块行为，尽管无共享变量或依赖。根源是 Transformer 自注意力在拼接模块间缺乏形式隔离，该干扰被形式化为组合行为泄漏（CBL）。

**方法**：在一个已部署的职位评估 Agent（Claude Sonnet 4.6）上，设计可复用的三通道探测协议：扰动非焦点模块的 volume（长度）、content（语义）和 form（格式），以配对实验检测对焦点模块决策的影响。执行 144 次试验，采用 Cohen’s d 和 bootstrap 95% CI 衡量效应。

**关键结果**：仅 content 通道产生可检测的配对效应（d=0.63，CI 不含零），但未导致推荐翻转，属于亚阈值干扰；该微小偏移在大规模部署（数千次决策）中会复合累积。CBL 与传统对抗注入、多智能体故障传播等正交，表明它是提示组合架构的固有风险。论文确立了跨模块干扰测量为提示组合 Agent 评估的必要环节。
