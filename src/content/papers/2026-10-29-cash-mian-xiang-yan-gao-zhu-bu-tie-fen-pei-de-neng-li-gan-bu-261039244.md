---
title: 'CASH: A Capability-Aware Subsidy Harness for Advertiser Subsidy Allocation'
title_zh: CASH：面向广告主补贴分配的能力感知补贴调度框架
authors:
- Minmao Wang
- Huihuang Lin
- Likang Wu
- Hongke Zhao
- Shijie Yi
- Fei Pan
affiliations:
- Fudan University
- Kuaishou Technology
- Tianjin University
arxiv_id: '2610.39244'
url: https://arxiv.org/abs/2610.39244
pdf_url: https://arxiv.org/pdf/2610.39244
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: 广告主补贴分配 · LLM Agent 与数值模型协作
tags:
- Advertiser Subsidy Allocation
- LLM Agents
- Capability Licenses
- Budget Allocation
- Online Advertising
- EPCG
one_liner: 以结果校准的 capability license 融合 LLM Agent 与数值模型，在线收入提升 15.35%
practical_value: '- 借鉴 outcome-grounded capability license：不全局信任 LLM 或数值模型，在账户×档位维度维护误差上限、支持度和区域准入，只让许可范围内的估计参与优化；适合把
  LLM 纳入线上决策但需控风险。

  - 共享预算问题写成 multiple-choice knapsack 并用对偶价分解；许可证能屏蔽未许可档位带来的跨账户误差传播，电商大促补贴/优惠券分配可直接复用。

  - 限频调用 LLM：用 pre-call judge 与 call-value 回归选择 top quota 账户调用，靠随机 audit 保留可观测性；CASH
  用 15% 的调用量恢复全量 86% 的 MAE 收益，成本敏感场景可用。

  - EPCG 式探索：用 Beta 后验和区域准入变化预估新增反馈对可靠覆盖的增益，动态规划分配反馈预算，比随机采样更能扩展可信任区域，可迁移到 RAG/冷启动补标签。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

动机：广告平台通过折扣补贴提升广告主竞争力，但传统分层经验配置无法刻画单个账户在不同补贴档位上的边际收益差异；共享预算下，某个账户的估计误差还会通过平台约束传导到其他账户。LLM 能融合运营知识但数值精度不可靠，数值模型在有反馈处准确、稀疏处易失效，单一来源无法全局信任。

方法关键点：
- 双估计器互补：Tool 数值响应模型预测 pre-discount revenue，并用 isotonic regression 保证折扣加深不降低收入；Agent 用 LLM 根据账户历史、运营信息和规则一次性生成整条补贴响应曲线。
- 结果校准的能力许可证：capability plugin 从 realized error 拟合 error-scale model，产出账户×档位级的误差上限和支持度；许可证需同时满足误差、经验支持、区域准入三个条件。
- 许可约束的路由与分配：judge 预先打分选 top quota 账户调用 LLM，其余走 Tool；有争议账户由 orchestrating agent 在许可选项内裁决。共享预算优化建模为 multiple-choice knapsack，通过对偶价分解为账户级选择。
- EPCG 闭环探索：按区域 Beta 后验和准入状态变化估算新增反馈对 Tool 可靠覆盖的增益，用动态规划分配反馈配额，成熟反馈再更新许可证与模型。

关键结果：离线 663,312 account-days，CASH 相比 Tool 降低 MAE 2.20%、RMSE 4.11%，仅 6,119 次 LLM 调用（约为全量 15%），恢复全量 86% 的 MAE 收益；许可证内 severe exceedance 率 6.29% vs 外 15.08%，并把未许可档位扰动造成的跨账户影响降为零。在线 1 个月、60% 流量：CASH 较 Control 在补贴率基本不变下提升 revenue per account +15.35%、ADVV +19.86%、7-day LTV +15.98%、14-day LTV +15.24%；较 Tool 再提升 revenue +6.31%。

最值得记住的一句话：不要追求单一估计器全局可信，而要把“在哪些账户和档位上能信任哪个估计器”作为可学习、可更新的资产，并与共享预算分配闭环迭代。
