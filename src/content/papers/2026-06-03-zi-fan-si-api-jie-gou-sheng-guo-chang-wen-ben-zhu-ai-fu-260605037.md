---
title: 'Self-Reflective APIs: Structure Beats Verbosity for AI Agent Recovery'
title_zh: 自反思API：结构胜过长文本，助AI Agent恢复
authors:
- Arquimedes Canedo
- Grama Chethan
affiliations:
- Siemens Digital Industries Software
arxiv_id: '2606.05037'
url: https://arxiv.org/abs/2606.05037
pdf_url: https://arxiv.org/pdf/2606.05037
published: '2026-06-03'
collected: '2026-06-04'
category: Agent
direction: Agent工具调用错误恢复的API设计
tags:
- API design
- LLM agents
- error recovery
- structured feedback
- self-reflective API
one_liner: 结构化修复建议让Agent任务完成率提升+36.7-40.0pp，token效率提高1.8-2.2倍。
practical_value: '- **在Agent调用的内部API中嵌入结构化修复建议**：当业务规则（如合规、库存、定价）验证失败时，返回 `recovery_feedback.suggestions[]`
  字段，包含具体的参数修改动作和值（如 `USE_SPECIFIC_BRAND`, `expected_amount: 3.5`），Agent可直接合并到下次请求，消除LLM盲目猜测的token浪费和失败重试。

  - **区分通用验证与领域知识验证来决定是否加结构化反馈**：对LLM训练数据覆盖的通用错误（如“需提供无麸质面粉”），纯文本诊断已足够；对领域特有约束（如认证品牌“Bob’s
  Red Mill Certified GF”、文化规则、实时状态），结构化建议才能解锁恢复。可在API设计时标记规则来源，按需注入修复载荷。

  - **在工程实现上采用约20行的轻量契约**：遵循Schema v0.1的最小模式，每个校验规则负责产出类型化动作+字面参数，并通过OpenAPI或系统提示告知Agent动作词汇表。该模式增加响应体积仅约11%，却能显著减少平均重试次数。

  - **注意结构化建议的适用局限**：当诊断文本本身即包含足够概念（如“蛋白霜不应含泡打粉”）时，结构化建议可能冗余；结构化载荷可能引入解析错误（如Agent误将单项建议当成整体重写），需对具体校验器做A/B评估。对于复合动作可能需提供操作语义（如diff格式）而非仅参数字面。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：LLM Agent调用API时遇到领域特有验证错误（如文化规范、认证品牌、精确数值），通用的纯文本错误信息无法提供足够修复线索，Agent只能靠训练先验猜测，导致高失败率和大量token消耗。论文提出“自反思API”：在验证失败时，响应携带机器可读的`recovery_feedback.suggestions[]`，包含具体参数修改动作和字面值，让Agent直接修复重试，无需额外推理。研究表明，当API拥有LLM不知道的专有业务逻辑时，结构化建议取代纯文本错误描述能显著提升恢复能力。

**方法**：
- 定义自反思API Schema v0.1：在HTTP 422响应中添加`recovery_feedback`对象，包含`type`、`message`、`suggestions[]`数组，每个建议指定动作类型（如`REPLACE_INCOMPATIBLE_INGREDIENT`）和对应参数。
- 设计三类反馈模式：**Intent Disambiguation**（语言请求消歧）、**Recovery Guidance**（修复指导，本文焦点）和未评估的**Confidence Signaling**。
- 在配方转换API上实现5类领域特定验证规则：食材文化兼容性、无麸质认证品牌、非标准缩放精度、度量模糊、级联多步错误。
- 构建简单重试循环Agent（最多5次），对比三种错误响应级别：**Traditional**（通用错误字符串）、**Verbose**（每条规则的纯文本诊断，但移除字面答案）、**Reflective**（Verbose + 结构化建议）。
- 系统审计两类答案泄露：校验消息泄露和任务提示泄露，并用`audit_prompt_leakage.py`自动化检测，确保对比公平。

**实验**：
- 数据集：10个对抗性任务，覆盖上下文相关食材、认证品牌、数值精度、多验证组合。
- 模型：Claude-haiku-4-5、Claude-sonnet-4-6、GPT-4o-mini，每格30次尝试。
- 结果：在Anthropic模型上，Reflective较Verbose成功率高+36.7--40.0pp（p≤0.0022），每成功任务token效率提升1.8--2.2倍；GPT-4o-mini提升+13.3pp但不显著（p=0.435）。三重挑战任务下Verbose和Traditional均完全失败（0/9），Reflective恢复7/9。在另一个账单API上复制了类似模式。

**核心洞见**：结构化建议的价值集中在LLM无法从训练数据推断的专有约束上；Verbose基线已能恢复通用概念性错误，Reflective额外增益体现在必须提供精确字面值的场景。
