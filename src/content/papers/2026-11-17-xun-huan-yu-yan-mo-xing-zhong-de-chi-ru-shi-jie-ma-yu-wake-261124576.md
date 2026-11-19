---
title: Late Entry in Looped Language Models
title_zh: 循环语言模型中的迟入式解码与 Wake 验证
authors:
- Ziqi Jin
- Jiaxi Li
- Weiwen Xu
- Aixin Sun
arxiv_id: '2611.24576'
url: https://arxiv.org/abs/2611.24576
pdf_url: https://arxiv.org/pdf/2611.24576
published: '2026-11-17'
collected: '2026-11-19'
category: LLM
direction: 循环层推理加速 · Late entry/Wake 验证
tags:
- Looped LLM
- Late Entry
- Wake Verification
- KV Cache
- Inference Acceleration
- CUDA Graph
one_liner: 新 token 跳过浅层迭代直接进入最后 K 次循环，用深层缓存替代计算，配合 Wake 验证实现贪心精确与有损加速
practical_value: '- 若线上采用循环/共享层 LLM（尤其低参数、高循环深度模型），可把 late entry 作为默认解码策略：新 token
  直接进入最后 K 次循环，读深 KV cache，跳过浅层计算；相比 early exit，不牺牲上下文深度，且在同等预算下质量更高。

  - 需要严格与离线 T-pass 贪心解码对齐的场景（如搜索词生成、推荐理由、Agent 工具参数解析），用 tau=0 的 Wake verification
  可在单个静态 CUDA graph 内保持 greedy-exact，同时获得数倍吞吐提升，避免多套推理代码维护成本。

  - 若业务可容忍有损（如批量生成候选 query/话题再排序），用 tau=inf 直接 late entry 可获得更高加速；可先离线评估 margin 分布，选一个合适的
  tau 做 margin-gated verification，自动在质量与回滚率之间平衡。

  - 工程上借鉴“已提交 tokens 异步补齐全深度 pass”的做法：新 token 只走关键路径 K 次循环，而旧 token 在背景并行的 GEMM 中完成剩余
  passes，把串行循环深度移出关键路径；这对低延迟 Agent 多轮交互尤其有用。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：循环语言模型用共享层重复 T 次处理每个 token，参数紧凑但推理延迟随 T 线性增长；传统 early-exit 在浅层停止，缓存 KV 状态深度不足，损失模型容量。本文探索相反策略：新 token 跳过初始 passes，直接从深层上下文缓存进入最后 K<T 次循环。

**方法关键点**：late entry 通过轻量微调解决 entry 边界 hidden-state norm mismatch，使深层缓存替代跳过的 token-local passes。为避免等待构建深层缓存，候选块仅在最后 K passes 上验证，先前 token 在后续步骤后台补齐 passes 1→T，不增加额外串行调用。Wake verification 将完成的 T-pass wake state 投影到输出 GEMM，用 logit-margin tolerance tau 统一三档：tau=0 贪心精确 T-pass、tau>0 margin-gated 验证、tau=inf 非回滚有损。全部逻辑封装在单个静态 CUDA graph。

**关键结果**：Ouro-2.6B (T=4) 上，K=2 Wake 在 tau=0 达 5.2x 贪心精确加速（比 K=4 block 提升 26%），tau=inf 达 6.8x（在匹配速度下比 trained early exit 高 16.9 分）。Huginn-3.5B 扩展到 T=32/64 时，tau=0 加速 6.1x/8.4x，tau=inf 达 10.6–12.5x。
