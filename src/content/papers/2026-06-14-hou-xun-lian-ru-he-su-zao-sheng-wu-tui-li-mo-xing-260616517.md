---
title: How Post-Training Shapes Biological Reasoning Models
title_zh: 后训练如何塑造生物推理模型
authors:
- Lukas Fesser
- Hanlin Zhang
- Michelle M. Li
- Eric Wang
- Bryan Perozzi
- Shekoofeh Azizi
- Sham M. Kakade
- Marinka Zitnik
affiliations:
- Harvard University
- Google DeepMind
- Google Research
arxiv_id: '2606.16517'
url: https://arxiv.org/abs/2606.16517
pdf_url: https://arxiv.org/pdf/2606.16517
published: '2026-06-14'
collected: '2026-06-28'
category: Training
direction: 多阶段后训练与泛化权衡分析
tags:
- post-training
- generalization
- over-specialization
- SFT
- RL
- biology
one_liner: 系统分析CPT、SFT、RL对生物推理模型泛化的不同影响，表明ID/OOD权衡取决于阶段组合而非单调提升
practical_value: '- **SFT 过拟合警告**：SFT 持续提升分布内 (ID) 效果，但分布外 (OOD) 性能会在早期达到峰值后下降。推荐系统微调时需监控
  OOD 指标，避免过度适配训练用户/物品分布。

  - **RL 恢复泛化**：在强 SFT 检查点上加 RL（奖励信号与任务对齐）可提升 OOD 并部分恢复泛化。对电商搜索/推荐中的个性化与冷启矛盾，可设计 RL
  阶段来对冲过拟合。

  - **训练预算分配**：固定总训练成本下，短 SFT + 大 RL 预算的 ID-OOD 权衡最佳。实际落地时，可优先保证 SFT 收敛早期即切换 RL，而非一味延长
  SFT。

  - **阶段非对称适配**：不同阶段对模型容量要求不同，CPT 受益于大模型，而 SFT/RL 增益更依赖质量。在大模型推荐系统中，可先 CPT 对齐领域语言，然后用少量高质量
  SFT 和充足 RL 调优。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：生物推理模型结合语言模型与多模态生物基础模型，但其后训练各阶段（CPT、SFT、RL）如何影响推理与泛化仍不清楚，尤其何时提升性能、何时导致过度专业化。

方法：在基因组学、转录组学和蛋白质三种生物模态上，控制骨干模型、CPT、SFT、RL 四个变量，训练超 100 个模型，系统测量 ID 和 OOD 性能。

关键结果：
- CPT 通过对齐生物语言提升下游性能。
- SFT 稳定提高 ID，但 OOD 性能先升后降，过度 SFT 导致泛化退化。
- RL 在强 SFT 检查点上使用对齐奖励，可提升 OOD 并部分恢复泛化。
- 固定后训练预算下，最佳 ID-OOD 折衷为短 SFT + 大 RL 分配，且各阶段适应容量不对称。

结论：生物推理性能并不随监督或计算量单调提升，而是取决于阶段组合。
