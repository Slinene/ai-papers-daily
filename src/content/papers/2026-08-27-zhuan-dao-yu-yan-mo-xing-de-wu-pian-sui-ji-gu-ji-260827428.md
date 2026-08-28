---
title: Stochastic Estimation of Transduced Language Models
title_zh: 转导语言模型的无偏随机估计
authors:
- Vésteinn Snæbjarnarson
- Samuel Kiegeland
- Manuel de Prada Corral
- Ryan Cotterell
- Tim Vieira
affiliations:
- ETH Zürich
- University of Copenhagen
- CHI-FRO
arxiv_id: '2608.27428'
url: https://arxiv.org/abs/2608.27428
pdf_url: https://arxiv.org/pdf/2608.27428
published: '2026-08-27'
collected: '2026-08-28'
category: LLM
direction: 无偏概率估计与 beam 采样优化
tags:
- Transduced Language Models
- Unbiased Estimation
- Beam Sampling
- Finite-State Transducer
- Sequential Monte Carlo
- Probability Estimation
one_liner: 提出无放回重采样校正的beam-summing估计器，对TLM目标前缀概率给出无偏估计并大幅降低长序列推理时间
practical_value: '- 生成式推荐/query 生成通常用 beam search + 阈值剪枝，这会给候选概率带来未知偏差。可以借鉴无放回采样 beam-summing
  替代，获得无偏概率估计，用于后续重排序或校准，并能量化被剪枝的质量损失。

  - 在 LLM 受限生成（如 query 规范化、属性抽取）或 FST 组合场景中，该方法比阈值剪枝快几个数量级，适合长目标串在线概率估计，可降低服务时延。

  - 该算法随概率质量增加动态减少粒子数，保证停机，对需要严格延迟预算的在线推理系统有借鉴：在高质量区域可提前结束搜索。

  - sequential Monte Carlo 基线有放回采样，该方法无放回且用 inclusion probability 校正，改善 compute-variance
  tradeoff，可迁移到用户模型重要性采样或日志策略评估。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：TLM 将预训练源模型与有限状态转导器组合，计算目标前缀概率需对所有映射到该前缀的源串求和，集合可指数大或无限。此前用阈值剪枝 beam summing 得到下界，误差未知。

**方法**：用无放回重采样源前缀，按 inclusion probability 的倒数加权，递归应用校正得到无偏估计，并能估计剪枝损失的质量。beam-summing 算法在扩展保留前缀时采样保留哪些，随概率质量增加减少粒子数，节省计算且保证以概率 1 停机。

**结果**：在百科文本和 DNA 上与有放回 SMC 基线比较，文本上 compute-variance tradeoff 更优，DNA 上相同最大粒子数误差更低；DNA 到氨基酸转导运行时间比阈值剪枝 beam summing 降低几个数量级，使长目标前缀概率估计可行；替换阈值剪枝为无偏采样后，阅读时间语料惊喜度估计大幅降低，但原结论不变。
