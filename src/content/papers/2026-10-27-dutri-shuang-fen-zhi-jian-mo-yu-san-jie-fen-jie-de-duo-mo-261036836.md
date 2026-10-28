---
title: 'DuTri: Dual-Branch Modeling with Triadic Factorization for Multimodal Multi-Scenario
  Recommendation'
title_zh: DuTri：双分支建模与三阶分解的多模态多场景推荐
authors:
- Jintao Huang
- Chaohua Yang
- Kailiang Hao
- Dugang Liu
- Xing Tang
- Zhong Ming
affiliations:
- 深圳大学
- 深圳技术大学
arxiv_id: '2610.36836'
url: https://arxiv.org/abs/2610.36836
pdf_url: https://arxiv.org/pdf/2610.36836
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: 多场景多模态推荐 · 双分支三阶分解
tags:
- Multi-Scenario Recommendation
- Multimodal Fusion
- CP Decomposition
- Residual Quantization
- Contrastive Learning
- CTR Prediction
one_liner: 提出 DuTri 双分支框架，用 CP 分解和残差量化学习三元协同偏好，指导多模态自适应融合，在多场景推荐上取得最优。
practical_value: '- 多场景多模态推荐不要简单把多模态特征拼进现有 MSR 骨干，可尝试双分支：协同分支专注 ID 交互建模，多模态分支处理内容语义，通过偏好表示桥接，避免参数共享架构在多模态下退化。

  - 用 CP 分解建模用户-场景-物品三维交互，得到用户、场景、物品因子，作为跨场景共享和场景特异的表示，可替代简单的共享嵌入，迁移到多场景 CTR 模型。

  - 残差量化（RQ）将连续偏好因子离散化，提升表示稳定性和泛化，类似于 Semantic ID 的思路，可用于工业推荐中对用户/场景/物品表示进行量化压缩。

  - 对比学习对齐协同物品表示与多模态表示，使协同信号和内容信号互相增强，可借鉴到多模态推荐或图文相关性建模中，提升融合效果。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：多场景推荐需要同时捕捉跨场景共性和场景特性，多模态信息（文本、图像）能提供丰富语义，但现有 MSR 方法通常将多模态特征直接输入原有参数共享架构，这可能不最优。受控实验显示，在 ID-only 下 MSR 骨干优于场景 MLP，但加入多模态后场景 MLP 反而更优，表明跨场景共享机制在多模态下失效，需要专门设计。

**方法关键点**：
- 双分支结构：协作分支建模用户-场景-物品三元交互，多模态分支融合 ID、文本、视觉特征。
- 协作分支采用 CP 分解得到用户、场景、物品因子，经残差量化（RQ）得到离散偏好表示，组合成协作表示。
- 多模态分支用用户和场景偏好通过门控生成模态权重，自适应加权融合多模态表示。
- 物品级对比学习对齐协作物品偏好与模态表示，促进信息交换。
- 预测时拼接用户 ID 表示、协作表示、多模态表示，送入场景特定 MLP。

**关键实验**：在 AntM2C（5 个场景）和 Amazon（3 个场景）数据集上，与多模态基线（Diff-MSIN、LMF、PSRQ 等）和多场景基线（STAR、HMoE、HierRec、AMS 等）对比，DuTri 取得最高 WAUC（AntM2C 0.8632 vs AMS 0.8598；Amazon 0.7437 vs AMS 0.7400）。消融实验证明对齐、CP 监督、RQ、门控等组件均有效。

**最值得记住**：将协同偏好学习和多模态融合解耦为双分支，用三阶偏好作为桥梁来指导融合，比直接早融合参数共享更有效。
