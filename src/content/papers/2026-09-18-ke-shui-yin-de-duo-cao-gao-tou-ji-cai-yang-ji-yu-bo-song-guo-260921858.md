---
title: Watermarkable Multi-Draft Speculative Sampling via Poisson Processes
title_zh: 可水印的多草稿投机采样：基于泊松过程
authors:
- Yanxiao Liu
- Sicheng Wan
- Zhan Gao
- Deniz Gündüz
affiliations:
- Imperial College London
- University of Washington
arxiv_id: '2609.21858'
url: https://arxiv.org/abs/2609.21858
pdf_url: https://arxiv.org/pdf/2609.21858
published: '2026-09-18'
collected: '2026-09-21'
category: Other
direction: LLM 推理加速 · 无偏水印
tags:
- Speculative Sampling
- Watermarking
- Poisson Process
- Drafter Invariance
- Multi-Draft
- LLM Inference
one_liner: 利用泊松过程实现多草稿投机采样，同时嵌入无偏水印且不损失采样效率
practical_value: '- 对于线上 LLM 生成服务（商品描述、广告文案、对话等），可直接采用该框架：用 target 大模型 + 轻量 draft
  模型做投机采样，在几乎不增加延迟的情况下嵌入可溯源水印，满足合规与内容审核需求。

  - 多草稿和 drafter invariance 特性对持续迭代友好：升级或替换 draft 小模型不会改变 target 输出（给定随机种子），保证线上 A/B
  测试一致性和缓存可复用，降低回归风险。

  - 泊松过程 / 指数竞赛的无偏采样器可迁移到生成式推荐中的语义 ID 采样：从分布中精确采样多个候选，且 keyed randomness 便于 A/B 分桶或水印注入。

  - 检测指标 ANLPPT 及其统计检验方法可直接用于评估生成文本的水印强度，在 UGC 内容溯源、广告文案防伪等场景具有工程借鉴价值。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：LLM 推理效率与输出溯源是部署中的两大痛点，分别对应投机采样与水印。但已有工作（Hu & Huang 2024）证明二者存在本质 trade-off，尤其多草稿下难以同时保持水印强度和采样效率。本文通过泊松过程设计新的多草稿投机采样算法，突破该 Pareto 前沿。

**方法关键点**：
- 基于 Poisson Functional Representation (PFR)，离散情形退化为指数竞赛（等价 Gumbel-max trick），实现无偏精确采样。
- 扩展至 multi-draft：利用 mapped Poisson process 一次从 target 分布采样 B 个候选，构建上下文索引投机树，实现 list-coupling without communication，获得 stopping-time drafter invariance（输出前缀仅依赖 target 侧随机性）。
- 水印嵌入：使用 keyed Poisson process 作为随机源，保证输出分布无偏；检测采用 Aaronson score (ANLPPT)，检测时仅需最终 token 序列和密钥。

**关键实验**：
- 配置：Qwen2.5-7B-Instruct 作 target，Qwen2.5-0.5B-Instruct 作 drafter，数据集 CNN/DailyMail 和 ELI5。
- 对比 baseline：VSpS、MWS、MSE、MSE-PSEUDO、BASIC-UWM、INVARIANT（Rowan et al. 2025，记为 GLS）。
- 结果：MPFR 在 B=2,4,6,8 时 AATPS 略优于 GLS（如 Qwen-CNN/DM 下 B=8 时 MPFR 3.409 vs GLS 3.384）；PFR 与 PFR-NOWM 的 AATPS 几乎无差异，水印几乎不牺牲效率；在 TPR@1%FPR 检测上 PFR/MPFR 持平强水印基线；drafter 替换时 TPR 漂移 <1 个百分点，远低于 MSE 的 12-22 个百分点。

**最值得记住的一句话**：泊松过程耦合能够同时实现多草稿投机采样与无偏水印，且具备 drafter 不变性，为可复现、可溯源的 LLM 高效推理提供了新路径。
