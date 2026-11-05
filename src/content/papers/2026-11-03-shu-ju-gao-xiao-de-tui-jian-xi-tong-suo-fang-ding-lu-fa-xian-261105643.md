---
title: Data-Efficient Scaling-Law Discovery for Recommendation Systems via Coupled
  Hyperparameter Scaling
title_zh: 数据高效的推荐系统缩放定律发现：耦合超参数缩放
authors:
- John Martabano Landy
- Louis C. Tiao
- Yao Xuan
- Luc Kien Hang
- Rupinder P. Khandpur
- Arvind M. Vepa
- Srinidhi Raghavendran
- Anirudh Agrawal
- Xiaoyi Leo Liu
- Jiang Liu
affiliations:
- Meta
arxiv_id: '2611.05643'
url: https://arxiv.org/abs/2611.05643
pdf_url: https://arxiv.org/pdf/2611.05643
published: '2026-11-03'
collected: '2026-11-05'
category: RecSys
direction: 推荐系统缩放定律 · 贝叶斯优化
tags:
- scaling laws
- Bayesian optimization
- recommender systems
- hyperparameter scaling
- Pareto frontier
- compute allocation
one_liner: 提出 Scaling Layer + Axia 工作流，用少量训练试验自动学习推荐模型复杂度-质量前沿，指导全舰队算力分配
practical_value: '- 把模型架构超参从高维原始参数压缩为 3 个语义缩放轴（embedding dim, interaction depth, interaction
  width），用 scaling rule 统一同组参数变化，搜索空间从不可枚举降到 16+4 次训练就能覆盖前沿；可直接复用到广告/推荐模型模板的新场景适配。

  - 先做 FLOPs/延迟 cost profiling（无需训练）获得成本先验，指导 cost-feasible 初始化采样；GP 对 log-cost 和
  NE 建模，log 变换捕捉幂律趋势，比直接用 BO 默认代理更准。

  - 用 constrained EI（模型刷新，cost ≤ 现役）和 EHVI（扩容探索前沿）做小批量自适应实验，比网格/随机搜索显著降低训练成本、提升 hypervolume；工程上可把
  16 init + 4 adaptive 作为默认预算起点。

  - 多模型 fleet 评估用 revenue share 加权的 Pareto 前沿改进 + 不确定性传播，决定 refresh/scale-up，避免单点评估偏差；适合大厂多场景模型统一算力治理。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机** 大型 Web 平台广告/排序模型具有异构架构，容量分布在嵌入、交互、序列等多个维度，参数互相耦合；手动为每个模型配置算力需要数天到数周训练试验，难以持续。虽然 LLM scaling law 可指导算力分配，但推荐模型不能仅靠参数量概括。

**方法关键点** 
- **Scaling Layer**：将原始架构参数分组为三个语义一致的缩放控制——embedding dimension d、interaction depth ℓ、interaction width w（宽度为伞参数，联合控制交互模块多个隐藏维度）。每个原始参数是所在组单个坐标的函数，使架构可缩放而不会比例失衡。
- **Axia 引擎**：先做成本分析（64 个配置测量 FLOPs），随后用 scaling-informed GP 代理建模 NE 和 log FLOPs，以 log 变换捕捉深度/宽度的幂律趋势，通过 constrained EI 或 EHVI 选择下一批训练配置。默认预算 16 个初始化 + 4 个自适应试验。
- **评估框架**：固定代表模型集，按 revenue share 加权 Pareto 前沿改进，并传播不确定性，得到 fleet utility。

**关键实验** 单代表模型上，Axia 在 160 MFLOPs 下达到最低 NE，相对 Random、BO(Ax)、Open-Loop Surrogate 分别多降 0.070%、0.059%、0.042%，hypervolume 高 24.5%、19.0%、7.9%；3 维 scaling layer 优于 1D/2D/6D。生产部署 34 个模型迭代两个周期，平均离线 NE 改善 0.66%，累计在线 lift 0.36%。

**最值得记住的一句话** 将耦合架构参数压缩成语义缩放轴、用成本感知的贝叶斯优化小样本探索性能-成本前沿，是把推荐模型 scaling law 变成可操作算力分配的实用路径。
