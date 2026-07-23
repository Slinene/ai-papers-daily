---
title: Zero-Observation User Reactivation with Gap-Driven Dimensional Gating
title_zh: 基于间隙驱动的维度门控实现零观察用户重激活
authors:
- Jiandong Ding
- Tianying Liu
- Fuyuan Liu
- Huijie Qin
- Tiandeng Wu
affiliations:
- Fudan University
- Huawei Technologies
arxiv_id: '2607.19802'
url: https://arxiv.org/abs/2607.19802
pdf_url: https://arxiv.org/pdf/2607.19802
published: '2026-07-22'
collected: '2026-07-23'
category: RecSys
direction: 长期不活跃用户的重激活与轻量插件
tags:
- Sequential Recommendation
- User Reactivation
- Gap-Driven Gating
- Parameter-Efficient
- Frozen Backbone
- Dimensional Routing
one_liner: 冻结序列推荐骨干，用维度门控融合历史与全局先验，从长间隔中恢复预测性能。
practical_value: '- **轻量插件复用已有模型**：冻结已有推荐模型（如SASRec、BERT4Rec）的骨干，仅训练一个66K参数的维度门控插件，可在不改变线上服务的前提下恢复长间隔用户的推荐效果，适合嵌入被多个下游服务共享的场景。

  - **可解释的置信度监控**：输出Historical Confidence Index（各维度门控均值），可实时观察不同间隙下模型对历史表示的信任程度，辅助运维与效果归因。

  - **全局先验的离线学习与更新**：用一个可学习的零初始化向量作为所有用户的通用fallback，训练后固定；对于品类快速变化的电商，可定期用新数据刷新该先验，低成本捕捉流行度漂移。

  - **全量微调与插件的取舍策略**：当允许更新骨干嵌入时，端到端重训可带来更高收益（如Hit@10从0.031提升至0.080）；当嵌入与召回、排序模型强耦合时，插件方案以零漂移和约40倍参数节省取得60%的增益，可作为平滑上线方案。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
序列推荐模型在用户长期沉默（超过一年无交互）后重新激活时，预间隙的历史表示可靠性下降，导致预测性能单调衰退。传统方法（如TiSASRec）仅建模序列内的时间间隔，未能显式校准长观察空白后的用户状态。该文将这一场景定义为“零观察重激活”问题，并在亚马逊三个品类数据集上验证了不同骨干（GRU4Rec、SASRec、BERT4Rec）的衰减模式。

### 方法
提出**DeltaGate**，一个冻结骨干的输出层插件，核心是**维度门控与全局先验的混合**：
- 利用用户最后交互以来的间隔天数Δ𝑡，与个性化表示h_pers拼接后通过两层MLP生成维度级门控g∈(0,1)^d。
- 将h_pers与一个可学习的零初始化全局先验h_global按g进行Hadamard混合：h_final = g⊙h_pers + (1-g)⊙h_global。
- 仅训练门控MLP和h_global（共66K参数），保持原模型参数与嵌入不变，训练目标为全量物品交叉熵损失。
- 适用于SASRec、GRU4Rec和BERT4Rec等多种序列编码器，对双向模型通过追加[MASK] token提取最后隐式表示。

### 关键实验
- **数据集**：Amazon Video Games、CDs & Vinyl、Movies & TV，按自然间隙分桶，测试集采用用户级留一法。
- **对比基线**：原始骨干、TiSASRec、端到端拼接间隙的TimeConcat。
- **核心结果**：在>365天桶内，DG-SASRec在Video Games上将Hit@10从0.031提升至0.047，CDs & Vinyl从0.022至0.040，Movies & TV从0.021至0.034；DG-BERT4Rec对应从0.025至0.046。
- **消融实验**：仅用全局先验( g=0) Hit@10仅0.005~0.008，证明增益来自维度路由而非完全替代历史。
- **工程对比**：插件方案仅66K参数，无骨干嵌入漂移；端到端TimeConcat E2E Hit@10为0.080，但需要更新2.6M参数，嵌入L2漂移139.7%。
- **可解释性诊断**：固定历史表示，改变Δ𝑡可观察到维度级门控值的单调变化（如某维度从0涨至0.97，另一维度从1跌至0.49）。

### 一句话
冻结骨干、维度门控与可学全局先验的组合，以极低参数代价和零嵌入漂移，显著缓解长期沉默用户的序列推荐衰减。
