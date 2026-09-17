---
title: How Lossless Is Lossless Speculative Decoding? The Role of Numerical Precision
  in Orthrus
title_zh: 无损推测解码真的无损吗？Orthrus 中数值精度的作用
authors:
- Ilya Koziev
- Leonid Sinev
- Ivan Oseledets
arxiv_id: '2609.15504'
url: https://arxiv.org/abs/2609.15504
pdf_url: https://arxiv.org/pdf/2609.15504
published: '2026-09-13'
collected: '2026-09-17'
category: LLM
direction: LLM 推理加速 · 数值精度影响
tags:
- Speculative Decoding
- Diffusion LLM
- Numerical Precision
- Orthrus
- Losslessness
one_liner: 独立复现验证 Orthrus 并行解码：BF16 下仅约 45% 轨迹精确匹配，FP32 则完全匹配，无损性依赖数值精度。
practical_value: '- 部署 LLM 加速推理（如 speculative decoding、并行解码）时，如果业务要求输出与原始 AR 模型完全一致（例如线上已审核的文案、推荐理由），必须检查数值精度（BF16
  vs FP32），否则可能出现轨迹不一致。

  - 验证推理加速方案时，不要只依赖下游任务指标（如 lm-eval-harness 分数），应单独评估轨迹等价性，防止下游指标的鲁棒性掩盖了一致性问题。

  - 论文发现匹配率与响应条件困惑度强相关：低置信度（高困惑度）的样本更容易出现不匹配，可在工程上针对高风险样本回退到 FP32 或原始 AR 解码。

  - 对于生成式推荐/Agent 场景，如果采用 BF16 推理并且追求确定性输出，建议在关键路径保留 FP32 或提高数值精度，同时建立数值精度影响的评估机制。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
自回归 LLM 解码受限于顺序生成，并行解码（如 Orthrus）试图通过混合自回归-扩散架构同时生成多个 token 来加速，并声称通过内部共识机制实现无损推测解码。但缺乏独立复现，尤其在不同数值精度下的实际损失程度未知。

**方法关键点**
作者独立复现 Orthrus：保持冻结 AR backbone，增加轻量 diffusion view 并行预测未来 token。在 BF16 和 FP32 两种精度下，对 1,190 个 prompt（覆盖 12 个领域）比较 Orthrus 输出与原始 AR 模型的精确轨迹匹配率，并考察匹配率与参考模型响应条件困惑度的关联；同时用 lm-eval-harness 评估下游任务表现。

**关键结果数字**
- BF16 推理时，精确轨迹匹配率仅为 45%（作者 checkpoint）和 43%（独立训练模型），远未达到完全无损。
- 匹配概率与响应条件困惑度强相关：模型越不确定的样本越容易出现轨迹分歧。
- 尽管轨迹不一致，下游 lm-eval-harness 基准未出现系统性退化。
- 改用 FP32 后，所有评估 prompt 均实现精确轨迹匹配，表明 Orthrus 的实际无损性高度依赖数值精度，且轨迹等价性与下游任务性能需分开评估。
