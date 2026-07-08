---
title: 'OmniOpt: Taxonomy, Geometry, and Benchmarking of Modern Optimizers'
title_zh: 'OmniOpt: 现代优化器分类、几何与基准评测'
authors:
- Siyuan Li
- Jiabao Pan
- Yumou Liu
- Zhuoli Ouyang
- Xin Jin
- Xinglong Xu
- Jingxuan Wei
- Shengye Pang
- Jintao Che
- Xuanhe Zhou
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai University
- Westlake University
- Shanghai Jiao Tong University
- UCAS
arxiv_id: '2607.04033'
url: https://arxiv.org/abs/2607.04033
pdf_url: https://arxiv.org/pdf/2607.04033
published: '2026-07-03'
collected: '2026-07-08'
category: Training
direction: 现代优化器统一分类与基准评测
tags:
- optimizer
- benchmark
- taxonomy
- large-scale training
- AdamW
- convergence
one_liner: 提出统一元流水线与LMO框架，构建双维度分类并系统性基准评测100+优化器
practical_value: '- 训练推荐模型（如CTR、CVR预估、多任务学习）时，可根据双维度分类快速筛选优化器：若追求收敛速度与泛化，可优先考虑AdamW；若显存受限，可尝试Lion或分布式优化器。

  - LMO统一框架帮助理解不同优化器的几何含义，方便在自研推荐模型时针对稀疏特征（如embedding）或稠密参数设计混合优化策略。

  - 基准结果显示多数优化器只在少数目标上占优，建议在实际业务中根据优化目标（稳定性、超参鲁棒性、计算开销）组织小规模预实验，避免盲目跟风新方法。

  - 论文提供了108个优化器的代码库和Hugging Face集成，可直接用于推荐模型的训练加速和对比实验。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现代优化器超过100种，在大规模模型训练中选择哪一个成为系统级决策，但缺乏统一视角来理清机制与效果的权衡，研究社区需要一个可操作的坐标系。

**方法**：OmniOpt提出三层统一框架。①**五阶段元流水线**：将任意优化器更新分解为T1（自适应矩）、T2（矩阵结构方法）、T3（离散化与量化）、T4（状态压缩）、T5（曲率与几何）五个阶段，发现多数方法只涉及其中的1-2个阶段。②**LMO数学统一**：用范数约束的线性最小化oracle统一表述不同优化器的核心操作。③基于上述两点构建**双维度分类**：维度A为方法论家族（5大机制族共108个方法），维度B为优化效果目标（收敛效率、计算成本、内存成本、稳定性、超参鲁棒性、泛化）。在语言模型预训练和图像分类两个领域，对多个尺度模型进行系统Benchmark，评估每个家族在不同目标上的表现，并标出优劣权衡。

**关键结果**：提供了完整的优化器家族效果剖面图，明确了不同机制与目标的对应关系，例如自适应矩方法在收敛效率和泛化上整体占优，但计算和内存开销较大；矩阵结构方法在内存上更有优势等。论文给出了面向显式目标和机制假设的优化器选择指南，并指出了未来发展方向。
