---
title: Memory Attention
title_zh: 记忆注意力：用token索引记忆替代value投影
authors:
- Jiale Kang
arxiv_id: '2609.28399'
url: https://arxiv.org/abs/2609.28399
pdf_url: https://arxiv.org/pdf/2609.28399
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: 注意力机制 · token memory
tags:
- Memory Attention
- Token Memory
- Value Projection
- CPU Offloading
- Language Modeling
- Attention
one_liner: 提出Memory Attention，以token索引记忆加上下文key构造value，支持归一化折叠与CPU卸载，提升语言建模和下游性能
practical_value: '- 将 token-indexed memory 放到 CPU/SSD 并 prefetch 的思路，可直接迁移到电商/广告场景的大词表、item
  ID、Semantic ID 等 embedding 存储，降低 GPU 显存占用，适合线上推理降本。

  - 用「key + norm(memory)」构造 value 替代独立 value projection，可减少参数和计算；在生成式推荐或用户序列建模中，可以尝试用静态
  item/token memory 与上下文 key 相加，保留个性化同时降低 FLOPs。

  - 推理时把归一化折叠进 embedding table 的工程技巧，能减少 per-token 计算步骤，对高 QPS 的搜索/推荐在线服务有直接参考价值。

  - 论文核心面向 LLM 预训练，业务迁移前需在推荐或 Agent 场景重新验证：token 静态表示对非语言 ID 的适用性、以及 memory 规模与显存/延迟权衡仍需实验。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

## 动机
标准 self-attention 的 value 来自上下文 hidden states，许多 token 内容可跨上下文复用，却被重复计算；同时现有 lookup-based 方法（Value Embedding、DeepEmbed、PLE、STEM、Engram）主要做容量补充，而非替代已有计算。作者研究：能否用 token-indexed memory 替代专用 value projection？

## 方法关键点
提出 Memory Attention (MA)，将 value 构造改为：

V = K + Norm(M)

其中 M 是按 token ID 查表得到的 layer-specific token memory，K 来自上下文 key，Norm 是归一化。memory 提供 token 静态表示，key 保留上下文依赖。推理时归一化可以折叠进 memory table，value 构造退化为 lookup + 加法。此外，token-indexed 检索天然支持 CPU offloading + prefetching，可进一步降低 GPU 参数存储。

## 关键结果
在匹配训练 token 预算、并增加 memory 参数的前提下，跨多种 attention 配置实验显示：语言建模困惑度改善，平均下游任务性能提升。说明用显式 token memory 替代部分 attention 计算，在扩大容量同时保持甚至提升质量是可行的。
