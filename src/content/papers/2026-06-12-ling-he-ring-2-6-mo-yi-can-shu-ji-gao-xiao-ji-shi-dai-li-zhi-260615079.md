---
title: 'Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence
  at Trillion-Parameter Scale'
title_zh: Ling 和 Ring 2.6：万亿参数级高效即时代理智能
authors:
- Ang Li
- Ben Liu
- Bin Han
- Bin Hu
- Bin Jing
- Binbin Hu
- Bing Li
- Cai Chen
- Caizhi Tang
- Changxin Tian
affiliations:
- Inclusion AI
arxiv_id: '2606.15079'
url: https://arxiv.org/abs/2606.15079
pdf_url: https://arxiv.org/pdf/2606.15079
published: '2026-06-12'
collected: '2026-06-17'
category: Agent
direction: Agent 高效训练与推理优化
tags:
- LLM
- Agent
- RL
- Linear Attention
- Token Efficiency
- Architecture Co-design
one_liner: 通过架构升级、混合线性注意力及强化学习框架实现高效推理与代理能力的万亿参数模型家族
practical_value: '- **长上下文推理效率**：混合线性注意力（Lightning Attention + MLA）可大幅降低长序列（如用户行为序列、多轮对话）的预填充和解码延迟，直接适用于电商搜索/推荐系统的实时重排序或解释生成场景。

  - **Token 效率优化**：最短正确响应蒸馏和双向偏好对齐能训练模型用更少 token 提供精准推荐理由或答案，降低服务成本，尤其适合用户触达、消息推送等延迟敏感的业务。

  - **Agent 训练稳定性**：KPop 异步 RL 调度框架可借鉴到多步搜索 Agent 的训练中，通过异步采集搜索、工具调用、工作流执行等环境交互数据，提升样本利用率和训练吞吐，适合构建能自主调用商品检索、价格对比等工具的购物助手。

  - **业务模型迁移升级**：论文从已有模型（Ling-2.0）通过架构迁移和继续训练而非从头预训练的方法，对于已有推荐/对话模型向 Agent 方向升级提供了一个低成本路径，避免全量重训。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Agent 场景要求 LLM 同时满足低延迟响应与强推理能力，传统训练方式在成本和效率上难以适配万亿参数规模。

**方法**：不从头训练，而是基于 Ling-2.0 进行架构迁移预训练与大规模后训练。架构上引入混合线性注意力，将 Lightning Attention 与 MLA 结合，提升长上下文训练和解码效率。Token 效率方面，通过进化链式思维、语言单元策略优化、双向偏好对齐和最短正确响应蒸馏等手段，提升输出中每个 token 的含金量。针对代理能力，提出 KPop 强化学习框架，通过异步调度编码、搜索、工具使用和工作流执行四类环境交互，实现 Ring-2.6-1T 的大规模稳定训练。模型系列中 Ling-2.6 专攻即时响应，Ring-2.6 侧重深度推理与复杂工作流。

**关键结果**：在保持推理能力的同时，显著降低长文本预填充耗时，单 token 能力密度提升；KPop 使 1T 参数模型在真实环境交互中收敛稳定，开源全部检查点。
