---
title: 'Beyond the Document: Compiled Context and Governed Agents for Any Work Product'
title_zh: 超越文档：面向任意工作产物的编译上下文与受治理代理
authors:
- James Rhodes
- George Kang
affiliations:
- AlphaBitCore, Inc.
arxiv_id: '2611.13055'
url: https://arxiv.org/abs/2611.13055
pdf_url: https://arxiv.org/pdf/2611.13055
published: '2026-11-09'
collected: '2026-11-12'
category: Agent
direction: Agent 上下文封装与治理交互
tags:
- Portable Agent Format
- Compiled Context
- Governed Agents
- Knowledge Packaging
- Retrieval
- LLM Agents
one_liner: 提出 Portable Agent Format，将编译上下文、证据与治理规则随工作产物打包，使后续问答准确率从 86% 提升至 96%
practical_value: '- 在电商导购/客服 Agent 中，把商品知识、政策、用户历史等编译成打包上下文，而非仅提供文档+检索，可显著提升后续多轮问答准确率（论文中
  hosted reader 96% vs 基线 86%）。

  - 显式打包治理规则（授权边界）让 Agent 通过返回 -1 拒绝越权或不确定回答，离线小模型 -1 率仅 2.9%，比裸源+指令的 56% 大幅下降，可用于合规要求严格的场景。

  - 包内包含 provenance/evidence 便于追溯回答来源，适合广告审核、价格策略解释等需要审计的业务。

  - 架构上 integrated selector 和 package-adapted writer 是提升效果的关键组件，建议在自建 Agent 时考虑将检索选择与生成器针对包结构进行适配，而非通用
  RAG。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统文档只保留工作可见结果，丢弃了研究、计算、假设、证据和授权边界，后续提问往往无法准确回答。

**方法关键点**：提出 Portable Agent Format (PAF) 包，将工作产物与编译上下文、证据、出处和规则一起交付。评估四个包（投资提案、基金研究、财务报表分析、工程事故审查），其中两个由专门 agent 生成，两个通过通用助理的打包技能生成。设置 400 个冻结问题和 12,000 评估响应，对比 hosted governed reader 与 instructions + raw-file retrieval、source-material chat、单独 instructions，以及 0.8B 参数离线 reader。消融测试 integrated selector 和 package-adapted writer 的贡献。

**关键结果**：hosted governed reader 总体成功 96% vs 基线 86%；可回答问题 94% vs 79%。source-material chat 和 instructions alone 分别仅 48% 和 74%。离线 reader 总体 69%，可回答 54%，-1 响应率 2.9%（基线 56%）。消融显示 integrated selector 和 package-adapted writer 带来优势。但离线检索在一金融数据包的 40 个历史记录问题上全部失败，表明编译知识有限制。论文支持将编译知识作为交付产物的一部分，但标准化互操作与端到端治理合规尚未验证。
