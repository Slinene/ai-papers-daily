---
title: Post-Trained MoE Can Skip Half Experts via Self-Distillation
title_zh: 后训练MoE可通过自蒸馏跳过半数专家
authors:
- Xingtai Lv
- Li Sheng
- Kaiyan Zhang
- Yichen You
- Siyan Gao
- Xueheng Luo
- Yuxin Zuo
- Yuchen Fan
- Junlin Yang
- Ganqu Cui
affiliations:
- Tsinghua University
- Shanghai AI Lab
- WeChat AI
- Kuaishou Technology
- Frontis.AI
arxiv_id: '2605.18643'
url: https://arxiv.org/abs/2605.18643
pdf_url: https://arxiv.org/pdf/2605.18643
published: '2026-05-17'
collected: '2026-05-19'
category: Training
direction: 动态MoE推理加速 · 自蒸馏适配
tags:
- MoE
- Dynamic Routing
- Self-Distillation
- Inference Acceleration
- Zero-Expert
- Post-Training
one_liner: 注入零输出专家并两阶段自蒸馏，将静态MoE转为动态，消减超50%专家计算且精度损失极小
practical_value: '- **部署加速**：已在线服务的 MoE 模型可直接注入零专家并通过自蒸馏转为动态路由，无需重新预训练，降低推理 FLOPs
  和耗时，适合电商对话、Agent 等对延迟敏感的场景。

  - **稳定迁移**：组级辅助损失（L_GA）仅在普通专家与零专家组之间施加平衡，保留原模型内部路由分布，避免能力坍塌，这一 trick 可复用于其他需要引入“跳过”选项的
  MoE 微调。

  - **蒸馏策略**：SFT + OPD 的两阶段设计先驯化路由再对齐分布，比单阶段更稳定；OPD 使用学生自身 rollout 并由教师提供 token 级目标，缩小训练-推理分布差异。

  - **计算分配信号**：零专家激活率与师生 logp 差、模型熵高度相关，而与任务难度解耦，可据此设计基于置信度的动态推理策略。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
已完整训练的 MoE 大模型（如经过 SFT、RL 的商用模型）在推理时每个 token 激活固定数量专家，造成算力浪费，尤其是对于简单 token。现有动态 MoE 方法多从预训练阶段介入或只做任务特定适配，无法直接应用于已部署的模型。本文探索如何以低成本将静态 MoE 转换为可动态跳过专家的版本。

**方法关键点**
- **零专家注入**：在现有专家层中增加不产生输出的“零专家”（输出恒为零），路由扩展至包含零专家，token 选择零专家即可省去实际计算。
- **两阶段自蒸馏**：以原模型为固定教师，先进行 SFT 阶段（教师采样数据监督训练），再进行 OPD 阶段（学生采样，教师对同一轨迹提供令牌级 KL 散度损失），使转换后的模型在自身推理分布下逼近原模型。
- **组辅助损失 L_GA**：将普通专家和零专家分为两组，只对两组间做负载均衡，从而控制零专家激活率（r_ZE）而不破坏普通专家内部的路由结构。
- **可调节的零专家组权重 w**：通过调整 w 控制目标 r_ZE，实现质量-效率 trade-off。

**关键实验**
- **模型与基准**：Qwen3-30B-A3B（128 专家，top-8）和 GLM-4.7-Flash（64 专家，top-4），在 AIME、GSM8K、MATH-500、LiveCodeBench、HumanEval+、MBPP+、IFEval 等 11 个基准上评估。
- **结果**：ZEDA 在 r_ZE≈50% 下平均精度损失微弱（Qwen 上仅降 0.7 分），显著优于 AdaMoE 和 Dynamic Skipping 等强基线（分别高出 6.1、4.0 分），并在 MMLU-Redux、GPQA 等 OOD 任务上保持竞争力。端到端推理吞吐提升约 1.20 倍。
- **适应成本**：8 卡 H200，Qwen 耗时 30 小时，GLM 耗时 61 小时，远低于重新训练。

**核心洞察**
零专家激活率与 token 级的教师-学生对数概率差及模型熵紧密相关，但不受整体任务难度影响，说明动态路由在 token 粒度上自发分配计算，而对困难的整体任务仍可保持大部分专家参与。
