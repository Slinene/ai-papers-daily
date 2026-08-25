---
title: 'ParaTempo: Efficient Parallel Reasoning via Temporal Confidence'
title_zh: ParaTempo：基于时序置信度的高效并行推理
authors:
- Xuteng Zhang
- Wenhao Zeng
- Xiaodong Gu
- Chao Hu
- Haotian Lin
- Yuling Shi
- Min Wang
- Beijun Shen
affiliations:
- Shanghai Jiao Tong University
- University of Pennsylvania
arxiv_id: '2608.16425'
url: https://arxiv.org/abs/2608.16425
pdf_url: https://arxiv.org/pdf/2608.16425
published: '2026-08-17'
collected: '2026-08-25'
category: Reasoning
direction: LLM 推理 · 分支级动态计算分配
tags:
- Temporal Confidence
- Parallel Reasoning
- Test-Time Compute
- Branch Pruning
- LLM Inference
- Training-Free
one_liner: 无需训练的异步并行推理框架，用时序置信度驱动分支剪枝/早退/分叉/投票停止，降延迟 21.8-32.2%、token 18.1-30.3% 且精度持平
practical_value: '- 生成式推荐/Agent 多路径决策：可把“周期性探测答案分布 + 时序置信度”作为分支管理信号，替代 final consensus
  或局部 token confidence，更早识别低质分支；适合电商复杂 Agent 的规划/工具调用、搜索 Query 多路改写投票等在线场景。

  - 工程实现无需训练，异步不等待慢分支：对商品文案多版本生成、RAG 多路检索答案生成等，可借鉴“低置信剪枝 → 高置信早退 → 释放算力分叉新分支”的编排，降低
  token 量与 P99 延迟。

  - 时序置信度计算可复用：对每个分支按滑动窗口聚合最近 probe 的答案分布，度量 dominant answer 集中度，作为收敛预警/停止投票信号，比 token-level
  entropy 更稳定；在生成式推荐语义 ID 投票或用户意图多解评估中可试。

  - 停止条件可参考 confidence-weighted vote 集中而非全分支完成，适合需快速响应、长尾分支拖累明显的业务。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
并行推理能提升大推理模型可靠性，但成本随分支数与推理深度增长。既有控制信号（final-answer consensus、局部 token confidence、孤立中间探针）要么延迟、要么与推理进展弱相关或噪声大，难做分支级动态控制。

### 方法关键点
- 提出 temporal confidence：每个推理分支周期性地被探针请求 tentative answer 概率分布，量化最近若干中间探针向 dominant answer 集中的尖锐程度。
- 用这一单一信号驱动完整控制：低置信分支剪枝；持续 commit 到 dominant answer 的分支提前退休；释放的算力用于分叉新分支；当置信加权投票集中时全局停止。
- 训练-free、异步，分支间无需同步，按分支收敛情况自适应分配计算。

### 关键结果
在数学与科学推理基准上，平均延迟降低 21.8–32.2%，总 token 消耗降低 18.1–30.3%，同时保持竞争力精度；temporal confidence 对后续分支收敛的稳定性和预测力优于 token-level 与瞬时信号。
