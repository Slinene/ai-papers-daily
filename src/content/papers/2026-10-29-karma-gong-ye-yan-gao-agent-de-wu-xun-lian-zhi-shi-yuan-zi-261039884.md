---
title: 'KARMA: Training-Free Knowledge-Atomic Harness Evolution for Industrial Advertising
  Agents'
title_zh: KARMA：工业广告 Agent 的无训练知识原子化 Harness 演化
authors:
- Xinhua Miao
- Yuanzhen Rong
- Weiru Zhang
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2610.39884'
url: https://arxiv.org/abs/2610.39884
pdf_url: https://arxiv.org/pdf/2610.39884
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: Agent harness 无训练知识演化
tags:
- LLM Agents
- Training-Free Adaptation
- Harness Evolution
- Modular Knowledge
- Regression Testing
- Online Advertising
one_liner: 冻结模型权重与可执行 harness，以六类类型化知识模块的原子编辑+验证门控，使广告 Agent 离线动作一致性平均提升 29.7%
practical_value: '- **把 prompt/harness 拆成可版本化的知识模块**：role、domain、experience、constraints、output_protocol、action_descriptions
  六类模块，规则带稳定 rule ID、来源、before/after journal，所有变更走唯一 write boundary。电商/广告 Agent 可借此在不改代码、不微调模型的情况下，按商品/活动/政策变化审计和回滚决策知识。

  - **先做确定性轨迹诊断，再做知识编辑**：Trace Verifier 不用 LLM 就把失败分为 no_action / wrong_action_type
  / wrong_direction，并按固定映射定位候选模块；同时把成功和失败轨迹都送给 Critic。能避免只看失败导致修复过拟合、破坏已有正确决策，适合推荐/广告策略中“该不该调、调哪里”的归因场景。

  - **小步编辑 + 验证门控 + 快照回滚**：每轮最多 3 个原子 edit，固定 validation set 要求 gain≥1 point 才保留，否则恢复
  snapshot；可缓存 baseline validation，避免每轮 2 次全量评估，工程成本可控。可直接复用到电商 Agent 的离线知识更新流程，降低上线风险。

  - **跨域知识复用要分源域评估**：Long-tail/Others 域演化出的规则对多数目标域都有正向迁移，平均 hold-out gain +15.38；但
  Automotive 源域对所有其他域都负迁移。若要做跨品类 Agent 知识冷启动，优先用长尾/综合流量积累的通用规则，但仍需在目标域做验证，不能假设迁移一定为正。'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：工业广告 Agent 需要随商品供给、流量模式和运营政策持续更新决策知识，但反复微调昂贵，手动维护 prompt 难以规模化；整段 prompt 重写会把领域知识、决策启发式、输出指令纠缠在一起，改 harness 代码又会引入工具和控制流验证成本。因此需要一个训练免费、可审计、可回滚的机制，在保持模型权重和可执行代码冻结的前提下，仅演化外部决策知识。

**方法关键点**：
- 知识外部化为六类类型化模块：role、domain、experience、constraints、output_protocol、action_descriptions；后两类是带 stable rule ID、来源、文本的有序规则列表，registry 是唯一写边界，支持 create/update/delete/replace 原子操作，并记录 journal 和完整目录快照。
- 内层 Agent 渲染知识为 prompt 和 response schema，先通过白名单 read-only 工具收集证据，再调用 finish_analysis 输出结构化决策：动作类型 budget/bid/item、方向、rationale、证据 ID。
- 外层循环先由 deterministic Trace Verifier 把轨迹分为满分成功、语义失败 no_action/wrong_action_type/wrong_direction、基础设施错误；失败类经固定映射定位候选模块，成功和失败都按操作、类型、方向聚类。
- Critic 同时接收完整失败/成功报告和紧凑轨迹，从 missing knowledge、conflicting rules、protocol timing、ambiguous wording 四个视角比较成功与失败，给出 edit proposals；Evolver 受限最多生成 3 个原子 edit patch，不能访问业务工具、shell 或 gate 控制。
- 验证门控：固定 validation set 计算候选 patch 增益，达到 θ=0.01（1 分）才保留，否则恢复快照；hold-out set 完全隔离，只在最后评估。

**关键实验**：
- 数据来自约 50 万条真实运营日志，覆盖 6 个电商域，每域 800 例（480 训练/160 验证/160 hold-out），三个 LLM 家族 Qwen3.8-Max、GLM-5.3、Kimi-K3。
- 18 个 domain-model 设置中，平均 hold-out score 从 30.19 提高到 39.15，+8.96 点、+29.7%，16 个提升。
- 证据消融：去掉成功或失败轨迹后，平均 hold-out gain 都减少超过一半：完整 KARMA +16.67，无成功 +8.23，无失败 +6.56。
- 跨域迁移：30 个 source-target pairs 平均 +8.54 点，约为 in-domain 平均 gain 的 71%；Long-tail/Others 作为源域平均 +15.38，而 Automotive 作为源域对所有目标域均负迁移。
- 引擎对比：同一 gate 和接口下，KARMA 在 H 域 hold-out gain +15.94，优于 GEPA +9.06、AHE +8.75；在 B 域 +18.13，优于 AHE +6.56，token 成本相近。

**最值得记住的一句话**：把可演化对象限定为带 stable ID、provenance、journal 和 snapshot 的类型化知识模块，并用 deterministic verifier + 成功/失败对比 + validation gate + rollback 组合，能在不改模型权重和 harness 代码的前提下，稳定提升工业广告 Agent 的离线动作一致性和跨域迁移能力。
