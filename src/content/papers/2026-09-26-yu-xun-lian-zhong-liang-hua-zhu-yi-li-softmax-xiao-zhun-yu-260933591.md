---
title: Pretraining Transformers with Quantized Softmax in Attention
title_zh: 预训练中量化注意力 Softmax：校准与直通梯度设计的影响
authors:
- Shangzhen Zhu
- Muyan Hu
- Tomasz Kozlowski
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2609.33591'
url: https://arxiv.org/abs/2609.33591
pdf_url: https://arxiv.org/pdf/2609.33591
published: '2026-09-26'
collected: '2026-09-30'
category: Training
direction: 低精度注意力 Softmax 训练
tags:
- quantized softmax
- straight-through estimator
- low-precision training
- attention
- calibration gradients
- pretraining
one_liner: 系统研究量化 softmax 前向与反向规则对预训练稳定性的影响，给出可复现的设计选择
practical_value: '- 工业推荐/Agent 里若对 Transformer 做 QAT 或量化 softmax 部署，不要用 `.detach()`
  隔离 calibration 统计量（row max/min）；必须让 row extrema 反向传播，否则训练前 25-30M tokens 看似正常，之后
  loss 突然恶化，末尾可差 0.65-3.07 nats。零和投影不能修复。

  - 做 hard rounding 量化时，优先 Prob-STE（在归一化后概率上放 STE），或校准从 MinMax 换成 fixed window to
  max（FWM）。在 K=4、124M/2.5B tokens 下 MinMax+Weight-STE 差 softmax 0.89 nats，而 FWM+Prob-STE
  只差 0.019；K=16 时 FWM+Weight-STE 差 0.004。

  - 如果允许可微实现，优先 LERP（分段线性插值）而非 Nearest hard rounding；K=4/16/32 在 2.5B tokens 都能收敛到
  softmax 0.005 nats 以内。

  - 评估时必须用训练时的 native forward；训练后替换成 exact softmax 会使 gap 扩大，LERP K=2 从 +0.005 跳到
  +1.814 nats，说明权重已经依赖训练算子。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：低精度 Transformer 训练已把线性层和 attention matmul 量化到 FP8/FP4，但 softmax 的指数和行归一化往往保持 FP16/FP32。能否把 softmax 也量化到粗粒度而保持预训练质量？这一问题不仅影响前向近似误差，还决定训练梯度，因为反向规则会塑造模型学到的分数几何。

方法：论文提出 K-interval attention 家族，三个设计轴：
- 校准：MinMax（按行内 min/max 布网格）vs FWM（固定窗口锚定 row max，窗口外置零）。
- 重建：LERP（分段线性插值）vs Nearest（硬舍入到最近网格中心）。
- 直通代理位置：Weight-STE（未归一化权重上）vs Prob-STE（归一化概率上）。
推导了含校准统计量（row extrema）的反向规则，并指出校准梯度必须保留；detach 行列极值会破坏 shift invariance 所蕴含的零和恒等式。

关键实验：GPT-2 结构 124M/1B，主要 FineWebEdu-3B，WikiText-103 等。124M@2.5B tokens：
- LERP K=4/16/32 最终与 softmax 差 ≤0.005 nats；FWM–Weight K=16 +0.004。
- MinMax–Weight K=4 差 +0.89 nats；MinMax–Prob K=4 +0.061；FWM–Weight K=4 +0.043；FWM–Prob K=4 +0.019。
- detach 校准梯度同前向但反传不完整，LERP K=32 延迟到 30M tokens 才分离，最终 +0.737 nats；仅恢复零和投影不能修复。
- 下游任务：大 loss 条件在 6 个 benchmark/7 配置上一致变差（MinMax–Weight K=4 掉 3.9–19.4 pp）；小 loss 条件差异方向不一，不能仅凭 NLL 等价保证下游一致。

最值得记住的一句: softmax 量化的失败不取决于前向近似本身，而取决于其反向规则是否携带正确的校准梯度；同一 hard forward 会因 Weight/Prob STE 与 MinMax/FWM 组合产生 0.02 到 0.89 nats 的训练差距。
