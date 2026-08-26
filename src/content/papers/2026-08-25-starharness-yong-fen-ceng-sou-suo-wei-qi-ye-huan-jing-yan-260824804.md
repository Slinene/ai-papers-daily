---
title: 'StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments'
title_zh: StarHarness：用分层搜索为企业环境演化 Agent Harness
authors:
- Esakkivel Esakkiraja
- Denis Akhiyarov
- Vikas Yadav
- Sai Rajeswar
- Patrice Bechard
- Sridhar Nemala
- Sagar Davasam
affiliations:
- ServiceNow
- Mila
- Université de Montréal
arxiv_id: '2608.24804'
url: https://arxiv.org/abs/2608.24804
pdf_url: https://arxiv.org/pdf/2608.24804
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent harness 演化 · 环境适配
tags:
- harness evolution
- agent
- tool use
- enterprise
- task stratification
- model transfer
one_liner: 提出 StarHarness，在冻结模型下分层搜索演化 Agent harness，企业基准提升 20-35pp 并可跨模型迁移
practical_value: '- 对电商/广告/搜索推荐里的 Agent 工具链，可以不微调模型，先优化 harness（prompt、tool schema、MCP
  参数预处理、subagent 结构、finish 逻辑）；本文在 4-12 个 accepted patches 内拿到 20-35pp 提升，工程成本很低。

  - 借鉴其分层任务池：按 baseline failure mode、task score、verifier pass rate 抽样，再把任务拆成 proposer
  可见 search set、隐藏 selection set 和 held-out；能直接评估泛化、防止 harness 搜索过拟合到具体 case。

  - 演化循环中加入便宜门控：scope/import/smoke 校验 + 单任务 test flip，不通过就不跑全量 selection eval；生产环境可大幅降低搜索成本。

  - 实际可复用的修复类型：清理 null/empty/placeholder 参数、补充 schema 约束、把隐式业务规则写进 prompt（如 priority
  与 impact/urgency 联动、保留 relationship 字段）、把日期/金额计算下沉到确定性工具；这些都适合迁移到订单、商品、营销工具等有状态业务
  Agent。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：工具密集的企业环境中，LLM Agent 的成败很大程度取决于 harness——prompt、工具接口、skills、MCP provider、subagent 结构和 loop 策略。模型权重不变也会因为接口错配、业务约定缺失而持续失败。手动调 harness 成本高，单纯 prompt optimization 覆盖不足，因此需要一种冻结模型权重、只搜索环境特定 harness 的方法。

**方法关键点**：
- StarHarness 把 harness 演化视为外层搜索：冻结模型权重，只编辑可执行 scaffold。
- 任务池构建：先按 baseline failure mode、task score、verifier pass rate 分层抽样约一半任务；再拆成 proposer 可见 search set、proposer 隐藏 selection set，剩余 held-out 用于泛化评估。
- 演化循环：proposer 生成 patch → scope/import/smoke 校验 → 单任务 test flip 门控 → 在 hidden selection set 评估 → 确定性接受，只有 selection mean 提升才 commit。
- Guardrails：禁止 task ID 分支、硬编码答案、verifier/ground truth 泄漏，只允许通用环境修复；支持 hill climbing 与 tree search 两种搜索策略。

**关键实验**：
- 三个企业 benchmark：ITBench SRE（40 tasks）、EnterpriseOps-Gym ITSM（103 tasks）、AutomationBench Finance（100 tasks）。
- 相对默认 Stirrup harness，StarHarness 在 4-12 个 accepted patches 后全 benchmark 提升 20-35pp；相对 GEPA prompt optimization 分别 +13.8/+22.3/+17.6pp。
- Held-out 泛化增益为 +31.7/+15.1/+29.3pp；同一 frozen harness 迁移到 GPT-5.4-mini、GPT-5.5、Qwen 系列均有提升，最高 +46.3pp。
- 成本降低 17%/53%/29%；EnterpriseOps 验证器通过率 34.5%→72.8%，AutomationBench guardrail violations 33→4。

**最值得记住的一句话**：冻结模型权重，只演化环境特定的 harness，就能在工具密集的企业 Agent 任务中换来 20-35pp 的稳定提升，且跨模型迁移。
