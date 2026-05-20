---
title: Tail Annealing for Heavy-Tailed Flow Matching
title_zh: 尾部退火：面向重尾流匹配的软对数变换
authors:
- Jean Pachebat
affiliations:
- CMAP, École Polytechnique, Institut Polytechnique de Paris
arxiv_id: '2605.20068'
url: https://arxiv.org/abs/2605.20068
pdf_url: https://arxiv.org/pdf/2605.20068
published: '2026-05-19'
collected: '2026-05-20'
category: Training
direction: Flow Matching · 重尾训练技巧
tags:
- Flow Matching
- Heavy-tailed
- Log-transform
- Tail annealing
- Generative model
- Hill estimator
one_liner: 用坐标级软对数变换与Hill诊断，让标准流匹配零架构修改即可生成重尾数据且零发散
practical_value: '- 电商用户行为数据（点击量、购买金额等）常呈现重尾，Log-FM 无需修改现有流匹配架构即可生成高质量重尾样本，用于数据增强或仿真

  - 自适应 Hill 诊断自动识别每个特征的重尾性并决定是否变换，省去人工判断，可集成到自动化数据 pipeline

  - 方法即插即用：训练前对重尾特征施加 soft-log 变换，生成后指数化还原，计算开销极低，适合大规模线上数据

  - 在极端分位数（如 CVaR₉₉）上表现优异且零严重发散，对风险敏感的电商场景（库存压力测试、欺诈检测模拟）有直接应用价值'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：标准流匹配等生成模型受 Lipschitz 架构限制，无法从高斯噪声生成重尾分布（如 Pareto 尾），且重尾数据与高斯插值存在病态。现有方案依赖专用架构或重尾基分布，实现复杂。  
**方法**：提出 Log-FM，训练前对每个坐标应用软对数变换 \(\phi(x)=\mathrm{sign}(x)\cdot\log(1+|x|)\)，将重尾压缩至易建模范围；生成样本后指数化恢复原尺度。通过 Hill 诊断自动判断每维是否需要变换，轻尾维度保持不变。理论直觉：对数映射将 Pareto 尾转化为指数分布，诱导的动力学实现了一种幂变换形式的“尾部退火”。  
**结果**：在 144 配置多变量基准（3 种 copula、维度最高 100、4 种尾指数）上，Log-FM 在 \(W_1\)、CVaR\(_{99}\) 和极端分位数指标全面领先专门基线，且 2880 次运行中零严重发散，验证了简单变换的鲁棒有效性。
