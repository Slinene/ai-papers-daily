---
title: 'Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents'
title_zh: Token-Flow 防火墙：持久化 AI Agent 的语义运行时审计
authors:
- Puji Wang
- Yingchen Zhang
- Ruqing Zhang
- Jiafeng Guo
- Xueqi Cheng
affiliations:
- State Key Laboratory of AI Safety
- Institute of Computing Technology, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2607.08395'
url: https://arxiv.org/abs/2607.08395
pdf_url: https://arxiv.org/pdf/2607.08395
published: '2026-07-09'
collected: '2026-07-11'
category: Agent
direction: Agent 运行时安全审计 · Token 流防火墙
tags:
- AI Agent
- Security
- Runtime Auditing
- LLM
- Semantic Firewall
- Token Flow
one_liner: 针对持久化 AI Agent，通过 token 流语义防火墙实现全覆盖预执行审计，将攻击成功率压至 12.5%
practical_value: '- 在构建持久化推荐 / 客服 Agent 时，可对记忆更新、工具参数、检索文件等自然语言 token 流嵌入边界感知审计节点，阻止不安全指令传播到执行器。

  - 采用 **轻量级本地检查 + 分级仲裁** 架构：绝大多数 benign 请求用本地规则快速放行（仅 0.69s 延迟），仅对模糊高风险案例才调用远端大模型裁决，实现安全与效率平衡。

  - 借鉴 source‑sink 审计记录的设计，为 Agent 数据流（尤其是来自外部工具的返回值）建立可追溯的语义日志，便于事后分析攻击路径。

  - 当系统中 Agent 可调用敏感 API（如商品上下架、价格修改）时，可利用类似机制在工具调用前进行语义拦截，避免 prompt 注入导致的误操作。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：持久化 AI Agent 将 LLM 从单轮对话扩展为长期运行的软件系统，其不安全内容可通过记忆、工具参数、文件检索等 token 流跨组件传播，攻击面远大于传统 chatbot。现有防御要么基于稀疏规则，要么依赖远端大模型全量审查，无法同时满足全覆盖与低延迟。  
**方法**：提出 TokenWall，一个语义运行时防火墙。核心思路是将 agent 内部所有安全敏感的 token 流（如记忆写入、工具调用参数）视为数据流，在关键边界（source‑sink）插入审计。它构建结构化的源‑汇审计记录，先用轻量本地检查器预审；若风险评分落在模糊区间，则自动升级到更强的大模型仲裁模块，避免全量远端调用。  
**关键结果**：在 CIK‑Bench 上，攻击成功率降至 12.5%，同时良性请求可执行通过率保持 97.4%（无需人工介入）。对良性路径仅引入 0.69 秒额外延迟，证明了在持久化 Agent 中实现实用级安全‑效用权衡的可行性。
