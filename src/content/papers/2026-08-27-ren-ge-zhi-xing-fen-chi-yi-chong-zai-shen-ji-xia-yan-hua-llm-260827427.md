---
title: 'Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents
  under Execution Audit'
title_zh: 人格-执行分离：一种在审计下演化 LLM Agent 的架构模式
authors:
- Yisen Xi
affiliations:
- Independent Researcher, Beijing, China
arxiv_id: '2608.27427'
url: https://arxiv.org/abs/2608.27427
pdf_url: https://arxiv.org/pdf/2608.27427
published: '2026-08-27'
collected: '2026-08-30'
category: Agent
direction: Agent 架构模式 · 信任域分离
tags:
- LLM Agents
- Architecture Pattern
- Trust Domains
- Execution Audit
- Persona Drift
- Governance
one_liner: 提出人格-执行分离（PES）架构，把 LLM Agent 的形象面与执行面分置不同信任域，以受治理契约桥兼顾自由演化与执行审计
practical_value: '- 在电商/推荐 Agent 中把“人设/话术”与“下单/券发放/支付”等执行面分到不同信任域；人设可高频 A/B 调优，执行侧规则/审计不变。用
  MCP 工具调用 + ACL + deny/ask/allow 审批矩阵做唯一过境通道。

  - 采用“绑定而非投影”：人设侧只持有 capability ID/SOP 引用，不复制执行逻辑或敏感数据；状态摘要可以回流，数据正文默认不流出，仅通过分级 DLP
  脱敏例外（如订单号/金额摘要）。避免双份 persona 导致漂移。

  - 对核心身份与表层人设分层：员工 ID/角色/SOP 绑定为审计锚点，不能随话术自由变更；审计 ledger 绑定核心身份而非 prompt 文本，防止 prompt
  注入或 profile poisoning 污染执行记录。

  - 工程化落地时，用 ADR 记录每个架构决策和 rejected alternative；如果必须单域实现，也要显式建立“类型化变更对象 + 外部执行门 +
  稳定审计锚点”，否则单域方案会在更高耦合成本下重建 PES。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
在受监管组织中，LLM Agent 既要作为“数字员工”持续演化人设/指令/语气（G1 自由漂移），又要对每项状态变更操作留痕审计（G2 执行可追溯）。单域架构下两者共享同一 prompt 与信任域：严治理则每次人设编辑都触发执行重验证，松治理则审计链不可靠。论文的切入点是架构而非提示工程。

### 方法关键点
- **双面一体**：同一个人身份跨两个信任域；表达面在低治理域承载完整 persona，执行面在高治理域只呈现 SOP 表单/引擎/账本，不持有对话人格。
- **绑定而非投影**：人设侧只引用 capability/SOP 标识，不复制执行逻辑或 persona 副本，避免第二真相源。
- **受治理契约桥**：三条数据面通道——状态摘要回流、数据正文默认不流出（仅分级 DLP 脱敏 E2 例外）、身份连续性；桥是 fail-closed 检查点，审批矩阵 deny/ask/allow、DLP、审计共同执行。
- **分层漂移**：核心身份（工号/角色/SOP 绑定）作为审计锚点不随人设漂移，表层人设可零合规成本自由改动。
- **构造性最小性**：在 LLM 表征不可区分下，单域要实现 G1-G3 必须重建类型化变更对象、外部执行门、稳定审计锚点，即 PES 在更高耦合成本下的重建。

### 关键结果
FIA Workbench 数字员工平台（金融行业开发/试点）一个月的 5 项 ADR 决策链从人设存储、能力绑定、单向阀、晋升工单到双面固化，均记录被拒绝方案。机制检查：5 种模型配置下未发现执行侧重验证污染（R=0.00），硬断言字段无人格指纹；分离前构建的探测表明人格与执行解耦是遗漏而非构造。8 个开源平台对比无一家同时满足 G1-G3。

### 最值得记住的一句话
把‘会变的部分’放进低治理域自由漂移，把‘必须留痕的部分’放进高治理域并只通过 fail-closed 桥连接，否则单域内的类型化变更、外部执行门和稳定审计锚点会以更高成本重新长出来。
