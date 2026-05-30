---
title: Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient
  Caching
title_zh: 通过凸重构和梯度缓存实现大模型高效测试时微调
authors:
- Alaa Khamis
- Alaa Maalouf
affiliations:
- University of Haifa
arxiv_id: '2605.30337'
url: https://arxiv.org/abs/2605.30337
pdf_url: https://arxiv.org/pdf/2605.30337
published: '2026-05-28'
collected: '2026-05-30'
category: Training
direction: 测试时微调 · 凸近似样本选择
tags:
- test-time finetuning
- convex approximation
- Frank-Wolfe
- gradient caching
- data selection
- LLM adaptation
one_liner: 将查询感知的样本选择建模为稀疏凸近似，通过几何整数化和梯度重用，在测试时微调中取得显著更优的质量-效率帕累托前沿。
practical_value: '- **查询感知的样本选择**：电商/Agent 场景中可借鉴 Frank-Wolfe 在 embedding 空间对 query
  做稀疏凸组合来选取训练样本，无需显式多样性惩罚项即可自动抑制冗余，比 kNN 或启发式信息增益选择更快且保持多样性，适用于在线低延迟样本挑选。

  - **几何整数化与梯度重用**：将连续权重转为整数计数的整数化过程，产生天然的重读样本块，从而允许缓存梯度并跨多次相同样本的更新步复用，减少 1.48× 的微调计算开销——适用于推荐系统中用户行为序列出现重复
  item 或 prompt 的在线微调场景。

  - **两阶段加速获得更大有效 batch**：选择阶段比 SIFT 快 12× 以上（0.059s vs 0.524s），结合梯度重用，可在相同墙钟时间内使用更大
  N，在强实时性约束下提升模型适应质量，这一思路可直接用于 Agent 每次查询时快速收集相关记忆并高效微调。

  - **低维投影加速**：当嵌入维度高时，可用 PCA 对候选池降维后再进行 Frank-Wolfe，保持选择质量的同时进一步压缩选择延迟，适用于大底座模型编码的高维表示。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
测试时微调（TTFT）为每个用户查询从大语料库中检索相关序列并轻量更新模型，能大幅缩小不同规模模型间的性能差距。但现有方法在选样效率上存在尖锐权衡：纯 kNN 检索虽快但易陷入冗余，信息论多样性选择虽好但开销昂贵。在推理延迟敏感的场景中，亟需一种既能保证选择质量又能高速完成的方法。

**方法关键点**  
- **凸近似选样**：将查询 q 在候选池 {p_i} 的嵌入空间中表示为稀疏凸组合，通过投影自由的 Frank-Wolfe 算法优化 ‖q − Pw‖²，自动获得相关且多样的支持集（权重非零的样本）；不依赖显式冗余惩罚，几何性质天然避开近似重复的方向。  
- **几何整数化**：将 Frank-Wolfe 返回的连续权重 w 转化为满足预算 N 的等权多样本集，通过“底分配 + 贪心填充 + 局部交换优化”最小化重构误差，形成紧贴凸组合的离散训练集；得到的重复样本为后续加速提供结构。  
- **梯度复用**：对整数化产生的连续相同样本块，本地缓存梯度并设定刷新间隔 r（默认 r=2），将前向‑反向计算次数从 N 降至约 ⌈N/r⌉，显著降低微调时延且几乎无损。  

**关键实验**  
在 The Pile 的 12 个子集上，以 GPT‑2 为基础模型，比较 kNN、SIFT 和 HullFT，以 BPB% 相对下降和总墙钟时间（选择+微调）衡量。在总时间 T ≤ 4s 的延时敏感区内，HullFT 在所有预算下均取得最低 BPB%，在最紧预算（1.75s）时比最强基线低 3.83%；选择阶段比 SIFT 平均快 12 倍，梯度复用实现 1.48× 微调加速。在 11/12 子集上均优于基线，尤其在高增益子集（如 Enron、GitHub、USPTO）优势显著。  

**核心启示**  
凸几何重构天然融合相关性和多样性，端到端框架为在线适应提供了“选得快、训得省”的新范式，其中梯度复用的思想可推广至任何存在重复样本块的增量微调场景。
