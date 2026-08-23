---
title: 'Multi-Method Causal Evidence Synthesis: Ranking Candidate Drivers by Convergent
  Cross-Method Evidence from Observational Data'
title_zh: 多方法因果证据合成：从观察数据中按交叉方法收敛证据排序候选驱动因素
authors:
- Manish Gupta
- Dipanjan De
affiliations:
- Tricon Infotech
arxiv_id: '2608.20187'
url: https://arxiv.org/abs/2608.20187
pdf_url: https://arxiv.org/pdf/2608.20187
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 因果证据合成 · 多方法融合
tags:
- Causal Inference
- Evidence Synthesis
- Ensemble
- Observational Data
- Hypothesis Prioritization
one_liner: 提出MCES框架，融合11种方法、8类数学传统，用收敛证据分数对候选驱动因素排序，避免单一方法误判。
practical_value: '- 在归因/特征筛选场景代替单一SHAP或回归：对同一面板数据（用户×时间×实验外）跑多个因果/相关方法（Granger、回归、IV等），输出归一化后线性意见池，优先看多方法共同指向的
  driver-outcome 对；可降低单方法假设失配带来的假阳性。

  - 先用 Structural-Behavioral Decomposition 删除定义性/代数关系：例如 CTR=点击/曝光、GMV=单价×单量这种恒等特征若作为候选
  driver，会天然高分；先识别并移除这类 tautological pairs。

  - 将 CES 作为假设生成工具而非因果结论：用于实验前排序候选干预点，不用它替代 AB 测试；可结合业务已有实验/反事实做 scenario-specific
  calibration，限制外推。

  - 工程化：方法池可并行执行，输出统一 [0,1] 归一化，成本可控；建议保存方法级别证据矩阵，便于审计和 case 复盘。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：实践中 observational causal inference 常用单一方法（回归、SHAP）并当因果真相；自动方法选择、结构集成也少跨数学传统。

**方法关键点**：MCES 对面板数据跑 11 种方法、8 类数学传统；先 Structural-Behavioral Decomposition 移除 candidate driver 中的定义性代数关系；输出标准化到 [0,1] 后以线性意见池合成 CES，衡量不同假设方法指向同一 driver-outcome 关系的收敛程度。定位为假设优先级排序，不声称干预性因果识别。

**关键结果数字**：在合成数据+Sachs+6个BN benchmark+两个合成域上，主场景 Precision@5=1.0、Precision@10=0.96；null pairs 达到 Moderate+ 收敛的比例低；证明无单方法在所有场景最优，MCES 是 method-agnostic default。
