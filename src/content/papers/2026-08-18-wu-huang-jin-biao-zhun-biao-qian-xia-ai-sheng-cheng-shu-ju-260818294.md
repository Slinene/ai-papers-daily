---
title: 'Debiased Inference for AI-Generated Data without Gold-Standard Labels: Identification
  via Multiple Imperfect Measurements'
title_zh: 无黄金标准标签下 AI 生成数据的去偏推断：基于多重不完美测量的识别
authors:
- Naoki Egami
- Sooahn Shin
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2608.18294'
url: https://arxiv.org/abs/2608.18294
pdf_url: https://arxiv.org/pdf/2608.18294
published: '2026-08-18'
collected: '2026-08-20'
category: Other
direction: 多不完美标注去偏推断
tags:
- debiased inference
- measurement error
- LLM annotations
- CP decomposition
- semiparametric inference
- multiple proxies
one_liner: 提出 DMM 框架，在无 gold-standard 标签时用多个不完美 AI 标注构建去偏桥函数，实现有效下游统计推断
practical_value: '- 不要把 LLM 标注直接当真实标签做下游回归/指标计算，即使准确率 >90% 也会产生显著偏差；当没有 gold labels
  时，可以用至少 3 个不同 LLM/prompt/temperature 输出作为 proxy，基于条件独立性识别真实标签分布并构造去偏矩估计。电商场景可迁移到用户意图分类、商品属性抽取、评论情感打分、广告内容审核等任务。

  - 条件变量 D 的设计是关键：把文本 embedding、任务难度特征（长度、模糊度、语言风格）、prompt 版本、模型家族等加入条件集，能缓解不同 LLM
  之间由于共享偏差导致的条件独立违背；同时要做条件独立性诊断，而不是默认假设成立。

  - 工程实现上，用 cross-fitting + EM 估计每个 proxy 的 class-specific error rate，桥函数采用 pair/triple
  多项式组合（3H2 - 2H3）可消除一阶估计误差，使 nuisance 模型只需 n^{-1/4} 收敛速度，适合大规模 LLM 标注 pipeline。

  - 监控 proxy 质量：新增一个标注器是否提升效率取决于其条件 bridge variance；如果某个模型准确率太差，可能增大估计方差，应加权或筛选后再加入
  DMM。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

## 动机
AI 测量越来越多被用于社会科学和商业分析，但 LLM 标注存在非经典测量误差：即使整体准确率超过 90%，直接忽略标注误差也会导致下游回归系数严重偏差、置信区间失效。现有纠偏方法（DSL、PPI）需要一组 gold-standard 标签用于训练或校正，而人工 gold labels 成本高、难以获得。

## 方法关键点
- 提出 DMM（Debiased inference with Multiple imperfect Measurements）框架：用至少 3 个不完美 AI 标注（不同 LLM、prompt、模型家族）代替 gold-standard 标签。
- 核心假设：多个 proxy 在真实标签和观测协变量 D 条件独立，即 X^{(1)} ⊥ … ⊥ X^{(J)} | X^*, D，其中 D 可包含文本 embedding、任务难度、prompt 版本等。
- 基于 CP 分解（Kruskal/Allman 等）识别每个 proxy 的 class-specific 分类错误率 η_{j,a}(d)，无需 gold labels。
- 构造 robust bridge function：H_R = 3H_2 - 2H_3，其中 H_2/H_3 是 pair/triple 平均桥函数，满足 E[H_R | X^*, D] = X^*，并且对 first-stage 估计误差有 Neyman 正交性，只需 nuisance 模型达到 n^{-1/4} 收敛速度。
- 用 cross-fitting 估计分类错误率，再代入下游矩函数 ψ_DMM 做去偏估计；扩展到 latent dependent variable 和多类别标签情形。

## 关键结果
- 理论证明 DMM estimator 一致且渐近正态，可构造有效置信区间；不需要知道哪个 proxy 被正确估计，对 J-1 个 proxy 的收敛具有多重稳健性。
- 模拟结果显示 DMM 给出有效推断，加入准确但不完美的 proxy 可提升效率；对同方差 proxy，渐近方差随 J^{-2} 下降，但新增 proxy 是否提升精度取决于其条件 bridge variance。
- 论文还提出用 J≥4 个 proxies 做条件独立性的过识别检验，以及当部分 gold labels 可用时与 DSL/PPI 结合的方案。

最值得记住的一句话：没有 gold labels 时，基于多个不完美标注的条件独立性和 CP 分解，可以构造出去偏且 Neyman 正交的桥函数进行有效下游推断。
