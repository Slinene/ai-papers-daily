---
title: 'SHARP: Semantic Hierarchical Agentic Reasoning for Next POI Prediction with
  Dynamic Memory'
title_zh: 语义分层智能体推理与动态记忆的下一兴趣点预测框架 SHARP
authors:
- Yuhang Zhan
- Silin Zhou
- Zhuo Chen
- Haoxiang Lei
- Yunren Feng
- Lisi Chen
- Shuo Shang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2611.14220'
url: https://arxiv.org/abs/2611.14220
pdf_url: https://arxiv.org/pdf/2611.14220
published: '2026-11-10'
collected: '2026-11-11'
category: RecSys
direction: 下一兴趣点预测 · 语义分层 Agent
tags:
- Next POI Prediction
- LLM Agent
- Semantic ID
- Dynamic Memory
- Time-aware Graph
- RQ-VAE
one_liner: 分层智能体先预测类目再引导语义 POI 打分，结合动态记忆与时间条件转移图提升预测
practical_value: '- **分层 LLM 预测 + 打分器**：让 LLM/Agent 只预测粗粒度类目（<100个）而非海量具体 item，避免直接输出
  item id；类目预测作为特征引导后续打分模型。可迁移到电商推荐：先预测用户意图类目，再在类目内用语义向量做召回/排序。

  - **动态轨迹记忆 Bank**：用一个小 Agent 把历史轨迹定期压缩成结构化 profile + recent state，保留长期偏好同时将 token
  开销从线性增长降到约 7k 稳定，节省 86-92% token。电商长行为序列建模可借鉴：维护可更新的用户摘要，避免每次喂全量历史。

  - **时间条件转移图**：显式构建 global + week-type + hour-bin + joint 多粒度类目转移图，用 graph retrieval
  tool 把当前时间条件下的转移概率作为 prompt 信息，避免全局聚合掩盖时段性行为。电商可构建类目-时段转移图，提升时令/大促推荐的可解释性。

  - **RQ-VAE Semantic ID 但不用生成式解码**：用 RQ-VAE 学 item 语义表示，关键是用选中的 codebook 向量拼接后过 encoder
  得到连续表示，而非直接用离散 code 序列做 autoregressive 生成；保留语义且可端到端梯度回传。生成式推荐可参考：用 semantic ID 但下游用向量打分，降低生成错误。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
下一兴趣点预测面临三个难题：LLM 的语义推理与具体 POI 映射困难；用户移动模式随时间变化，完整历史会超出 LLM 上下文；全局转移图平滑了特定时间条件下的转移规律。

## 方法关键点
- **分层智能体框架**：Trajectory Memory Agent 维护动态记忆，包含长期 profile、近期 context state 和个人统计；只增量更新 profile，避免每次处理完整历史。
- **多粒度时间感知类目转移图**：构建 global、week-type、hour-bin 及 joint 四类图，显式提供当前时间条件下的类目转移概率，供 Agent 和 POI predictor 使用。
- **类别预测引导 POI 预测**：Category Predict Agent 基于记忆、目标时间和图信息预测 Top-K 类目；后续 POI predictor 以类目预测为引导，而非让 LLM 直接输出 POI。
- **RQ-VAE 语义 POI 表示**：用 Item2Vec + 结构化特征编码后经 RQ-VAE 离散化为 SID，但下游使用选中的 codebook 向量经 Semantic Encoder 得到连续表示，并与 POI predictor 联合端到端优化。

## 关键结果
在 NYC、TKY、CA 三个数据集上与 12 个 baseline 对比，SHARP 相较最强 baseline CoMaPOI 平均提升 Acc@5 5.29 个百分点、Acc@10 4.52 个百分点；相对 Acc@5 提升分别为 6.07%、14.82%、21.45%。动态记忆使 token 消耗稳定在约 7k，较 Full History 节省 86.14%-91.86%，同时类目 Acc@5 比只用当前轨迹提升 10.11-12.70 个百分点。消融显示移除动态记忆对 Acc@10 影响最大，下降 4.05-6.32 个百分点。

## 最值得记住的一句话
让 LLM 预测粗粒度意图类别并作为引导信号，比让它直接预测具体 item 更稳；配合可端到端优化的 semantic item 表示，能有效连接语义推理与具体推荐。
