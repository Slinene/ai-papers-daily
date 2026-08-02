---
title: 'THGFM: Dual-Branch Temporal Heterogeneous Graph Fusion Model'
title_zh: THGFM：双分支时序异构图融合模型
authors:
- Yixin Peng
- Diego Collarana
- Er Jin
- Stefan Decker
affiliations:
- RWTH Aachen University
- Fraunhofer FIT
arxiv_id: '2607.27303'
url: https://arxiv.org/abs/2607.27303
pdf_url: https://arxiv.org/pdf/2607.27303
published: '2026-07-29'
collected: '2026-08-02'
category: RecSys
direction: 时序异构图表示学习
tags:
- Temporal Heterogeneous Graphs
- Graph Transformers
- Rotary Temporal Attention
- Dual-Branch Architecture
- Type-Conditioned Gating
- Relative Time Encoding
one_liner: 双分支架构融合共享与类型特定时序注意力，配合旋转时序注意力，实现高效跨类型迁移与关系感知特化
practical_value: '- **双分支融合与类型门控**：在电商多实体（用户/商品/查询）行为图建模中，可拆分为共享分支（捕捉通用模式）和关系类型特定分支（捕获关系语义），并通过类型条件门控动态平衡二者，避免共享与特化互斥，适合异构行为序列建模。

  - **旋转时序注意力**：将相对时间差以相位旋转注入注意力计算，可直接用于用户行为序列 Transformer，替代传统位置编码或加法时间嵌入，尤其适用于间隔不均匀的点击流建模。

  - **非竞争融合机制**：独立特征向门控允许同时增强两分支，而非 softmax 抑制，可迁移到多任务或多模态推荐中的特征融合层，保留更多互补信息。

  - **工程实现轻量**：门控融合仅在特征维度上加权，旋转编码无需额外参数，易于在现有 GNN/Transformer 推荐模型中增量集成。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：现实推荐与信息系统中，用户、商品、查询等实体通过多种关系动态交互，构成时序异构图。现有方法难以兼顾跨类型的参数高效转移和关系感知的特化，且时间信息常作为附加特征而非直接嵌入注意力核心，限制了时序动态的捕捉能力。

**方法关键点**：
- **双分支架构**：共享空间时序注意力分支实现参数高效的跨类型模式共享；关系类型划分时序注意力分支针对每种关系独立建模，保留类型特异性。
- **类型条件非竞争门控融合**：为两分支分配独立、类型条件的逐特征门控，允许同时放大或抑制，避免零和竞争，实现自适应融合。
- **旋转时序注意力**：用相对时间差的一半作为相位旋转查询和键，在注意力计算中直接编码时间间隔，无缝集成到 Transformer 内核中。

**关键结果**：在 OAG-CS、PF、OGBN-MAG、HTAG 等学术异构图基准上，THGFM 六任务平均提升 +3.25%，其中链路预测 OAG-CS PV 最高提升 +12.37%，节点分类 PF-L₂ / L₁ 分别提升 +4.87% / +1.18%，在 OGBN-MAG、HTAG-ArXiv、HTAG-DBLP 上分别提升 +4.24%、+3.73%、+4.61%。
