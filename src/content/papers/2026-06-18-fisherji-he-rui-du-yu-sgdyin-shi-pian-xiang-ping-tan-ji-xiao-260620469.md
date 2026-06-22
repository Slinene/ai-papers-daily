---
title: Fisher-Geometric Sharpness and the Implicit Bias of SGD toward Flat Minima
title_zh: Fisher几何锐度与SGD隐式偏向平坦极小值
authors:
- Md Sakir Ahmed
- Kumaresh Sarmah
- Hemen Dutta
affiliations:
- Gauhati University
arxiv_id: '2606.20469'
url: https://arxiv.org/abs/2606.20469
pdf_url: https://arxiv.org/pdf/2606.20469
published: '2026-06-18'
collected: '2026-06-22'
category: Training
direction: 优化理论 · 信息几何平坦性
tags:
- Fisher Information
- Flat Minima
- Riemannian Geometry
- Generalization
- SGD
- Information Geometry
one_liner: 定义重参数化不变的Riemannian sharpness，证明SGD噪声偏向Fisher几何平坦解，并给出泛化界
practical_value: '- 训练推荐模型时，可定期计算参数的 Fisher 锐度（对角 Fisher 近似即可）作为泛化监控指标，替代 Hessian
  谱等欧氏平坦性指标，避免重参数化（如 embedding 缩放、特征归一化）导致的不可比问题。

  - 优化器设计可借鉴梯度噪声协方差与 FIM 成正比的结构：在推荐模型分布式训练中，若按 FIM 方向调整噪声注入，可能自动偏向平坦解，改善尾部物品 / 冷启动场景的泛化。

  - 若团队用 K‑FAC 等二阶优化，其 FIM 估计本身已接近重参数化不变，可作为 flatness‑aware 正则的天然基架，比欧氏 Hessian 更稳定。

  - 注意：论文实验仅覆盖 CNN 与小数据集，直接迁移到大模型或搜索推荐需谨慎；但将 sharpness 纳入早停或 checkpoint 选择的思路可直接复用。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**  
深度学习直觉认为 SGD 偏好平坦极小值且平坦解泛化更好，但 Hessian 迹或最大特征值这类欧氏平坦性度量在保持网络函数不变的重新参数化下会改变，动摇了该直觉的理论基础（Dinh 等）。  

**方法关键点**  
- 在 Fisher 信息矩阵（FIM）诱导的统计流形上定义 **Riemannian 锐度 (S_R)**：基于损失曲率与 Fisher 度规的相容关系，证明 S_R 在光滑函数保持重参数化下严格不变（真 FIM）；实践中用对角经验 Fisher 近似，只得到近似不变性，精确不变需 K‑FAC 等结构化估计器。  
- 将 mini‑batch SGD 的梯度噪声建模为协方差与 FIM 成比例的高斯分布，推导相应的连续时间随机微分方程，得到参数的稳态分布正比于 exp(‑β·S_R)，即概率质量指数级集中在 S_R 低的 Riemannian‑flat 区域。  
- 给出一个由 S_R 显式控制的 PAC‑Bayes 泛化界，从理论上连接几何偏差与测试性能。  

**关键结果**  
- 在 MNIST 和 CIFAR‑10 上，S_R 与验证误差高度相关（欧氏锐度做不到），且 S_R 的降低幅度随学习率 η 与 batch size 比值 η/B 线性增大，与理论预测一致。  
- 验证对角线 FIM 近似的 S_R 已足以体现重参数化不变的泛化跟踪能力。
