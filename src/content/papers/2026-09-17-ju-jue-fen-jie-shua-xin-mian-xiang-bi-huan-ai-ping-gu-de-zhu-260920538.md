---
title: 'Refuse, Decompose, Refresh: A Claim-Safe Protocol for Closed-Loop AI Evaluation'
title_zh: 拒绝、分解、刷新：面向闭环 AI 评估的主张安全协议
authors:
- Peiying Zhu
- Sidi Chang
affiliations:
- Blossom AI
arxiv_id: '2609.20538'
url: https://arxiv.org/abs/2609.20538
pdf_url: https://arxiv.org/pdf/2609.20538
published: '2026-09-17'
collected: '2026-09-19'
category: Eval
direction: AI 评估协议 · 主张安全
tags:
- AI evaluation
- claim safety
- abstention
- distribution shift
- closed-loop
- selective prediction
one_liner: 提出由 Refuse、Decompose、Refresh 构成的评估协议，将结论限定在有观测支持的范围内，并在闭环模拟器中实证
practical_value: '- 把评估流程从单一 PASS/FAIL 改为三阶段：先判断参考流/匹配比较是否有足够支持，再按组件和流量段分解报告，最后对漂移告警先重算参考而非直接报障；适合推荐系统
  A/B 实验与离线评估，避免整体指标提升掩盖不可观测组件失败。

  - 对闭环推荐/Agent 系统，策略决定曝光和状态访问，许多失败不会留下可测痕迹；建议记录未覆盖组件与弃权单元，将“未观测”显式作为结果一部分，而不是当作“无故障”。可采用预注册保留集与
  aggregate-only 监控，降低选择性报告风险。

  - 零故障场景用精确二项上限报告不确定性（如 0/20 时单边 95% 上限 0.1391），在安全/风控相关评估中展示 CI 而非点估计，避免过度自信。

  - 漂移告警处理可迁移：当线上特征分布或请求类型变化时，先让参考基线失效并重算，而不是直接判定模型故障，减少电商大促等非平稳时期的误报。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：AI 评估即使完全可复现，也可能支持错误结论。闭环系统中，被评估策略决定访问哪些状态、哪些组件可观测，因此部分故障不会留下可测痕迹，单点 PASS/FAIL 容易产生无效主张。

方法关键点：提出三项动作构成的可执行协议。Refuse：当干净参考流或匹配运行时比较缺乏支持时主动弃权；Decompose：把协议执行、操作误接受、结构假设分开报告，不用一个科学 PASS/FAIL 标签；Refresh：把分布漂移告警视为参考地图失效、需要重算的信号，而不是直接当作故障证据。在 aggregate-only 模拟器中实例化：24 个策略组件、3 种需求域、2 个故障掩码族、独立开发集与保留集。预注册保留集包含 1,440 案例、21,600 分区行。

关键结果：72 个 regime-component 单元中只有 55 个通过参考准入，55 个中 54 个保持运行时准入，弃权成为结果的一部分。20 个有表示的组件中稳定误接受为 0，冻结 0.20 规则下单边精确 95% 上限为 0.1391。在 540 个单元-arm 行、20 个组件聚类内，cell-minus-traffic 负对数似然差为 0.1264 nats/row，95% 组件聚类区间为 [0.0593, 0.1918]。漂移日志显示 clean fault-null 流在三个需求域分别触发 15/15、0/15、14/15 次告警，仅中间域匹配冻结检测器参考，说明 null 必须相对参考定义。核心贡献不是通用阈值，而是连接可观测支持、统计校准与每个数字所能证明结论的契约。
