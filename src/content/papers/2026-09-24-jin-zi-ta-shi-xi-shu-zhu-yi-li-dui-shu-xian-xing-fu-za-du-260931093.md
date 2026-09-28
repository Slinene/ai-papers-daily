---
title: Block Sparse Attention with Log-Linear Complexity
title_zh: 金字塔式稀疏注意力：对数线性复杂度
authors:
- Bohao Tang
- Zhen Qin
- Yuqi Pan
- Zheng Li
- Pengfei Liu
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- ByteDance Seed
arxiv_id: '2609.31093'
url: https://arxiv.org/abs/2609.31093
pdf_url: https://arxiv.org/pdf/2609.31093
published: '2026-09-24'
collected: '2026-09-28'
category: LLM
direction: 长上下文 LLM 稀疏注意力加速
tags:
- Sparse Attention
- Long Context
- Block Sparse
- Log-Linear Complexity
- Triton Kernel
- Top-K Selection
one_liner: PISA 用金字塔 Top-K 块选择 + LogSumExp 评分，把可训练稀疏注意力的选择复杂度从 O(N^2) 降至 O(N log N)
practical_value: '- 用户行为序列、商品文档、Agent 长记忆等长上下文场景，可以将 block sparse attention 的 Top-K
  选择换成 PISA 的层级候选缩小：长序列（>64K）下路由 latency 显著低于普通 BSA，适合海量长行为序列或长文档理解；短序列（<16K）仍用普通
  BSA 更划算。

  - 工程实现可借鉴两段式 kernel：训练/prefill 阶段先做 intermediate-level 路由，再把同一 leaf key block 的
  query 聚成 tile 复用 key IO，Qtile=4 时 64K+ 额外获得约 1.3× 加速；解码阶段用单 kernel 融合所有层级避免多次 launch，缓存
  mean pyramid 只更新当前 token 的祖先路径，均摊 O(log N)。

  - 块打分用 LogSumExp 而不用均值或均值+方差：LSE 保留更高阶信息，提升 Top-K 块选择质量和检索类/containment 任务准确率；在
  GQA 下按 query heads 求和 LSE 做共享块选择可复用，但要注意它和 full attention 的 head-mass 平均排序规则不完全一致。

  - 若业务中有 Agent/RAG 长候选集粗筛，可把“池化层级 + 每层 bounded Top-K 扩展”作为两阶段检索范式：先粗粒度过滤，再对少数候选精确打分，避免全量候选打分；训练时梯度只经过选中
  attention，离散选择不参与反传，可作为稀疏模块插入现有结构。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

长上下文 LLM 中 full self-attention 是 O(N^2)，block sparse attention 虽将 attention 计算降到线性，但 Top-K block selection 仍需对每个 query 扫描所有 key blocks，选择阶段仍是 O(N^2/C)，在超长序列上成为主要瓶颈。

## 方法关键点

- 构造 key 金字塔：最细粒度是 block size C 的 leaf blocks，向上逐层 mean pooling，合并因子为 2，形成 O(log N) 层；coarse-to-fine 选择从最粗层开始，候选集从 1 开始，每层对 bounded 候选集算分、Select Top-K、只扩展被选中块的 child，直到 leaf。
- 打分：leaf 块用 raw-key 的 exact LSE；中间块用 child mean summaries 的 LSE；消融中 PISA-1 用均值、PISA-2 用均值+方差，完整 LSE 效果更好。
- 复杂度：固定 K、g、C 与 head 维度，每 query 每层最多评估 gK 个候选，总选择复杂度 O(N log N)；解码均摊 O(log N)/步。
- Kernel：训练/prefill 用两段式，先级联路由不物化 QK 矩阵，再按 leaf block 聚合 query tile 复用 key IO；解码用单 kernel 减少 launch 开销；GQA 中同一 KV head 的 query heads 共享 block 选择。

## 关键实验

在 418M / 1.47B / 2.67B 三个 scale，100B tokens 4K 预训练 + 10B 16K CPT，对比 Full Attention、NSA、HiLS、BSA。语言建模 loss 与常识推理基本可比；六个 containment 检索任务平均精度在三个 scale 的稀疏方法中最高；2.67B RULER 长检索平均 acc 62.80，高于 BSA 54.99，低于 Full Attention 66.24；块选择质量 Recall@8 与 attention mass ratio 最高。

块选择 latency 上，4K-16K BSA 更快；但从 64K 起 PISA 反超，相对 BSA 在 64K / 128K / 256K 分别快 2.86× / 5.31× / 9.95×。

**最值得记住的一句话**：只有把 Top-K block selection 从全量打分改成金字塔逐层 LSE 候选缩小，可训练稀疏注意力的选择复杂度才能真正降到 O(N log N)，并在长序列上获得硬件层面的实际加速。
