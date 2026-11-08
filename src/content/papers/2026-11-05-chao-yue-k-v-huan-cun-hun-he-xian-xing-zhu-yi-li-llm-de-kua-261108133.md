---
title: 'Beyond K/V Caches: Cross-Model State Handoff in Hybrid Linear-Attention LLMs'
title_zh: 超越 K/V 缓存：混合线性注意力 LLM 的跨模型状态交接
authors:
- Jiacheng Cai
- Tao Zhang
- Siqi Liang
- Yun Dai
- Ziqian Zeng
affiliations:
- South China University of Technology, China
arxiv_id: '2611.08133'
url: https://arxiv.org/abs/2611.08133
pdf_url: https://arxiv.org/pdf/2611.08133
published: '2026-11-05'
collected: '2026-11-08'
category: LLM
direction: 跨模型状态交接 · 混合线性注意力
tags:
- cross-model state transfer
- linear attention
- KV cache
- prefill reuse
- Qwen3.5
- continuation calibration
one_liner: 统一迁移 FA K/V、REC、Conv 三类状态，通过功能校准实现跨模型免重复 prefill，16K 加速 21.9 倍
practical_value: '- **多模型路由/级联场景可直接借鉴状态交接思路**：如果业务中部署同 family 不同尺寸 LLM 做 cascading/routing，小模型已处理的长上下文无需让大模型重新
  prefill，可将小模型的 FA K/V、REC、Conv 状态通过 affine 映射和低秩增量合并迁移过去，减少切换成本。

  - **功能校准优先于状态重建误差**：不要只优化 REC 或 hidden state 的 MSE；应冻结目标模型，用 continuation 的输出 KL/候选分布校准适配器。该论文显示更低
  REC 重建误差反而可能提高 continuation KL，对任何需要迁移隐藏状态或蒸馏中间表示的方案都有警示。

  - **工程部署上可复用 LoRA 增量合并**：FA cache 映射可以用 rank-4 LoRA 训练增量后合并到基础 affine 权重，在线推理只做一次前向映射；REC
  修正则保留为一次条件前向计算，不参与每步自回归。这种 offline 训练、online 单次转换的拆分适合低延迟服务。

  - **边界一致性需要工程化保证**：FA/REC/Conv 与 position metadata 必须在同一 prefix boundary 安装，包括 KV
  长度、位置索引、mask；否则后续 target 计算会出现对齐错误。实现时建议建立统一状态 schema 与校验步骤。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
生产级 LLM 部署常通过 cascading/routing 平衡成本与质量，不同尺寸模型共享 family。切换模型时，目标模型需要对已有上下文重复 prefill，长会话下开销很大。现有跨模型状态迁移只覆盖 full-attention K/V caches；而 Qwen3.5 这类混合线性注意力模型还保留 recurrent state（REC）和 convolution history（Conv），且 Conv 会影响后续 REC 更新，扰动效果可超出卷积窗口持续存在。控制实验表明，REC 重建误差更低未必改善 continuation——因此需要面向目标模型可继续使用的状态交接。

**方法关键点**
- 统一迁移三类状态：FA K/V cache、REC 矩阵、Conv history，并保持 position metadata 在同一 prefix boundary 一致安装。
- FA cache：每个目标 FA 层选四个源支持层，K/V 分开 affine 映射；先 de-RoPE，映射后施加目标 RoPE；最终用 rank-4 LoRA 增量校准并合并到基础映射，在线只做一次前向。
- REC 映射：按 GDN Q/K head 分 16 组，每个目标 REC 层选四个源 REC 层，在设计矩阵坐标上做 8→3 的 grouped affine，不混合坐标或原生 head 组。
- 4B→27B 额外带状态条件 REC 校正：用所有 mapped target REC 的 row/col mean 构建全局 summary，经分块 alternating sum 和 LayerNorm 后过 affine+tanh 生成系数，再以最多 rank-2 的方向矩阵一次性修正 REC。
- Conv 对齐：每个目标 recurrent 层取对应源第一层，Q/K/V 分组做共享 channel affine mapping，四个 history slot 保持时间顺序，不跨 slot 混合。
- 功能校准通过冻结目标模型完成：使用 continuation 的 forward KL、数学 token CE、选择题候选分布 KL 等监督，而非只最小化状态重建 MSE。

**关键实验与结果**
在 ARC-C、HellaSwag、WinoGrande、MMLU、GSM8K 五个 benchmark 上评估 Qwen3.5-4B/9B → 27B 切换。4B→27B 平均 task retention 89.88%，9B→27B 94.11%，分别比最强 hybrid baseline CacheLink 高 3.56 和 7.10 个百分点；9B→27B 在 MMLU 上从 67.93% 提升到 88.22%。在 16K 合成上下文且 source cache 已就绪的情况下，handoff body latency 分别为 399.02ms 和 402.79ms，相对 target prefill 达到 21.66× 和 21.91× 加速（不计 source prefill、LM head 和生成）。诊断实验显示：仅恢复 REC 的 KL 为 0.00721，而恢复 Conv 为 0.07023；REC residual 将初始相对 MSE 从 1.00671 降至 0.28380，但 continuation KL 反而从 0.64829 升至 0.69142。

**最值得记住**：跨模型状态交接的核心不是重建误差，而是 continuation compatibility——通过冻结目标模型做功能校准，确保目标后续能有效利用转移状态并持续更新。
