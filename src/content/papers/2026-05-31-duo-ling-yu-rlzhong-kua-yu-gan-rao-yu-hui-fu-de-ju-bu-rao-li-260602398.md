---
title: A Local Perturbation Theory for Cross-Domain Interference and Recovery in Multi-Domain
  RL
title_zh: 多领域RL中跨域干扰与恢复的局部扰动理论
authors:
- Lei Yang
- Siyu Ding
- Deyi Xiong
affiliations:
- TJUNLP Lab, College of Intelligence and Computing, Tianjin University
- Baidu Inc.
arxiv_id: '2606.02398'
url: https://arxiv.org/abs/2606.02398
pdf_url: https://arxiv.org/pdf/2606.02398
published: '2026-05-31'
collected: '2026-06-03'
category: Training
direction: LLM多领域RL训练干扰机理与恢复
tags:
- multi-domain RL
- interference
- parameter sparsity
- second-order damage
- refresh training
- LLM
one_liner: 揭示多领域RL顺序训练的稀疏共享冲突子空间，通过refresh即可高效恢复旧领域性能
practical_value: '- 顺序微调LLM多个任务时，可通过简短的“刷新”步骤（用极少量旧域数据再训练几步）以极小代价恢复受损域性能，避免昂贵联合训练。

  - 干扰集中于低维冲突子空间，可在线监测模型顶部稀疏神经元的梯度方向重叠或参数变化冲突，提前预警新任务训练对旧能力的损害。

  - 训练免回滚方法揭示了冲突坐标集的存在，可对已部署模型做选择性参数回退，精准修复特定指标退化而无需全量回滚。

  - 对于电商多技能Agent，不同能力微调可采用LoRA等稀疏适配，冲突时仅需刷新对应适配器，大幅降低跨域干扰风险。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机：** 对LLM进行多领域RL后训练时，顺序训练常导致先验域性能大幅退化。现有灾难性遗忘或全局梯度冲突解释不充分，实验发现即使全模型梯度接近正交，干扰仍存在。

**方法关键点：**
- 单域RL产生稀疏、小幅参数编辑，不同域间top变化神经元重叠弱，但共享活跃计算路径，更新方向决定协同或冲突。
- 构建局部扰动模型，证明后训练域的损害主要来自二阶损伤项，集中于共享冲突子空间。
- 提出简短域刷新（如重新训练几步）可收缩该子空间的有害成分，实现选择性能恢复；同时发现基于稀疏代理冲突坐标集的训练免回滚也能部分恢复性能。

**关键结果：** 按 Code→Math→QA→Creative Writing 顺序训练后，Math 得分降至57.66，仅3步 Re-Math 刷新后回升至66.04，且不影响其他域，平均分达最优66.39。Math-QA对的训练免回滚操作也部分恢复了Math性能，直接证实了局部损伤机制。
