---
title: 'A Unified Per-Token Gating Family for On-Policy Distillation: FKL/RKL Mixing
  with Multi-Channel and Bias Coefficients'
title_zh: 统一 per-token 门控族：FKL/RKL 混合的多通道与偏置参数化
authors:
- Suwan Wu
- Yumeng Lin
- Pengcheng Yuan
- Xiaolong Jiang
affiliations:
- Xiaohongshu Inc.
- Tianjin University
arxiv_id: '2609.11768'
url: https://arxiv.org/abs/2609.11768
pdf_url: https://arxiv.org/pdf/2609.11768
published: '2026-09-10'
collected: '2026-09-12'
category: Training
direction: LLM 知识蒸馏损失门控统一参数化
tags:
- knowledge distillation
- on-policy distillation
- FKL
- RKL
- per-token gating
- LLM
one_liner: 把 on-policy 蒸馏中的 per-token FKL/RKL 门控统一为四系数参数化，EOPD/ToDi 成为其一维特例
practical_value: '- 做 LLM 蒸馏时，可把 FKL/RKL 混合权重从固定标量升级为 per-token 门控 λ_t=σ(a·h_t+b·u(x)+c+d·gap_t)，用
  teacher 熵 h_t、学生/教师 gap_t 等已能计算的信号作为特征，几乎不额外增加工程成本。

  - 可将 EOPD、ToDi 这类已有门控方法放进统一坐标里做 sweep；至少先跑 entropy-only、gap-only、bias-only 三条 1D
  线，再叠加多通道和偏置，比盲调 FKL/RKL 权重更有方向。

  - 显式 bias c 值得单独保留：它等价于一个可学习的全局混合偏好，部署到不同业务语料（商品文案/搜索改写/push 文案）时可以作为任务先验快速调节。

  - 该文在短输出分类任务上方向性收益多，但 n=3 不显著；迁移到电商/推荐文本生成时，建议用多 seed paired replication 评估真实线上收益，别被单
  seed 的 33/36 这类计数误导。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：on-policy distillation 中 FKL/RKL 的 per-token 门控已成常用手段，但 EOPD、ToDi 各自固定单一门控信号和方向，缺少统一比较框架。

方法：将门控参数化为 λ_t=σ(a·h_t+b·u(x)+c+d·gap_t)。其中 h_t 为 teacher 熵，u(x) 为上下文相关项，gap_t 为 student/teacher 差异信号，c 为显式偏置。EOPD、ToDi 的方向对齐代理可看作该参数化的 1D 限制；全族额外引入多通道组合和偏置自由度。

结果：在 TweetEval emotion/hate 任务上，Qwen3-32B teacher 蒸馏 Qwen3-4B student，全族配置在 36 个可比 cell 中有 33 个超过等幅单通道限制；26-cell mean-match 隔离实验中，动态门控在 19 个 cell 超过按 effective KL 匹配的静态基线。扩展到 offensive 任务后，9 个 headline 对比的 3-seed 配对重复实验方向一致，但单点估计更小，n=3 下不显著。作者定位为短输出分类 OPD 中 per-token 门控设计的共享坐标系统。
