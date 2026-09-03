---
title: 'GenCAR: Generative Counterfactual Alignment with Risk-Controlled Selection
  for Out-of-Distribution Recommendation'
title_zh: 面向分布外推荐的生成式反事实对齐与风险控制选择
authors:
- Qianqian Wang
- Yunshan Li
- Jiawen Zeng
- Wenwu Gong
- Lili Yang
affiliations:
- Southern University of Science and Technology
- University of Pennsylvania
arxiv_id: '2609.02162'
url: https://arxiv.org/abs/2609.02162
pdf_url: https://arxiv.org/pdf/2609.02162
published: '2026-09-02'
collected: '2026-09-03'
category: RecSys
direction: OOD 推荐 · 反事实生成 + 保形 FDR 控制
tags:
- OOD recommendation
- counterfactual generation
- conformal prediction
- FDR control
- LLM4Rec
- selection inference
one_liner: 提出 GenCAR：离线用 LLM 生成反事实候选并微调排序模型，在线用 conformal+BH 控制 proxy-label FDR，不调用
  LLM 提升 OOD 推荐恢复
practical_value: '- LLM 离线反事实样本生成：在场景变化（大促、季节、推荐位策略）前，用 LLM 基于用户 stable preference
  anchors 生成目标环境候选，通过 trust radius 过滤后微调精排模型，避免在线 LLM 成本。

  - 风险控制的选择层：借鉴 conformal p-values + BH/BY 对推荐集合做 FDR 控制，按批次决定输出数量；允许空列表相当于“不推荐”，适合付费/敏感场景（广告、消息推送、商品推荐）的体验保障。

  - 偏好-环境解耦的 SCM 架构：将用户 embedding 分解为 stable preference 和 environment 两部分，只更新 item
  embedding 进行反事实微调，可稳定适配环境变化，适合流量分布频繁变化的业务。

  - 轻量对齐预测器替代在线 LLM：用 LLM 生成的 proxy label 训练一个 MLP/score head，在线只计算 embedding 得分，既保留语义对齐信号又保证
  <1ms 延迟。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
训练与服务分布不一致（曝光、热度、时间变化）时，固定 top-K 推荐会失准；盲目扩大候选集虽可能覆盖更多有用 item，却引入低质量推荐。现有 OOD 方法或改善排序、或生成反事实候选，但都没有在服务侧控制“误推荐”比例。论文形式化 α-VCR 问题：在 retained counterfactual support 最大化的同时，保持 proxy-label FDR ≤ α。

## 方法关键点
- 用 SCM 解耦 latent：z_c 稳定偏好、z_e 环境、η 噪声；环境变化仅发生在 p_e(z_e)。
- 反事实构造：固定 z_c，干预 z_e 为目标环境；将 z_c 的 top-K item anchors 作为偏好描述喂给 LLM，生成候选及 alignment score；再用 trust-radius δ 过滤与 z_c 余弦距离过大的候选；通过 BPR 微调仅更新 item embeddings。
- 风险校准：LLM 对齐分数阈值得到 proxy label，训练轻量对齐预测器 h；用 disjoint proxy-null calibration set 计算 conformal p-values（lower-tail）。
- 在线选择：对候选池应用 BH（PRDS 假设）或 BY（任意依赖），返回满足 FDR 约束的最大 pooled 集合；用户列表可为空（弃权）。在线不调用 LLM，只保留 encoder、item embeddings、h 和校准分数。

## 关键结果
- Recall@10 较 CausalVAE backbone 提升：ML-100K +11.0%，Coat +19.1%，Amazon-Book +43.5%；在所有 LLM-free 方法中最高。
- 在 5 个候选池上 realized proxy FDP ≤ α=0.30：Coat 0.188、ML-100K 0.195、ML-1M 0.089、Beauty 0.054、Amazon-Book 0.048。
- 在线推理 <1ms/用户，而在线 LLM 重排 TallRec 约 5.4s/用户。
- 部分离线覆盖（Steam 38% 用户有 LLM CF）时，基础微调仍接近 backbone；显式保留变体 R@10 +9.2%。
- KL-clamped 偏好-环境解耦使反事实新颖率从 18.3% 升到 70.3%，收益从接近 0 升至约 8.0%。

**最值得记住的一句话**：把 LLM 留在离线做“目标环境”反事实监督，再用 conformal + BH 做风险控制的选择层，可以同时拿到 OOD 候选恢复提升和在线毫秒级服务。
