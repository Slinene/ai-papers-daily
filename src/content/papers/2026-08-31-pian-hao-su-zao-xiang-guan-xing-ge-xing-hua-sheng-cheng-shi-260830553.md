---
title: 'Preference Shapes Relevance: Cross-component Hierarchical Semantic Alignment
  for Personalized Generative Retrieval'
title_zh: 偏好塑造相关性：个性化生成式检索的跨组件层级语义对齐
authors:
- Gaoming Zhang
- Angqing Jiang
- Jianchun Song
- Kena Qi
- Dayao Chen
- Wei Lin
- Defu Lian
affiliations:
- University of Science and Technology of China
- Meituan
arxiv_id: '2608.30553'
url: https://arxiv.org/abs/2608.30553
pdf_url: https://arxiv.org/pdf/2608.30553
published: '2026-08-31'
collected: '2026-09-01'
category: GenRec
direction: 生成式检索 · 个性化语义对齐
tags:
- Generative Retrieval
- Semantic ID
- RQ-VAE
- Personalization
- Inference Acceleration
- Contrastive Learning
one_liner: 提出 CHAP：层级语义对齐与双视图个性化生成式检索，单次解码加速，线上转化提升2.98%
practical_value: '- 冻结 RQ-VAE codebook，对 query encoder 做 cross-sample alignment +
  层级对比学习 + soft probability distillation，可显著缩小 query 与 item 的 Semantic ID 语义 gap，适合电商搜索直接复用；但需预留
  codebook 动态更新机制，避免丢失协同过滤信号。

  - 用 sparse SID + dense raw embedding 双视图建模用户历史：sparse 提供稳定粗排结构，dense 补足长尾/个性化语义，尤其对歧义
  query 有效；为防止历史行为淹没当前 query，decoder 初始化只用 query，不要喂完整历史当前缀。

  - 推理架构上，将 Transformer Decoder 限制为单次前向，后续层级 SID 用轻量 residual block 生成；并行采样 50 个候选后，用
  temperature-normalized sparse/dense 分数乘性融合做重排。该设计把 QPS 从 32.4 提升到 78.9，适合线上低延迟召回。

  - 业务目标不要只看 CTR：CHAP 线上 UV-CXR +2.09%、支付订单 +2.98%，说明语义对齐 + 双视图更能触达转化意图；部署时可通过 Triton
  解耦模块，不依赖 query cache，保证实时性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

动机：生成式检索（GR）通过生成 Semantic ID 直接召回物品，但现有 SID 仅由物品内容训练，query 意图与静态物品表征之间存在语义鸿沟；同时 GR 很少建模用户行为序列，且逐层自回归解码导致线上推理延迟过高。CHAP 针对这三个问题，从层级语义对齐和推理加速入手做个性化 GR。

方法关键点：
- Hierarchical Semantic Alignment：冻结预训练 RQ-VAE codebook，对 query encoder 做交叉样本对齐（cross-commitment + cross-reconstruction）、层级感知对比学习（逐层对齐 query/target 的 partial quantization）和 soft probability distillation，把 query 拉进 item 的量化路径空间。
- 双视图序列建模：用户历史中每个 item 同时输入 sparse 离散 SID 和 dense 原始语义向量；decoder 只以 query 的双视图初始化，强制通过 cross-attention 检索历史，避免历史偏好压倒当前 query。
- Residual Cascading Generation：decoder 只做一次前向，后续 SID 层级用轻量 residual blocks 逐层生成，避免重复 heavy decoder；再 concat 重构 quantization 到 dense head 做细化。
- 候选打分：并行采样 M=50 个 SID，对稀疏 log-prob 和 dense cosine 分别 temperature-normalized Softmax 后乘性融合。

实验：在 ESCI-us、KuaiSearch、Amazon、Local-Life 四个真实数据集上对比 14 个 baseline。CHAP 在 ESCI-us 的 R@10 为 0.1127（COBRA 0.0585），在 Local-Life R@10 为 0.5803（COBRA 0.5020），显著优于强 GR baseline；14 天线上 A/B 中 UV-CTR +0.77%、UV-CXR +2.09%、订单量 +2.98%，同时推理 QPS 78.9，约为 COBRA 的 2.4 倍。

最值得记住：把 query 对齐到预训练 SID 的量化路径，并用 sparse SID 做结构骨架、dense 向量做语义细化，配合单 pass residual 解码，可以在提升个性化相关性的同时解决 GR 线上延迟。
