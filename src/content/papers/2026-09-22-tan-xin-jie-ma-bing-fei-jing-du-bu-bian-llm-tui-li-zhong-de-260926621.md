---
title: 'Greedy Decoding Is Not Precision-Invariant: Cross-Precision Output Divergence
  in LLM Inference'
title_zh: 贪心解码并非精度不变：LLM 推理中的跨精度输出分歧
authors:
- Gaoyuan Du
- Anam Nawaz Khan
- Rex Zhou
- Xiaoyang Liu
- Deepayan Chakrabarti
- Fnu Suya
- Xueping Li
affiliations:
- University of Tennessee, Knoxville
- University of Chicago
- Amazon
- University of Texas at Austin
arxiv_id: '2609.26621'
url: https://arxiv.org/abs/2609.26621
pdf_url: https://arxiv.org/pdf/2609.26621
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: LLM 推理 · 精度一致性
tags:
- greedy decoding
- precision
- FP16
- BF16
- LM head
- inference
one_liner: 证明 BF16/FP16 下贪心解码会系统性分歧，提出低 margin 触发 FP32 LM head 重算，一致性提升 22–36pp 且延迟开销
  <4%
practical_value: '- 线上 LLM 推理要显式固定 dtype：BF16 与 FP16 不能视为等价，尤其 greedy decode 用于召回/排序/文案/query
  改写时，跨精度差异会造成离线在线或 A/B 的隐性不一致。可在服务配置中锁死 MatMul/attention/lm_head 精度，并用固定 prompt 集做跨精度
  diff 测试。

  - 如果需要在低精度下保持与高精度输出一致，不要全模型 FP32 重算；可移植 selective FP32 lm_head recomputation：仅当
  top-2 logit margin 低于阈值时用 FP32 重算 lm_head，低 batch 单流下延迟 <4%，一致性显著提升。可封装成 inference
  wrapper 或 engine option。

  - 注意适用边界：batch size >= 8 或端到端 FP8 下 body 误差主导，该方法失效；不要把它当作确定性保证。限流/批处理场景需要单独评估。

  - 对 LLM 驱动的推荐/Agent pipeline，若输出 token 用于下游决策（商品 ID、工具调用、query 改写），低 margin token
  flip 会级联放大；可针对低 top-2 margin 的高风险样本做高精度重算或投票，并监控 margin 分布作为质量信号。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：业界常把 greedy decoding 视为确定性，但实际部署中 BF16 与 FP16 在相同硬件上会产生不同输出。这项工作用 6 个模型（1.1B–7B，覆盖 4 个家族，另在 12B 刻画）和 3 个 benchmark 评估，发现 49–100% 的 prompt 出现跨精度分歧；一个 token flip 会级联为轨迹级差异。

**方法关键**：通过误差传播分析发现 LLM body 的 22 层累积误差不能区分 flip 与 non-flip；分歧主要取决于 lm_head 处 top-2 logit margin 与 top-2 候选方向扰动的相对大小。基于此提出 selective FP32 lm_head recomputation：仅当 margin 低于阈值时用 FP32 重算 lm_head。

**关键结果**：5 个可检验干预预测全部命中，包括更大的 FP32 计算范围反而会降低一致性。低 batch（<=4）单流推理下，该方法在 A10G 上带来 +22–36pp exact agreement（L4/A100 为 +12–21pp），延迟开销 <4%；但 batch size >=8 或端到端 FP8 时收益消失，说明只是部分缓解，不能保证确定性。训练期精度稳定性可能是适用边界的关键因素。
