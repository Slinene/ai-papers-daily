---
title: Plan Pointers and Record-Directive Form in Budgeted Verification of Inherited
  Agent Memory
title_zh: 继承式 Agent 记忆预算验证中的计划指针与记录指令形式
authors:
- Kazuki Nakayashiki
affiliations:
- Glasp
arxiv_id: '2609.03450'
url: https://arxiv.org/abs/2609.03450
pdf_url: https://arxiv.org/pdf/2609.03450
published: '2026-09-03'
collected: '2026-09-06'
category: Agent
direction: Agent 记忆检索的指令形式消融
tags:
- Agent Memory
- Budgeted Verification
- Prompt Design
- Record Directive
- Plan Pointer
- LLM Evaluation
one_liner: 用 12 项注册实验（14,760 次尝试）量化 memory store 中 criterion 与 id 等 directive 形式如何改变
  budgeted agent 拉取哪条记录
practical_value: '- 在预算有限的 Agent 记忆/知识库检索里（例如商品库、用户历史记录），优先把“去哪找”写成可判定的 criterion，而不是裸
  ID：六个模型上长度匹配的 criterion 比 bare id 平均高 +35.0 个百分点。

  - 不要在 criterion 后追加 ID：在 Claude 三个模型上 ID 后缀会把 criterion 效应完全取消（Opus 5 从 40/40 掉到
  0/40）；若必须同时给出，可测试显式 ratification line + 两信用预算来恢复。

  - Prompt 的微小改动即可改变 Agent 拉取哪条记录：单字符 plan pointer 效应 +78.0/+81.7 pts，六个字节匹配编辑也各有独立效应；生产上要对
  memory/directive 模板做版本控制并针对关键行为回归。

  - 结果跨模型/API 不稳定：OpenRouter 九模型未复现直接 provider 面板的 criterion 优越性；80 runs 重跑中 15/30
  对比仍在误差内或未解决。建议在自有模型组合与 store 内容上做注册式 A/B，避免把单一 provider 结论直接泛化。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：Agent 继承记忆库但无法完全重读，推理时必须在验证预算内选择拉取少数记录；如果不能控制它拉哪条，未核查的 stale constraint 可能带偏决策。前期工作显示 Agent 会集中检查支持当前计划的记忆，而不是关键约束。

**方法关键点**：在一条 instrument lineage 上做 12 项注册研究（14,760 次尝试），固定模型面板，做精确 prompt 编辑。场景为六条一行记忆、Agent 最多拉一条归档源记录；对比 directive 形式：pointer（id）、criterion（识别标准）、两者追加；覆盖直接 provider、OpenRouter 多模型、不同 criterion 措辞、第二个 store、延伸至决策等变体。

**关键结果**：六个直接模型上长度匹配的 criterion 比裸 id 高 +35.0 个百分点 [31.2, 38.8]（Study D），但 OpenRouter 九模型未通过注册优越性规则（Study E）。三个 Claude 模型上追加 id 会取消 criterion 效应：Opus 5 从 40/40 掉到 0/40（Study F-x）；字节匹配编辑各有独立效应（Study G），80 runs 重跑中 15/30 对比在误差内、15 未解决（Study G'）。ratification line（+96.0 pts）加两信用预算在所有三个模型上恢复目标（Study J）；suffix 的取消在 Opus 5 五中四、Fable 5.1 全五成立（Study H2）。继续到决策时，criterion 让 Opus 5 的选择转向当前记录 +100.0 pts，但在 Fable 5.1 反向（Study I）。单字符 plan pointer +78.0 pts，前瞻重跑 +81.7 pts（Study B/B'）。所有结果均为固定面板上精确编辑的描述性效应，无机制断言。
