---
title: Every Weight Is a Path of Shared Discrete Decisions
title_zh: TWIG：每个权重都是共享离散决策路径
authors:
- Ammar Ali
- Stamatis Lefkimmiatis
affiliations:
- LEAD Lab, ITMO University
arxiv_id: '2610.31931'
url: https://arxiv.org/abs/2610.31931
pdf_url: https://arxiv.org/pdf/2610.31931
published: '2026-10-21'
collected: '2026-10-26'
category: Other
direction: 模型压缩 · 权重离散化
tags:
- TWIG
- Weight Sharing
- Quantization
- Pruning
- Discrete Optimization
- LLM Compression
one_liner: 提出 TWIG 树结构权重表示，统一剪枝、量化、低秩与码本，LLM 权重以更少加法达到与 GPTQ 同等误差
practical_value: '- 业务部署 LLM/推荐模型时可统一压缩流程：TWIG 把剪枝、量化、低秩、码本、权重共享合并为同一树结构决策，避免分阶段工具链（先剪枝再量化再低秩）造成误差累积，可用一个优化目标联合搜索。

  - 对延迟敏感、希望硬件固权/推理加速的电商搜索或广告模型，可尝试将关键层表示为 signed power-of-two 项，使乘法变移位加法，降低电路成本；优先用于
  outlier 明显或冗余大的 FFN/embedding 层，实测此类矩阵可减少更多加法。

  - 工程实现上可借鉴“共享路径继承”思想：让一组权重共享高层离散门（sign/scale/index），仅叶节点不同，既能大幅减少元数据存储，又便于在芯片制造前固化。

  - 当前证据仅来自 5 个权重矩阵，尚未验证全模型端到端精度与吞吐；业务落地前需先做全模型压缩实验，评估与 GPTQ/AWQ 等成熟方案的端到端指标。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：部署神经网络需要离散化/压缩，但现有剪枝、量化、低秩、码本、权重共享各有格式与求解器，且硬件固权需逐权重常数乘法器。权重格式虽已朝共享决策演进（group scales、shared exponents 等），但未统一到底。

方法关键点：TWIG 将每个权重定义为路径末端的小离散决策——符号、2 的幂移位、零门、共享表索引；路径上共享决策被所有子权重继承，存储一次、应用一次。可将任意训练网络写成 TWIG；当决策为 2 的幂时，权重层变成几乎全由连线和加法器构成的电路，适合芯片固定权重。剪枝、量化、低秩、码本、权重共享变成对同一对象的编辑，单一优化器可为整网联合选择；决策选择对应高阶 Boltzmann 机基态问题，可用退火器/量子优化器求解。

关键结果：在 LLM 的 5 个权重矩阵上，flat tree + signed power-of-two 项按权重优化电路成本，无 group scales，3/4-bit 精度下同等层误差比 GPTQ 少 9–15% 加法；强离群矩阵少 20–55%。
