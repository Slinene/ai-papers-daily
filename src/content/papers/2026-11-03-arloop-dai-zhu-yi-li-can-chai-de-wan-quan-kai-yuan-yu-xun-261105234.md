---
title: 'ARLoop: Fully-Open Pre-trained Looped Transformers with Attention Residuals'
title_zh: ARLoop：带注意力残差的完全开源预训练循环 Transformer
authors:
- Yuekun Yao
- Yupei Du
- Dawei Zhu
- Huan Sun
affiliations:
- The Ohio State University
- Saarland University
arxiv_id: '2611.05234'
url: https://arxiv.org/abs/2611.05234
pdf_url: https://arxiv.org/pdf/2611.05234
published: '2026-11-03'
collected: '2026-11-04'
category: Training
direction: 高效 LLM 预训练 · 循环 Transformer
tags:
- Looped Transformers
- Attention Residuals
- Pretraining
- Sliding-Window Attention
- Parameter-Efficient LLM
- Recurrent Depth
one_liner: 提出 ARLoop，用滑动窗口深度注意力改进循环 Transformer，1.2B/0.5T 模型超过 Huginn-3.5B 并接近 Qwen3.5-2B
practical_value: '- **循环 Transformer 是低成本 LLM 基座的可选路线**：如果你的业务要用 LLM 做 Agent/生成式推荐，但
  GPU 预算有限，ARLoop 这种「共享层 + 多次 recurrence」的架构可以显著降低参数量，同时保留较深的有效计算图；尤其数学/代码类推理任务收益明显。

  - **滑动窗口深度注意力是可直接复用的 trick**：在循环结构中，每个子层只用 embedding + 最近 3 个 residual block 做深度注意力，比全量历史更省显存/带宽，吞吐损失约
  10%，但效果不降反升；这适合你自研深层共享模型时直接套用。

  - **固定 recurrence 训练，推理时不要超过训练最大值**：论文发现动态 recurrence 不如固定值；推理时 recurrences 超过训练最大值也无法继续涨点。线上
  serving 时可以把最大 recurrences 固定到训练值，避免无效计算。

  - **Value residuals 对深层循环模型稳定性很重要**：尤其搭配 Sandwich Norm 时，没有 value residuals 会出现表示坍塌、训练失败；如果你自己训练很深的共享层模型，可以加入
  gated token embedding 注入来稳定训练。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
循环 Transformer 通过反复复用同一组 transformer 层来增加有效深度，能在不增加参数量的情况下扩展计算。但标准 PreNorm 残差把历史深度信息以固定单位系数累加到单一残差流，缺少对不同深度中间表示的选择机制；已有残差设计多停留在小规模验证，缺少真实 LLM 预训练、数学/代码等复杂生成任务的证据。

**方法关键点**  
- **ARLoop 架构**：在每个有效子层，用可学习 query 对残差源做深度注意力聚合，替代 PreNorm 的单位系数累加；残差源按块组织成 block attention residuals，降低存储和计算开销。
- **滑动窗口深度注意力**：只保留 input embedding 和最近 W 个 residual block（默认 W=3），循环 Transformer 中够用，且在较大 recurrence 下比全历史更好；这与标准 Transformer 中滑动窗口反而降低收益的结论相反。
- **训练策略**：采用固定 recurrence 训练，优于动态 recurrence；大规模模型使用 SmolLM 风格多阶段数据配方、GQA、SwiGLU、4096 context。

**关键结果**  
控制实验中，140M/370M 模型上 ARLoop 的验证 PPL 一致低于 PreNorm、Sandwich-Norm、DeepLoop、Parcae；140M 且 R=5 时 PPL 15.84 vs PreNorm 16.34。真实预训练下，0.6B/180B tokens 的 ARLoop 比 PreNorm 在 GSM8K 上 +5.2、MBPP 上 +3.1；1.2B/0.5T tokens 的 ARLoop 在全部 8 个 benchmark 上超过 Huginn-3.5B，并接近 Qwen3.5-2B，例如 GSM8K 63.1 vs 60.6。分析显示，深度注意力权重集中在近期 block，跨 recurrence 残差块余弦相似度很高，支撑滑动窗口设计。

最值得记住：循环 Transformer 中，近期 3 个残差块 + embedding 就够，不必保留全量深度历史，这让参数效率与训练/推理开销可以兼得。
