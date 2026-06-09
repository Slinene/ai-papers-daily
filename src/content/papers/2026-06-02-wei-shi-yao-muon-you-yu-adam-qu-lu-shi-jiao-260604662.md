---
title: 'Why Muon Outperforms Adam: A Curvature Perspective'
title_zh: 为什么 Muon 优于 Adam：曲率视角
authors:
- Shuche Wang
- Fengzhuo Zhang
- Jiaxiang Li
- Dirk Bergemann
- Zhuoran Yang
affiliations:
- National University of Singapore
- Yale University
- University of Minnesota
arxiv_id: '2606.04662'
url: https://arxiv.org/abs/2606.04662
pdf_url: https://arxiv.org/pdf/2606.04662
published: '2026-06-02'
collected: '2026-06-09'
category: Training
direction: 优化器比较 · 曲率与 NDS
tags:
- Muon
- Adam
- Curvature
- Normalized Directional Sharpness
- LLM Training
- Optimizer
one_liner: Muon 因更低的标准化方向锐度 (NDS) 实现更小的二阶曲率惩罚，从而获得更大的一步损失下降。
practical_value: '- 在大规模推荐或 Agent 模型训练中，可尝试用 Muon 替代 Adam，尤其在数据长尾分布下，Muon 可能带来更快的收敛和更好的泛化。

  - 关注 NDS 作为优化器选择的度量：优先选用在训练后段 NDS 更低的优化器，这可能意味着更平滑的收敛和更小的曲率惩罚。

  - Muon 的频谱归一化思想可迁移到其他自适应优化器中：通过显式约束更新矩阵的奇异值能量分布，避免梯度对齐高曲率方向导致的优化震荡。

  - 数据不平衡（如电商用户行为幂率分布）会放大 Muon 的优势，可据此设计自动优化器选取策略：当数据偏度超过阈值时切换至 Muon 类优化器。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Muon 在 LLM 预训练中比 Adam 快约 2 倍，但其几何优势来源不明。本文从优化景观的曲率角度给出解释。

**方法**：
- 对训练损失进行二阶泰勒展开，将一步损失下降分解为一阶增益和二阶曲率惩罚。
- 曲率惩罚进一步拆解为更新范数平方与标准化方向锐度 (NDS)。
- 在 Zipf-PCFG 合成数据上控制不平衡度，分析数据分布对 NDS 的影响；进行层内/跨层曲率分解。
- 构建异质曲率二次问题，证明 Muon 通过平衡不同曲率分量的更新能量，获得更低平均 NDS。

**关键结果**：
- 在匹配验证损失时，Muon 比 Adam 的一步损失下降更大，源于更小的曲率惩罚 (NDS 更低)，而非更新范数差异。
- 数据不平衡程度越高，Muon 的 NDS 优势越显著；训练中后期，Muon 的低 NDS 主要来自更小的层内曲率。
- 理论证明：当曲率异质性足够强时，Muon 相比 GD 获得更低 NDS 和更优的局部二次损失。
