---
title: 'The Dice Roll Method: A Standardized Protocol for Repeated-Query Auditing
  of Large Language Model Brand Recommendations'
title_zh: LLM 品牌推荐重复查询审计的 Dice Roll 标准化协议
authors:
- Dmitrij Żatuchin
affiliations:
- Department of Information Technologies, Estonian Entrepreneurship University of
  Applied Sciences (EUAS), Tallinn, Estonia
- Rankfor.AI, Tallinn, Estonia
arxiv_id: '2609.04047'
url: https://arxiv.org/abs/2609.04047
pdf_url: https://arxiv.org/pdf/2609.04047
published: '2026-09-03'
collected: '2026-09-05'
category: Eval
direction: LLM 重复查询审计协议
tags:
- LLM auditing
- brand recommendation
- reliability
- generalizability theory
- bootstrap
- simulation-based power
one_liner: 为 LLM 品牌推荐重复查询审计提供统计可靠性迭代标准与指标组合，外部验证 37/39 单元复现
practical_value: '- 在内部评估 LLM 推荐品牌/商品稳定性时，直接套用三档迭代标准：探索性 n=5（G=0.58）、确认性 n=10（G=0.74）、严格
  n=15（G=0.81），结合 Cliff''s delta 效应量阈值做决策，避免拍脑袋定重复次数。

  - 用多指标 battery 替代单一指标：同时统计 count（出现频次）、set（集合重叠）、embedding（语义相似度）、fairness-adjusted
  PASOR（公平调整），警惕只盯准确率或 top-1 的误导。

  - 处理 LLM 输出的计数或离散品牌分布时，用 negative-binomial mixed model 加依赖保持 bootstrap，而不是正态假设的
  t-test；token 采样导致的过度离散会很严重。

  - 对 prompt 改版、模型升级或温度参数调整，可以引入 KS 检验和 PSI 漂移诊断，在 pinned model snapshot 上监控输出分布变化，防止无声漂移破坏推荐一致性。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 品牌推荐审计普遍使用重复相同 prompt 来捕捉随机波动，但迭代次数、稳定性指标、可靠性阈值缺乏标准；且 LLM 自回归生成的条件分布非高斯，传统统计方法不适用。

**方法关键点**：基于温度缩放 nucleus sampling 的生成模型，将总响应方差分解为 token 级采样、prompt 措辞、run-to-run、模型版本四部分。分析栈包括：negative-binomial 广义线性混合模型（迭代作为嵌套在 prompt/model/language 内的重复测量）、Cliff's delta 作为分布无关效应量、依赖保持 bootstrap、simr 模拟功效、generalizability theory D-study 可靠性分解、对 pinned snapshot 的 KS/PSI 漂移诊断。重新分析 5 个审计研究，约 190k 观测、270+ 品牌、6 种语言、迭代次数 5 到 40。

**关键结果**：D-study 给出三档迭代指导——探索性 n=5（G=0.58）、确认性 n=10（G=0.74）、严格 n=15（G=0.81），并与 Cliff's delta 阈值挂钩。四类指标族（count、set、embedding、fairness-adjusted PASOR）互补，Bootstrap 校正 Spearman 相关矩阵支持用紧凑指标电池而非单一指标。预注册外部验证在 Motoki 100-round 数据、Rozado 24-model sweep、llm-stability 三个独立语料上，37/39 单元复现 D-study 可靠性预测，n=5 功效值精确到两位小数；固定层级不可迁移，支持 pilot-then-solve 的解读。
