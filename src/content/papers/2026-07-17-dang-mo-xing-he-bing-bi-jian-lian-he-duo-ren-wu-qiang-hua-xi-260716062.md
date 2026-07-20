---
title: 'When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector
  Geometry Analysis'
title_zh: 当模型合并比肩联合多任务强化学习：任务向量几何分析
authors:
- S. Aaron McClendon
affiliations:
- Aimpoint Digital Labs
arxiv_id: '2607.16062'
url: https://arxiv.org/abs/2607.16062
pdf_url: https://arxiv.org/pdf/2607.16062
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: Agent模型合并 · 任务向量几何分析
tags:
- Model Merging
- Task Vectors
- Reinforcement Learning
- LLM Agents
- LoRA
- AppWorld
one_liner: 合并独立RL专家在AppWorld上匹敌联合多任务RL，因任务向量近正交使精细合并方法退化为均匀平均
practical_value: '- **合并RL Agent的策略选择**：若各专家任务向量余弦相似度接近零（<0.1），直接模型平均（如TIES、RAM+等复杂方法）即可达到联合训练效果，无需花费精力调优合并超参。

  - **几何诊断工具**：定期监控训练中任务向量间的余弦相似度，若持续增长并超过某一阈值（如>0.2），可提前终止训练或启用更强干扰消解合并法；若始终近正交，则可安全使用简单平均。

  - **支持度与方向解耦的教训**：即使多个LoRA专家修改完全相同模块（支持度高重叠），其参数更新方向仍可能近乎正交。设计合并算法时，不能仅依赖支持度重叠（如RAM）来判别共享与私有知识，应引入方向性指标（如余弦或主子空间对齐）。

  - **独立训练再合并的可行性**：在电商Agent多技能（如搜索、比价、下单）RL训练中，若数据/环境无法集中，可分别训练专项Agent后用平均合并，几乎不损失组合能力。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：模型合并通常用于无法联合训练的场景，但缺乏与真正联合多任务RL的公平比较。该工作在Agent基准AppWorld上，用相同数据训练独立专家与联合模型，对比合并（TIES、RAM+）与联合RL的效果，并从任务向量几何角度解释为何合并方法无差异。

**方法关键点**
- 基座：Qwen3-8B，LoRA rank=16适配所有注意力与MLP投影矩阵。
- RL训练：LOOP（实际退化为RLOO），K=6，奖励为任务单元测试通过率。
- 模型：Difficulty-1专家（仅d1任务）、Difficulty-2专家（仅d2任务）、联合模型（d1+d2），均~10轮迭代。
- 合并：TIES（trim + 符号投票 + 不相交平均）与RAM+（支持度共现划分，独特坐标放大，r_RAM=0.1，α_clip=2.0）。
- 评估：168个test_normal任务，主要指标二进制Task Goal Completion (TGC)，辅以连续部分学分分数。

**关键实验结果**
- TGC：所有RL模型（专家、合并、联合）统计无显著差异（McNemar p均>0.55），但均显著优于基础模型。联合 vs. RAM+ p=1.00，联合 vs. TIES p=0.66。
- 任务向量余弦：d1与d2专家余弦仅0.06-0.10，支持重叠~65%但符号一致率~51.9%（接近随机）。
- 余弦随训练迭代从0.002升至0.103，但仍属近正交（~84°）。地板/天花板校准（随机初始化<1e-4，同权重不同检查点~0.8）确认非LoRA低秩假象。
- 连续指标虽显示合并略低于未合并模型，但分析表明这是平均化行为所致，非能力退化，且指标方向与TGC完全相反。

**核心结论**：在该设置下，合并即均匀平均，因任务向量近乎方向独立；支撑度共现与方向解耦，使RAM等精细操作缺乏干预空间。对于可共享数据的应用，联合训练无额外收益；对于独立训练场景，简单平均合并已足够。
