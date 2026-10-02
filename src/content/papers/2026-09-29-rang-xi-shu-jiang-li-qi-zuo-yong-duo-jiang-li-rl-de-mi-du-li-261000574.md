---
title: 'Make Sparse Rewards Count: Density-Aware Reward Aggregation for Multi-Reward
  RL'
title_zh: 让稀疏奖励起作用：多奖励 RL 的密度感知奖励聚合
authors:
- Tong Zheng
- Skylar Zhai
- Zhan Cheng
- TianMing Sha
- Youling Huang
- Shuo Zhou
- Shaotong Qi
- Jingcheng Liang
- Xuwei Ding
- Pengcheng Xu
affiliations:
- University of Chinese Academy of Sciences
- University of Minnesota Twin Cities
- University of Wisconsin–Madison
- Stony Brook University
- Kuaishou Technology
arxiv_id: '2610.00574'
url: https://arxiv.org/abs/2610.00574
pdf_url: https://arxiv.org/pdf/2610.00574
published: '2026-09-29'
collected: '2026-10-02'
category: Training
direction: 多奖励 RL 的密度感知聚合
tags:
- Multi-Reward RL
- GRPO
- Reward Aggregation
- Advantage Energy
- Density-Aware
- LLM Post-training
one_liner: 提出 DARA，通过逆平方根密度校正放大稀疏奖励的信号，加速多奖励 RL 训练且不改变策略优化目标
practical_value: '- 多目标 LLM 后训练中，若直接对多个 reward 求和或平均，稀疏目标（如格式合规、工具调用、长度合规）容易被稠密目标淹没。可仿照
  DARA 在 GRPO/GDPO 实现中按 batch 内每个 reward 非零优势的比例动态计算权重，对稀疏目标施加 inverse-square-root
  加权，无需人工反复调 reward coefficient。

  - 监控每个 reward 的 advantage energy 或 active-group density，可以量化判断哪些目标学习停滞；当某个目标 density
  骤降时自动提高其聚合权重，比训练后看指标再手动调参更早发现信号失衡。

  - DARA 只改 reward aggregation，不改变底层 policy optimization objective 或梯度计算，可作为即插即用模块嵌入现有
  RLHF/GRPO 流程，工程风险低；只需在 batch 内按 reward 保存 group-level advantages 即可计算 density。

  - 对电商 Agent、对话式推荐、商品文案生成等需要同时满足「格式/调用/质量」等多约束的 LLM 应用，稀疏约束信号密度很低，DARA 的密度感知聚合能减少达到高合规率所需训练步数，降低迭代成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
多奖励 RL 训练 LLM 时，GDPO 的 reward-wise normalization 保留组内相对信息，但不同 reward 仍有学习进度不均衡。稀疏 reward 在多数 rollout group 里没有非零相对优势，信号容易被淹没。  

**方法关键点**  
定义 advantage energy 为 batch 内某 reward 的 squared advantages 之和。在理想 GDPO 归一化下，advantage energy 正比于 active-group density，即该 reward 提供非零相对优势的 group 占比。基于此提出 Density-Aware Reward Aggregation，采用逆平方根密度校正：密度越低的 reward 在聚合时权重越大。DARA 从每个 rollout batch 计算权重，动态适应训练过程中 reward 活跃度的变化，且不修改底层 policy optimization objective。  

**关键结果**  
在 tool calling 上，DARA 达到高 format compliance 最多减少 26% 训练步数；在数学推理上，near-saturated length compliance 最多减少 65% 训练步数；最终性能与 GDPO 保持可比，说明加速收敛未牺牲最终效果。
