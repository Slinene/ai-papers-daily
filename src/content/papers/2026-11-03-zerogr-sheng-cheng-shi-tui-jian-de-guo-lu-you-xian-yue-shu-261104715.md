---
title: 'ZeroGR: Filtering-First Constrained Decoding for Generative Recommendation'
title_zh: ZeroGR：生成式推荐的过滤优先约束解码系统
authors:
- Xiangrui Yang
- Jiawei Yang
- Liang Zeng
- Daqian Ding
- Ziqian Liu
- Bing Tian
- Cheng Peng
- Yunfeng Zhao
- Fangyu Zhang
- Jiaqiang Liu
affiliations:
- The University of Hong Kong
- Peking University
- Kuaishou Technology
- Huazhong University of Science and Technology
arxiv_id: '2611.04715'
url: https://arxiv.org/abs/2611.04715
pdf_url: https://arxiv.org/pdf/2611.04715
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 生成式推荐 · SID 约束解码
tags:
- Constrained Decoding
- Generative Recommendation
- Semantic ID
- GPU Serving
- Beam Search
- Filtering Index
one_liner: 提出过滤优先的 GPU 约束解码系统，先滤除非法 SID 再算 logits，召回与先打分几乎一致且延迟最高降 9.9×
practical_value: '- 生成式推荐/搜索里如果采用 SID 或树约束解码，建议把 filtering 前置到 projection 之前：先查有效
  next tokens，再只对有效 token 计算 logits。论文在 MovieLens-1M 上验证先过滤与先打分返回物品重叠 99.90%，召回一致，但投影计算量可下降
  85%–99.95%。这基本可以无痛迁移到线上解码器，先上线 A/B 验证质量即可。

  - 过滤索引按解码步切片，并按各步有效候选密度混用稀疏/稠密表示：早期 dense 对齐 token 列，后期 sparse 只存有效 SID，且用 entry
  position 隐式表示 successor state，省掉 successor 数组和 item id 存储。对显存敏感、目录亿级 item 的场景可显著减少
  GPU 索引占用。

  - 执行层用“共享候选槽位 + hybrid projection”：每个 beam 固定槽位，过滤/打分/选择直接读写同一槽位，避免动态 prefix sum；每步用
  warm-up 在 full 与 selective projection 之间选最快，避免稀疏步不规则 kernel 反而拖慢。适合在 CUDA/Triton
  实现 SID 解码时复用。

  - 索引重建采用两遍 CPU 布局引导并行填充 + 双缓冲 pinned memory 异步 H2D 流式搬运，把重建延迟压到更新窗口内，且不与在线推理抢 GPU/带宽。电商
  item 目录频繁更新时可直接借鉴。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

生成式推荐（GR）用 SID 自回归生成物品标识，beam search 每步既要给候选打分（scoring），也要过滤非法序列（filtering）。传统 scoring-first 先对全部词表算 logits 再 mask，但有效候选密度极低：工业生成式搜索数据集中，从第 2 步的 14.29% 降到第 5 步的 0.05%，意味着 85.7%–99.95% 的投影计算被浪费。问题是，过滤优先是否安全？论文在 MovieLens-1M 上验证：先过滤与先打分返回物品重叠 99.90%，recall 几乎一致。于是核心挑战变成：如何在 GPU 上真正把“少算 logits”转化为低延迟。

## 方法关键点

- **Step-sliced filtering index**：索引按解码步切成 M1..ML，每步独立表示。根据有效候选密度选择 sparse 或 dense：稠密步用 token 对齐的 successor table；稀疏步只存有效 SID 数组和边界数组。稀疏映射用 entry position 隐式表示 successor state，省掉 successor 数组；最后一步不存 item id，显著降低 GPU 显存。
- **Shared-slot execution**：每个 beam 固定候选槽位，过滤、投影、归一化、top-k 选择共享同一槽位，避免跨 beam 的动态 prefix sum。选择性投影用 work queue 跳过空槽，hidden vector 只加载一次到 shared memory，warp 级做 dot product。
- **Hybrid projection**：每步在 dense+full、sparse+full、sparse+selective 三种组合中用 warm-up 选延迟最低者，适配不同稀疏度和 GPU/精度/批大小，避免稀疏步不规则 kernel 反而拖慢。
- **Layout-guided streaming construction**：CPU 两遍构造：第一遍按 LCP 计数确定各 fragment 布局，第二遍并行填充；双缓冲 pinned memory 异步 H2D 流式搬运，重建不与在线推理抢 GPU 算力或带宽。

## 关键实验

在 Search（近 10 亿条 5-token SID，18,432 输出头）、Watch（41.7 亿条 3-token SID，8,192 输出头）、Synthetic-7（2^30 条 7-token）上对比 Unconstrained、CPU trie、FlashTrie、STATIC。Search 上 batch 32 FP16 总解码 1.88ms，比 Unconstrained 快 9.1×；Watch 上比 CPU trie 最高快 205×；Synthetic-7 在 V=16K、batch 32 时比 Unconstrained 快 19.5×。索引显存最多省 74.5%，重建加快 278×。过滤+投影阶段贡献最大加速，最高比 CPU trie 快 120×。

最值得记住的一句话：目录约束在解码前就确定了要算哪些 logits，先过滤能让 GPU 推理成本随有效 token 数而非词表大小增长，且几乎不牺牲推荐质量。
