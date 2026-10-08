---
title: 'SkillSandbox: Skill Verification via Dynamic Scenario Synthesis'
title_zh: SkillSandbox：动态场景合成验证技能可重用性
authors:
- Serin Kim
- Kwangwook Seo
- Dokyung Song
- Jinyoung Yeo
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2610.10088'
url: https://arxiv.org/abs/2610.10088
pdf_url: https://arxiv.org/pdf/2610.10088
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: 自我进化 Agent 技能验证与库管理
tags:
- Agent Skills
- Skill Verification
- Scenario Synthesis
- Self-evolving Agents
- Execution Feedback
- Skill Library Curation
one_liner: 围绕每个技能动态合成新场景，对比有无技能的执行轨迹来验证其可重用性，构建更可靠的技能库
practical_value: '- 把「技能库/策略库入库前验证」从历史任务重放改为**动态合成验证场景**：针对每个策略/技能的适用条件，用 LLM 生成保留核心约束但改变上下文的新场景，这样能暴露策略是否真正可迁移。对应电商推荐中，可以针对某条
  query 改写规则或排序策略，合成不同类目、不同用户意图的模拟请求，验证其泛化性。

  - 借鉴 **VERIFIER 的三维度打分**：executability（策略是否被正确触发并执行）、utility（是否提升成功/转化）、efficiency（是否增加额外步骤/延迟）。在推荐系统里，可以对同一场景跑
  A/B（有/无该策略），比较转化率和平均步数，用折扣回报差来量化净收益，过滤掉「看似合理但引入回归」的规则。

  - 关注 **Recovery 和 Regression 指标**：论文强调可靠验证必须同时看新策略解决了多少之前失败的任务，以及是否让原来能成功的任务变失败。在电商推荐或广告策略上线时，除了看整体提升，还要监控对已稳定场景的回归，避免新策略破坏现有效果。

  - 验证不依赖更强外部模型：结构化场景构建和固定打分让执行器自身的模型即可完成可靠验证，业务中可用现有服务模型做策略筛选，无需额外引入更贵的模型。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
自我进化 Agent 从任务经验蒸馏技能存入库中复用，但技能可能包含错误流程或不可迁移知识，未经验证的技能会反复干扰 Agent 行为。现有验证方法从已有静态任务池中选择任务，存在两个问题：源任务重放只提供相关但不新颖的证据；其他任务虽新颖但未必触发技能适用情境。实证分析显示：语义相似任务中技能相关情境覆盖率最高仅 6.66/10；下游经验流中 17–32% 技能在 500 个任务后仍未被用到，45–56% 技能不足 5 次使用。因此需要围绕目标技能动态构造场景。

## 方法关键点
- 提出 SkillSandbox 框架，由 PROPOSER、BUILDER、VERIFIER 三个组件构成。
- PROPOSER 根据技能 condition、源任务和轨迹，输出程序化 specification，规定保留哪些条件、修改哪些细节以构造新上下文。
- BUILDER 根据 specification 绑定环境数据，生成可执行任务和配置，并通过验证循环保证场景满足条件且不同于已有场景，每个技能生成 5 个有效场景。
- VERIFIER 在同一个合成场景中对比有无技能的执行轨迹，从 executability（原则是否可执行）、utility（是否提高成功率）、efficiency（是否减少步数）三方面打分，用折扣回报差 Δu = r⁺γ^{T⁺-t⁺} - r⁻γ^{T⁻-t⁻} 计算可重用性得分，大于 0 保留，否则拒绝。
- 评价指标除成功率、平均步数外，引入 Recovery（无技能失败但有技能成功）和 Regression（无技能成功但有技能失败）。

## 关键实验
在 ALFWorld 和 WebShop 上，用 Qwen3.5-9B、Gemini 3.1 Flash-Lite、Qwen3.5-27B 三个模型测试。与 No Skill、Vanilla Skill、ReasoningBank、MemP、ExpeL、ACE、SkillOS 对比，构建 100 个源任务技能库，冻结后在 held-out 任务上评估。
- Qwen3.5-9B ALFWorld SR 从 32.1 提升到 66.4（+106.9%），WebShop SR 从 18.8 提升到 22.2，Score 从 47.1 提升到 59.1，同时步数下降。
- Gemini WebShop SR 从 25.6 提升到 36.2（+41.4%），Score 从 58.9 提升到 64.8。
- Qwen3.5-27B WebShop SR 从 32.2 提升到 45.0（+39.8%）。
- 消融显示：合成场景验证的 F1 明显高于源任务和随机任务（WebShop 88.9 vs 43.2/63.6），且库性能更好；验证与 held-out 技能效果的 Spearman 相关性在 WebShop 达 0.665；用更强模型 PROPOSER 并不提升验证准确性。

## 最值得记住
技能验证的核心不是选择已有任务，而是按需构造一个既触发技能适用条件又不同于源经验的新场景，用同一执行器对比有无技能的表现。
