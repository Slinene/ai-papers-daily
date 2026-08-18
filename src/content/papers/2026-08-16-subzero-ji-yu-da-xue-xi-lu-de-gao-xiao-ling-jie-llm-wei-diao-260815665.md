---
title: 'SubZero+: Efficient Zeroth-Order LLM Fine-Tuning via Large Learning Rates'
title_zh: SubZero+：基于大学习率的高效零阶 LLM 微调
authors:
- Ziming Yu
- Shuyao Xiao
- Xingyu Zhao
- Sike Wang
- Pan Zhou
- Peiyu Zang
- Xiangda Yan
- Yongjie Yang
- Jia Li
affiliations:
- Beijing Normal University
- Singapore Management University
- Xiaomi Inc.
- Beijing Key Laboratory of Artificial Intelligence for Education
- Engineering Research Center of Intelligent Technology and Educational Application
  (MOE)
arxiv_id: '2608.15665'
url: https://arxiv.org/abs/2608.15665
pdf_url: https://arxiv.org/pdf/2608.15665
published: '2026-08-16'
collected: '2026-08-18'
category: Training
direction: 零阶优化 · 低秩子空间微调
tags:
- Zeroth-Order Optimization
- LLM Fine-Tuning
- Low-Rank Subspace
- Adam
- Memory-Efficient
- Multi-Query
one_liner: 在低秩子空间内多查询梯度估计+低秩Adam+Haar符号校正，让零阶微调能使用大学习率并稳定提升性能
practical_value: '- 在显存受限的 LLM 微调/适配任务中（如 24GB 卡微调 8B 模型、边缘端私有化部署），可直接借鉴 SubZero+
  的“低秩子空间内多查询 ZO”方案：每步 K+1 次前向，无反向传播，显存接近推理；在相同前向预算下，K=50-100 可显著提高稳定性和准确率。适合 query
  生成、文案生成等轻量生成任务的快速适配。

  - 若业务里已有 LoRA 等低秩适配模块，可将优化器换成“子空间 Adam”：在低秩参数上维护 r×r 的一阶/二阶矩，按元素自适应步长，几乎不增加显存，但能扩大可用学习率范围、减少调参成本。对广告标题生成、搜索词推荐等多场景快速迭代尤其有用。

  - 实现注意：用 QR 分解生成随机投影矩阵时，务必对 Q 按 R 对角元素做 sign correction，否则投影矩阵不是 Haar 分布，会导致方向性偏差，影响优化稳定性。该工程细节可落地到任何使用随机子空间/扰动的算法中（如差分隐私、对抗训练、ZO
  超参搜索）。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：Zeroth-order (ZO) 优化让 LLM 微调无需反向传播，可将激活内存降到推理级，适合显存受限场景；但其梯度估计方差随参数量增大，导致学习率极小、收敛慢且对学习率极敏感。SubZero 用层内低秩子空间把方差从 O(d) 降到 O(r^2)，但仍使用单查询+SGD，且 QR 子空间构造存在实现依赖的方向偏差，未能释放大学习率和自适应优化潜力。

**方法关键点**：
- 多查询子空间梯度估计：固定每层投影矩阵 U_i,V_i，在同一低秩子空间内采样 K 个扰动，用 K+1 次前向（1 个 baseline + K 个扰动）计算平均低维梯度；信号在子空间基底上对齐、正交噪声被抵消，缓解 multi-query paradox，避免 O(d) 辅助状态。
- 低秩子空间 Adam：在 r×r 子空间内维护一阶/二阶矩，按元素自适应步长，按层曲率调整更新幅度；内存仅增 2r^2 每层，仍为推理级显存。
- QR 符号校正：对 torch.linalg.qr 输出按 R 对角线符号翻转 Q 对应列，保证投影矩阵 Haar 分布，消除实现依赖方向偏差。

**关键实验与数字**：
在 OPT-1.3B/13B/30B、LLaMA3.1-8B、Qwen2.5-32B 上跑 SuperGLUE，覆盖 FT 和 LoRA，对比 MeZO、SubZero、FO Adam。FT 平均准确率：OPT-1.3B 上 66.3（MeZO 64.6，SubZero 65.5）；LLaMA3.1-8B 上 83.3（82.3/82.5）；OPT-13B 上 73.0（69.9/70.3）；Qwen2.5-32B 上 87.4（MeZO 83.6，SubZero 85.1）。LoRA 方案下平均领先约 2 个百分点。学习率鲁棒性：SST-2 上 SubZero+ 最优 LR 2e-2 得 86.5%，LR 提 1.5 倍仅降 0.5pp；MeZO 最优 LR 1e-4 得 83.3%，LR 加倍掉至 51.7%。显存：OPT-13B FT 下 SubZero+ 仅比 MeZO 多约 1%。

**最值得记住的一句话**：多查询与低秩子空间结合，是在不牺牲推理级内存的前提下，让 ZO 微调用上大学习率和 Adam 的关键。
