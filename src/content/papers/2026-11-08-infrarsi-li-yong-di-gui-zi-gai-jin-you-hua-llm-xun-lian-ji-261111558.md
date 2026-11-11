---
title: 'InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure'
title_zh: InfraRSI：利用递归自改进优化 LLM 训练基础设施
authors:
- InfraRSI Team
- Yuchuan Tian
- Haocheng Mei
- Ye Yuan
- Chao Xu
- Boxun Li
- Guohao Dai
- Kai Han
- Allen Chen
- Yunhe Wang
affiliations:
- Peking University
arxiv_id: '2611.11558'
url: https://arxiv.org/abs/2611.11558
pdf_url: https://arxiv.org/pdf/2611.11558
published: '2026-11-08'
collected: '2026-11-11'
category: Training
direction: Agent 自动化训练基础设施调优
tags:
- Recursive Self-Improvement
- Agent
- LLM Training
- Infrastructure Optimization
- MoE
- MFU
one_liner: 五阶段 Agent 工作流用全局执行时间与截尾内存模型，实现 LLM 训练最高 2.75 倍加速与 MFU 提升至 30%
practical_value: '- 五阶段 Agent 工作流（init/doctor/run/report/apply）可作为电商/广告大规模模型训练调优的自动化框架：固定可编辑范围与任务契约，防止优化过程牺牲精度或稳定性。

  - 同时拟合全局执行时间模型和截尾峰值内存模型，把 OOM 失败样本也纳入建模，用于预估每个配置的内存成本，适合业务中超参/资源配置搜索时降低试错成本。

  - 在自动化调优中加入多指标不变性约束（loss/timing invariants）可有效防止 reward hacking，可直接迁移到推荐系统 Agent
  自动优化中，避免短视的加速/内存优化损害线上效果。

  - 跨硬件经验银行与在线先验修订机制值得借鉴：按集群/GPU 架构沉淀优化经验，并将 LLM 的先验速度估计用实测数据校准，能加速多环境模型训练调优。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
分布式 LLM 训练吞吐受启动配置、算子内核、通信调度等多因素紧耦合影响，单个改动容易导致 OOM、编译器冲突、测量抖动或数值漂移。现有调优器或编码 Agent 通常从单一配置贪心迭代，难以全局权衡速度与内存。

## 方法关键点
InfraRSI 提出五阶段 agentic 工作流：init 锁定可编辑范围与固定任务契约（负载、loss、时间不变性），防止 reward hacking；doctor 分析基线阶段并校准集群噪声；run 从多样化经验种子配置初始化，全局拟合执行时间和截尾峰值内存模型（含 OOM 失败样本），据此估算各设置的内存成本，修订 LLM 速度先验，将内存消耗型优化与省内存配置和代码补丁配对；report/apply 审计源码路径、核算失败试次成本并提交改进。

## 关键结果
在四个单节点/多节点 dense 和 MoE LLM 训练负载上，InfraRSI 实现最高 2.75× 加速，平均 MFU 从 17.4% 提升至 30.0%，超过现有配置调优器和编码 Agent，并能跨 GPU 架构迁移经验。
