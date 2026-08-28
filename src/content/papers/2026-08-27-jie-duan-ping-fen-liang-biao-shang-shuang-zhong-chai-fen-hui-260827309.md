---
title: 'Difference-in-Differences on a Censored Rating Scale Can Manufacture an Effect:
  Evidence from a Pre-Registered LLM-Judge Audit'
title_zh: 截断评分量表上双重差分会制造效应：预注册 LLM 法官审计证据
authors:
- Shuyi Fan
- Boyuan Deng
- Mengyu Xu
- Xinhong Xie
- Chenyang Li
- Hongyang Zhang
affiliations:
- Columbia University
- Johns Hopkins University
- The University of Chicago
- The Pennsylvania State University
- The Hong Kong Polytechnic University
arxiv_id: '2608.27309'
url: https://arxiv.org/abs/2608.27309
pdf_url: https://arxiv.org/pdf/2608.27309
published: '2026-08-27'
collected: '2026-08-28'
category: Eval
direction: LLM 评估 · 双重差分识别问题
tags:
- LLM Judge
- Difference-in-Differences
- Censored Rating
- Audit
- Identification
one_liner: 揭示 LLM 法官审计中双重差分在 bounded 评分量表上无法识别偏差，显著交互可能纯由截断衰减制造
practical_value: '- 业务中用 LLM 评分（如生成质量、推荐理由、搜索相关性）时，若评分是有界顺序量表（1-5 分），避免直接用双重差分（DiD）估计处理效应：两组候选评分与边界距离不同，共同
  severity shift 会被不等衰减，产生虚假交互。先检查评分分布与边界接近程度，对近边界样本做敏感性分析或采用 censored/Tobit 类模型。

  - 做 LLM-as-judge 审计（如审计推荐理由偏见、搜索结果排序公平性）时，区分“偏好差异”与“量表衰减差异”：论文给出从审计自身评分中计算 severity
  shift 与 floor/ceiling 贡献的闭式方法，可作为审计 pipeline 的后验诊断，量化被截断部分贡献的假效应比例。

  - 预注册审计主端点 null 而某个交互显著时，不要急于解释为异质性效应；上报前用零偏好构造（zero differential preference）对照，检查该交互是否能由纯截断机制重现，论文示例中可重现
  79-85%。

  - 电商推荐 A/B 测试或 LLM 评估中，若评分指标有天花板/地板效应，优先使用不受截断影响的指标（排名、胜率、偏好选择率）或对评分做截断矫正，否则可能错误归因。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 作为评审者时，审计常采用双重差分设计：固定 item，对比两个候选响应，再跨操纵属性差分，最后从有界评分量表读取效应。作者指出该端点在该量表上不可识别：每个双重差分项受到各自的截断份额影响，观测统计量混淆了差异偏好与差异衰减。共同 severity shift 在两项被不等截断时会制造交互，尤其当 stimulus 靠近边界时。

方法：理论推导截断量表上双重差分识别失败机制，并在预注册审计（990 calls，frozen pedagogy judge）中检验。预注册主端点为 stated learner profile 对 scaffolding preference 的影响。

结果：主效应 null（+0.085，95% BCa [-0.167, +0.353]，p=0.684）；一个名义显著交互 +0.378（p=0.002）被证明未被识别为偏好：构造零差异偏好的数据，仅用观测 severity shift 和量表地板就能重现 79-85% 的交互效应。闭式分解显示该贡献可从审计自身评分中测量。
