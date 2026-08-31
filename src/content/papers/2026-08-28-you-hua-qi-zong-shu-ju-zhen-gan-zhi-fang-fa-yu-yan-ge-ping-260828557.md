---
title: 'Blog: Survey of Optimizers'
title_zh: 优化器综述：矩阵感知方法与严格评估协议
authors:
- Ruoran Xu
arxiv_id: '2608.28557'
url: https://arxiv.org/abs/2608.28557
pdf_url: https://arxiv.org/pdf/2608.28557
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: 训练优化器设计空间与评估协议
tags:
- optimizer survey
- matrix-aware methods
- AdamW
- Muon
- Shampoo
- schedule-free
one_liner: 沿时间估计、更新几何、时间线管理、表示与系统四轴综述优化器，指出矩阵感知有效但无普适AdamW替代
practical_value: '- 微调推荐/搜索排序大模型或训练生成式推荐模型时，AdamW仍是默认基准；若Transformer权重矩阵占比高，可对attention投影层、embedding层分组试验Muon/Shampoo等矩阵感知方法，但需控制调优预算，避免一次性全量替换。

  - 工程上部署低精度训练或分片训练时，优化器状态量化会直接影响收敛与最终业务指标（如CTR AUC、NDCG），需在业务验证集上确认，不能只看训练loss。

  - 面对小批量在线学习或流式更新场景，可尝试schedule-free或小批量校正方法，降低对学习率调度和batch size的敏感性，减少调参成本。

  - 建立优化器评估协议：固定数据量、批量大小、参数分区、训练时长和硬件环境，同时报告tokens/s或samples/s、显存占用与最终业务指标，避免单维度对比得出误导性结论。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：2025–2026年神经优化不再只是Adam变体序列；设计单元从坐标扩展到矩阵和层，从固定训练时间线到时间策略，从数学更新规则到需经受分片和低精度计算的表示。

方法关键点：survey沿四个基本独立轴组织优化器：时间估计（temporal estimation，梯度历史统计）、更新几何（update geometry，如Muon的谱归一化、Shampoo和SOAP的历史矩阵统计、自适应与混合矩阵方法）、时间线管理（horizon management，如schedule-free训练、小批量校正）、表示与系统（representation and systems，如内存高效优化器、量化优化器状态）。

关键结果：矩阵感知方法是真实进展，但没有上下文无关的AdamW替代品；最佳选择随模型规模、数据-参数比、批量大小、调度、参数分区、调优预算以及目标指标（tokens、FLOPs、wall-clock time、memory）变化。实践后果是优化器设计的组合视角和更严格评估协议。无具体数值，主要为定性结论。
