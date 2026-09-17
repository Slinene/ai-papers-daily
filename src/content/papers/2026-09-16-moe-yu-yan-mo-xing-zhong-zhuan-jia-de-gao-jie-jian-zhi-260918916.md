---
title: Higher-order pruning of experts in mixture-of-experts language models
title_zh: MoE 语言模型中专家的高阶剪枝
authors:
- Alex M. Tseng
- Prannay Kaul
- Luca Zancato
- Wei Xia
- Stefano Soatto
affiliations:
- AWS Agentic AI
- AI Fundamental Research
arxiv_id: '2609.18916'
url: https://arxiv.org/abs/2609.18916
pdf_url: https://arxiv.org/pdf/2609.18916
published: '2026-09-16'
collected: '2026-09-17'
category: LLM
direction: MoE 专家剪枝 · 二阶交互建模
tags:
- MoE
- Expert Pruning
- Second-Order
- Model Compression
- Interaction
one_liner: 提出 HOPE 二阶专家剪枝，考虑专家协同交互，显著优于一阶方法，在高剪枝率及 Agent 任务上优势更大
practical_value: '- 对业务中部署的大规模 MoE 推荐/排序模型，可参考 HOPE 的交互矩阵思路，在专家剪枝时不仅看单个专家的激活/输出贡献，而是记录
  pair 共激活的乘积，构建 F 矩阵并解 QP；工程实现轻量，校准开销仅增加 6-7%，QP 每层 1-2 秒。

  - 剪枝校准集需匹配目标场景：HOPE 在 coding/agentic 校准集上表现不同，建议按业务流量（搜索、推荐、广告）分别采集校准数据，避免跨域剪枝性能损失。

  - HOPE 保留的专家组具有高协同评分，剪枝后模型可作为 downstream SFT 起点且优势持续，适合在业务中先剪枝再微调以进一步恢复/提升效果。

  - 高剪枝率（40-50%）释放内存最多，正是部署价值最大的区间，此时二阶交互优势最显著；若业务需要极限压缩，应优先采用二阶剪枝而非简单一阶方法。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
MoE 语言模型参数量巨大，专家层占主导，导致 GPU 内存瓶颈。专家剪枝能永久移除专家、直接减少内存占用，并且可与量化叠加。但此前方法（Frequency、EAN、MAN、REAP）均为“一阶”：对每个专家独立打分，忽略专家之间的协同与交互。实际 MoE 推理是组合性的，某些专家对频繁共同激活，若仅按个体重要性剪枝，会破坏这些协同结构，尤其在 40-50% 高剪枝率时性能崩塌。

**方法关键点**
- 从剪枝误差分解出发，聚焦替代误差，推导出可优化的上界 Z=(sum_{j∈P∩T} g_j ||f_j||)^2，展开后显式包含 pairwise 交互项。
- 在校准集上记录专家共激活时的 gate 加权输出乘积，构建每层一个 E×E 交互矩阵 F：对角为个体贡献，非对角为协同贡献。
- 将最小化 E[Z] 转化为二进制二次规划 p^T F p，约束 p∈{0,1}^E 且 sum p=|P|，连续松弛求解后取 top |P| 作为剪枝集。
- REAP 是 HOPE 忽略非对角项的特例，因此 HOPE 的增益完全来自交互项。

**关键结果**
在 Qwen3.5-122B-A10B、Qwen3.5-35B-A3B、GLM-4.5-Air 三个模型上，使用 Evol-CodeAlpaca 和 SWE-Bench verified 两种校准集，剪枝率 10-50%。50% 剪枝下，HOPE 平均 rank 1.58（5 个方法中），优于 REAP 的 2.42；在 agentic coding 上最高比 REAP 高 6.1%。全部条件下 HOPE top-1 率 39%，top-2 率 67%，head-to-head 平均胜率 73%。F 矩阵非对角平均幅度为对角的 33%，证实交互信号不可忽略。校准稳定性高（同数据多次试验 Jaccard >0.95），跨校准集 Jaccard 0.60 且与 REAP 相当。HOPE 保留的专家具有更强的协同结构，剪枝后继续 SFT 仍保持优势。

**最值得记住的一句话**：在 MoE 剪枝中，专家间协同交互是高剪枝率下避免性能崩溃的关键，二阶交互矩阵能以极小计算开销保留这些结构。
