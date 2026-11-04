---
title: 'OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking
  with One Autoregressive Transformer'
title_zh: OneTrans-GSR：单自回归 Transformer 统一重排/混排的生成式 Slate 排序范式
authors:
- Feng Cheng
- Yu-Hsuan Huang
- Fengyi Wang
- Chaofan Zhou
- Zhennan Zhu
- Huan He
- Bo Zhang
- Ruoqi Zhang
- Zhanfeng Mo
- Ziwei Liu
affiliations:
- ByteDance
arxiv_id: '2611.04720'
url: https://arxiv.org/abs/2611.04720
pdf_url: https://arxiv.org/pdf/2611.04720
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 生成式推荐 · Slate 排序统一重排与混排
tags:
- Generative Recommendation
- Slate Generation
- Reinforcement Learning
- Reward Model
- Reranking
- Mix-Ranking
one_liner: 单自回归 Transformer 统一重排/混排直接生成 slate，线上 GMV/u +2.63%、广告价值 +2.06%、复购 +2.03%，延迟降
  13%
practical_value: '- 架构上，用离线 reward model + 线上直接生成替代在线 Generator-Evaluator：线上只跑 decoder，多个候选按
  sequence log-prob 选最优，RM 不参与 serving，换来 13% 延迟下降；在重排/混排链路中值得复用。

  - 多目标融合上，不同 reward 目标先 min-max 归一化再几何平均，RM reward 与业务规则满意度 reward 分开标准化后组合，避免量纲差异导致单一目标主导；RM
  ensemble 加 disagreement penalty 防 reward overfitting。

  - 约束注入上，硬约束放在 decoding 的 masks/logit adjustments（tag-frequency 窗口、相似度惩罚、广告 boost），软偏好作为额外
  RL reward 而不是后处理规则，能保留生成模型的端到端优化空间。

  - 工程细节上，candidate 在 prefill 中互相 attend 比 output-only/cross-attention 更优；输出侧 stop-gradient
  防止候选 embedding collapse；共享 prefill KV cache 提升吞吐，可直接迁移到生成式候选生成/LLM 排序。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业推荐系统通常由级联的 pointwise 打分和手工规则拼装最终曝光 slate，重排与混排依赖专家规则和低容量模型，无法随数据/算力扩展。本文把 slate 生成建模为学习问题，用单一 decoder-only 自回归 Transformer 统一重排和混排，直接生成有序曝光列表。

**方法关键点**
- 模型基于 OneTrans blocks 的 decoder；prefill 阶段候选池与用户序列在 block-causal attention 下交互；逐 token 采样，使用 temperature-scaled cosine + 约束 logit adjustments/masks；同一候选 embedding 表只通过输入路径更新（stop-gradient）。
- 奖励模型 RM 用 EOS token 读完整 slate，输出 ListClick/ListOrder/ListGMV；另有 LTV RM 预测 14 天复购并按项聚合；RM 仅离线使用，容量不受线上延迟限制。
- 多目标 RL：GMR-PO 将各目标 min-max 归一化后几何平均，RM advantage 与软业务偏好奖励分别标准化再相加；用 GRPO 式 clip loss + KL 在 fresh rollout 组上更新；RM ensemble 加 disagreement penalty 抑制 reward hacking。
- 业务约束：硬约束在解码时通过 tag-frequency 窗口、similarity penalty、广告 boost 等实现；软偏好作为独立 reward 训练。

**关键实验**
- 在线 A/B：GMV/u +2.63%、advertiser value +2.06%、repurchase rate +2.03%，端到端重排+混排延迟降 13%。
- 离线相比 logged Generator-Evaluator：ListClick +7.68%、ListOrder +31.32%、ListGMV +28.70%；去掉自回归、RL 或 fine-rank score 显著变差，prefill 交互优于 output-only/cross-attention。
- RM 表现：ListClick AUC 0.8162、ListOrder AUC 0.8976；EOS readout 的 PCOC 1.00；pointwise CTR/CVR AUC 较上游 fine-ranker 分别 +1.23%/+0.62%。

最值得记住的是：把 slate 生成从规则专家系统变成可随算力扩展的学习策略，是重排/混排走向端到端生成的关键一步。
