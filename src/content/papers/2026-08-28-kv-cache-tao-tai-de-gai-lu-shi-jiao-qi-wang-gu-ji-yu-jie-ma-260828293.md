---
title: A Probabilistic Interpretation of KV Cache Eviction
title_zh: KV Cache 淘汰的概率视角：期望估计与解码期校正
authors:
- Renato Geh
- Alex Chen
- Daniel Israel
- Aditya Grover
- Guy Van den Broeck
affiliations:
- University of California, Los Angeles
arxiv_id: '2608.28293'
url: https://arxiv.org/abs/2608.28293
pdf_url: https://arxiv.org/pdf/2608.28293
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM 推理 · KV cache 压缩
tags:
- KV cache
- eviction
- importance sampling
- LLM inference
- attention
- bias-variance
one_liner: 将 KV cache 淘汰形式化为期望估计问题，提出可纠偏的概率淘汰与解码期校正
practical_value: '- 部署长上下文 LLM 服务（Agent 记忆、商品描述、用户行为序列）时，现有 H2O/SnapKV 等确定式 top-k
  淘汰在特定任务上可能灾难性失效；改用论文的 probabilistic eviction + decode-time correction 能提升多任务鲁棒性，适合同一模型同时服务检索、问答、推荐解释等场景。

  - 工程迁移成本低：可把已有 score-based 淘汰策略改造成 proposal 分布（如 πH2O=normalize H2O scores），按 head/group
  采样并记录 counts，解码时用 Algorithm 1 的自归一化重要性采样校正，改动集中在 attention 计算，无需重训或改模型。

  - 温度缩放 τ 是简单可用的 bias-variance 旋钮：高压缩、低采样数时增大 τ 抑制方差，低压缩时保持 τ=1 降低偏差；可按业务 latency/quality
  目标做 per-head 或全局 budget 调优。

  - 全局压缩率分配可利用论文的采样数与 coupon collector 关系做预算分配，让不同层/head 自适应获得不同压缩率；GQA 模型需用 group
  内 mixture proposal 保持支持集一致。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机

KV cache 淘汰通常被当作启发式问题：根据 attention score 选 top-k 保留即可。但论文指出两个被忽视的问题：一是缺乏形式化，二是淘汰后分布被扭曲，解码时仍按保留项重新 softmax 会带来不可控偏差。因此需要从概率角度重新定义 KV cache 淘汰。

## 方法关键点

- **形式化与硬度**：将 KVEVICTION 定义为在压缩率 r 下选择索引集合 I 使注意力输出误差 ≤ ε；证明其 NP-complete，归约自 PARTITION。
- **概率解释**：attention 每行是一个 categorical 分布，输出就是 E[V]；KV 淘汰等价于从该分布做期望估计。
- **概率淘汰**：从 proposal 分布 π 采样 m 次，保留被采样到的 unique entries；相比 top-k 的零方差但无界偏差，概率淘汰在淘汰时刻更接近无偏。
- **解码期校正**：用 self-normalized importance sampling 矫正被淘汰项导致的分布形变；期望按淘汰前/后拆成两部分，前段用采样 counts 加权估计，后段精确计算。
- **与现有方法的关系**：H2O、SnapKV、TOVA、K-norm、StreamingLLM 都可看作零方差、无界偏差的确定性 top-k 估计器；其 score 可归一化成 proposal 分布。
- **方差控制**：温度 τ 调整 importance weights，τ=1 为原始校正，τ→∞ 接近不校正；用于在高压缩下降低方差。

## 关键实验

在 Llama3.2-3B 和 Qwen3-4B 上评测 LongBench 与 RULER 子集，对比 StreamingLLM、SnapKV、TOVA、H2O、K-norm。结果显示：

- 低到中等压缩率下，πmin-h 等概率淘汰 + 校正方案在平均分和 win score 上达到或超过 SOTA，尤其 πmin-h 在不同任务上最稳健。
- 高压缩率下，所有方法性能趋近，但概率淘汰仍具竞争力。
- MAE 实验表明，概率淘汰把 bias-variance 曲线显式化：低压缩时方差、偏差都低；高压缩时方差上升，通过温度 τ 可抑制方差。

最值得记住的一句话：现有 KV 淘汰方法本质是零方差但无界偏差的估计器，概率淘汰 + 自归一化重要性采样把淘汰变成一个可控制 bias-variance 的期望估计问题。
