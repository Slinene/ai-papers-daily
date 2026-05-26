---
title: 'LENS: A Staged Design for Interaction Granularityin Sequential CTR Prediction'
title_zh: 'LENS: 序列CTR交互粒度分阶段设计'
authors:
- Yuan Wang
- Yue Liu
- Jun Zhang
- Jie Jiang
affiliations:
- Tencent Inc.
arxiv_id: '2605.25583'
url: https://arxiv.org/abs/2605.25583
pdf_url: https://arxiv.org/pdf/2605.25583
published: '2026-05-25'
collected: '2026-05-26'
category: RecSys
direction: 潜在查询骨干的目标条件增强与交互粒度设计
tags:
- Sequential CTR
- Latent-Query
- Target-Conditioned
- Position Bias
- Query-Specific
- Density-driven
one_liner: 提出分阶段框架，通过静态位置先验和目标条件残差在潜在查询骨干中恢复目标特异性，并发现密度驱动的条件源规则
practical_value: '- **分阶段设计交互粒度**：将目标-历史交互分解为骨干瓶颈、位置先验、目标条件三层，可在不同骨干间独立优化和迁移，降低架构升级风险。

  - **QueryPos 作为便携式位置先验**：为每个潜在查询添加可学习的位置偏差，尤其适合长序列（≥200），参数极小（<10K），可轻松集成到任意带交叉注意力的骨干中。

  - **LENS 零初始化目标条件模块**：通过 TCQG（控制哪些查询激活）和 TCPB（控制从哪里读取历史），在不改变骨干计算模式的前提下恢复候选特异性；零初始化保证从原始骨干平滑启动，适合在线迭代。

  - **密度驱动的条件源规则**：当样本/项目 > 50 时仅用目标 Item Embedding，反之拼接序列均值，避免稀疏 Embedding 成为瓶颈，对电商长尾商品建模有直接指导。

  - **稀疏曝光日志的序列处理**：使用类型化曝光历史（添加 action type embedding）而非过滤正样本，能保留长尾序列覆盖度，大幅提升冷启动物料在序列侧的表示学习。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
序列CTR预测中，目标如何与用户历史交互的粒度是关键设计维度。DIN等细粒度方法直接计算目标与每个历史物品的注意力，依赖充分训练的Item Embedding，对长尾物品脆弱；HyFormer等潜在查询方法用少量查询压缩历史，更鲁棒但丢失了候选特异性。现有架构将交互粒度固定为架构副作用，缺乏显式设计。

## 方法
提出分阶段设计框架：
- **阶段1**：选择交互瓶颈（如HyFormer的潜在查询解码器）。
- **阶段2**：添加Query-Specific Position Bias (QueryPos)，为每个查询学习独立的位置偏好曲线，作为静态位置先验。
- **阶段3**：LENS模块组，由**目标条件查询门(TCQG)**（控制哪些潜在查询激活）和**目标条件位置偏差(TCPB)**（控制查询从历史何处检索）组成，均零初始化，保证从骨干未修改状态起步。
- **条件源规则**：根据训练样本/物品密度自动选择条件信号——>50时仅用目标Embedding，否则拼接序列均值，解决稀疏Embedding不可靠问题。

## 关键实验
在4个数据集（KuaiRec约1000样本/物品、TaobaoAd约59、TAAC约22、KuaiRand约1.1）上，以HyFormer为参考骨干，并迁移到MixFormer和OneTrans。所有12个骨干×数据集组合均获得正向总增益。关键数字：
- HyFormer上QueryPos+LENS较基座提升：KuaiRec +0.0090，TaobaoAd +0.0009，TAAC +0.0036，KuaiRand +0.0266 AUC。
- LENS在KuaiRand上超过DIN +0.0434 AUC，在稀疏场景优势显著。
- 消融表明TCQG和TCPB互补，TCPB在中等/稀疏密度下贡献主要增益。
- 交叉骨干可移植性验证了设计的分层性与非架构绑定。

## 值得记住的一句话
交互粒度不是固定的架构选择，而是一个可分层的设计维度：通过跨骨干可移植的QueryPos位置先验和LENS目标条件残差，可以在不破坏原始计算流的前提下递归地恢复候选特异性。
