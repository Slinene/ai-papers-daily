---
title: 'Multi-Decoder OneRec: Controllable Generative Retrieval for Multi-Objective
  Industrial Recommendation'
title_zh: 多解码器 OneRec：工业推荐中可控的多目标生成式检索
authors:
- You Wang
- Zhao Liu
- Guoping Tang
- Yiqing Yang
- Shuo Su
- Jing Liu
- Naifu Zhou
- Xiaoyou Zhou
- Wei Jiang
- Jian Liang
affiliations:
- Kuaishou Technology
arxiv_id: '2607.26500'
url: https://arxiv.org/abs/2607.26500
pdf_url: https://arxiv.org/pdf/2607.26500
published: '2026-07-29'
collected: '2026-07-30'
category: GenRec
direction: 生成式检索 · 多目标配额可控
tags:
- Generative Retrieval
- Semantic ID
- Multi-Objective
- LoRA
- Constrained Beam Search
- Industrial Recommendation
one_liner: 用共享编码器+多 LoRA 解码器+约束束搜索，在统一生成式检索框架下实现多目标候选配额可控、梯度隔离与互补去重
practical_value: '- 多目标生成式推荐可借鉴该 **共享基座 + LoRA 专家 + 梯度隔离** 方案：保留一个通用的 General Decoder
  吸收曝光样本，每个业务目标（时长、互动、冷启）仅挂载低秩 LoRA 和独立的 BOS / SID 残差，新增目标不干扰主解码器。

  - **连续反馈的 RL 微调**值得尝试：对时长类目标，不做阈值二值化，直接用用户历史组统计标准化持续奖励，结合 L-GBPO + KL 参考正则，能保留偏好强度且不破坏通用
  SID 合法生成能力。

  - 多路解码时务必用 **约束束搜索（MD-CBS）** 避免配额浪费：不同目标解码器按优先级运行，已生成的前缀或完整 SID 在后续路由中被屏蔽，实验证明完整
  SID 级别屏蔽优于浅层前缀屏蔽，可恢复几乎全部有效候选数。

  - 若资源有限，可通过 **配额与束宽解耦** 实现成本控制：3 个 LoRA 仅增加 20% 参数量，推理时可通过减小单个解码器的束宽/配额来调节 FLOPs，配额向哪个目标倾斜即可定向提升该路召回。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
工业推荐系统通常为不同目标（时长、互动、冷启）维护独立召回通路并分配显式配额，但随着通路增多，建模、训练和推理日益碎片化。基于 Semantic ID 的生成式检索提供了统一方案，但单一解码器会耦合各目标策略，导致负迁移和候选重叠，无法兼顾统一建模与目标间配额控制。  

**方法**  
提出 **Multi-Decoder OneRec**，在共享基座上构建多个目标专用解码器：  
- **架构**：一个通用 Decoder（曝光通路）和多个轻量 LoRA 专家解码器（如 Long-View、Like、Watch-time），各自拥有独立 BOS 嵌入和 SID 嵌入残差。梯度仅流向对应 LoRA 参数，基座参数仅由曝光样本更新。  
- **训练**：离散目标用行为过滤的 NTP（SFT）；连续目标（如观看时长）用组内标准化相对奖励 + L-GBPO 策略优化，并以通用 Decoder 的 stop-gradient 分布作为 KL 正则参考，防止生成非法 SID。  
- **推理**：**多解码器约束束搜索（MD-CBS）** 按优先级执行各解码器，已产生的完整 SID 被后续路由屏蔽，最后通用 Decoder 补全配额至预算 B。  

**数据集与结果**  
公开了 **Kwai26** 基准（1.31B 记录，31.85M Item-ID，25.03M 有效 SID 项）。在相同预算 512 下，Multi-Decoder OneRec 比单解码器 OneRec 在曝光、Long-View、Like、Watch-time 的 Recall@512 上分别提升 1.69%、4.04%、5.54%、5.62%。生产 A/B 测试中，人均使用时长 +0.37%，7 日留存 +0.19%，分享设备数 +0.19%，冷启曝光 +2.09%。  

**核心结论**  
"统一生成式检索可以通过共享基座、LoRA 专家的梯度隔离训练和跨解码器的约束解码，实现显式的配额控制与互补候选生成，同时保留通用曝光能力。"
