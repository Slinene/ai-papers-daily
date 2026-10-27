---
title: Towards a Unified Framework of Optimal Input-Side Dimensional Configuration
  for Deep CTR Prediction
title_zh: 面向深度 CTR 预测的最优输入侧维度配置统一框架
authors:
- Chaohua Yang
- Fuyuan Lyu
- Xing Tang
- Dugang Liu
- Xiuqiang He
- Zhong Ming
affiliations:
- 深圳大学
- McGill University
- Shenzhen Technology University
arxiv_id: '2610.35695'
url: https://arxiv.org/abs/2610.35695
pdf_url: https://arxiv.org/pdf/2610.35695
published: '2026-10-26'
collected: '2026-10-27'
category: RecSys
direction: 输入侧选择 · 最优传输协调
tags:
- Deep CTR Prediction
- Input-side Selection
- Optimal Transport
- Feature Selection
- Embedding Pruning
- Sample Reweighting
one_liner: 用最优传输协调样本、特征、嵌入单元三层选择，联合配置输入侧信息提升 CTR 模型 AUC
practical_value: '- 在精排 CTR 模型上，不要只做单层优化：样本去噪、特征 gate、embedding 维度裁剪可共享一个信息路径联合搜索；采样保留比例约束
  + 细粒度稀疏正则能防止搜索坍缩。

  - 借鉴 search-and-retrain：搜索阶段用连续 gate/soft mask 学习配置，结束后硬化为 lookup table 再重训 backbone；线上推理只增加
  mask 查表，无额外打分开销。

  - 跨粒度选择冲突可用 selection-weighted Optimal Transport 协调：粗粒度选择作为总质量，细粒度归一化分配，用 cosine
  表示不相似度作为运输成本；比直接对 mask 做 cosine/KL 有稳定提升。

  - 样本 selector 只用于构造 retrain 集，不参与 serving，业务上可安全地用样本级去噪提升训练质量而不担心线上延迟。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
CTR 预测性能不仅依赖特征交互架构，还取决于输入侧信息配置。已有样本选择、特征选择、embedding 单元裁剪通常独立优化，只沿单一维度做选择；但它们本质都是对 embedding tensor 施加不同轴向上的 mask，且跨层存在依赖：特征被 mask 后其内部单元选择失效，高权重样本若特征被大量抑制则样本决策失效。仅靠共享 prediction loss 联合学习容易导致选择冲突，限制效果。因此需要显式协调样本、特征、embedding 单元三层配置。

## 方法关键点
- 统一配置路径：样本权重 s_i、特征 gate g_i、embedding-unit mask M_i 按信息流依次作用；特征/单元 gate 先用 annealed sigmoid 软化，样本 selector 基于配置后 tensor 打分。
- 跨层协调：引入 selection-weighted Optimal Transport 成本，覆盖 sample–feature、feature–unit、sample–unit 三条关系；粗粒度选择作为总质量 α，细粒度归一化分配 π，用 cosine 表示不相似度作为 ground cost，避免强制映射到同一支持集。
- 两阶段优化：搜索阶段联合优化 CTR loss、三级选择正则（特征/单元稀疏 + 样本保留比例约束 + entropy 二值化）和 OT 协调 loss；搜索后将连续 gate 以 0.5 阈值硬化为 lookup table，重训 backbone。

## 关键结果
在 Avazu、Criteo、MovieLens-1M、AliCCP 四个数据集上，配合 DNN、DeepFM、DCN、AutoInt、FinalMLP 五种 backbone，OptIDC 均高于单层选择与无协调的 IDC。Avazu 上 DNN backbone：Backbone AUC 0.7893，IDC 0.7915，OptIDC 0.7930；Criteo 上 Backbone 0.8097，IDC 0.8110，OptIDC 0.8113。Ablation 显示两层联合优于单层，加入对应 OT 后进一步提升，移除任一 OT 项均下降。效率方面，Avazu 每 batch 推理耗时 0.0041s，与单层选择方法相当，总训练时间 2575s，低于 OptEmbed/AutoDim。

最值得记住：用 selection-weighted OT 把不同粒度选择统一成 coarse mass + fine allocation 的运输成本，能在保留各层语义的同时显式协调输入侧配置。
