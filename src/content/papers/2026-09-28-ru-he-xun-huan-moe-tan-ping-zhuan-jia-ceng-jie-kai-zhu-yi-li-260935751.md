---
title: 'How to Loop MoE: Flatten the Experts, Untie the Attention'
title_zh: 如何循环 MoE：摊平专家层、解开注意力
authors:
- Shouren Wang
- Chuang Ma
- Mohsen Hariri
- Debargha Ganguly
- Wang Yang
- Xiaoqing Tong
- Qianying Liu
- Xiaotian Han
- Vipin Chaudhary
affiliations:
- Case Western Reserve University
- Kyoto University
- NII LLMC
arxiv_id: '2609.35751'
url: https://arxiv.org/abs/2609.35751
pdf_url: https://arxiv.org/pdf/2609.35751
published: '2026-09-28'
collected: '2026-09-29'
category: Training
direction: Looped MoE 架构训练与专家路由
tags:
- MoE
- Looped Transformer
- Attention Sharing
- Routing Metrics
- Pretraining Efficiency
one_liner: Foil 在固定专家参数与每 token 计算下，通过摊平专家层并给每次循环独立注意力，提升 looped MoE 预训练与路由健康度
practical_value: '- 在固定 expert 参数和每 token 计算预算下，优先采用“浅而宽 + 多轮循环”的 recurrent core，而不是深而窄：把现有
  MoE 层合并到更少层、增加每层 expert 数并循环更多次，同等成本通常能拿到更低 LM loss 和更健康路由。

  - 循环 block 中不要全程共享 attention：给每个 loop pass 单独 attention 参数，experts/router 继续共享；这几乎不增加推理
  compute，但能恢复摊平时丢掉的 attention 参数，训练损失和 zero-shot 均更优。

  - 监控 MoE 路由不能只看 load balance：可加 MMR（router 第一名 vs 池中位数概率比）和 per-pass MMR peak；MMR
  见顶后继续 flatten/循环收益最弱，适合做架构搜索早停或上线前诊断。

  - 做小规模架构 ablation 时，可先用 tied attention 探索循环轮数，因为加 passes 不增加参数；但最终生产配置应切换为 per-pass
  attention。低流量 expert 不等于无用，不要仅按流量直接裁剪。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
Looped Transformer 通过重复使用同一 block 以计算换参数；sparse MoE 每 token 只激活少数 expert。二者结合能让 token 在多次循环中触达不同 expert，但此前没有人系统回答：在固定 expert 参数和每 token 计算下，expert 应如何在层与循环间分布，以及 attention 是否该跨 pass 共享。

## 方法关键点
- 提出 Foil：在固定参数和 compute 下做 flatten，即把 shape (E,D,L) 映射为 (2E,D/2,2L)，使每层 expert 数翻倍、层数减半、循环次数翻倍；总 expert 参数和 expert 调用量不变，但每次 routing 的候选池更大，equivalent expert 数从 128 增至 1024。
- 将 attention 从共享中“解开”：experts 和 routers 跨 pass 共享，但每个 pass 拥有独立 attention 参数，不增加推理 compute，弥补 flatten 丢掉的 attention 参数。
- 设计三类指标：每 token 触达的 distinct experts、load balance B2、以及 MMR（第一名概率 vs 池中位数概率比），用于诊断路由质量。

## 关键实验
在 FineWeb-Edu 100BT 数据上训练，主模型约 553.7M 参数，20B tokens 预训练并继续训练到 100B tokens。与未摊平 baseline (8,8,2) 相比：20B 时所有 Foil loss 更低；100B 时 loss 随 flatten 程度单调改善，Foil-1 低 0.012 nat，下游 LAMBADA/HellaSwag/XWinograd 持平或更好。Untied attention 在每种 shape 下都优于 tied，最扁平配置 100B 下差 0.049 nat，且路由更均衡、更自信。消融显示 widen expert layer 与增加 loop pass 互相放大收益；load balance 单独无法指示健康专家分化，MMR 能更好追踪路由健康度。
