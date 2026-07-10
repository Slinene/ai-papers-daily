---
title: Resample or Reroute? Budget-Aware Test-Time Model Selection for Large Language
  Models
title_zh: 重采样还是重路由？LLM测试时模型选择的预算分配策略
authors:
- Teng-Ruei Chen
arxiv_id: '2607.08665'
url: https://arxiv.org/abs/2607.08665
pdf_url: https://arxiv.org/pdf/2607.08665
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: 测试时模型选择与预算分配
tags:
- LLM routing
- budget-aware
- resampling
- rerouting
- test-time compute
- verifier
one_liner: 提出在线策略 RoR，在单查询成本预算下动态分配重采样与重路由，最大化正确性。
practical_value: '- 电商搜索/推荐场景中若调用多尺寸 LLM，可借鉴 RoR 动态分配预算：对简单查询用廉价模型多次采样求一致，对困难查询路由到强模型，避免固定级联或
  Best-of-K 的浪费。

  - 使用边际正确性增益估计驱动在线决策，比静态规则更能适应查询难度分布的变化，适合后台异步或实时生成广告文案、商品摘要等场景。

  - 验证器质量是关键：文中用一致性投票或弱验证器仍有效，提示我们可以用业务指标（点击率、转化率）离线训练轻量级验证器来指导在线分配，但验证器退化时收益消失，需持续监控。

  - 工程上可利用已有模型池和多路采样，实现一个 meta-controller 层，对每条请求在重采样次数与路由目标间做动态决策，提升整体成本-质量帕累托前沿。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有 LLM 路由方法要么固定路由到某个模型，要么无限制重采样，未考虑两者在单条查询成本预算下的竞争关系。实际系统既有不完美的验证器又有预算约束，需要统一决策。

**方法**：将问题形式化为预算感知的测试时模型选择，提出 Resample-or-Reroute (RoR) 在线分配策略。核心是根据历史交互估计每个候选动作（继续采样当前模型 vs. 切换到另一模型）的边际正确性增益与成本之比，按增益/成本比贪心分配预算。策略利用了选择与采样的可恢复性非对称性：采样可逐步提升正确性，而路由错误可能不可逆。

**结果**：在 4 个基准、11 个开源模型池的重放实验中，RoR 在与单路由、Best-of-K、级联等基线的对比中取得更优的成本-质量帕累托前沿，尤其在模型差异大的基准上收益最大。消融显示收益依赖于验证器质量，劣化验证器会缩小收益；在加入价格权重和纯一致性验证器的情况下仍保持鲁棒性。
