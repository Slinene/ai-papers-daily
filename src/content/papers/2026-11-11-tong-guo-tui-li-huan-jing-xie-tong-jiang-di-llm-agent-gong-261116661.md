---
title: Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment
  Coordination
title_zh: 通过推理-环境协同降低 LLM Agent 工作负载批次完工时间
authors:
- Wei Feng
- Meiling Chen
- Boxiao Chen
- Lu Liu
- Bin Zi
- Libin Ye
- Xingyu Lu
- Lei Xu
- Jun Zhou
affiliations:
- Ling Team, Ant Group
arxiv_id: '2611.16661'
url: https://arxiv.org/abs/2611.16661
pdf_url: https://arxiv.org/pdf/2611.16661
published: '2026-11-11'
collected: '2026-11-17'
category: Agent
direction: Agent 批次推理调度优化
tags:
- Makespan Optimization
- KV Cache
- Inference Scheduling
- Agent Workloads
- GPU Memory
- Trajectory Routing
one_liner: 协同优化推理与环境调度，使 LLM Agent 任务批次完工时间降低 10.4%–65% 且评估分数保持一致
practical_value: '- 在批量跑 agent 评测、合成数据或 RL rollout 时，用批次 makespan 替代单请求延迟作为优化目标；将环境执行与推理调度解耦，并采用进度感知调度（如
  CAAS）优先处理长链任务，可显著缩短长尾。

  - 参考 workload-based resource model 动态调整 GPU 显存在 KV cache 与 recurrent state（如混合模型或长序列
  RNN）之间的分配，并结合 sample concurrency 控制并行度，避免重计算带来的额外时延。

  - 利用 trajectory-aware routing 对相似轨迹/前缀做 KV cache 复用，可迁移到推荐系统中相似 prompt（如相似用户画像、商品描述模板）的批量推理，提升吞吐。

  - 评估优化效果时可用 controlled replay 将环境响应与耗时录制后回放，隔离推理与调度变量，便于离线归因和快速消融。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM agent 训练开发流程中的 benchmark 评估、合成数据生成、RL rollout 常需批量执行 agent 任务，下游阶段等待整批完成，因此批次 makespan 比请求级延迟更影响开发效率。

**方法关键点**：
- 针对混合 LLM，建立 workload-based resource model，指导 GPU 显存在 KV cache 与 recurrent state 之间分配，并给出参考 sample 并发度，以并行换吞吐同时控制重计算。
- 采用 trajectory-aware routing 和 scheduling，提升前缀缓存复用并平衡 worker 负载。
- 在环境容量受限时，将样本准入与环境执行解耦，引入 Chain-Advancing Action Scheduling (CAAS)，基于已观察进度优先调度长链，缩短批次尾部。
- 通过 controlled replay 结合真实推理与录制好的环境响应和时长，支持对各项优化做独立消融。

**关键结果**：在 BFCL、SWE-bench Multilingual、WideSearch、MCP-Atlas 四个 benchmark 上，用 Ling-3.0-Flash 与 Ling-3.1-Flash 实测，makespan 降低 10.4%–65.0%，评估分数保持对齐；方法已用于 Ling-3.x 系列模型训练与评估工作流，加速模型迭代。
