---
title: 'D^3-MOPD: Adaptive Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation'
title_zh: D^3-MOPD：自适应动态领域调度的高效多教师蒸馏
authors:
- Zechen Sun
- Zhiwei Zhang
- Fei Zhao
- Juntao Li
- Mu Chuan
- Huayu Deng
- Guojian Zhan
- Wenliang Chen
- Yao Hu
- Min Zhang
affiliations:
- AllSpark Team
arxiv_id: '2608.24987'
url: https://arxiv.org/abs/2608.24987
pdf_url: https://arxiv.org/pdf/2608.24987
published: '2026-08-24'
collected: '2026-08-28'
category: Training
direction: 多教师蒸馏 · 在线动态调度
tags:
- Multi-teacher distillation
- Dynamic scheduling
- Reverse KL
- LLM training
- Domain adaptation
one_liner: 提出零开销动态调度器，复用每领域reverse-KL信号在线调整多教师蒸馏的数据混合比例，大幅提升收敛效率与性能
practical_value: '- 借鉴 per-domain loss/KL 轨迹作为在线调度信号：在多任务/多域推荐模型（如首页推荐、搜索、广告域联合训练）中，定期追踪各任务的收敛速度与剩余提升空间，动态调整采样比例，避免固定混合导致快任务过拟合、慢任务欠训练。

  - 使用 off-process 异步 watcher 实现零开销调度：不侵入训练主循环，适合在现有训练框架中轻量集成，无需改动核心代码即可获得收益。

  - 调度策略可迁移到多场景 LLM 微调：当不同领域数据收敛速度差异大时，优先分配资源给“难但可学”的领域，减少已饱和领域的采样，能显著降低达到目标性能所需的训练步数。

  - 结论“领域越多、收敛模式差异越大，动态调度收益越大”提示：在电商多域多目标场景下，随着接入业务域增多，这类自适应调度可能带来超线性训练效率提升。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
多教师 on-policy 蒸馏（MOPD）通过最小化每领域 reverse-KL 散度将多个领域专家教师压缩到单个学生模型。但现有方法固定每领域数据混合比例，忽略不同领域收敛速度差异显著：快的领域早饱和，慢的领域欠训练，造成计算浪费和性能损失。

**方法关键点**  
提出 D^3-MOPD，一个零开销调度器，直接复用训练中已有的每领域 reverse-KL 信号来在线调整领域混合比例。核心是一个运行在训练进程外的异步 watcher，周期性追踪各领域 KL 轨迹，估计剩余提升空间（remaining headroom）和当前改善速率（improvement rate），据此调整领域采样比例，不修改核心训练循环。该方法可自然扩展到任意数量领域，且领域越多、收敛模式差异越大，调度收益越高。

**关键结果**  
在 Qwen3.6-35B-A3B 学生模型上，从四个领域专家教师蒸馏。与 vanilla MOPD 相比，D^3-MOPD 将平均 student-to-teacher 性能差距缩小到 97%（vanilla 为 63%），达到相同峰值性能所需的 rollout 步数减少约 3 倍；在七个基准测试中有三个超过专家教师。
