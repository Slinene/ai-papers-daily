---
title: 'Canopy: Exploiting Piecewise Smooth Tree Priors for Multi-Fidelity Bandits'
title_zh: Canopy：利用分段平滑树先验的多保真度老虎机
authors:
- Michael Jerge
- Suman Jana
affiliations:
- Amazon
- Columbia University
arxiv_id: '2609.30017'
url: https://arxiv.org/abs/2609.30017
pdf_url: https://arxiv.org/pdf/2609.30017
published: '2026-09-24'
collected: '2026-09-25'
category: Reasoning
direction: 多保真树 bandit 优化 LLM 推理决策
tags:
- multi-fidelity bandits
- tree search
- LLM inference
- model routing
- prefix caching
- test-time compute
one_liner: 提出 CANOPY，在线学习树结构上的分段平滑性失效位置，将昂贵评估集中到不连续区域，提升多保真决策效率
practical_value: '- 在电商/广告的**多模型路由或策略选择**中，可借鉴 CANOPY 的树结构多保真评估：用廉价内部节点（如小模型打分、压缩特征）快速估计候选池价值，只在检测到局部不平滑（如收益发生跳变）时才触发昂贵全量评估，显著降低
  GPU 成本。

  - 对**生成式推荐 / Agent 的 test-time search**，CANOPY 相比 uniform best-of-N 在 SWE-bench
  上多解决 1.6 倍问题，说明通过随机路径探针识别搜索树中的高不确定分支，把预算集中在最有希望的子树上，可复用其「在线聚合偏差证书」思想提升 beam search
  或候选生成的效率。

  - **Prompt 修剪与缓存管理**中，可将 prompt token 序列建模为树，内部节点快速估计压缩前后的效果差异，仅在检测到质量突变时才进行完整生成评估；对
  prefix caching 场景，CANOPY 的树节点价值估计可用于决定哪些前缀值得缓存或继续扩展，提升命中率并降低首 token 延迟。

  - 算法层面，CANOPY 的保证「额外成本与不连续点数量可加」提示：在业务多臂老虎机问题中，如果收益函数分段平滑且边界未知，可采用类似随机探针 + 局部偏差检测的机制，避免全局平滑假设导致的搜索低效。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：许多 LLM 推理问题（模型路由、前缀缓存管理、prompt 修剪、测试时搜索）本质是在树上做优化。自回归生成天然形成树结构，内部节点提供廉价但有偏的估计，叶评估昂贵但准确。传统层次 bandit 依赖预先指定的全局平滑性 schedule，而真实目标往往分段平滑，最优解可能在尖锐边界附近，全局假设导致预算浪费。

**方法**：CANOPY 是一种多保真树 bandit，不假设全局平滑，而是在线学习何处平滑先验有效。它使用廉价的随机路径探针构造局部聚合偏差的在线证书，一旦检测到某个单元格存在平滑性违反，就将昂贵的叶评估定向到该区域。算法在固定预算和遗憾上给出保证：额外成本与不连续点数量可加，无违反时恢复平滑树速率，违反密集时退化为结构盲搜索。

**结果**：在模型路由、top-k 识别、测试时搜索、前缀缓存和 prompt 修剪五个场景上，CANOPY 在匹配预算下一致优于基线。具体包括：1000 模型池 top-10 recall 提升 2.9 倍；SWE-bench Verified 解决数比 best-of-N 高 1.6 倍；前缀缓存场景的首 token 延迟中位数降低 3.6 倍。
