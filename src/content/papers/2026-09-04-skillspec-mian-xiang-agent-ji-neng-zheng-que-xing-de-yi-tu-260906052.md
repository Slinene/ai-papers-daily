---
title: 'SkillSpec: Intent-Masked Specification Reasoning for Agent Skill Correctness'
title_zh: SkillSpec：面向 Agent 技能正确性的意图掩码规格推理
authors:
- Yizhuo Zhang
- Bo Kang
- Yi Yang
- Zhiyu Duan
- Zhouteng Ye
- Shunkun Yang
affiliations:
- Beihang University
arxiv_id: '2609.06052'
url: https://arxiv.org/abs/2609.06052
pdf_url: https://arxiv.org/pdf/2609.06052
published: '2026-09-04'
collected: '2026-09-23'
category: Agent
direction: Agent 技能质量保证 · 规格推理
tags:
- LLM Agents
- Skill Correctness
- Specification Reasoning
- Intent Mask
- Sandbox Validation
one_liner: 将 Agent 技能正确性形式化为规格推理，用意图掩码多视图联合检测语义与实现缺陷，真实技能库精度 61.2%
practical_value: '- 在构建内部 Agent 工具/技能库时，将每个技能的描述、参数、代码实现纳入统一图索引，定期做“声明意图 vs 实现行为”一致性检查，拦截
  LLM 调用错误工具导致的静默失败。

  - 可借鉴 intent mask 的多视图推理：验证技能或工具描述时不要一次性灌入全部上下文，而是分别从整体、血缘、邻居、局部四个视角生成规格，再联合推理，平衡上下文偏置与推断不足。

  - 对技能/工具变更接入沙箱自动验证，自动生成用例检查声明的输入输出约束，能可靠覆盖代码节点缺陷；纯文本节点需额外规则或改写为结构化规格。

  - 61.2% 精度可作为发布流水线的预筛卡点，不能全自动替代人工复核，适合在技能库规模化前拦截多数边界缺陷。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Agent 系统越来越依赖可复用技能抽象，技能通常捆绑自由文本指令与异构代码资源。其正确性故障超出普通代码缺陷，常表现为意图冲突等语义不一致，并因底层模型能力被掩盖为静默失败。因此需要一种面向任务边界与泛化性的显式正确性保障。

**方法关键点**：SkillSpec 将技能正确性建模为 Hoare 风格的规格推理问题。先将异构技能仓库转成统一图表示，对齐描述、指令和代码。对每个节点，从周边声明的意图导出 ExpectSpec，并基于部分披露意图下的编码行为推断 FactSpec。引入 intent mask 调节 holistic、lineage、neighborhood、local 四种视图，避免上下文过多带来偏置或过少导致推断无据。联合这些视图标出候选缺陷，并在隔离沙箱中自动验证。

**关键结果**：在 SkillsBench 及广泛下载仓库的 515 个真实技能上，找出 763 个经人工确认的缺陷，覆盖 239 个技能，精度 61.2%。节点级分析显示，规格推理对代码节点持续可靠，纯文本节点仍是主要瓶颈；多数缺陷出现在声明意图与实现的边界处。
