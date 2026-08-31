---
title: 'Deriving Scaling Laws for OpenEuroLLM Models: Learning Rate, Batch Size and
  Loss'
title_zh: 推导 OpenEuroLLM 模型的缩放定律：学习率、批量大小与损失
authors:
- Niccolò Ajroldi
- Diana Alexandra Onutu
- Haider Al-Tahan
- Jörg Franke
- Sampo Pyysalo
- Jenia Jitsev
- Aaron Klein
affiliations:
- ELLIS Institute Tübingen
- Eindhoven University of Technology
- Georgia Institute of Technology
- University of Freiburg
- Jülich Supercomputing Center (JSC)
arxiv_id: '2608.28308'
url: https://arxiv.org/abs/2608.28308
pdf_url: https://arxiv.org/pdf/2608.28308
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: LLM 预训练超参缩放定律
tags:
- Scaling Laws
- Learning Rate
- Batch Size
- Pretraining
- OpenEuroLLM
one_liner: 系统研究 LLM 预训练中学习率与 batch size 的联合最优缩放及边际演化，并刻画损失对模型容量和数据规模的依赖
practical_value: '- **在业务微调或预训练领域大模型时，先做小规模超参扫描，再用拟合的缩放关系外推到大模型**：避免在全尺寸模型上重复扫描 learning
  rate 和 batch size，节省算力；尤其适合电商 search/推荐语料上训练 Query 生成、意图识别或商品描述生成模型。

  - **采用 Warmup-Stable-Decay 三段式 schedule 时，关注 stable 与 decay 阶段最优超参是否可迁移**：如果发现最优
  lr/bs 不迁移，需要在 decay 阶段单独调参；这对追求最终 loss 最优的领域模型训练有直接指导意义。

  - **用显式建模模型容量与数据规模交互的 scaling forms 判断欠训练/过训练**：在有限数据预算（如电商垂直域语料）和模型规模约束下，预估增加数据或参数带来的
  loss 收益，辅助资源分配决策。

  - **开源全部预训练 runs 可直接复用为 baseline 或 warm start**：若企业计划从零预训练多语言/英语为主的电商领域 LLM，可参考其
  scaling 流程与超参选择，减少摸索成本。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 预训练中 learning rate 和 batch size 的选取直接影响训练效率与 scaling law 的准确性。若超参未随模型容量和数据规模正确缩放，测得的性能会反映超参误调而非架构或数据特性。需要明确最优 learning rate 与 batch size 的联合缩放关系，以及它们各自随模型和数据规模的边际演化。

**方法关键点**：
- 研究联合最优 learning rate 和 batch size 的缩放行为，并单独分析两者的边际演化，建立模型捕捉这些关系。
- 采用 Warmup-Stable-Decay learning rate schedule，考察 broad hyperparameters、模型规模和数据预算下的 annealing 收益，并检验最优 learning rate / batch size 在 stable 与 decay 阶段是否可迁移。
- 评估近期提出的显式建模模型容量与数据集大小交互的 scaling forms，用于刻画 undertraining 和 overtraining 两种状态。

**关键结果**：显式交互式 scaling forms 能有效捕捉实验中的 undertraining 与 overtraining 区域；该工作为未来 OpenEuroLLM 模型开发建立了首个 baseline 和 scaling procedure，并开源全部预训练 runs 集合。
