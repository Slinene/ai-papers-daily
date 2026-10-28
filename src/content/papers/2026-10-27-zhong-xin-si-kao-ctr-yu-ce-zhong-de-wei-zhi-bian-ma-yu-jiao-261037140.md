---
title: Rethinking Positional Encoding and Interaction Granularity for CTR Prediction
title_zh: 重新思考 CTR 预测中的位置编码与交互粒度
authors:
- Xinxun Zhang
- Yuxiang Wang
- Xiaokai Zhou
- Jiayue Li
- Yi Li
- Yue Liu
- Jun Zhang
- Xiaoling Zhou
- Tieyun Qian
- Xiao Yan
affiliations:
- Wuhan University
- Tencent Inc.
- Peking University
arxiv_id: '2610.37140'
url: https://arxiv.org/abs/2610.37140
pdf_url: https://arxiv.org/pdf/2610.37140
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: CTR 预测 · 位置编码与交互粒度
tags:
- CTR prediction
- Transformer
- positional encoding
- temporal grouping
- behavior sequence modeling
- attention mechanism
one_liner: 提出 TRIP，结合目标感知的秩-时间位置编码与时间组因果交互，显著提升 CTR 预测 AUC
practical_value: '- 在用户行为序列建模中，不要盲目使用标准位置编码（如 learned APE、RoPE），很多情况下 NoPE 可能持平或更好；但结合序列
  rank 与目标相对时间（target-relative time）的编码能稳定提升，低秩分解可大幅减少参数（3.8–21.6×）。

  - 将行为序列按距当前请求的时间间隔分组（对数时间桶），组内做双向 attention，组间保持 causal，既捕捉短期兴趣又保留长期演化；组摘要压缩可降低
  6.3–32.8% 训练时间，且 AUC 不降反升。

  - 引入 masked item reconstruction 辅助任务（仅训练时启用），可增强行为表示的上下文学习，不增加推理成本。

  - 对时间偏置做密度校正（减去 λ log 频次），防止高频时间桶主导注意力，在电商/广告数据中尤其重要。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

现有 Transformer-based CTR 模型通常沿用 NLP 的 index-based 位置编码和 token 级 causal attention，但作者在 OneTrans 上实证发现：绝大多数位置编码并未超过 NoPE，而在 target-relative temporal group 内放开 causal 约束却能带来提升。这引出核心问题：CTR 预测到底需要什么样的位置编码和交互粒度？

## 方法关键点

- **Factorized Rank Encoding (FRE)**：将行为序列的 ordinal rank 用低秩分解表示，每个 rank 对应一组系数与共享基向量的线性组合，参数量远小于 full learned APE。
- **Target-Relative Time Encoding (TRTE)**：编码行为到当前目标的时间距离，采用对数时间刻度（粗到细），提供两种实现：
  - TRIP-B：可学习的 temporal potential 作为 attention bias，并带密度校正（减去 λ log 频次以抵消高频时间桶的注意力质量优势）。
  - TRIP-R：将时间差映射为 RoPE 旋转坐标，对 query/key 施加目标相对旋转。
- **Temporal Group-Causal Interaction (TGCI)**：按目标相对时间将历史行为分组，组内双向 attention，组间 causal attention；引入 masked item reconstruction 辅助任务；将组内行为平均池化为组摘要，供后续层建模兴趣演化，降低计算。

## 关键实验

在 KuaiRec、KuaiRand、TAAC、TaobaoAd 四个公开数据集上，TRIP-B 击败 11 个 baseline（包括 DeepFM、DIN、DIEN、OneTrans、MixFormer 等），AUC 平均相对提升 1.47%，TAAC 上最大提升 4.45%。位置编码迁移实验在 OneTrans、HyFormer、MixFormer 三个 backbone 上验证 FRE+TRTE 优于 8 种其他编码，最高相对提升 4.20%。消融实验证明 rank、target-relative time、密度校正、组内双向交互和重建任务均有效。

## 最值得记住的一句话

**对 CTR 预测而言，结合序列 rank 与目标相对时间的位置编码，并在目标相对时间分组内做双向交互，比传统 token 级 causal attention 更有效，也更高效。**
