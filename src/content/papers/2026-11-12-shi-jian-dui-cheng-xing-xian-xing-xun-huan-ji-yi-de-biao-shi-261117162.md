---
title: 'Symmetry in Time: A Representation Theory of Linear Recurrent Memory'
title_zh: 时间对称性：线性循环记忆的表示理论
authors:
- Anif N. Shikder
- Ramit Dey
- Jan Minac
- Lyle E. Muller
affiliations:
- Fields Lab for Network Computation, Fields Institute, Toronto ON, Canada
- Department of Mathematics, Western University, London ON, Canada
- Department of Neuroscience, University of Texas at Dallas, Richardson TX, United
  States
arxiv_id: '2611.17162'
url: https://arxiv.org/abs/2611.17162
pdf_url: https://arxiv.org/pdf/2611.17162
published: '2026-11-12'
collected: '2026-11-14'
category: Other
direction: SSM 表示理论与序列建模改进
tags:
- State Space Models
- Representation Theory
- Quaternion
- Sequence Modeling
- State Tracking
- Long-range Memory
one_liner: 用表示理论证明对角SSM无法跟踪非交换群顺序，提出四元数通道HyperSSM仅用5个状态数解决S5任务并泛化25倍
practical_value: '- 若业务中用 SSM/Mamba 等线性注意力模型处理用户行为序列、会话状态等顺序敏感任务，注意默认对角化会丢失输入顺序、只记录行为种类。需要顺序建模时可评估非对角传递矩阵或四元数通道，保持线性推理的同时恢复顺序跟踪能力。

  - HyperSSM 的四元数通道仅增加 4 倍实数状态维度，却能表征非交换旋转与几何变换。对含角度、轨迹、周期性（如用户 24h 行为环、设备姿态）的特征可能比实/复线性层更高效，工程上可直接实现为
  4 通道实数。

  - 论文表明仅用最终答案监督即可学会群结构，适合稀疏标签下的长程状态推断（如从用户长期行为推断会员阶段、偏好演化）。可尝试将循环状态视为隐式记忆，减少人工特征工程。

  - 传递矩阵的块结构（实/复/四元数）可直接解释模型编码了什么变换。在风控、归因或广告竞价需要审计序列模型时，可借鉴这一可解释性视角检查学习到的状态转移。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：主流 SSM 通过将递归对角化实现并行扫描与线性推理，但每个隐藏状态通道乘以输入依赖的标量，这些标量可交换，导致状态只记录哪些输入出现、不记录顺序，之前已观察到状态跟踪失败。

方法关键点：用群表示论形式化状态更新，将输入序列 monoid 映射为线性表示。证明 SSM 能跟踪群当且仅当该群是过渡矩阵生成群的商。由此推出：对角实数和复数值 SSM 只能跟踪可交换群；任何能跟踪群的 SSM 必须把过渡矩阵分裂为实数、复数和四元数上的独立块。据此提出 HyperSSM，增加四元数通道，保持线性时间推理和并行训练，且仅用最终答案监督训练。

关键结果：在近期状态跟踪基准上，HyperSSM 以最多 5 个状态数精确求解群任务，包括 32 生成元的 S5（之前 SSM 处于随机水平），并泛化到比训练序列长 25 倍的长度。进一步利用传递矩阵的可解释性，恢复真实陀螺仪校准、不完美量子比特门旋转和蛋白质骨架几何。
