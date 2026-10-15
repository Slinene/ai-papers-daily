---
title: Latent Compaction with Test-Time Training
title_zh: 潜在压缩与测试时训练：可训练 KV Cache 压缩
authors:
- Yingfa Chen
- Xingyu Shen
- Chaojun Xiao
- Xu Han
affiliations:
- Tsinghua University
arxiv_id: '2610.20582'
url: https://arxiv.org/abs/2610.20582
pdf_url: https://arxiv.org/pdf/2610.20582
published: '2026-10-14'
collected: '2026-10-15'
category: Training
direction: LLM 长上下文 KV cache 压缩 · 测试时训练
tags:
- KV cache compression
- test-time training
- long context
- attention distillation
- Latent Compaction
- LLM inference
one_liner: 将压缩 KV cache 视为可训练参数，用测试时训练拟合注意力与蒸馏，在 32× 压缩下 RULER 达 96.7%
practical_value: '- 商品详情页、用户长期行为序列、长评论等重复使用的长上下文，可离线预压成可训练 KV cache。模型权重冻结，线上多 query
  复用，适合推荐/搜索中大量候选文档场景；但注意论文只考核逻辑 KV-pair 预算，实际物理内存与速度需自行测评。

  - 测试时训练不需要下游真实 query：用 480 个通用 prompt 与 teacher 全量 cache 生成 rollouts，就能提供 attention
  与蒸馏监督。电商可以模板化商品属性、风格、摘要等通用问题，避免依赖真实用户日志。

  - 初始化组合可直接复用：KVZip+ 重建分数选 preserver（占 75% 效果最好）、teacher attention 选 anchor、farthest-first
  选 diversifier；ablations 表明 preserver 预算分配对准确率影响最大。

  - 若把压缩文档 cache 与后续 query cache 合并，必须按 log-normalizer 加权而不是等权平均，否则准确率几乎归零；attention
  bias 贡献有限但可保留。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文中 KV cache 随文档长度线性增长，注意力解码阶段内存带宽和显存压力大。已有方法多为选择原始 KV 对（eviction），或拟合注意力输出，但在 32× 以上激进压缩时检索精度快速下降。核心挑战是在问题未知的情况下，为文档保留足够信息以供后续任意查询。

### 方法关键点
- **初始化**：每个 layer/head 平均 B 个 slot，分为三类——preserver 由全局 KVZip+ 重建分数最高者组成（占总预算 75%）；anchor 由 teacher attention 分数最高者（占 anchor+diversifier 预算的 25%，含首 token）；diversifier 用 farthest-first traversal 选 key 距离最远者补满。
- **Stage 1 注意力拟合**：冻结 preserver，训练 anchor 和 diversifier 的 key/value/bias，逼近 full-cache 的 attention output 与 log-normalizer，均做标准化 MSE。监督 query 来自 480 个通用文档 prompt 的 teacher 前向。
- **Stage 2 端到端蒸馏**：放开全部条目，基于同样的 teacher rollouts 做蒸馏：将 teacher 概率分解为 top-20 token 和 tail 总质量，用 KL 匹配这两部分，再加一个对 teacher greedy token 的 LM loss。
- **推理合并**：压缩文档 cache 与后续 question/generated 的 KV 通过各自的 log-normalizer 加权合并，相当于一个统一 softmax，不能等权平均；每个 slot 还学习 attention bias 补偿 mass 变化。

### 关键结果
在 Qwen3-1.7B 上，RULER 16K 上下文 32× 压缩时，Latent Compaction 准确率 96.7%，KVZip+ 仅 40.0%；LongBench 在 16×/32× 下优于 KVZip+ 和文本摘要；Phonebook Lookup 16× 压缩平均 80.67%（4K 87.75/8K 83.75/16K 70.50），并迁移到 0.6B/4B/8B 和 MiniCPM5。消融显示：去掉 stage1 平均掉到 13.92，去掉 stage2 掉到 70.67，stage1 去掉 logZ MSE 掉到 36.50，推理时用等权平均仅 0.17。

> 最值得记住：把 KV cache 当成待训练的神经网络参数，先用重建/注意力/多样性混合初始化，再分两步拟合与蒸馏，即便完全不知道下游问题，也能大幅保住压缩后的检索准确率。
