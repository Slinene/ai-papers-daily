---
title: 'CADENCE: Closing the Reasoning Gap via Coverage-Adaptive On-Policy Distillation'
title_zh: CADENCE：通过覆盖自适应在策略蒸馏弥合推理差距
authors:
- Satyam Kumar
- Saurabh Jha
arxiv_id: '2607.16955'
url: https://arxiv.org/abs/2607.16955
pdf_url: https://arxiv.org/pdf/2607.16955
published: '2026-07-17'
collected: '2026-07-31'
category: Training
direction: LLM 推理蒸馏 · 在策略蒸馏
tags:
- Knowledge Distillation
- On-Policy
- Reasoning
- KL Divergence
- Coverage-Adaptive
- Dense Reward
one_liner: 用覆盖自适应调度、分叉提升与稠密奖励等六个组件，在单台 Mac 上将 0.5B 学生推理提升 21%+
practical_value: '- **DRIFT 与 COVA 的 token 级前向-反向 KL 切换**：可迁移到业务小模型蒸馏，避免初期学生概率崩溃；在电商搜索
  query 改写或推荐理由生成中，当学生模型输出分布与教师差距大时，可借鉴覆盖自适应的 β 调度，从 reverse-KL 逐步过渡到 forward-KL。

  - **FTB（分叉 token 提升）**：利用高熵 token 位置作为关键“决策点”集中梯度，类似在推荐 Agent 的推理链中，对不确定性高的步骤（如商品属性对比）加强学习信号，提升推理可靠性。

  - **CCD 稠密奖励与部分正确反馈**：将二元对错信号替换为数值相似度部分奖励，适合电商场景中候选商品排序或价格合理性判断等非严格 0/1 任务，可提高训练效率。

  - **全在策略、单机可跑**：蒸馏全程无需数据中心级别资源，64GB 统一内存的 Mac Studio 即可完成，适合中小团队快速迭代推理模型。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：在策略蒸馏用于将大语言模型推理能力迁移给小模型时，存在三个连环失效模式：冷启动时学生给教师偏好 token 的概率几乎为零（冷启动崩溃）；仅基于时间的 KL 散度调度忽略学生当前的覆盖状态；二元奖励稀疏，丢失了部分正确推理链中的信息。

**方法**：CADENCE 框架针对每个问题提出修复。核心 DRIFT 机制在学生采样的轨迹上，于每个 token 位置动态混合前向 KL 与反向 KL 的替代目标（非序列级梯度估计）。六个扩展组件：（A）COVA 覆盖自适应 β 调度，根据学生生成正确 token 的比例有条件地加速从前向到反向的过渡；（B）FTB 分叉 token 提升，利用全局归一化熵参考定位高熵决策点并放大梯度；（C）CCD 稠密奖励，结合答案正确性和错误但接近答案的数值邻近度给予部分反馈，将非零奖励比例从 38% 提升至约 55%；（D）LAP 简短优先的正确 rollout 强化，仅按回复长度归一化；（E）EMR 熵匹配正则化器用于校准；（F）BSD 引导自蒸馏阶段。

**结果**：在 GSM8K 和 MATH-500 上，使用 0.5B 学生从 1.5B 教师蒸馏，pass@1 达 69.8±0.5%（预训练基线 48.7%，教师差距闭合 63.2%）；用 3B 教师可达 72.1±0.4%（闭合 76.2%）。比最强等计算量基线（DRIFT+二元奖励）高 4.4±0.7 分。所有实验在单台 Apple Mac Studio（M 系列，64GB 统一内存）上完成。
