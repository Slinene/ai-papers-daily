---
title: 'MediSkill-Evo: Process-Constrained Self-Evolution for Evidence-Grounded Clinical
  Interaction'
title_zh: MediSkill-Evo：面向循证临床交互的过程约束自进化智能体
authors:
- Ruoyu Wu
- Shenfu Xie
- Yinqian Sun
- Haibo Tong
- Feifei Zhao
affiliations:
- Brain-inspired Cognitive AI Lab, Institute of Automation, Chinese Academy of Sciences
- Beijing Key Laboratory of Safe AI and Superalignment
- Beijing Institute of AI Safety and Governance
- School of Artificial Intelligence, University of Chinese Academy of Sciences
- Long-term AI
arxiv_id: '2608.23397'
url: https://arxiv.org/abs/2608.23397
pdf_url: https://arxiv.org/pdf/2608.23397
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent 自进化记忆与过程约束决策
tags:
- Self-evolving memory
- Process constraints
- Typed memory banks
- Clinical agents
- Safety evaluation
- Request-gated tools
one_liner: 用四库分离的自进化记忆与过程约束偏好控制，提升临床交互的证据获取与安全决策。
practical_value: '- 把记忆按知识类型拆分并绑定不同校验/决策权：电商/Agent 不要把可复用策略、平台规则、商品 schema、视觉流程放进同一向量库；可迁移为“话术策略库
  / 平台政策规则库 / 商品与活动 schema / 多模态识别流程”，每类分别做 provenance、support、replay、leakage 校验，测试时冻结
  snapshot。

  - 硬约束前置、打分后置：在广告/推荐 Agent 的动作生成中，先用 Symbolic Verifier 过滤掉违反库存、预算、品牌安全、合规约束的候选，再用
  Critic 排序；软惩罚不能抵消硬违反，缺失信息保持 unknown，不当作负样本。

  - 离线评测造“孤立压力”版本：用 deterministic controller 控制哪些特征延迟/不可用，只测特定 process obligation，比只看
  CTR/GMV 更能暴露 Agent 在信息缺失下的错误行为；对应大促缺货、延迟价格、标签缺失等压力集。

  - 多模态工具用 request-gated 接口和 original-pixel fallback：保留无工具路径与按需调用审计，避免把工具增益与模型能力混淆；MedSAM
  带来的 3 点诊断提升明确只是界面可行性，不是因果证据。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：临床 Agent 在部分可观测条件下必须自行获取并解读证据，最终诊断正确不能证明过程符合证据边界与安全约束。现有经验记忆把可复用策略、流程规则、证据语义、视觉流程混在同一个检索接口里，但不同知识类型需要不同的校验范围和决策权限。

**方法关键点**：
- 四库自进化记忆：Clinical Skill（病例策略）、Process Rule（流程约束）、Symbolic Schema（证据来源与状态转移）、Measurement（视觉流程）分离存储，分别经过 provenance、support、replay、controller 安全与泄漏校验后发布到冻结的测试快照。
- Process-Constrained Preference Harness：先触发规则强制动作；否则生成候选动作，由 Symbolic Verifier 过滤控制器无效/证据缺失/安全前提不满足的候选，再由 Clinical Process Critic 按诊断特异性、证据对齐、治疗完整、安全、分诊、检查效率打分；硬违反不可用软惩罚救回。
- 缺失证据保持 RESULTS_UNAVAILABLE，不当作阴性；所有结果必须绑定到有效请求。

**关键结果**：300 个 held-out Qwen 病例上，MediSkill-Evo 诊断准确率从 61.33% 提升到 69.00%，治疗意图覆盖从 33.62% 到 66.44%，自动打分的 critical failure 从 31.00% 降到 16.33%；DeepSeek 端点方向一致。180 个硬隔离压力条件中，patient-behavior 目标恢复 93.61%（超最强 baseline +17.22），temporal evidence 恢复 100%（+27.22），triage red flag 恢复 92.22%（+34.44）；但对不可用检查的请求率只有 30.00%，低于所有 baseline，diagnosis-pressure recovery 68.89% 低于 Reflexion 77.22%。多模态 MedSAM 条件仅提升诊断 3.00 点、core 3.24 点，作者明确只证明 request-gated 工具界面可行性。

**最值得记住的一句话**：记忆的关键不只是检索，而是知识类型决定它如何被验证、在决策时获得多少权限；缺失证据必须保持 unknown，不能被模型推断或工具结果悄悄变成事实。
