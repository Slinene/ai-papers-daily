---
title: 'ATLAS: Learning to Recommend Across Unseen Domains'
title_zh: ATLAS：多源域泛化零样本推荐框架，无需目标域适配
authors:
- Pervez Shaik
- Prosenjit Biswas
- Abhinav Thorat
- Ravi Kolla
- Niranjan Pedanekar
affiliations:
- Sony Research India
arxiv_id: '2608.03899'
url: https://arxiv.org/abs/2608.03899
pdf_url: https://arxiv.org/pdf/2608.03899
published: '2026-08-04'
collected: '2026-08-05'
category: RecSys
direction: 多源推荐域泛化 · 零样本检索
tags:
- Domain Generalization
- Zero-Shot Recommendation
- Gromov-Wasserstein
- Adversarial Alignment
- RVQ
- Multi-source Recommendation
one_liner: 通过对抗对齐 + Gromov-Wasserstein 对齐 + 残差矢量量化，在不接触目标域的条件下实现零样本推荐。
practical_value: '- **item 侧领域混淆**：用对抗训练 + 梯度反转层让 item 投影后的表示无法被线性分类器区分来源域，工程上可直接用于多业务线
  item embedding 统一，无需额外对齐模块。

  - **用户交互几何对齐**：引入 Gromov-Wasserstein 下界损失匹配不同域内用户间距离分布，无需用户重叠，适合迁移用户冷启动场景——新域用户仅凭少量交互历史就能获得合理表示。

  - **离散码本作为信息瓶颈**：残差矢量量化（RVQ）层次化码本强制丢弃域特有变化，实验表明使用码本重建向量比连续投影提升零样本 HR 平均 45%，可作为推荐模型轻量化或跨域迁移的通用技巧。

  - **源域多样性是关键**：实验证实源域数量从 2 扩到 5 时零样本性能单调上升，提示实际业务中应尽可能聚合异构场景（如不同品类、国家）联合训练，而不是只依赖单一主域。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现代推荐系统严重依赖领域内训练，跨域转移通常需要目标域数据参与训练或适配，无法直接部署到完全陌生的品类或市场。本文定义“推荐域泛化 (RDG)”——仅用多个源域训练一个冻结模型，在未见目标域上执行零样本检索，域间用户与物品均不重叠。

**方法关键点**
- **item 统一**：用冻结 Sentence-BERT 获得语义嵌入，通过共享 MLP + 对抗训练（梯度反转层，K 类域判别器）使投影向量在球面上域不可区分，保留推荐语义、去除域特有信息。
- **user 统一**：用户表示结合 LightGCN 协同信号与交互序列语义均值，经共享 MLP 投影后，用 Gromov-Wasserstein 下界损失对齐不同域的用户内距离分布，迫使几何结构一致，无需用户身份对应。
- **离散化码本**：在统一空间上施加分层残差矢量量化 (RVQ)，用软 Sinkhorn 赋值训练、硬最近码字推理，码本充当信息瓶颈抑制域特有差异。
- **损失组合**：排名损失 (BPR) + 对抗损失 + GW 损失 + 量化损失 + 辅助正则项，端到端训练后冻结所有可迁移模块。
- **零样本推理**：新域用户仅用交互物品语义均值作为初始表示，经冻结投影和码本重建后，以内积检索 top-K 物品。

**关键实验**
- 数据：Amazon Reviews 2023，5 个源域（Beauty, Automotive, Movies & TV, Video Games, Electronics），10 个未见目标域。
- 基线与结果：ATLASZS 在多数未见域上超越领域专用、跨域、通用和 LLM 基线，HR@10 平均相对提升 24%；与 UniSRecZS 持平，但 ATLAS 无需微调即优于所有 LLM 点推基线。
- 消融：联合对抗 + GW 比单独使用提升明显；RVQ 重建比连续投影平均 HR 提升 45%；源域从 2 增至 5 时零样本性能单调上升。

**核心启示**
“推荐知识”可以从异质源域直接习得，无需目标域适应或 LLM 推理——充分的对齐与离散化是跨域通用检索模型的关键。
