---
title: Optimizing Effective Training Time for Large-Scale Recommendation Systems
title_zh: 优化大规模推荐系统训练的有效训练时间
authors:
- Mingming Ding
- Ruilin Chen
- Yuzhen Huang
- Hang Qi
- Menglu Yu
- San Tan
- Damian Reeves
- Boris Sarana
- Kevin Tang
- Satendra Gera
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2610.02057'
url: https://arxiv.org/abs/2610.02057
pdf_url: https://arxiv.org/pdf/2610.02057
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: 大规模推荐训练效率优化
tags:
- Effective Training Time
- Training Efficiency
- PyTorch 2
- Checkpointing
- Distributed Training
- Recommendation Systems
one_liner: 定义ETT%并优化推荐训练生命周期开销，使6个模型平均ETT提升15.5个百分点
practical_value: '- 建立两级 ETT% 看板：把 TTS / NoF / TTR 再拆到调度、trainer 初始化、PT2 编译、wasted
  training、shutdown，并映射到 owner，设置 service level 告警。电商/广告训练平台可直接照搬，避免只盯 MFU。

  - 优先优化冷启动与恢复共享路径：用 synthetic fast-batch 解除数据管道预热与 PT2 编译的串行依赖，把初始化阶段并行化。因为恢复会重复冷启动，收益按
  (1+NoF) 放大。

  - PT2 编译治理很划算：对变化维度做 mark_dynamic，剪裁 Triton autotune 并固化为静态配置，稳定 symbolic hash，使用
  Mega-Cache 复用编译产物；冷缓存编译从 2050s 降到 254s。

  - checkpoint 和发布拆离 GPU 关键路径：异步 checkpoint + PyTorch native staging 可降低 save blocking
  约 77%；把模型发布从 trainer 内改为 anchor checkpoint + standalone CPU job，每个 job 可释放约 30 分钟
  GPU 占用。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
推荐模型需要持续吸收新用户行为，但在 Meta 最大广告推荐训练中，只有 50-60% 的端到端 wall time 真正训练新数据；初始化、编译、checkpoint、发布、失败恢复等生命周期开销大量占用 GPU。MFU 只看 step 内效率，Goodput 又不够定位到可负责的基础组件。因此提出 ETT% 和两级分解，把空闲 GPU 时间变成可治理指标。

**方法关键点**
- ETT% = 1 - (TTS + NoF × TTR) / E2E wall time；L2 拆成调度、trainer 初始化、PT2 编译、有效训练、wasted training、shutdown，每项有 owner。
- Trainer 初始化：消除 per-table all_gather，用 synthetic fast-batch 解除 DPP warm-up 与 PT2 编译串行依赖，并行初始化组件，TTS 累计降 41%。
- PT2 编译：mark_dynamic 减少动态 shape 重编译，跳过部分 built-in tracing，剪裁 Triton autotune，修 symbolic hash，使用 Mega-Cache 复用；冷缓存编译 2050s→254s（87.6%）。
- Checkpoint/发布：异步 checkpoint + PyTorch native staging 降低 save blocking 约 77%；standalone CPU 发布替代 in-trainer publishing，shutdown 省约 30 分钟/job。

**关键实验**
7 个推荐/排序模型，8–2000 张 H100，配对 baseline/optimized，固定 2 次 induced failures，各跑 10–12h。ETT% 从 59–85% 提升到 80–93%，平均 +15.5 pp；最大的 workload 达 85%。恢复路径贡献 58% 的时间节省，TTR 降幅为 TTS 降幅的 1.8–8.6 倍；fleet-wide ETT% 从约 80% 升到 90% 以上。

最值得记住的一句话：优化冷启动/恢复共享路径的收益会按 (1+NoF) 放大，训练效率治理必须把生命周期当成一等公民。
