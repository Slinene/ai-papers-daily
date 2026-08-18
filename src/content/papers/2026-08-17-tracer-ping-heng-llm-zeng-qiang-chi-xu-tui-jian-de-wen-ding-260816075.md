---
title: 'TRACER: Balancing Stability-Plasticity-Cognitivity Trilemma for LLM Enhanced
  Continual Recommendation'
title_zh: TRACER：平衡 LLM 增强持续推荐的稳定性-可塑性-认知性三元悖论
authors:
- WooJoo Kim
- HyunSik Yoo
- JunYoung Kim
- JaeHyung Lim
- SeongKu Kang
- HwanJo Yu
affiliations:
- Pohang University of Science and Technology
- University of Illinois Urbana-Champaign
- Korea University
arxiv_id: '2608.16075'
url: https://arxiv.org/abs/2608.16075
pdf_url: https://arxiv.org/pdf/2608.16075
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: LLM 增强的持续推荐 · SPC 权衡
tags:
- Continual Recommendation
- LLM Enhancer
- Stability-Plasticity
- Semantic Representation
- LoRA
- LightGCN
one_liner: 提出 TRACER，通过 Procrustes 初始化、置信门控+LoRA 推理、梯度同步 guidance，在 LLM 增强持续推荐中同时缓解遗忘、适应与语义偏置
practical_value: '- 在持续推荐/流式更新中引入 LLM 语义 embedding 时，不要无脑 concat 或全量微调 adapter：建议按初始化/推理/损失三处分别设计约束。冷启动
  item/user 可用正交 Procrustes 将语义 embedding 旋转到已有 ID 协同空间，再做局部邻居校准，避免语义空间与协同空间坐标系不一致。

  - 线上 serving 用 LLM 语义特征时，可加 confidence gating + LoRA 低秩更新 adapter。按曝光频率门控：高冷实体更多注入语义，热门实体更多信任
  ID 协同；跨 stage merge LoRA residual、冻结 bias，防止语义主导 ID 学习。

  - 训练目标里做语义对齐时，先计算 rec loss 与 semantic guide loss 的实体级梯度 cosine；同向才开启 semantic guide，反向则切换为对上一轮参数的
  retrospective regularization（已有实体）或直接只学 rec（新实体）。这比固定权重蒸馏更能保护历史和新兴趣。

  - 评估 LLM 增强持续推荐时别只看整体 NDCG；建议补 BWT/TRG/SRT 类指标，分别监控历史遗忘、新兴趣适应、语义先验贡献，避免出现 KAR/LLM-ESR
  式语义过拟合而 TRG 很低的问题。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
持续推荐从流式交互中捕捉用户兴趣变化，但每阶段数据稀疏，ID embedding 更新不足。用 LLM 预计算语义表示做增强可解决稀疏，但 naive 注入会破坏稳定性（保留历史偏好）与可塑性（适应兴趣漂移）的平衡，并引入认知性（利用 LLM 语义先验）后形成 SPC trilemma。论文先通过 guidance / initialization / utilization 三类 enhancer 验证，发现它们分别偏向 stability / plasticity / cognitivity，naive combination 则放大语义主导。

## 方法关键点
TRACER 沿学习 workflow 设计三个模块：
- **Procrustes Projection (PP)**：初始化新实体时，用上一阶段已有实体求解正交 Procrustes，将 LLM 语义子空间旋转到协同子空间；再做局部校准，融合邻居 ID embedding，冲突时降低语义权重。
- **Confidence-gated Condensation (CC)**：推理时用 gating 输出 confidence 控制语义注入强度，最终表示 `[e; c φ(x)]`；adapter 用 LoRA，跨 stage merge residual、冻结 bias，限制语义主导。
- **Semantic Synchronization (SS)**：guidance 处计算 rec 与 guide 每个实体的梯度 cosine；同向开启 InfoNCE 语义 guidance，反向则已有实体做 retrospective regularization 锚定上一轮参数，新实体只学 rec。

## 关键实验
在 Amazon 四个类目 + Yelp 上评估，60% 数据做 base block，40% 分 3 个流式 block。baseline 包括 MF/LightGCN × {Full-Batch, Fine-Tune, ReLoop2, PISA} × {RLMRec, LLM2X, KAR, LLM-ESR}。NDCG@20 的 ACC 最高提升 **14.38%**（LightGCN/Yelp），BWT/TRG/SRT 全部最优；内存接近 No-Enhancer，训练更快。消融显示去掉 CC 后 SRT 显著下降，去掉 SS 后 BWT 明显下降，PP 对 TRG 关键。

## 最值得记住的一句话
LLM 语义先验不是直接注入越多越好，要在初始化/推理/优化三阶段分别做拓扑对齐、置信门控与梯度同步，才能让语义增强成为持续推荐的催化剂。
