---
title: 'BOUND: Brief-Guided Corrective Preference Distillation at Search-Control Boundaries'
title_zh: 搜索控制边界的简报引导纠正性偏好蒸馏
authors:
- Qingying Niu
- Ruiyang Ren
- Wayne Xin Zhao
- Yaliang Li
affiliations:
- Renmin University of China
- Alibaba Group
arxiv_id: '2608.08768'
url: https://arxiv.org/abs/2608.08768
pdf_url: https://arxiv.org/pdf/2608.08768
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: LLM搜索代理·漂移纠正与偏好蒸馏
tags:
- Persistent Search Drift
- Preference Distillation
- Search-State Brief
- DPO
- Agent Training
- Search Control
one_liner: 通过任务锚定的搜索状态简报从学生交动中构造状态匹配偏好对，纠正持久搜索漂移
practical_value: '- 训练搜索/对话代理时，可为每个决策时刻构建一份教师端 **search-state brief**（含原始目标、关键约束、已获证据与缺失信息），以此作为训练时的特权参考，避免教师被学生已产生的误导上下文带偏。

  - 利用学生自身交动的失败轨迹构造 **状态匹配偏好对**：失败步骤的原始延续 vs 教师针对该错误生成的纠正延续；成功轨迹中，最早的证据支撑答案 vs 不必要的继续检索。仅在训练时使用这些偏好执行
  DPO，推理时无需额外开销。

  - 偏好对的选择应结合 **brief引导的局部错误评估与 rollout 最终结果**，不预设失败轨迹中每一步都错，也不丢弃成功轨迹中的终止监督信号，以此过滤噪声样本。

  - 电商场景的多步商品检索或客服代理，常因召回的相关文档引发主题漂移或约束丢失；可借鉴 BOUND 在状态层面锚定原始意图与约束，通过 DPO 巩固正确的搜索控制决策。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
大模型搜索代理通过多步检索与推理逐步解决信息需求，但局部相关的证据可能造成 **持久搜索漂移**：错误锚点（替换原始实体）、遗漏关键约束、或滑向局部相关但偏离主目标的子话题。现有训练方法多用完整轨迹监督或结果奖励，难以区分局部合理但与任务偏离的继续。

## 方法
BOUND 是一种 **简报引导的纠正性偏好蒸馏** 框架，只在训练时使用教师端特权信息。

- **搜索状态简报 (search-state brief)**：对每个学生引发的决策时刻状态，教师生成包含原始搜索目标、关键约束、已确认证据、缺失信息、漂移状态的私有结构化描述，作为稳定的任务级参考。
- **决策时刻评估与偏好构造**：教师结合简报评价学生原始延续是否包含可纠正的局部搜索错误。对失败轨迹，将错误延续与针对该错误生成的纠正配对；对成功轨迹，将最早证据支持的答案与不必要的继续检索配对。每个配对共享相同的学生可见状态，仅对比局部搜索决策差异。
- **验证与裁剪**：仅保留通过格式和逻辑验证的配对，且被拒延续必须涉及检索动作，以此确保对比信号聚焦搜索控制边界。
- **DPO 蒸馏**：用 DPO 将所有验证后的状态匹配偏好对蒸馏到学生策略，教师侧简报与计算不入推理。

## 关键结果
在 HotpotQA、MuSiQue、2WikiMultiHopQA、Bamboogle、FRAMES、GAIA、BrowseComp‑Plus 上评估。
- 使用 Qwen3‑4B‑Instruct 初始化，BOUND 在 6 个数据集中 5 个领先，14 项指标里的 12 项最优。
- 相比 Trajectory SFT，Bamboogle 的 EM 提升 **5.6** 个百分点，BrowseComp‑Plus 准确率提升 **4.8** 个百分点。
- 消融证实：去除重定向监督、使用学生自生成纠正、或丢弃简报均显著降低性能；结合简报评估与 rollout 结果比单独使用任一信号均更有效。

> **最值得记住的一句话：** 把原始搜索目标写成教师特权简报，在训练时解剖学生自身的失败步骤，构造不同局域决策的偏好对，就能让模型学会在搜索上下文中守住任务边界。
