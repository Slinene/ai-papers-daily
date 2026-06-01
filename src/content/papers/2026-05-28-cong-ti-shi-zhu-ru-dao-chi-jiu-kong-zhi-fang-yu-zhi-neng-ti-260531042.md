---
title: 'From Prompt Injection to Persistent Control: Defending Agentic Harness Against
  Trojan Backdoors'
title_zh: 从提示注入到持久控制：防御智能体框架中的特洛伊后门
authors:
- Jiejun Tan
- Zhicheng Dou
- Xinyu Yang
- Yuyang Hu
- Yiruo Cheng
- Xiaoxi Li
- Ji-Rong Wen
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2605.31042'
url: https://arxiv.org/abs/2605.31042
pdf_url: https://arxiv.org/pdf/2605.31042
published: '2026-05-28'
collected: '2026-06-01'
category: Agent
direction: LLM Agent安全：多步注入攻击与防御
tags:
- Prompt Injection
- Trojan Attack
- Agent Security
- Multi-step Attack
- Benchmark
- Defense
one_liner: 揭示多步特洛伊攻击范式，提出ClawTrojan基准和DASGuard防御方法，实现95.5%攻击成功率与强动态防御
practical_value: '- 在构建本地智能体工具（如文件读写、API调用）时，需考虑跨步骤的上下文攻击：单步无害的注入可能被持久化并延迟执行，防御应追踪数据来源和传播。

  - DASGuard的防御策略可借鉴：扫描敏感文件中的控制类文本（如指令、代码），追溯其来源，若非可信源则移除或净化，结合运行时阻断和提交清洁。

  - 设计Agent系统时，应区分可信与不可信数据源，对来自外部文件或工具输出的内容进行沙箱处理，避免污染工作空间状态。

  - 对于电商场景中的Agent（如自动客服、订单处理），防止通过用户输入或外部文档植入的后门，可借鉴ClawTrojan的攻击场景进行安全评估。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM智能体逐渐从聊天机器人演变为操作真实工作空间的工具，能够读写文件、调用工具并跨会话复用状态。攻击者可以在文件或工具输出中嵌入提示注入，智能体读取后将其存储并在后续步骤中执行，形成多步特洛伊攻击。这种攻击的每一步单独看都无害，但组合起来可将不可信文本转化为持久控制内容。现有防御通常孤立检查每个步骤，能阻断明显的恶意行为，但无法检测早期写入操作（植入后门）。

**方法**：作者构建ClawTrojan基准，模拟本地智能体工作空间中的多步攻击，在OpenClaw式环境中评估GPT-5.4等模型。此外提出DASGuard防御，扫描敏感本地文件中的控制类文本，追溯其来源，并移除来自非可信来源的控制内容，结合运行时攻击阻断和对工作空间的清洁提交。

**结果**：ClawTrojan在GPT-5.4上达到95.5%的攻击成功率，而传统单轮提示注入攻击几乎为零。DASGuard通过动态防御有效降低了攻击成功率，展示了组合防御的效力。
