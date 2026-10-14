---
title: Kwai Summary Attention V2 Technical Report
title_zh: 快手摘要注意力 V2 技术报告：C-KSA 与 S-KSA
authors:
- OneRec Team
- Chenglong Chu
- Guohong Mu
- Guowang Zhang
- Hao Peng
- Hui Wang
- Jian Liang
- Jiangxia Cao
- Jiao Ou
- Jiaxin Deng
affiliations:
- Kuaishou
arxiv_id: '2610.18654'
url: https://arxiv.org/abs/2610.18654
pdf_url: https://arxiv.org/pdf/2610.18654
published: '2026-10-13'
collected: '2026-10-14'
category: LLM
direction: 长上下文高效注意力 · 二级KV压缩与稀疏索引
tags:
- KSA
- KV cache compression
- sparse attention
- long-context LLM
- C-KSA
- S-KSA
one_liner: 在 Hybrid KSA 上新增 C-KSA 与 S-KSA，把 Summary 同时用作可二级压缩 KV 记忆和稀疏索引，128K 下 KV
  cache 减少 40.4%、prefill 达 1.51×
practical_value: '- 如果业务中已有或计划引入 Summary/landmark token 机制，可参考 C-KSA 的二级压缩：把每 km 个
  Summary KV 池化为 layer-local Meta entry，Summary 序列继续按原粒度前向传播，远程缓存按 ks*km 倍压缩。这样可以从已有
  Hybrid 模型低成本 retrofit，不用重新设计 chunk size。

  - S-KSA 的 block-level routing 比 token-level 索引候选数少 b 倍，适合在电商搜索/广告 Agent 的长候选列表、长商品序列中做稀疏读取；其默认参数
  b=4、remote budget K=4096、local window 1024 可作为起步配置，block size 放大到 8 会明显掉点，需谨慎。

  - 如果只允许训练新模块，可冻结 backbone 做 module-only 适配：C-KSA 先对齐 attention 输出再全参微调，S-KSA 用 dense
  teacher 蒸馏 block 选择，18.5B tokens 即可接近 parent；block teacher 用 max pooling 不要用 sum
  pooling，后者会稀释 salient token 信号。

  - 注意失败模式：频繁词提取等全局聚合任务在 128K 下从 45% 跌到 26.67%。若业务需要跨长上下文做类目频次、属性统计等聚合型召回/排序信号，应保留
  dense 分支或额外聚合结构，不要完全依赖 sparse attention。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
Hybrid KSA-Full 架构里 Summary token 只作为低分辨率 memory，KSA 层的压缩粒度被 chunk size 绑死；Full attention 层虽然保留原文访问，但实际上大多数 token 无关紧要。这导致 KV cache 压缩不灵活，Full 层仍付出二次预填充成本。

## 方法关键点
- **C-KSA**：把每 km 个连续 Summary KV 通过 learned dimension-wise weights 池化为 layer-local Meta entry；Meta 不参与跨层前向，Summary 表示粒度不变。远程历史缓存压缩比从 ks 提升到 ks*km（8*128=1024）。加入 log km 注意力修正，避免局部窗口吸走过多的 softmax 质量。
- **S-KSA**：用现成 Summary 为每个 b-token block 生成 routing key，Lightning Indexer 选 top blocks，main attention 只读被选原文 KV + attention sink + local window；候选数比 token-level 索引少 b 倍，且不读压缩文本。
- **适配与 kernel**：保持 3:1 布局（三层 C-KSA + 一层 S-KSA），可从预训练 Hybrid KSA 直接 retrofit。C-KSA 先 module-only 对齐 attention 输出，再做全参适配；S-KSA 只用 module-only，以 dense attention 概率做 block 级 KL 蒸馏。Kernel 侧用 direct addressing、fused block scoring 和共享 tiled prefill。

## 关键结果
在 1.9B MHA 上，C-KSA+S-KSA 的 128K RULER mean 为 72.39%，接近 Hybrid KSA 的 72.61%，明显超过 Full 的 67.55%；128K 分数为 65.01% vs 65.35% vs 48.75%。128K 下 resident KV cache 从 Hybrid KSA 的 10.59 GiB 降到 6.31 GiB，减少 40.4%；prefill 吞吐达到 1.51× Hybrid KSA、2.16× Full；decode 提升 1.27×。4B GQA 模型上 RULER mean 84.15% vs Hybrid KSA 84.45%，验证了向更大模型和 GQA 的迁移。主要退化在频繁词提取：45.00% → 26.67%。

最值得记住的一句话：**Summary token 可以同时承担“可二级压缩的 KV memory”和“块级稀疏索引”两种角色，在不改变 Summary 布局的前提下 retrofit 已有 Hybrid 模型，实现大幅降 cache/提吞吐，同时接近 parent 的长上下文检索能力。**
