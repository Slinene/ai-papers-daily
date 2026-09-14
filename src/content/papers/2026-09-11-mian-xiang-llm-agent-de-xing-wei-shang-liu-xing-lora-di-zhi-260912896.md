---
title: Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents
title_zh: 面向 LLM Agent 的行为商流形 LoRA 低秩适配框架
authors:
- Pengyang Zhou
- Xiaobin Tu
- Zhengxi Liu
- Rongkun Xue
- Haochen Li
- Miancan Liu
- Ziyuan Chen
- Yinggui Wang
- Jinkui Ren
- Xiantao Zhang
affiliations:
- Alibaba Cloud
arxiv_id: '2609.12896'
url: https://arxiv.org/abs/2609.12896
pdf_url: https://arxiv.org/pdf/2609.12896
published: '2026-09-11'
collected: '2026-09-14'
category: Training
direction: LLM Agent 低秩适配优化
tags:
- LoRA
- LLM Agents
- Low-Rank Adaptation
- Behavior Quotient
- Multi-task Learning
- Decision Distribution
one_liner: 通过行为商流形平衡冗余更新并保持决策分布的低秩适配方法
practical_value: '- 若业务中需要用 LoRA 微调多能力/多任务 LLM Agent，可考虑用单个 adapter 替代多 adapter 部署，以降低存储与路由开销；但需注意多样轨迹下的冗余更新与压缩失真问题。

  - 从决策分布而非权重空间定义更新冗余：在电商/推荐场景微调多目标策略模型时，梯度方向可能在参数上不同但在输出分布上等价，可通过行为商流形上的局部密度对样本或轨迹重新加权，缓解对重复行为模式的过度拟合。

  - DPC 的低秩压缩思路值得借鉴：在压缩策略模型或生成式推荐组件时，不应只最小化权重误差，还要约束决策分布失真，这对保持线上行为一致性很重要。

  - 方法偏理论，实现复杂度较高；如果团队已有多 adapter LoRA 路由的工程基础，迁移价值有限，但 BQB 中“按行为分布密度加权更新”的思路相对轻量，可以局部尝试。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
LLM Agent 通常需要任务特定微调，LoRA 是常用高效方案。多 adapter 设计会带来存储增长和推理路由开销，而单个 LoRA 在多样化 agent 轨迹下存在两个问题：一是不同轨迹虽然参数梯度不同，但可能在决策分布上产生等价变化，导致冗余更新过度强调重复行为；二是聚合后的更新可能超出 adapter 的秩预算，直接在权重空间近似会扭曲原本要实现的决策变化。  

**方法关键点**  
提出 BQ-LoRA，包含两个模块：行为商平衡（BQB）和决策保持压缩（DPC）。BQB 从决策分布构造局部行为商流形，在商切空间按轨迹更新方向的局部密度重新加权，抑制冗余更新；DPC 将平衡后的梯度投影到固定秩切空间，并联合控制有效权重误差与决策分布失真进行重分解，避免低秩压缩破坏行为变化。  

**结果**  
在 AppWorld 和 BrowseComp-Plus 两个 LLM Agent 基准上，BQ-LoRA 与标准 LoRA 及近期低秩适应方法进行对比实验，同时消融实验验证 BQB 和 DPC 两个组件的互补效果。摘要未给出具体数值，但明确该方法在对比中体现出优势。
