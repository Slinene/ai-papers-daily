---
title: 'Don''t Rewrite the SID Map: Topology Preservation for Generative Retrieval
  in Dynamic E-Commerce Search'
title_zh: 别重写 SID 映射：动态电商搜索生成式检索的拓扑保持
authors:
- Jianbo Zhu
- Xing Fang
- Xiaopeng Chu
- Mingmin Jin
- Jing Wang
- Bokang Wang
- Jiaqi Ye
- Xiang Zhang
affiliations:
- Taobao & Tmall Group of Alibaba
- Nankai University
- University of Science and Technology of China
arxiv_id: '2610.26105'
url: https://arxiv.org/abs/2610.26105
pdf_url: https://arxiv.org/pdf/2610.26105
published: '2026-10-19'
collected: '2026-10-20'
category: GenRec
direction: 生成式检索 · SID 拓扑保持
tags:
- Semantic ID
- Generative Retrieval
- E-commerce Search
- Dynamic Update
- Topology Preservation
- Semantic Drift
one_liner: 系统量化 SID 重映射损害，提出冻结旧 SID/插入新物品/热启动的拓扑保持更新原则，线上 GMV +1.16%
practical_value: '- 生产级生成式检索更新 SID 映射时，优先冻结旧 item 的 SID，新 item 按业务价值插入；避免整体重映射。该方法在
  TmallAPP 7 天热启动更新 + 每日插入新 SID 的线上方案中带来 UCTCVR +0.29%、GMV +1.16%。

  - 离线评估必须同时看窄 beam 和宽 beam：宽 beam 会掩盖语义漂移。文中映射刷新在 HR@1000 仅掉 8.33-10.85%，但 HR@1 掉
  41.78-62.05%。如果线上 serving 用窄 beam，宽 beam 离线指标会给出虚假安全感。

  - warm-start 直接 fine-tune 旧 checkpoint 即可，不要做 model soup / weight interpolation。Frozen
  warm-start 对旧 item HR@1 提升约 10%，新 item HR@1 提升约 109%；而权重混合同等或更差。若没有算力做 warm-start，宁可不训练继续冻结旧
  SID，也不要重映射后微调。

  - 电商大 item 量级下，hybrid collision-aware SID 设计可控：头部 top-100 唯一 token，尾部共享 bucket，比
  full-sparse 略优且更省码本；可作为生成式检索落地的工程选择。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

生成式检索把 item 检索变成自回归生成 Semantic ID（SID）序列。在电商搜索这种动态环境里，item 不断新增、业务信号持续变化，SID 映射和模型必须周期性更新。但每次更新都可能让模型已学到的解码路径失效：同一个 SID 推理时解析到不同 item，即 semantic drift。此前工作多关注如何构造更好的初始 SID，缺少对“映射变化程度 → 检索质量损失”的系统量化，也常忽略宽 beam 评估对 drift 的掩盖效应。

**方法关键点**

- SID 三层结构：前两层由 RQ-VAE + query-item 对比学习得到语义前缀，第三层按业务价值排序 token；采用 hybrid collision-aware 设计，头部 top-100 唯一 token，尾部共享 bucket。
- 更新策略拆成两个独立维度：mapping policy（Full-Re / Frozen / Thresholded）与 training strategy（no-retrain / warm-start）。warm-start 只重训第三阶段，低学习率续训。
- 模型基于 Qwen2.5-0.5B，三阶段训练：Item→SID、Query→SID、User+Query→SID。

**关键实验与结果**

在 67 天大规模电商搜索日志上，30 天初始训练 + 30 天更新周期 + 7 天第二周期验证。结论：

- 宽 beam 掩盖 drift：映射刷新时 HR@1 掉 41.78-62.05%，HR@1000 仅掉 8.33-10.85%。
- 重映射比例 γ 与检索质量严格单调负相关：γ 从 0% 到 72.75%，HR@1 最多掉 42.66%。
- 同样 warm-start 预算下，Full-Re 仍明显弱于 Frozen；Full-Re 训练后甚至不如 no-retrain 的 Frozen，说明模型已内化 SID 空间拓扑，短预算续训练无法修复拓扑破坏。
- Frozen warm-start 对旧 item HR@1 提升约 10%，新 item HR@1 提升约 109%；直接使用新 checkpoint 优于 model soup。
- 三周线上 A/B：UCTCVR +0.29%，GMV +1.16%。

**最值得记住的一句话**

插入新物品、冻结旧物品；能 warm-start 就 warm-start，否则就冻结；永远不要改变模型已经学过的 SID。
