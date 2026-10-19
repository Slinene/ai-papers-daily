---
title: 'BizBench: Unveiling Hidden Challenges in Deploying Long-Horizon Agents for
  Real-World Business'
title_zh: BizBench：揭示真实业务长程智能体部署中的隐藏挑战
authors:
- Enhan Zhao
- Yongqi Tong
- Xuejun Yu
- Hang Wang
- Pan Wang
- Yichao Wang
- Di He
- Jianshe Li
- Wei Wu
affiliations:
- Peking University
- Ant International
arxiv_id: '2610.20424'
url: https://arxiv.org/abs/2610.20424
pdf_url: https://arxiv.org/pdf/2610.20424
published: '2026-10-13'
collected: '2026-10-19'
category: Eval
direction: 长程 Agent 业务执行评测
tags:
- long-horizon agents
- business benchmark
- tool use
- execution validity
- policy compliance
- user simulation
one_liner: 构建含789文档/601工具的支付业务基准，同时评估目标达成与中间执行合规，前沿模型严格成功率仅64%
practical_value: '- 把「目标达成」和「执行合规」拆开评估，用确定性 checks 回放 execution trace，而不是只看最终状态；能抓到
  pre-approval 执行、储备金中途跌破等最终结果掩盖不了的违规。

  - 业务规则要显式建模 scope/版本/生效期，让 agent 先判断适用规则再执行；单纯 RAG 召回不足，需增加规则冲突消解和时效校验。

  - 用户/客户私有信息需多轮澄清，信息获取比文档检索更影响效果；全量客户披露使 strict success 从 43.3% 提升到 70.0%，建议在业务 Agent
  中设计结构化信息需求列表和主动澄清机制。

  - 工具调用冗余严重，如 DeepSeek-V4.1-Flash 为 Golden 的 1.71 倍，且大量重复读取；可引入检索去重、budget 感知或停止条件，降低长程执行成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有长程 agent 基准多只关注最终任务成功，很少评估中间执行是否合规。但在支付等真实业务中，即使最终目标完成，中间违规也可能造成资金或合规损失。同时规则分散、过时、冲突，检索到信息不等于选对适用规则。

**方法关键点**
- 从头部支付公司真实流程抽象出可执行环境：789 份知识文档、601 个可发现业务工具，并保留 scope/版本/生效期。
- 50 个多轮任务，涉及资源约束、时序依赖、历史承诺、过时/冲突指导；LLM 用户模拟器按需披露私有信息和审批。
- 评估用确定性 checks 分三类：目标 G、过程合规 P、保护对象/禁止副作用 F，严格成功 = G∧P∧F；不指定唯一路径，允许合法替代方案。
- 用 Golden traces 重放验证可满足性，再用合法变体和定向违规测试 evaluator。

**关键结果**
- Claude Opus 5 严格成功率 64.0%，GPT-6 Sol 61.3%；Qwen3.8-27B 目标达成 42.0% 但严格仅 32.7%，说明只看结果会掩盖无效执行。
- DeepSeek-V4.1-Flash 平均 191.3 次工具调用，约为 Golden 的 1.71 倍；Qwen3.5-9B 150 次运行 0 次达成全部目标。
- 信息消融：默认 43.3%，提供 gold doc 50.0%，全量用户披露 70.0%；客户侧信息获取比文档检索更难。
- 工具调用 budget 敏感：2×Golden 上限时严格成功率从 43.3% 降至 26.7%。

**最值得记住的一句话**
真实业务 Agent 的成功必须同时满足最终达成和全程合规，中间违规无法靠最终结果弥补。
