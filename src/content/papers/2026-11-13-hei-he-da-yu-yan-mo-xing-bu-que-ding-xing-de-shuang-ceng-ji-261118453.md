---
title: Black-Box Uncertainty Quantification for Large Language Models via Ensemble-of-Ensembles
title_zh: 黑盒大语言模型不确定性的双层集成量化
authors:
- Wang Ma
- Debarun Bhattacharjya
- Junkyu Lee
- Nhan H Pham
- Harsha Kokel
- Qiang Ji
affiliations:
- Rensselaer Polytechnic Institute
- Lirio
- IBM Software Innovation Lab
arxiv_id: '2611.18453'
url: https://arxiv.org/abs/2611.18453
pdf_url: https://arxiv.org/pdf/2611.18453
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: LLM 不确定性量化 · 黑盒双层集成
tags:
- Uncertainty Quantification
- Black-box LLM
- Aleatoric-Epistemic
- Semantic Perturbation
- Ensemble
- Embedding Space
one_liner: 用内层随机解码+外层语义扰动构成双层集成，在嵌入空间按总协方差定律分解偶然/认知不确定性，仅需黑盒采样
practical_value: '- 黑盒 API 场景：对商品文案、query 改写、推荐解释等 LLM 输出，不需要 logits/权重；同一 prompt
  多次温度采样做内层，语义等价改写 prompt 做外层，在 embedding 空间计算总协方差分解 AU/EU。AU 高说明 prompt 有歧义，可约束改写；EU
  高说明模型缺知识，可触发 RAG 或人工审核。

  - 工程实现 trick：样本量少时用论文的 bias-corrected epistemic estimator（嵌套 MC 偏差修正），避免 EU 被高估；embedding
  建议用语义 embedding 而非文本 token 完全一致，否则同义不同措辞会虚增 AU。

  - 在 Agent/多步推荐流程中，把该 UQ 作为路由信号：query 生成后 AU 高则下游保守执行，EU 高则补充知识或换更大模型；论文的配对干预证明 AU/EU
  分别响应 prompt 歧义与知识缺口，可作为监控指标。

  - 注意主要面向 API-only 黑盒 LLM，需额外 paraphrase 与多次采样成本；建议对高价值关键输出使用，不必全量。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 可靠部署需要区分 prompt 本身的歧义（aleatoric, AU）与模型知识缺失（epistemic, EU）。白盒 Bayesian/deep-ensemble 在 LLM 规模计算成本高且需权重访问；现有黑盒方法通常只给标量，无法分解。

**方法**：提出双层集成：固定 prompt 下随机解码构成内层；对 prompt 做保留语义的扰动构成外层。在连续嵌入空间测量变异，利用 total covariance 做 within/between-perturbation 分解，分别估计 AU/EU，只需黑盒采样。理论贡献包括有限样本嵌套 MC 的偏差恒等式和偏差修正 EU 估计；Bayesian bridge 将扰动群体的 AU/EU 与 Bayesian 目标联系起来；separation 结果证明一致性黑盒方法会漏掉某些失败模式，而扰动 EU 可检测。

**结果**：在 5 个 short QA benchmarks、4 个 instruction-tuned LLMs（两家系两种尺度）上，估计器与强白盒基线可竞争；在相同生成预算下，与领先黑盒方法在 error ranking 上持平，同时能分解 AU/EU。配对受控干预显示 AU 和 EU 选择性响应 prompt 歧义和知识缺口。NQ long-answer 试点表明无需重训即可扩展到 claim-level factuality。
