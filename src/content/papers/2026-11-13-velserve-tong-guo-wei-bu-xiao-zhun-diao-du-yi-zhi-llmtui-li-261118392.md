---
title: 'VelServe: Taming Decode Jitters in LLM Inference with Tail-Calibrated Scheduling'
title_zh: VelServe：通过尾部校准调度抑制LLM推理中的解码抖动
authors:
- Ishaan Datta
- Alind Khare
- Koushik Kumar Dey
- Ratnesh Jamidar
- Anand Kumar Singh
affiliations:
- Sprinklr
- Microsoft
arxiv_id: '2611.18392'
url: https://arxiv.org/abs/2611.18392
pdf_url: https://arxiv.org/pdf/2611.18392
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: LLM推理服务调度优化
tags:
- LLM inference
- latency SLO
- tail latency
- decode scheduling
- jitter
- prefill-decode
one_liner: 用自身迭代延迟的尾部分布校准每步解码携带的prefill量，提升SLO goodput 2.4-4.4倍以上。
practical_value: '- 在 LLM 在线服务中，不要只依赖平均延迟预测；测量自身 decode step 的尾部延迟（如 P99），为每个迭代预留
  headroom，防止罕见超时被长输出放大为大量 SLO 违反。

  - 对 TTFT SLO 按 prompt 长度分级：长 prompt 的 TTFT 截止时间通常更宽松，因此调度时可优先服务短等待或短 prompt 请求，把长请求延后但仍在
  SLO 内，提高吞吐。

  - 在 prefill-decode 拆解架构中，控制 prefill 接纳间隔，确保单个请求不会在多个慢接纳步骤上累积超过其 P99 目标，适合 Agent
  多步推理或长文本生成场景。

  - 将 SLO 转化为“允许延迟步骤的频率”这一可测量指标，动态调整 prefill 工作负载，比固定预算更鲁棒，可迁移到推荐系统在线推理网关的流量控制。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

## 动机
交互式 LLM 服务必须满足 TTFT 与 TBT 的 SLO。研究发现聚合与拆解服务中均存在 decode jitter：一次抖动会延迟 batch 中所有请求，而长回复可能有数百个 decode step，因此哪怕罕见超时也会造成大量 SLO 违反。SLO 感知调度器通常将 prefill 预算压到刚好满足平均 TBT，没有余量应对预测误差或主机停顿；拆解架构虽能稳定平均 TBT，但接纳新请求的 step 仍会延迟。

## 方法关键点
VelServe 是一个尾部校准调度器。它测量自身迭代延迟的尾部，由 SLO 决定“迟到 step”允许的罕见程度，然后在每个 decode step 中留出足够 headroom，防止超时并满足目标 decode 延迟。这一 headroom 会降低 prefill 吞吐，因此 VelServe 优先服务等待时间最短的 prompt：当 TTFT 截止时间随 prompt 长度增长时，被延后的长 prompt 有更多时间余量。在 prefill-decode 拆解场景下，它间隔地接纳请求，确保没有请求等待的慢接纳 step 数超过 P99 目标允许的次数。

## 关键结果数字
在三种注意力机制与不同工作负载下，VelServe 在 Qwen3-8B 和 DeepSeek-V4-Flash 上达到最强基线 2.4–2.9 倍的 SLO goodput，在 DeepSeek-V2-Lite 上至少 4.4 倍；在八 GPU 拆解部署中，满足 SLO 的请求数达到 SOTA 基线的两倍以上。
