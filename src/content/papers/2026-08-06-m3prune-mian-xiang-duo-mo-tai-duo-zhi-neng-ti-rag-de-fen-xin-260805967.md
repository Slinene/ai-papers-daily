---
title: 'M$^3$Prune: Hierarchical Collaborative Pruning for Efficient Multi-Modal Multi-Agent
  Retrieval-Augmented Generation'
title_zh: M³Prune：面向多模态多智能体 RAG 的分层通信剪枝
authors:
- Taolin Zhang
- Weizi shao
- Zijie Zhou
- Chen Chen
- Daiyang Yu
- Tingyuan Hu
- Chengyu Wang
- Xiaofeng He
affiliations:
- Hefei University of Technology
- East China Normal University
- China University of Petroleum
- Guangdong University of Finance and Economics
- Alibaba Group
arxiv_id: '2608.05967'
url: https://arxiv.org/abs/2608.05967
pdf_url: https://arxiv.org/pdf/2608.05967
published: '2026-08-06'
collected: '2026-08-09'
category: MultiAgent
direction: 多智能体协作效率优化
tags:
- multi-modal
- multi-agent
- RAG
- communication pruning
- token efficiency
one_liner: 通过分层学习稀疏通信拓扑剪枝多智能体冗余交互，在提升多模态 RAG 准确率的同时大幅降低 token 开销
practical_value: '- 在多智能体推荐或对话系统中，可直接引入可学习的软邻接矩阵（Gumbel-Softmax）对 Agent 间的通信权重建模，用策略梯度在训练时自动发现关键通信链路，替代固定拓扑。

  - 分层剪枝策略（先剪模态内冗余，再剪模态间冗余）可迁移至多源信息（如商品图文、评论）的智能体协作，减少跨模态噪声，提升决策效率。

  - 渐进式剪枝中的退化剪枝率 \(p^{(t)} = p^{(t-1)} \cdot \exp(-t/T)\) 和核范数正则项可作为通信成本控制模板，直接用于生产级多
  Agent 系统的持续优化，避免一次性剪枝带来的不稳定。

  - 模态对齐损失 \(L_{align}\) 可借鉴于推荐中多模态特征融合的对齐训练，显式保持图文 Agent 间语义一致性，防止因剪枝导致的协同失效。'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

**动机**  
多模态 RAG 引入多智能体协作后性能显著提升，但固定通信拓扑带来大量冗余交互，导致 token 开销增长、计算成本上升，甚至噪声干扰最终答案。尤其在图文双模态场景下，不加区分的全连接通信会使部分 Agent 被无关信息淹没。因此，需要自适应地修剪冗余通信边，在维持任务性能的同时大幅降低通信成本。

**方法关键点**  
- **分层剪枝框架**：先对文本、视觉模态分别进行图稀疏化，再对跨模态图进行稀疏化，最后通过渐进式剪枝得到紧凑的推理拓扑。  
- **可学习软邻接矩阵**：利用 Gumbel-Softmax 将离散邻接矩阵松弛为连续权重，每轮动态调整边的重要性，用策略梯度优化任务效用与稀疏性（核范数正则）的平衡。  
- **模态对齐损失**：在跨模态图优化中加入对齐项，鼓励 \(A^{txt\rightarrow vis}\) 与 \(A^{vis\rightarrow txt}\) 的一致性，保持语义协同。  
- **渐进式剪枝**：训练中每轮按衰减率 \(p^{(t)}=p^{(t-1)}e^{-t/T}\) 保留 top K 条边，逐步剔除低频连接，最终推理时使用训练收敛后的稀疏图。

**关键结果**  
在 MultimodalQA、Vidoseek 和 ScienceQA 三个基准上，使用 Llama3.2-VL-11B、Qwen2.5-VL-7B 和 Qwen-VL-Max 作为骨架。M³Prune 较最强多智能体基线（如 ViDoRAG、HM-RAG）：  
- 平均准确率提升 **9.4%**，token 效率提升 **23.8%**（同等精度下 token 消耗显著更低）；  
- Qwen-VL-Max 下 Vidoseek Acc★ 达 **73.95%**，显著超过 ViDoRAG（68.43%）和 E-Agent（68.27%）；  
- 消融证实模态对齐与核范数正则对性能的关键贡献，去掉后分别下降 2~4 个点。  

**一句话精要**  
“对多模态多智能体通信图分层学习稀疏连接，既能抑制噪声、又能保留关键交互，是提高复杂 RAG 系统效率的可靠范式。”
