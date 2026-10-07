---
title: 'HLA: Expressive Hybrid Linear Attention via Chunk-Wise Dynamic Mixing'
title_zh: HLA：基于分块动态混合的高表达混合线性注意力
authors:
- Zhuokun Chen
- Xi Lin
- Xiyu Wu
- Jiahao He
- Jianfei Cai
- Bohan Zhuang
affiliations:
- Monash University
- Zhejiang University
arxiv_id: '2610.05842'
url: https://arxiv.org/abs/2610.05842
pdf_url: https://arxiv.org/pdf/2610.05842
published: '2026-10-04'
collected: '2026-10-07'
category: LLM
direction: 高效长上下文注意力机制
tags:
- Linear Attention
- Long-Context Modeling
- Gated DeltaNet
- Query-Dependent Routing
- Chunk-Wise Attention
- Efficient Inference
one_liner: 将历史 chunk 表示为仿射转移并用查询相关门控动态混合，提升长上下文检索
practical_value: '- 对长序列用户行为/会话建模：可将历史按固定长度切 chunk，用 self-attentive pooling 得到 chunk
  代表向量，再基于当前 query/item state 计算 sigmoid 门控，稀疏选择相关历史 chunk；论文中 chunk size 256、pooling
  window 32 是最优 trade-off，可作为初始超参。

  - 工程上：HLA 用 chunk 级仿射转移 (A_j,B_j) 压缩历史，缓存规模为 N(d^2+Pd)，chunk=256 时比匹配 KV cache 省
  50%；推理时权重<0.1 直接置零且不重新归一化，可跳过零权重状态转移，适合长会话推荐或 Agent 记忆系统做稀疏检索。

  - 训练目标：用 effective support（Hill number）构造 L_budget/L_support，鼓励每个 query 只路由到少量历史
  chunk，提升推理稀疏性和长程泛化；业务上可只训练 router、冻结 backbone，低成本改造已有 GDN/线性注意力模型。

  - 局限：论文未评测 Agent 多轮工具调用、持续记忆等场景，且推理延迟增加约 10–19%；若用于长程 Agent 记忆或电商超长上下文排序，需自行补充多轮、跨任务、工具反馈评测。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

线性注意力通过把历史压缩为固定大小状态实现 O(1) 解码内存，但早期稀疏信息在长上下文中容易衰减或被覆盖。即使 Gated DeltaNet（GDN）有内容相关更新，历史 chunk 经过长链仿射转移后仍会逐渐丢失；MHLA 用固定 chunk mixing，无法根据 query 自适应。因此需要 query-dependent 的 chunk-level attention，在保持线性注意力效率的同时恢复长程稀疏检索能力。

## 方法关键点

- 将 GDN 的 recurrence 写成 chunk-wise affine transition：`S_j = A_j S_{j-1} + B_j`，完整 chunk 的效果由一个乘法转移 A_j 和加法记忆 B_j 精确表示。
- 对每个 completed chunk，用窗口 self-attentive pooling 得到 P 个代表向量 U_j；query 与代表向量的相似度通过 log-mean-exp 聚合，再用 sigmoid 得到每个历史 chunk 的独立权重 w_i,j。
- 不是简单地加权 chunk readout，而是用 w 在仿射转移中插值 identity：`S_i,j = [(1-w)I + wA_j] S_{i,j-1} + wB_j`，同时控制该 chunk 的加法记忆和对早期状态的变换。
- 训练时加 L_budget 与 L_support，用 effective support（Hill number）鼓励路由集中；推理时权重低于 0.1 置零且不重新归一化，实现稀疏 inference。

## 关键实验

在 Qwen3.5-base 0.8B–9B 上做 pretrained adaptation，只训练 routing/pooling 模块，freeze backbone。LongBench-V2 相对 Native GDN 提升 5.57/1.99/1.39/1.19 个百分点；RULER 13 任务平均提升 3.974/1.250/1.401/1.013 个百分点。其中 0.8B LongBench-V2 从 22.86 提升到 28.43。

在 1.3B from-scratch 设定下，同样 100B tokens、4K 训练 context，RULER 从 4K 到 32K 的提升逐步扩大：+0.83/+2.67/+3.07/+4.22 个百分点，32K 时从 3.65 提升到 7.87。S1 needle 任务在 8K/16K/32K 分别从 56.6/23.8/11.2 提升到 100/97/67.4。

Ablation 显示 chunk size 256 最优，pooling window 32 最优；chunk=256 时历史状态缓存比匹配 KV cache 省 50%。推理 prefill 延迟增加 9.8–14.9%，decode 增加 13.9–18.8%。

最值得记住的一句话：HLA 通过 query-dependent 地门控 chunk 级仿射转移，保留了线性注意力的固定状态高效解码，同时把长程稀疏检索能力大幅拉近 softmax attention。
