---
title: 'CONCORD-Rec: Catalog-Conditioned Modality Utility for Semantic-ID Diffusion
  Recommendation'
title_zh: 面向语义 ID 扩散推荐的目录条件模态效用模型 CONCORD-Rec
authors:
- Haopeng Jin
- Bingkang Shi
- Tao Yu
- Yifei Ma
- Hao Liu
- Hongzhu Yi
- Jinwen Luo
affiliations:
- Tencent
- University of Chinese Academy of Sciences
- Beijing University of Posts and Telecommunications
arxiv_id: '2611.23710'
url: https://arxiv.org/abs/2611.23710
pdf_url: https://arxiv.org/pdf/2611.23710
published: '2026-11-18'
collected: '2026-11-19'
category: GenRec
direction: 生成式推荐 · Semantic ID 多模态门控
tags:
- Semantic ID
- Diffusion
- Multimodal
- Modality gating
- Counterfactual utility
- Recommendation
one_liner: 用目录约束的 counterfactual utility 监督 token 级门控，在多模态缺失/冲突下提升 Semantic ID 扩散推荐质量
practical_value: '- **多模态排序/召回中的可靠性门控**：不要直接 concat 多模态特征后统一融合；可引入 base branch + bounded
  residual 的 logit 接口，缺失或冲突时自动退化到行为模型，避免误导信号在迭代 denoising 中放大。

  - **Catalog-conditioned utility 监督可迁移**：用跨折 teacher 在可行目录上计算“加入某模态前后的 target partition
  loss 差”作为 gate target，比直接蒸馏 token 概率更贴近目录消歧目标；适合电商标题/图片不一致、素材缺失等场景。

  - **低延迟 Semantic ID 解码**：用 inverted index posting lists 支持任意 mask 位置，解码时按完整 feasible
  item 成块提交代码，避免逐位置 argmax 生成无效 item 元组；配合可靠 gate 可在 1–4 步达到 16 步 uniform 质量，在线降 p95。

  - **评估协议要区分 missing/conflict**：建议构建 matched clean/missing/conflict 数据集，单独验证模态可靠性，而不是只看
  clean ranking。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
语义 ID（Semantic ID）生成式推荐常用离散扩散，但多模态内容并不总是有用：封面、标题、音频可能缺失、退化或语义冲突；固定融合权重和无约束 token gate 会把误导信号在迭代 denoising 中放大。核心问题是“可观察的模态”与“对当前候选集有预测价值的模态”并不等价。

### 方法关键点
- 冻结 content encoder + 可训练 projection/history pool；行为 Transformer 产生 h0 和 base logits。
- 对每个未解析 SID position，tokenwise gate 在 base slot 与 available modalities 上做 masked softmax；modality residual 通过 B tanh 限制在 ±B，保证干扰不无限放大。
- 离线监督：跨折 teacher 在同一 masked state 与 exact feasible catalog 上，对比含/不含某模态的 target code partition loss 差（Shapley coalition sampling），得到 signed utility；student 用 KL 拟合 detached target。
- 解码使用 inverted index posting lists 构造支持集，按 complete feasible item 成块提交，避免逐位置 argmax 产生无效语义 ID。

### 关键实验
- MicroLens-100K：clean +4.00%，30% missing +7.95%，30% conflict +14.63% NDCG@20。
- 机制替换证明 catalog-partition utility 优于 raw-token utility / score-substitution / whole-item gate / CMM-only distillation。
- 服务成本：4 步 NFE 达到 0.068798 NDCG@20 且 p95 16.25ms，对比 uniform 16 步 0.067000 / 51.00ms，质量 +2.68%，延迟降低 68.14%。

> 最值得记住：生成式推荐中的模态价值不是静态的，应以目录约束下的 counterfactual utility 动态分配有界残差，并始终保留行为模型 fallback。
