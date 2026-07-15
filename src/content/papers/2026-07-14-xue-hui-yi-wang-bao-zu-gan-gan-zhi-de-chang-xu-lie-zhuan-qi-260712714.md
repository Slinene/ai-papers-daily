---
title: 'Learning to Forget: Satiation-Aware Long-Sequence Transducers for Mitigating
  Post-Purchase Redundancy'
title_zh: 学会遗忘：饱足感感知的长序列转换器缓解购买后冗余推荐
authors:
- Yipin Dai
- Ruocong Tang
- Xing Fang
- Yang Huang
- Jing Wang
- Zhentao Song
- He Guo
arxiv_id: '2607.12714'
url: https://arxiv.org/abs/2607.12714
pdf_url: https://arxiv.org/pdf/2607.12714
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 序列推荐 · 兴趣生命周期建模
tags:
- Sequential Recommendation
- Interest Exit
- Post-purchase Redundancy
- Dual-path Cross-Attention
- Satiation Mechanism
- Self-supervised Learning
one_liner: 提出饱足感感知机制，建模兴趣退出与唤醒周期，将购买后重复推荐率降低超60%
practical_value: '- 区分点击与购买信号：购买常标志意图结束，应实时抑制同类推荐，避免刚买又推相同品类。

  - 引入兴趣饱和与唤醒机制：可借鉴自适应饱和门控（ASGU），购买后立即施加“遗忘”掩码，并随时间衰减逐步恢复，结合预测的下次购买周期动态调节。

  - 双路径交叉注意力设计：一条路径抑制已完成意图的历史点击，另一条从长期序列提取补货规律，适合分离即时兴趣与周期性需求。

  - 自监督辅助任务：预测下次购买时间（TTNP）无需人工标注，可迁移到其他推荐场景学习商品生命周期。'
score: 9
source: arxiv-cs.IR
depth: abstract
---

动机：电商序列推荐将购买等同正向偏好，但真实购买常代表兴趣终止（Interest Exit），导致购买后冗余推荐。现有模型忽视动作-意图不对称，引发严重购后体验恶化。

方法：提出端到端框架SAM，显式建模兴趣生命周期。三大核心：1. 双路径交叉注意力——逆行抑制已满足意图对应的历史点击，同时检索长期购买中的个性化补货节奏；2. 自适应饱和门控单元（ASGU）——生成时间敏感软掩码，购入后立即压制相关兴趣，并随预测复购周期临近逐步“唤醒”；3. 自监督下次购买时间预测辅助任务（TTNP），无标注学习潜在商品生命周期。

结果：工业数据集离线实验及在线A/B测试显示，SAM将购后重复率（PPRR）降低超60%。
