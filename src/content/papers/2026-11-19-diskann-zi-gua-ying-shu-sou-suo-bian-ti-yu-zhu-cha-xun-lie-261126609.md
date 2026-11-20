---
title: Variants of Beam Search for DiskANN
title_zh: DiskANN 自适应束搜索变体与逐查询列表大小预测
authors:
- Viraj Agrawal
- Kirankumar Shiragur
affiliations:
- Microsoft Research India
arxiv_id: '2611.26609'
url: https://arxiv.org/abs/2611.26609
pdf_url: https://arxiv.org/pdf/2611.26609
published: '2026-11-19'
collected: '2026-11-20'
category: Other
direction: 近似最近邻搜索 · 自适应束搜索
tags:
- ANN search
- DiskANN
- adaptive beam search
- query cost allocation
- vector retrieval
- beam predictor
one_liner: 统一 ABS 在 α-可达图上的近似保证，并设计逐查询 beam width 预测器，SSD 查询延迟最多降 29.6%
practical_value: '- 把固定 beam width/搜索预算改成「短 pilot 搜索 → 提取轨迹与距离特征 → 预测该 query 的收敛难度
  → 继续原搜索」，pilot 不重启、直接扩容；适合推荐/RAG 高并发向量检索降本。

  - 离线训练时不要直接回归 recall 或延迟，而是用 Lagrangian relaxation 生成每个 query 的最优 L 标签：min 平均距离计算
  s.t. 平均 recall 达标；只需一次 CBS sweep，比精确 DP 实用。

  - 工程实现重点：pilot 期间把被 beam 淘汰或未入 list 的候选存入临时 buffer，预测后按 bL 扩容续跑，用 nth_element 只处理增量候选，避免重新排序/重启带来的
  overhead。

  - 注意收益主要来自 mean latency，99.9 百分位尾部延迟通常高于 CBS；若业务有严格 p99/SLA 约束，需要加 clip 上限或与固定搜索策略融合。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：图索引（DiskANN/HNSW）主导十亿级 ANN，但 classical beam search 给所有 query 固定 list size；ABS 证明按 query 难度自适应能提高成本效率，但缺乏 α-reachable 图上的统一理论，也没有显式优化每个 query 该用多少预算。

方法关键点：
- 理论上证明 ABS（参数 γ）在 α-reachable 图上任意度量下近似比为 (α+1)/(α(γ+1)-1)；在 sorted α-reachable + ℓ2 下收紧为 max(α/(α(γ+1)-1), (α²+1)/(α²(γ+1)-1))，统一 Indyk-Xu、Gollapudi、Al-Jazzazi 的结果。
- 提出 beam predictor：先跑 L=K 的 pilot beam search，提取 6 个特征（top-K 距离 d1、dK、均值/标准差；轨迹特征 sdp、c90），线性回归预测 log L*，再用单一 scale 校准到目标平均 recall。
- 训练标签来自离线 CBS sweep，用 Lagrangian relaxation 解 multiple-choice knapsack：min 平均距离计算 s.t. 平均 recall≥rT，无需精确 DP。
- 工程上继续 pilot 而非重启：临时 buffer 保存被淘汰候选，预测后按 bL 扩容并续跑，用 nth_element 只迁移增量候选。

关键实验：三个 100M 数据集（SIFT/DEEP/MSSpaceV）、DiskANN 快预处理 sorted graph、SSD 和内存。匹配 recall 下，SSD 查询延迟比 CBS 最多低 29.6%，15 个设置中 14 个更快；比 ABS 11/15 更快，最多快 6.5%，最慢仅 +1.4%。内存距离计算比 CBS 少 1.3–23.7%，比 ABS 少 0–3.9%。95% recall 时随 K 增大，BP 相对 ABS 的优势扩大。注意理论保证不直接覆盖 fast preprocessing graphs，但 recall 随 γ 单调上升，sorted graph 优于 shuffled graph。

最值得记住：用成本最优分配训练的轻量 pilot 特征预测器，让每个 query 独立选 beam width，比固定 ABS/CBS 更接近「不浪费计算」。
