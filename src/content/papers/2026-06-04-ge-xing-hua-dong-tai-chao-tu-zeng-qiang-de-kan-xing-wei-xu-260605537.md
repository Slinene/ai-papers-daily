---
title: PHKT:Personalized Dynamic Hypergraph-enhanced KAN-Transformer for Multi-behavior
  Sequential Recommendation
title_zh: 个性化动态超图增强的KAN-Transformer多行为序列推荐
authors:
- Ruijie Du
- Hao Chen
- Xin Zhang
- Dongjing Wang
- Ze Zhang
- Xudong Shen
- Runze Wu
- Dongjin Yu
affiliations:
- Hangzhou Dianzi University
- Sanya Traditional Chinese Medicine Hospital
- Rocket Force University of Engineering
- NetEase Inc.
arxiv_id: '2606.05537'
url: https://arxiv.org/abs/2606.05537
pdf_url: https://arxiv.org/pdf/2606.05537
published: '2026-06-04'
collected: '2026-06-06'
category: RecSys
direction: 多行为序列推荐 · 超图与KAN
tags:
- Multi-behavior Recommendation
- Hypergraph
- KAN
- Transformer
- Sequential Recommendation
one_liner: 融合个性化动态超图与KAN-Transformer，同时捕捉行为异质高阶关系和细粒度非线性模式
practical_value: '- **动态行为权重超图**：针对电商多行为（浏览、加购、购买），根据用户历史行为计算个性化权重，加权 item 相似度矩阵构建动态超边，有效捕捉用户特定的高阶行为关系，可直接增强推荐系统中辅助行为的利用效率。

  - **KAN 替换 FFN**：用 Kolmogorov-Arnold Network 替代 Transformer 中的前馈网络，按输入维度学习独立的径向基函数组合，为不同潜在行为模式提供专用响应函数，解决标准
  FFN 的“共享映射”问题，在行为序列建模中可提升细粒度拟合能力。

  - **双分支融合架构**：超图分支捕获结构与共现关系，KAN-Transformer 分支建模时序与非线性偏好演化，通过可学习的融合系数平衡两者，适用于电商场景中复杂行为序列的联合建模。

  - **行为权重先验**：对各行为类型预设差异化初始权重（如购买=1，加购=0.7，浏览=0.3），与数据集动态匹配，可作为工业级多行为推荐的基础配置，降低噪声行为干扰。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：多行为序列推荐利用用户多种行为（浏览、加购、购买）的时序交互预测目标行为，但现有方法存在两个关键局限：一是静态超图无法根据用户个性化语义动态加权高阶关系；二是标准 Transformer 的统一前馈网络强制所有潜在行为模式共享相同的非线性激活模板，难以适应不同模式对目标行为的差异化贡献函数。因此，需要一种同时建模个性化异质高阶关系与模式专属非线性响应的架构。

**方法**：提出 PHKT，包含两个核心模块。
- **个性化动态超图（PHDW）**：根据用户历史行为计算行为类型权重，动态重加权 item 余弦相似度矩阵，从加权矩阵中为每个 item 选择 k 个最相似 item 构建超边，形成用户级个性化超图。通过超图卷积传播，聚合行为感知的高阶共现关系。
- **KAN-Transformer**：将 Transformer 的 FFN 替换为 KAN 层，对每个输入维度独立生成若干径向基函数，并用可学习权重组合它们，使不同维度可以学习各自的非线性响应函数，从而对不同的潜在行为模式实现细粒度的贡献建模。最终通过可学习系数融合超图输出与 KAN-Transformer 输出，用于掩码物品预测。

**实验**：在 RetailRocket、Tmall、IJCAI 三个真实多行为数据集上，与 9 个基线（包括 FEARec、SASRecCPR、MBHT、MBSRec 等）对比。PHKT 在所有指标（HR@5/10、NDCG@5/10、MRR@5）上均取得最优。例如，在 IJCAI 上 HR@10 达到 0.583，比第二名 MBHT 提升 49.9%；在 Tmall 上 MRR@5 达到 0.326，比 MBSRec 提升 50.2%。消融实验验证了 KAN 层和动态超图模块的各自增益，参数分析给出最优特征维度与 KAN 层数的建议。
