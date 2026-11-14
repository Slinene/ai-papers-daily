---
title: Sketching Language Models for Context Attribution
title_zh: 语言模型上下文归因的草图算法
authors:
- Christopher Liaw
- Aranyak Mehta
- Grigoris Velegkas
- Felix Zhou
affiliations:
- Google Research
- Yale University
arxiv_id: '2611.17313'
url: https://arxiv.org/abs/2611.17313
pdf_url: https://arxiv.org/pdf/2611.17313
published: '2026-11-12'
collected: '2026-11-14'
category: Eval
direction: LLM 上下文归因 · 查询复杂度
tags:
- Context Attribution
- Leave-one-out
- Sketching
- Query Complexity
- Taylor Stability
- Language Models
one_liner: 在稳定性假设下用草图算法以 O(√log(1/ε)/ε) 次评估估计所有 token 的 LOO 归因值，并证明下界最优
practical_value: '- 在 prompt 结构复杂的推荐/Agent 场景，LOO attribution 可定位关键上下文：用户长期偏好、候选商品属性、指令约束；Sketching
  算法把 O(n) 次模型调用降到 ~O(1/ε)，适合离线归因分析或线上调试。

  - 做 prompt 消融/敏感度分析时，先验证 token coefficient 是否快速衰减；若满足 stability，可用低阶 Taylor 近似做高效归因，不必对所有
  token 重算模型输出。

  - 算法上借鉴 backprop circuit 上前向微分的思路：在自回归生成中评估 token 贡献，可以在反向图中复用中间激活，结合缓存降低方差；实现复杂度高，建议从离线工具链开始。

  - 查询复杂度下界提示 O(1/ε) 是渐进最优，业务中做归因不必追求过分精确，量级上可以接受；可结合批处理与缓存进一步摊薄成本。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：上下文归因用于分析移除 prompt 中不同片段对 LLM 输出的影响。Leave-one-out (LOO) 是直接做法，但 n 个 token 需要 n 次模型评估，成本不可接受。

**方法关键点**：在稳定性假设下，将模型输出视为算术电路，利用 Taylor 系数稳定性，构建 sketching 估计器。关键 trick：不在原始前向电路，而在 backpropagation circuit 上做 forward differentiation，使方差大幅下降，开销仅常数倍于同阶前向草图。由此得到 O(√log(1/ε)/ε) 次评估的上界。

**结果**：证明该查询复杂度在 oracle 模型下匹配下界 Ω(√log(1/ε)/ε)，即渐进最优；实验验证系数衰减，并在小模型检索任务上验证 sketching 性能。
