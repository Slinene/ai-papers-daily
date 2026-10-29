---
title: Truncate or Not? A Scaling Study of Looped Transformers with Truncated Backpropagation
title_zh: 截断与否？循环Transformer截断BPTT的缩放研究
authors:
- Xuyuan Xiong
- Siyu Chen
- Zihan Shao
- Yue Su
- Weiyang Jin
- Ping Luo
- Zhuoran Yang
- Xihui Liu
affiliations:
- MMLab, The University of Hong Kong
- Yale University
arxiv_id: '2610.26030'
url: https://arxiv.org/abs/2610.26030
pdf_url: https://arxiv.org/pdf/2610.26030
published: '2026-10-19'
collected: '2026-10-29'
category: Training
direction: 循环Transformer训练与缩放律
tags:
- Looped Transformer
- BPTT
- Truncated Backpropagation
- Scaling Law
- Training Efficiency
one_liner: 拟合统一缩放律发现完整BPTT优于截断，两圈循环用27%少参数和8%多计算达到更低验证损失
practical_value: '- 若在推荐/广告模型中采用共享层块的循环结构以减少参数量，不要为了省显存而截断BPTT；在同等总计算预算下，完整BPTT通过更少前向循环反而效果更好，可优先降低循环次数而非截断反向传播。

  - 缩放律表明截断会“折扣”有效参数，因此在估算模型容量或做资源规划时，应把截断后的有效参数而非原始参数纳入考虑，尤其对于参数量敏感的端侧或在线学习场景。

  - 当业务强约束参数量（如模型部署在边缘设备），可考虑训练两圈完整BPTT的循环Transformer，比计算最优非循环模型少约27%非embedding参数，且仅需多约8%训练计算，适合参数受限但训练算力相对宽裕的情况。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：Looped transformers复用同一层块以增加计算深度而不增加可训练参数，训练依赖BPTT。为节省训练开销，通常将BPTT截断至最后几个循环，但截断引入有偏梯度，可能削弱循环带来的收益。

方法：作者系统研究截断的价值，联合改变模型规模、训练token数、前向与反向循环数，进行近600组训练实验，并用“有效参数”概念拟合统一缩放律，刻画循环与截断的联合效应。

关键结果：尽管截断能节省训练计算，但拟合的缩放律在联合优化前向与反向循环数时更倾向于完整BPTT；在相同计算量下，完整BPTT搭配更少循环始终优于同算力的截断设置。定律进一步指出：固定模型大小时，计算最优的循环数和训练token数都随计算预算增长；当模型大小也可调整时，两圈完全训练的循环是最优设置。该设置相比计算最优的非循环模型，在更低验证损失的同时，非embedding参数减少约27%，训练计算仅增加约8%。
