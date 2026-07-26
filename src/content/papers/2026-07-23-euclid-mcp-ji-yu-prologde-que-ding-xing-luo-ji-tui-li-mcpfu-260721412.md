---
title: 'Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning
  via Prolog'
title_zh: Euclid-MCP：基于Prolog的确定性逻辑推理MCP服务器
authors:
- Bartolomeo Bogliolo
arxiv_id: '2607.21412'
url: https://arxiv.org/abs/2607.21412
pdf_url: https://arxiv.org/pdf/2607.21412
published: '2026-07-23'
collected: '2026-07-26'
category: Reasoning
direction: 神经符号推理 · 确定性逻辑引擎
tags:
- Neuro-Symbolic AI
- MCP
- Prolog
- Deterministic Reasoning
- Rule Enforcement
- LLM Augmentation
one_liner: 通过MCP暴露Prolog推理引擎，让LLM委托确定性逻辑推理，弥补语义RAG在规则执行上的不足
practical_value: '- 在广告合规、搜索推荐政策审核等需要严格规则执行的场景中，可用确定性符号引擎替代或补充语义检索，避免LLM幻觉，并提供可审计的证明树。

  - MCP工具化设计便于将确定性推理服务快速集成到Agent工作流中，支持规则查询、诊断、假设分析等模式，提升系统可信度。

  - Euclid-IR是一种声明式、易读的中间表示，LLM可较可靠地生成事实与规则，降低构建形式化规则库的门槛。

  - 可结合RAG与符号推理：用RAG召回相关策略文本，再用符号引擎验证具体配置是否合规，即“检索+验证”的混合范式。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
LLM在需要严格多步逻辑推导、可审计决策的场景（如业务规则执行、合规审查）中系统性不可靠，易产生幻觉且缺乏解释性。语义RAG基于近似匹配检索规则，无法保证逻辑充分性和一致性，是“用钻头钉钉子”。因此需要一个标准化、可复用的确定性推理层。

## 方法关键点
- **Euclid-MCP架构**：实现为Python MCP服务器，内部调用SWI-Prolog子进程，对外暴露4个工具（reason、diagnose、what_if、check_kb），支持“验证-翻译-运行-检查-修复”循环。
- **Euclid-IR**：引擎无关的中间表示，仅保留Horn子句核心（事实、规则、否定、算术），语法简洁，LLM易于生成，可编译到Prolog或其他后端。
- **推理委托**：LLM只负责将自然语言问题转化为Euclid-IR事实与规则，实际演绎由确定性推理引擎完成，LLM不参与推理链。
- **安全与审计**：生成代码经过安全过滤（禁止文件/网络等），输出包含完整证明树。

## 关键实验
- **数据集**：IT安全合规场景（30用户/50资源→578事实；200用户/300资源→3872事实），另加1000用户RBAC基准（1053事实）。
- **对比方案**：LLM单独（8B本地模型、480B云端模型）vs 8B+Euclid-MCP。
- **结果**：小知识库下所有方法准确率相当；大知识库下LLM单独准确率仅2/5，Euclid-MCP达5/5，且延迟更低（963ms vs 6966ms），输出令牌极少（12 vs 165）。证明规模超过LLM上下文窗口时，确定性推理是必要的。

## 一句话记住
“语义RAG是规则执行的错误工具；当事实超出LLM上下文窗口时，必须用确定性逻辑引擎。”
