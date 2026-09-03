---
title: 'Beyond Modality Harmony: Orthogonal Purification and Topology-Guided MoE for
  Conflict-Aware Multimodal Recommendation'
title_zh: 超越模态和谐：正交净化与拓扑引导MoE的冲突感知多模态推荐
authors:
- Jialin Liu
- Zhaorui Zhang
- Ray C. C. Cheung
affiliations:
- City University of Hong Kong
- The Hong Kong Polytechnic University
arxiv_id: '2609.02152'
url: https://arxiv.org/abs/2609.02152
pdf_url: https://arxiv.org/pdf/2609.02152
published: '2026-09-02'
collected: '2026-09-03'
category: RecSys
direction: 多模态推荐 · 去噪融合
tags:
- Multimodal Recommendation
- Orthogonal Purification
- Mixture-of-Experts
- Graph Neural Networks
- Contrastive Learning
- Denoising
one_liner: 提出OrthoRec，用协同引导正交净化和拓扑感知MoE解决多模态推荐中的模态-拓扑冲突
practical_value: '- **多模态融合改造成残差净化思路**：电商图文/视频常存在标题党、主图诱骗，直接 concat 或 gate 会污染协同信号。可借鉴
  CGOP：先用纯协同 embedding 作为锚，把视觉/文本特征投影到平行/正交方向，只保留平行分量并做能量归一化后残差注入，低成本缓解模态噪声。

  - **多模态专家融合不用 softmax 门控**：TAR-MoE 用解耦 sigmoid 门控替代传统 softmax 注意力，打破“模态之间零和竞争”，每个模态专家可独立决定注入强度。在电商多模态排序/召回模型中可直接替换融合层，避免视觉强、文本弱的
  item 被错误压制。

  - **对比学习负样本别强行对齐**：safe-SSL 对矛盾 pair 动态降低对比损失，适合电商中图像与交互语义不一致的样本。如果业务在多模态对比学习时遇到噪声对，可加入置信度惩罚或自适应温度，而不是全量强制对齐。

  - **稀疏 item 鲁棒性有直接价值**：实验显示对稀疏 item 的改善，说明该去噪机制在新品/长尾商品多模态建模上可能比复杂跨模态模型更稳。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态推荐普遍依赖“模态和谐”假设，认为图文/视频特征天然有益且与用户交互拓扑对齐。但真实场景中视觉诱骗、语义错配普遍存在，强行融合会污染纯协同表示。

**方法关键点**：
- **Collaborative-Guided Orthogonal Purification (CGOP)**：以纯协同 embedding 为锚，将多模态特征几何解耦为平行与正交方向；对正交噪声做能量保持归一化并自适应截断，既修正欺骗性语义方向，又保留模态表示容量。
- **Topology-Aware Routing Mixture-of-Experts (TAR-MoE)**：利用协同拓扑进行路由，采用解耦 sigmoid 门控打破 softmax 的零和竞争，让每种净化后的模态自主决定注入尺度。
- **safe-SSL**：动态惩罚矛盾 pair 的强制对比对齐，减少噪声负样本对表示学习的伤害。

**关键结果**：在三个 Amazon 真实数据集上，OrthoRec 一致超过近期强基线，并在模态噪声与 item 稀疏场景下表现出更强的鲁棒性。
