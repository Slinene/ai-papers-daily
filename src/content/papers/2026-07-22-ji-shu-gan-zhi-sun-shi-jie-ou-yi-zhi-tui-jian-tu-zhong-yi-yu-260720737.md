---
title: 'Cardinality-Decomposed Loss: Matching Training Objectives to Relation Structure
  in Heterogeneous Recommendation Graphs'
title_zh: 基数感知损失：解耦异质推荐图中一对多与一对一关系的训练目标
authors:
- Parul Maheshwari
- Amulya Paruchuri
- Yiqing Zou
- Alireza Sahami Shirazi
- Farhad Farahani
- Prakhar Mehrotra
affiliations:
- PayPal AI
- PayPal Inc.
arxiv_id: '2607.20737'
url: https://arxiv.org/abs/2607.20737
pdf_url: https://arxiv.org/pdf/2607.20737
published: '2026-07-22'
collected: '2026-07-25'
category: RecSys
direction: 异质图推荐 · 基数感知损失
tags:
- Graph Neural Networks
- Heterogeneous Graphs
- Cardinality-Decomposed Loss
- BPR
- Cross Entropy
- Embedding Collapse
one_liner: 在异质图中按关系基数分解损失——BPR给一对多，交叉熵给一对一——根治属性嵌入崩塌且不影响排名指标的无声失败
practical_value: '- **按关系基数分配损失函数**：在业务异质图（用户-商品+用户-属性/商品-属性）中，请检查每个边的基数特征。若为一对一（如性别、城市、离散分桶），则应用交叉熵（CE）而不用BPR；BPR只用于一对多（如点击、购买）。这能从根上防止属性嵌入的余弦相似度崩塌至0.9+。

  - **低成本检测“无声失败”**：固定周期用线性探针（逻辑回归）评估属性嵌入的可区分性（AUC），而非只看NDCG。若属性嵌入余弦相似度中位数>0.5，意味着几何结构崩溃而排名指标未必报警。

  - **λ 权衡与两轴框架**：通过计算属性标签与物品共现的Jaccard相似度估算**语义对齐**，并检查属性节点是否直接相邻以判断**拓扑泄漏**。高语义对齐下λ=1.0可直接提升NDCG；低对齐但无泄漏时用λ扫描寻找帕累托前沿；有高泄漏时CDL仍改善排名与嵌入纯度。

  - **共享编码器中的梯度冲突监控**：在训练初期记录BPR与CE在共享参数上的梯度余弦相似度，若持续为负，则需增大λ使CE信号更强，避免过早早停。该信号可用于自适应λ调度。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
在推荐系统的异质图（用户-商品交互+用户属性等）中，所有关系通常统一使用BPR损失。但一对一关系（如用户-性别）使用BPR会错误地将“未被分配”当作负样本，导致属性嵌入的几何结构塌缩至接近随机（余弦相似度高达0.93–0.98）。该崩塌不影响NDCG等排名指标，形成监测盲区，却污染用户表征、损害下游个性化与冷启动。

**方法**  
- 提出**基数分解损失（CDL）**：根据关系基数分配损失——一对多（如交互）用BPR，一对一（如离散属性）用交叉熵，组合为 \\(L_{\text{CDL}} = L_{\text{BPR}} + \lambda \cdot L_{\text{CE}}\\)。
- 二者共享两层的HeteroSAGE编码器，一对一关系接线性分类头，缺失标签通过掩码处理。
- 仅引入一个超参数λ，通过网格扫描控制两类目标的相对强度。
- 机理分析：梯度余弦相似度测量显示BPR与CE在共享参数上持续竞争（负相关），证实损失冲突。

**关键实验**  
- 数据集：MovieLens-1M、Last.fm-360K、BookCrossing、Yelp和PayPal内部工业图（1M用户、178M交互），覆盖用户侧和物品侧一对一属性。
- 对比基线：CF基线（仅BPR监督交互边，属性边只参与消息传递）和统一BPR（所有关系均用BPR）。
- CDL在所有数据集上显著恢复属性可区分性：线性探针AUC提高30–42个百分点（如Last.fm性别AUC +42.1pp）。
- 当属性与偏好**语义对齐**时，同时提升排名：Last.fm NDCG@10 +7.8%，Yelp +2.9%，Audience Factory +3.3%；低对齐时（MovieLens、BookCrossing）以可控的NDCG代价（-7.2%~-15.8%）换取属性嵌入健康。
- 揭示两轴框架：语义对齐与拓扑泄漏，解释λ扫描行为并指导实践。

**最值得记住的一句话**  
“按关系基数选择损失——一对一用交叉熵，一对多用BPR——只需一张基数和一个小λ，就能修复看不见的嵌入崩塌。”
